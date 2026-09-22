#!/usr/bin/env ruby
# Rose Homes LV preview server + Command Center executor.
#
#   ruby serve.rb            # http://localhost:8091
#
# Two jobs:
#   1. Serve the workspace as static files, same as it always did.
#   2. Back the Command Center at Rose Homes LV/Dashboard/index.html with a small
#      localhost API that runs allow-listed skills through headless `claude -p`.
#
# Safety, deliberately:
#   - Binds 127.0.0.1 only. Nothing off this machine can reach it.
#   - Every runnable command is a constant in COMMANDS below. The page sends an id,
#     never a command string, so a compromised page cannot invent a new command.
#   - Commands are spawned as an argv array. No shell, so no interpolation and no
#     quoting bugs.
#   - Cross-origin POSTs are refused. A random website you visit can otherwise POST
#     to localhost, which for a server that runs code is the whole ballgame.

# Ruby picks its default encoding from the environment. Launched from a plist or a
# bare nohup there is no LANG, so it lands on US-ASCII and every read of a baked
# panel containing an arrow or a curly quote makes JSON.generate raise. Pin it.
Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

require 'webrick'
require 'json'
require 'fileutils'
require 'securerandom'
require 'time'

ROOT  = __dir__
DASH  = File.join(ROOT, 'Rose Homes LV', 'Dashboard')
RUNS  = File.join(DASH, 'runs')
BAKED = File.join(RUNS, 'baked')
LOG   = File.join(DASH, 'completion-log.json')
PORT  = 8091

FileUtils.mkdir_p(BAKED)

# ---------------------------------------------------------------- command allowlist
#
# :baked  read a file the 6am build already wrote. Instant, spends nothing.
# :live   run headless claude. Draws Ryan's Max plan limits, so keep this list short.
#
# :prompt is what gets handed to claude as a single argv element.
# :perm   defaults to acceptEdits. bypassPermissions is never used here.

COMMANDS = {
  # ---- baked ----
  'daily-checklist' => { mode: :baked, label: 'Daily checklist' },
  'tc-status'       => { mode: :baked, label: 'TC actions'      },
  'deadlines'       => { mode: :baked, label: 'Deadlines'       },
  'money'           => { mode: :baked, label: 'Money detail'    },

  # ---- live ----
  'rebuild' => {
    mode: :live, label: 'Rebuild data', timeout: 600, model: 'sonnet',
    # The four .md filenames below are NOT cosmetic. Each baked button reads
    # runs/baked/<its own command id>.md, so these names must stay in sync with
    # the :baked entries above or the buttons report "never built".
    prompt: 'Rebuild the Rose Homes LV Command Center data. Re-read every ' \
            'Rose Homes LV/Clients/Transactions/*/transaction.json plus the listings and ' \
            'buyers folders, then regenerate Rose Homes LV/Dashboard/data/*.json.\n\n' \
            'Then write EXACTLY these four files in Rose Homes LV/Dashboard/runs/baked/, ' \
            'using these exact filenames and no others:\n' \
            '  daily-checklist.md  - what Ryan should do today, grouped by time of day, ' \
            'pulled from real deadlines and open items.\n' \
            '  tc-status.md        - per active transaction: next step, who owes what, ' \
            'what is blocked.\n' \
            '  deadlines.md        - every dated obligation across all deals, soonest ' \
            'first, each marked overdue / today / upcoming.\n' \
            '  money.md            - commission math per deal plus YTD closed and ' \
            'pipeline totals.\n\n' \
            'Overwrite those four if they exist. Each is Markdown, no front matter, ' \
            'opens with an h2 title. Treat every transaction.json as read only, never ' \
            'write to them. Mark any derived or estimated figure or date as estimated ' \
            'rather than presenting it as recorded fact, and write NOT FOUND for missing ' \
            'data instead of inferring it. No em-dashes anywhere in the output, ' \
            'per the workspace rule: use commas, periods, or the word and.'
  },
  'expired-workflow' => { mode: :live, label: 'Expireds',      prompt: '/expired-workflow', model: 'sonnet' },
  'local-news'       => { mode: :live, label: 'Local news',    prompt: '/local-news',       model: 'sonnet' },
  'weekly-update'    => { mode: :live, label: 'Seller report', prompt: '/weekly-update',    model: 'sonnet' },
  # client-facing writing, worth the better model
  'blog-writer'      => { mode: :live, label: 'Blog',          prompt: '/blog-writer',      model: 'opus' },
  'seller-cma'       => { mode: :live, label: 'CMA',           prompt: '/seller-cma',       model: 'opus' },

  # ---- free text from the prompt box ----
  'ask' => { mode: :live, label: 'Claude', free: true, model: 'sonnet' },
}.freeze

DEFAULT_TIMEOUT = 900
DEFAULT_MODEL   = 'sonnet'
# Only these may reach --model. Anything else from the page is ignored.
MODELS = %w[sonnet opus haiku].freeze

# ---------------------------------------------------------------- run registry
RUNS_MU = Mutex.new
ACTIVE  = {}   # run_id => hash

