#!/usr/bin/env python3
"""
Lofty blog API helper (background, no focus needed)
===================================================
Runs Lofty's own blog API from inside any open cms.lofty.com Chrome tab, so it
uses Ryan's logged-in session. Nothing is clicked and Chrome never needs focus.

Usage:
    python3 lofty_api.py dump out.json               All published posts (full detail fields)
    python3 lofty_api.py patch patches.json          Apply {"<postId>": {"field": value}}
    python3 lofty_api.py patch patches.json --dry    Show what would change

patch GETs each post, sets only the given fields (title, customSchema, content...),
POSTs the full object back, re-reads it and checks each field stuck.

Gotchas (learned 2026-09-21):
  - Save fails with code 100004 "601" if content contains a <script> block.
  - POST /api-blog/post/task needs the ?120104=844766273598872 query.
  - Category: POST /api-blog/post/updateCategoryName?120104=844766273598872
    {postId, nameList:[{id, name}]}. "Las Vegas Real Estate" = id 70025.

Requirements: macOS, Chrome > View > Developer > Allow JavaScript from Apple
Events, a cms.lofty.com tab open and logged in (any tab, any window).
"""
import json
import os
import subprocess
import uuid
import sys
import time
from pathlib import Path

JS_FILE = Path(f"/tmp/lofty-api-js-{os.getpid()}.js")  # per process, so runs can overlap
H = ("var H={'Accept':'application/json, text/plain, */*','Content-Type':'application/json',"
     "'CURRENTSITEID':120104,'CURRENTLANGUAGE':'en','CMSACCOUNTROLE':0};")
SAVE_Q = "?120104=844766273598872"
_TAB = None


def find_tab():
    """(window id, tab id) of a cms.lofty.com tab, preferring the blog page."""
    script = '''set out to ""
tell application "Google Chrome"
  repeat with w in windows
    repeat with t in tabs of w
      if URL of t contains "cms.lofty.com" then set out to out & (id of w) & "," & (id of t) & "," & (URL of t) & linefeed
    end repeat
  end repeat
end tell
return out'''
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, timeout=30)
    rows = [l.split(",", 2) for l in r.stdout.strip().splitlines() if l.count(",") >= 2]
    if not rows:
        sys.exit("No cms.lofty.com tab open in Chrome. Open the Lofty blog page and retry.")
    rows.sort(key=lambda x: "/blog" not in x[2])
    for w, t, _ in rows:  # skip a tab whose page is frozen
        try:
            r = subprocess.run(["osascript", "-e", f'tell application "Google Chrome" to tell '
                                f'tab id {t} of window id {w} to execute javascript "1+1"'],
                               capture_output=True, text=True, timeout=10)
            if r.stdout.strip() == "2":
                return int(w), int(t)
        except subprocess.TimeoutExpired:
            pass
    sys.exit("No responsive cms.lofty.com tab. Reload the Lofty blog tab and retry.")


def js(code, tries=3):
    global _TAB
    if _TAB is None:
        _TAB = find_tab()
    JS_FILE.write_text(code)
    w, t = _TAB
    for _ in range(tries):
        try:
            r = subprocess.run(["osascript", "-e",
                                f'set c to read POSIX file "{JS_FILE}" as «class utf8»\n'
                                f'tell application "Google Chrome"\ntell (tab id {t} of window id {w}) '
                                f'to execute javascript c\nend tell'],
                               capture_output=True, text=True, timeout=60)
            return r.stdout.strip()
        except subprocess.TimeoutExpired:
            time.sleep(5)
    return "TIMEOUT"


def run_async(body, wait=300):
    """Run an async JS body in the page; it must set window.__lofty to a string.
    Each call gets its own result slot, so two scripts can share one tab."""
    key = "__lofty_" + uuid.uuid4().hex[:8]
    body = body.replace("window.__lofty", f"window.{key}")
    js(f"window.{key}='PENDING';(async function(){{try{{" + body +
       f"}}catch(e){{window.{key}='ERR '+e}}}})();''")
    end = time.time() + wait
    while time.time() < end:
        time.sleep(2)
        r = js(f"window.{key}")
        if r not in ("PENDING", "TIMEOUT"):
            js(f"delete window.{key}")
            return r
    return "TIMEOUT"


