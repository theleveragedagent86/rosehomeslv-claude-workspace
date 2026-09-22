# Optional: Load directly into excalidraw.com via Chrome MCP

When the Chrome MCP tools (`mcp__Claude_in_Chrome__*`) are available, you can skip the drag-drop step and load the scene straight into the user's open Excalidraw tab.

**When to use this path:** the user asks to "load it for me", "open it in Excalidraw", or "show me", AND Chrome MCP is available. Otherwise just hand over the `.excalidraw` file path.

---

## Steps

### 1. Start a local CORS-enabled HTTP server

Excalidraw's React app needs to fetch the file from somewhere CORS allows. A local server in `/Users/ryanrose/Downloads/Claude/` with `Access-Control-Allow-Origin: *` does the job. Run it as a background task:

```bash
python3 -c "
import http.server, socketserver, threading, os
os.chdir('/Users/ryanrose/Downloads/Claude')
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    def log_message(self, format, *args): pass
s = socketserver.TCPServer(('', 9877), H)
threading.Thread(target=s.serve_forever, daemon=True).start()
import time; time.sleep(300)
" &
```

Pick an unused port (9877 has worked). Verify with `curl -s http://localhost:9877/<slug>.excalidraw | head -c 50` before moving on.

### 2. Open excalidraw.com in Chrome

```
mcp__Claude_in_Chrome__tabs_context_mcp(createIfEmpty: true)
mcp__Claude_in_Chrome__navigate(url: "https://excalidraw.com", tabId: <id>)
```

Wait ~3 seconds for the React app to mount.

### 3. Inject the scene via React fiber

Excalidraw exposes `updateScene` on the React component instance. Walk the fiber tree to find it, then call it with the elements:

```javascript
(async () => {
  const res = await fetch('http://localhost:9877/<slug>.excalidraw?t=' + Date.now());
  const data = await res.json();
  const app = document.querySelector('.excalidraw');
  const fk = Object.keys(app).find(k => k.startsWith('__reactFiber'));
  const sn = app[fk].return.stateNode;
  sn.updateScene({elements: data.elements, commitToStore: true});
  sn.scrollToContent(undefined, {fitToViewport: true, viewportZoomFactor: 0.85});
  return 'Loaded ' + data.elements.length + ' elements';
})();
```

Run via `mcp__Claude_in_Chrome__javascript_tool`. The cache-buster query param (`?t=...`) matters because Chrome will otherwise serve a stale copy if you reload after editing.

### 4. Screenshot for the user

```
mcp__Claude_in_Chrome__computer(action: "screenshot", save_to_disk: true)
```

This proves the scene loaded and lets the user spot any layout issues.

### 5. Stop the server

```bash
pkill -f "9877" 2>/dev/null
```

---

## Pitfalls

- **First time only:** if you call `clipboard.readText()` instead of fetch, Chrome shows a permission prompt that freezes the renderer. Always use the fetch + local server path.
- **Stale tab:** if the Excalidraw tab was loaded before the React fiber walk, it works. If you reload mid-session, re-walk the fiber.
- **Multiple tabs:** `document.querySelector('.excalidraw')` only returns the first match. If the user has multiple Excalidraw tabs open, target the active one explicitly.
- **`updateScene` replaces, not appends:** calling it wipes whatever was on the canvas. If the user had work in progress, ask before loading.
