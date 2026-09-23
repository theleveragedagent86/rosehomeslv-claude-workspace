# Fix: "Post Now" never publishes

## What is happening
Lofty's "Post Now" button only acts on a **trusted** (real) click. The publisher injects
JavaScript through AppleScript, and a JavaScript `element.click()` is NOT trusted, so Lofty's
submit handler ignores it. Every field fills, but nothing publishes.

Confirmed by test: a synthetic `.click()` on Post Now did nothing (no submit, no validation),
while a real click fired the handler and jumped to validation. So the cure is to make the final
activation a real OS event.

## Drop-in replacement for click_post_now()
This focuses the button in JavaScript (allowed), then sends a trusted Enter keystroke via
System Events, which the focused button treats as a real activation.

```python
def click_post_now():
    """Focus the Post Now button, then activate it with a TRUSTED Enter keystroke."""
    # 1. Focus the real Post Now button inside the editor dialog
    focused = chrome_js("""
    var dialog = document.querySelector('.edit-blog-dialog');
    var done = 'FAIL: no dialog';
    if (dialog) {
        var btns = dialog.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.trim() === 'Post Now' && btns[i].offsetHeight > 0) {
                btns[i].focus();
                done = (document.activeElement === btns[i]) ? 'focused' : 'FAIL: not focused';
                break;
            }
        }
    }
    done;
    """)
    if not focused or "focused" != str(focused).strip():
        return False

    # 2. Bring Chrome forward and send a TRUSTED Enter (key code 36) to the focused button.
    #    Requires: System Settings > Privacy & Security > Accessibility -> enable Terminal.
    subprocess.run(['osascript', '-e',
        'tell application "Google Chrome" to activate'], capture_output=True)
    time.sleep(0.5)
    subprocess.run(['osascript', '-e',
        'tell application "System Events" to key code 36'], capture_output=True)  # 36 = Return
    time.sleep(2)

    # 3. Confirm any follow-up dialog (also trusted, via focus + Enter is usually not needed,
    #    but keep the JS confirm as a fallback for the OK/Confirm popup).
    chrome_js("""
    var btns = document.querySelectorAll('.el-message-box__btns button, .el-dialog button');
    for (var i = 0; i < btns.length; i++) {
        var t = btns[i].textContent.trim();
        if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && btns[i].offsetHeight > 0) {
            btns[i].focus(); btns[i].click(); break;
        }
    }
    """)
    time.sleep(3)

    # 4. Verify the editor closed (a real publish closes the dialog).
    still_open = chrome_js("!!document.querySelector('.edit-blog-dialog')")
    return still_open != "true"
```

## One-time setup
Give your terminal permission to send keystrokes:
System Settings > Privacy & Security > Accessibility > enable **Terminal** (or iTerm).
You already granted "Allow JavaScript from Apple Events" in Chrome, which is still required.

## Then re-run
```
python3 /Users/ryanrose/Downloads/Claude/_System/plugins/local-news-plugin/publish-local-news.py 2026-08-09 --yes
```

## If key code 36 does not activate on your macOS
Fallback: use a real click at the button's screen coordinates instead of the keystroke. Replace
step 2 with:

```python
    coords = chrome_js("""
    var dlg = document.querySelector('.edit-blog-dialog');
    var b = null, btns = dlg.querySelectorAll('button.cms-button');
    for (var i=0;i<btns.length;i++){ if(btns[i].textContent.trim()==='Post Now'&&btns[i].offsetHeight>0){b=btns[i];break;} }
    var r = b.getBoundingClientRect();
    var x = Math.round(window.screenX + r.left + r.width/2);
    var y = Math.round(window.screenY + (window.outerHeight - window.innerHeight) + r.top + r.height/2);
    x + ',' + y;
    """)
    x, y = coords.split(',')
    subprocess.run(['osascript', '-e',
        f'tell application "System Events" to click at {{{x}, {y}}}'], capture_output=True)
```
(Also needs Accessibility permission for Terminal.)