def dump(path):
    posts, pn = [], 1
    while True:
        res = run_async(H + f"""var l=(await (await fetch('/api-blog/post/listV2?keywords=&status=1&pageNum={pn}&pageSize=200&t='+Date.now(),{{credentials:'include',headers:H}})).json()).data.postList;
window.__lofty=JSON.stringify(l.map(p=>({{id:p.id,slug:p.slug,title:p.title,cat:(p.categoryList||[]).map(c=>c.name),
seoTitle:p.seoTitle,seoDescription:p.seoDescription,seoKeyword:p.seoKeyword,postDate:p.postDate,updateTime:p.updateTime,
featuredImage:p.featuredImage,schema:p.customSchema||'',content:p.content||''}})));""")
        if not res.startswith("["):
            sys.exit(f"dump failed on page {pn}: {res[:200]}")
        page = json.loads(res)
        if not page:
            break
        posts += page
        print(f"  page {pn}: {len(posts)} posts", flush=True)
        pn += 1
    Path(path).write_text(json.dumps(posts))
    print(f"Saved {len(posts)} posts to {path}")


def patch(patches, dry=False, chunk=20):
    """patches: {postId: {field: value}}. Returns list of [id, slug, status]."""
    items = list(patches.items())
    out = []
    for i in range(0, len(items), chunk):
        part = dict(items[i:i + chunk])
        res = run_async(H + """var P=%s, DRY=%s, out=[];
for(const id in P){
 var d=(await (await fetch('/api-blog/post/'+id+'?t='+Date.now(),{credentials:'include',headers:H})).json()).data;
 if(!d){out.push([id,'','FAIL not found']);continue;}
 var ch=Object.keys(P[id]).filter(k=>d[k]!==P[id][k]);
 if(!ch.length){out.push([id,d.slug,'SAME']);continue;}
 if(DRY){out.push([id,d.slug,'WOULD '+ch.join(',')]);continue;}
 ch.forEach(k=>d[k]=P[id][k]);
 var j=await (await fetch('/api-blog/post/task%s',{method:'POST',credentials:'include',headers:H,body:JSON.stringify(d)})).json();
 var d2=(await (await fetch('/api-blog/post/'+id+'?t='+Date.now(),{credentials:'include',headers:H})).json()).data;
 var bad=ch.filter(k=>d2[k]!==P[id][k]);
 out.push([id,d.slug,j.status.code===0&&!bad.length?'OK '+ch.join(','):'FAIL '+j.status.code+' '+j.status.msg+' '+bad.join(',')]);
}
window.__lofty=JSON.stringify(out);""" % (json.dumps(part), "true" if dry else "false", SAVE_Q), 600)
        if not res.startswith("["):
            print(f"  chunk {i}: {res[:200]}", flush=True)
            out += [[k, "", "FAIL " + res[:80]] for k in part]
            continue
        rows = json.loads(res)
        out += rows
        bad = [r for r in rows if r[2].startswith("FAIL")]
        print(f"  {min(i + chunk, len(items))}/{len(items)} done, {len(bad)} failed in chunk", flush=True)
    return out


def find_by_slug(slugs):
    """{slug: post id} for published posts whose slug is in slugs."""
    want = json.dumps(sorted(set(slugs)))
    res = run_async(H + """var W=new Set(%s), out={};
for(var pn=1;pn<=40;pn++){var l=(await (await fetch('/api-blog/post/listV2?keywords=&status=1&pageNum='+pn+'&pageSize=500&t='+Date.now(),{credentials:'include',headers:H})).json()).data.postList;
 if(!l.length)break; l.forEach(p=>{if(W.has(p.slug))out[p.slug]=p.id});}
window.__lofty=JSON.stringify(out);""" % want, 300)
    if not res.startswith("{"):
        sys.exit(f"slug lookup failed: {res[:200]}")
    return json.loads(res)


def read(ids, fields=("content", "customSchema", "featuredImage", "title", "slug"), chunk=20):
    """Fetch post details by id. Returns {id: {field: value}}."""
    ids, out = [int(i) for i in ids], {}
    for i in range(0, len(ids), chunk):
        part = ids[i:i + chunk]
        res = run_async(H + """var IDS=%s, F=%s, out={};
for(const id of IDS){
  var d=(await (await fetch('/api-blog/post/'+id+'?t='+Date.now(),{credentials:'include',headers:H})).json()).data;
  if(!d)continue; var o={}; for(const k of F)o[k]=d[k]; out[id]=o;
}
window.__lofty=JSON.stringify(out);""" % (json.dumps(part), json.dumps(list(fields))), 180)
        if not res.startswith("{"):
            sys.exit(f"read failed: {res[:200]}")
        out.update({int(k): v for k, v in json.loads(res).items()})
        print(f"  read {len(out)}/{len(ids)}", flush=True)
    return out


