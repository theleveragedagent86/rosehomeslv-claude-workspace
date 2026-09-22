#!/usr/bin/env python3
"""PostToolUse hook: remind to update the nearest CLAUDE.md Folder Map when a
structural change (add/remove/move/rename) happens. Non-blocking, low-noise:
stays completely silent unless it detects a real structural change in the
workspace, and always exits 0 so it can never break a tool call."""
import sys, json, os, re

WORKSPACE = "/Users/ryanrose/Downloads/Claude"
SKIP = ("/.git/", "/node_modules/", "/scratchpad/", "/_dist/", "/__pycache__/",
        "/temporary screenshots/")
# structural verb only when it's in command position (start or after a separator)
STRUCT = re.compile(
    r'(?:(?:^|\|\||&&|[;&|]|\bsudo\s+|\bxargs\s+)\s*(?:mv|rm|rmdir|mkdir|cp|touch)\b)'
    r'|(?:\bgit\s+(?:mv|rm)\b)')


def nearest_claude_md(start_dir):
    d = os.path.abspath(start_dir)
    while d.startswith(WORKSPACE):
        c = os.path.join(d, "CLAUDE.md")
        if os.path.isfile(c):
            return c
        if d == WORKSPACE:
            break
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return None


def emit(context):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        },
        "suppressOutput": True,
    }))
    sys.exit(0)


def main():
    data = json.loads(sys.stdin.read() or "{}")
    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}
    cwd = data.get("cwd") or WORKSPACE

    if tool == "Write":
        fp = ti.get("file_path", "")
        if not fp:
            return
        ap = os.path.abspath(fp)
        if not ap.startswith(WORKSPACE) or any(s in ap for s in SKIP):
            return
        base = os.path.basename(ap)
        if base in ("CLAUDE.md", ".DS_Store"):
            return
        cm = nearest_claude_md(os.path.dirname(ap))
        # If the file is already named in the nearest CLAUDE.md, treat as an edit
        # (not a new addition) and stay silent.
        if cm:
            try:
                if base in open(cm, encoding="utf-8").read():
                    return
            except OSError:
                pass
        rel = os.path.relpath(ap, WORKSPACE)
        tgt = os.path.relpath(cm, WORKSPACE) if cm else "the nearest CLAUDE.md"
        emit(f"[Folder-map reminder] You just created '{rel}'. Per the workspace "
             f"maintenance rule, if this is a new file/folder that belongs in the "
             f"structure, add it to the Folder Map in '{tgt}' (and the parent's) "
             f"before you finish this task.")
        return

    if tool == "Bash":
        cmd = ti.get("command", "") or ""
        if not STRUCT.search(cmd):
            return
        # Ignore ops that only touch temp/scratch/dist areas
        if WORKSPACE not in cmd and ("scratchpad" in cmd or "/tmp/" in cmd):
            return
        # Collect workspace paths: quoted strings first (handle spaces), then bare runs
        paths = []
        for m in re.finditer(r'"([^"]*)"|\'([^\']*)\'', cmd):
            s = m.group(1) if m.group(1) is not None else m.group(2)
            if s and s.startswith(WORKSPACE):
                paths.append(s)
        paths += re.findall(r'/Users/ryanrose/Downloads/Claude[^\s"\';|&)]*', cmd)
        # prefer the most specific (longest) real path
        target_dir = cwd
        for p in sorted(paths, key=len, reverse=True):
            if any(s in p for s in SKIP):
                continue
            target_dir = p if os.path.isdir(p) else os.path.dirname(p)
            break
        cm = nearest_claude_md(target_dir)
        tgt = os.path.relpath(cm, WORKSPACE) if cm else "the nearest CLAUDE.md"
        verb = (cmd.strip().split() or ["a command"])[0]
        emit(f"[Folder-map reminder] `{verb}` may have added/removed/moved files. "
             f"Per the workspace maintenance rule, if the folder structure changed, "
             f"update the Folder Map in '{tgt}' (and the parent's) before you finish "
             f"this task.")
        return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