def run_state(id)
  RUNS_MU.synchronize { ACTIVE[id] && ACTIVE[id].dup }
end

def run_update(id)
  RUNS_MU.synchronize { yield ACTIVE[id] }
end

def stamp
  Time.now.utc.strftime('%Y-%m-%dT%H-%M-%SZ')
end

# Launch `claude -p` and stream its JSONL back into the run record.
def start_live_run(run_id, cmd_id, prompt, timeout, perm, model)
  argv = ['claude', '-p', prompt,
          '--output-format', 'stream-json', '--verbose',
          '--permission-mode', perm,
          '--model', model]

  Thread.new do
    began = Time.now
    begin
      IO.popen(argv, 'r', chdir: ROOT, err: [:child, :out], external_encoding: 'UTF-8') do |io|
        run_update(run_id) { |r| r[:pid] = io.pid }

        killer = Thread.new do
          sleep timeout
          begin
            Process.kill('TERM', io.pid)
            run_update(run_id) { |r| r[:timed_out] = true }
          rescue Errno::ESRCH
          end
        end

        io.each_line do |line|
          begin
            ev = JSON.parse(line)
          rescue JSON::ParserError
            next
          end
          absorb_event(run_id, ev)
        end
        killer.kill
      end
      code = $?.respond_to?(:exitstatus) ? $?.exitstatus : nil
      run_update(run_id) do |r|
        r[:status] = r[:timed_out] ? 'timeout' : (code == 0 ? 'done' : 'error')
        r[:exit]   = code
        r[:ended]  = Time.now.utc.iso8601
        r[:secs]   = (Time.now - began).round(1)
      end
    rescue Errno::ENOENT
      run_update(run_id) do |r|
        r[:status] = 'error'
        r[:text] << "\nCould not find the `claude` CLI on PATH.\n"
        r[:ended] = Time.now.utc.iso8601
      end
    rescue => e
      run_update(run_id) do |r|
        r[:status] = 'error'
        r[:text] << "\n#{e.class}: #{e.message}\n"
        r[:ended] = Time.now.utc.iso8601
      end
    end
    persist_run(run_id, cmd_id)
  end
end

# Turn one stream-json event into readable output plus usage numbers.
def absorb_event(run_id, ev)
  case ev['type']
  when 'assistant'
    blocks = (ev.dig('message', 'content') || [])
    blocks.each do |b|
      case b['type']
      when 'text'
        run_update(run_id) { |r| r[:text] << b['text'].to_s }
      when 'tool_use'
        run_update(run_id) { |r| r[:steps] << b['name'].to_s }
      end
    end
  when 'result'
    run_update(run_id) do |r|
      u = ev['usage'] || {}
      r[:usage] = {
        'input'       => u['input_tokens'],
        'output'      => u['output_tokens'],
        'cache_read'  => u['cache_read_input_tokens'],
        'cache_write' => u['cache_creation_input_tokens'],
        'cost_usd'    => ev['total_cost_usd']
      }
      # The final result carries the whole answer. Prefer it over the streamed
      # fragments so the panel never shows a half-written response.
      r[:text] = ev['result'].to_s unless ev['result'].to_s.strip.empty?
    end
  end
end

def persist_run(run_id, cmd_id)
  r = run_state(run_id) or return
  # run_id suffix because two runs can start inside the same second and would
  # otherwise overwrite each other.
  base = File.join(RUNS, "#{r[:started_stamp]}_#{cmd_id}_#{run_id[0, 8]}")
  File.write(base + '.md', r[:text].to_s)
  File.write(base + '.json', JSON.pretty_generate(
    'run'     => run_id,
    'command' => cmd_id,
    'label'   => r[:label],
    'model'   => r[:model],
    'status'  => r[:status],
    'started' => r[:started],
    'ended'   => r[:ended],
    'secs'    => r[:secs],
    'steps'   => r[:steps],
    'usage'   => r[:usage]
  ))
rescue => e
  warn "could not persist run #{run_id}: #{e.message}"
end

# ---------------------------------------------------------------- http helpers
def json_out(res, status, body)
  res.status = status
  res['Content-Type'] = 'application/json; charset=utf-8'
  res.body = JSON.generate(body)
end