def create(posts, category):
    """Publish new posts. posts: list of dicts with title, slug, content, seoTitle,
    seoKeyword, seoDescription, customSchema. Returns [[slug, status]].

    Mirrors what Lofty's editor sends on Publish: author from the account,
    category by id, featured image = first <img> in the body (the editor's own
    linkage rule), status 1, postDate now. Skips any slug that already exists.
    """
    out = []
    for p in posts:
        res = run_async(H + """var P=%s, CAT=%s;
var ex=(await (await fetch('/api-blog/post/duplicate-slug?slug='+encodeURIComponent(P.slug)+'&t='+Date.now(),{credentials:'include',headers:H})).json()).data;
if(ex && ex.flag!==false){window.__lofty=JSON.stringify([P.slug,'EXISTS']);return;}
var cats=(await (await fetch('/api-blog/category/list?t='+Date.now(),{credentials:'include',headers:H})).json()).data.categoryList;
var c=cats.find(x=>x.name===CAT);
var author=(await (await fetch('/api-blog/post/listV2?keywords=&status=1&pageNum=1&pageSize=1&t='+Date.now(),{credentials:'include',headers:H})).json()).data.postList[0].author||'Ryan Rose';
var img=(P.content.match(/<img[^>]+src=["']([^"']+)["']/i)||[])[1]||'';
var d={title:P.title,author:author,content:P.content.replace(/<\\/script>/g,'<\\\\/script>'),categoryList:c?[{id:c.id,name:c.name}]:[{name:CAT}],
 featuredImage:img,imageAltText:'',showFeatureImage:false,seoTitle:P.seoTitle,seoKeyword:P.seoKeyword,seoDescription:P.seoDescription,
 slug:P.slug,customSchema:P.customSchema,status:1,postDate:Date.now()};
var j=await (await fetch('/api-blog/post/task%s',{method:'POST',credentials:'include',headers:H,body:JSON.stringify(d)})).json();
if(j.status.code!==0){window.__lofty=JSON.stringify([P.slug,'FAIL '+j.status.code+' '+j.status.msg]);return;}
var l=(await (await fetch('/api-blog/post/listV2?keywords=&status=1&pageNum=1&pageSize=50&t='+Date.now(),{credentials:'include',headers:H})).json()).data.postList;
var got=l.find(x=>x.slug===P.slug);
if(!got){window.__lofty=JSON.stringify([P.slug,'FAIL saved but not found in published list']);return;}
var d2=(await (await fetch('/api-blog/post/'+got.id+'?t='+Date.now(),{credentials:'include',headers:H})).json()).data;
var bad=['title','seoTitle','seoKeyword','seoDescription','customSchema'].filter(k=>(d2[k]||'')!==(d[k]||''));
if(!(d2.categoryList||[]).some(x=>x.name===CAT))bad.push('category');
window.__lofty=JSON.stringify([P.slug,bad.length?'FAIL check '+bad.join(','):'OK '+got.id]);""" % (
            json.dumps(p), json.dumps(category), SAVE_Q), 120)
        row = json.loads(res) if res.startswith("[") else [p["slug"], "FAIL " + res[:100]]
        ok = row[1].startswith("OK")
        print(f"  {'OK' if ok else '!!':2} {row[0]}  {'' if ok else row[1]}", flush=True)
        out.append(row)
    return out


def set_category(assign):
    """assign: {post id: category name}. Uses Lofty's own category endpoint."""
    res = run_async(H + """var A=%s, out=[];
var cats=(await (await fetch('/api-blog/category/list?t='+Date.now(),{credentials:'include',headers:H})).json()).data.categoryList;
for(const id in A){
 var c=cats.find(x=>x.name===A[id]);
 if(!c){out.push([id,'FAIL no category '+A[id]]);continue;}
 var j=await (await fetch('/api-blog/post/updateCategoryName%s',{method:'POST',credentials:'include',headers:H,body:JSON.stringify({postId:Number(id),nameList:[{id:c.id,name:c.name}]})})).json();
 var d=(await (await fetch('/api-blog/post/'+id+'?t='+Date.now(),{credentials:'include',headers:H})).json()).data;
 out.push([id,(j.status.code===0&&(d.categoryList||[]).some(x=>x.name===A[id]))?'OK '+A[id]:'FAIL '+j.status.msg]);
}
window.__lofty=JSON.stringify(out);""" % (json.dumps(assign), SAVE_Q), 300)
    if not res.startswith("["):
        sys.exit(f"category update failed: {res[:200]}")
    return json.loads(res)


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("dump", "patch"):
        sys.exit(__doc__)
    if sys.argv[1] == "dump":
        dump(sys.argv[2])
    else:
        rows = patch(json.loads(Path(sys.argv[2]).read_text()), dry="--dry" in sys.argv)
        from collections import Counter
        print(dict(Counter(r[2].split(" ")[0] for r in rows)))
        for r in rows:
            if r[2].startswith("FAIL"):
                print("  ", r)