# Refuse cross-origin writes. Same-origin fetch from our own page sends either no
# Origin or our own; anything else is another site poking at localhost.
def same_origin?(req)
  o = req['Origin']
  return true if o.nil? || o.empty?
  %W[http://localhost:#{PORT} http://127.0.0.1:#{PORT}].include?(o)
end

def read_json(req)
  JSON.parse(req.body.to_s)
rescue
  nil
end

# ---------------------------------------------------------------- server
server = WEBrick::HTTPServer.new(
  :Port         => PORT,
  :BindAddress  => '127.0.0.1',
  :DocumentRoot => Dir.pwd
)

# POST /api/run  -> {run: id} , or for baked commands the content straight back
server.mount_proc '/api/run' do |req, res|
  if req.request_method == 'GET'
    id = req.query['run'].to_s
    r  = run_state(id)
    next json_out(res, 404, 'error' => 'unknown run') unless r
    next json_out(res, 200,
      'status' => r[:status], 'label' => r[:label], 'text' => r[:text],
      'steps'  => r[:steps].last(6), 'usage' => r[:usage], 'secs' => r[:secs],
      'model'  => r[:model])
  end

  next json_out(res, 405, 'error' => 'use GET or POST') unless req.request_method == 'POST'
  next json_out(res, 403, 'error' => 'cross-origin refused') unless same_origin?(req)
  unless req['Content-Type'].to_s.start_with?('application/json')
    next json_out(res, 415, 'error' => 'send application/json')
  end

  body = read_json(req)
  next json_out(res, 400, 'error' => 'bad json') unless body.is_a?(Hash)

  cmd_id = body['id'].to_s
  spec   = COMMANDS[cmd_id]
  next json_out(res, 400, 'error' => "unknown command: #{cmd_id}") unless spec

  # ---- baked: just read what the build already wrote ----
  if spec[:mode] == :baked
    path = File.join(BAKED, "#{cmd_id}.md")
    if File.exist?(path)
      next json_out(res, 200, 'mode' => 'baked', 'label' => spec[:label],
        'status' => 'done', 'text' => File.read(path, encoding: 'UTF-8'),
        'built' => File.mtime(path).utc.iso8601)
    else
      next json_out(res, 200, 'mode' => 'baked', 'label' => spec[:label],
        'status' => 'missing',
        'text' => "No baked output yet for #{spec[:label]}.\n\n" \
                  "The 6am build writes it to Dashboard/runs/baked/#{cmd_id}.md. " \
                  "Click Rebuild data to generate it now.")
    end
  end

  # ---- live: run headless claude ----
  prompt =
    if spec[:free]
      p = body['prompt'].to_s.strip
      next json_out(res, 400, 'error' => 'empty prompt') if p.empty?
      next json_out(res, 400, 'error' => 'prompt too long') if p.length > 4000
      p
    else
      scope = body['scope'].to_s.strip
      base  = spec[:prompt]
      (scope.empty? || scope =~ /\Aall active deals\z/i) ? base : "#{base}\n\nScope: #{scope}"
    end

  run_id = SecureRandom.uuid
  now    = Time.now.utc
  RUNS_MU.synchronize do
    ACTIVE[run_id] = {
      status: 'running', label: spec[:label], text: +'', steps: [],
      usage: nil, started: now.iso8601, started_stamp: stamp
    }
  end
  # page override wins, then the command default, then sonnet
  want  = body['model'].to_s
  model = MODELS.include?(want) ? want : (spec[:model] || DEFAULT_MODEL)

  RUNS_MU.synchronize { ACTIVE[run_id][:model] = model }
  start_live_run(run_id, cmd_id, prompt,
                 spec[:timeout] || DEFAULT_TIMEOUT,
                 spec[:perm] || 'acceptEdits', model)

  json_out(res, 202, 'mode' => 'live', 'run' => run_id,
           'label' => spec[:label], 'model' => model)
end

# GET /api/runs -> recent run history for the activity feed
server.mount_proc '/api/runs' do |req, res|
  files = Dir[File.join(RUNS, '*.json')].sort.reverse.first(25)
  items = files.map do |f|
    begin
      JSON.parse(File.read(f, encoding: 'UTF-8'))
    rescue
      nil
    end
  end.compact
  json_out(res, 200, 'runs' => items)
end

# GET/POST /api/checklist -> per-day task completion
server.mount_proc '/api/checklist' do |req, res|
  data = File.exist?(LOG) ? (JSON.parse(File.read(LOG, encoding: 'UTF-8')) rescue {}) : {}

  if req.request_method == 'GET'
    day = req.query['date'].to_s
    day = Time.now.strftime('%Y-%m-%d') if day.empty?
    next json_out(res, 200, 'date' => day, 'done' => data[day] || {})
  end

  next json_out(res, 403, 'error' => 'cross-origin refused') unless same_origin?(req)
  body = read_json(req)
  next json_out(res, 400, 'error' => 'bad json') unless body.is_a?(Hash)

  day  = body['date'].to_s
  day  = Time.now.strftime('%Y-%m-%d') if day.empty?
  task = body['task'].to_s
  next json_out(res, 400, 'error' => 'missing task') if task.empty?

  data[day] ||= {}
  if body['done']
    data[day][task] = Time.now.utc.iso8601
  else
    data[day].delete(task)
  end
  File.write(LOG, JSON.pretty_generate(data))
  json_out(res, 200, 'date' => day, 'done' => data[day])
end

trap('INT')  { server.shutdown }
trap('TERM') { server.shutdown }

puts "Rose Homes LV server on http://localhost:#{PORT}  (127.0.0.1 only)"
puts "Command Center: http://localhost:#{PORT}/Rose%20Homes%20LV/Dashboard/index.html"
puts "#{COMMANDS.count { |_, v| v[:mode] == :live }} live commands, " \
     "#{COMMANDS.count { |_, v| v[:mode] == :baked }} baked"
server.start
