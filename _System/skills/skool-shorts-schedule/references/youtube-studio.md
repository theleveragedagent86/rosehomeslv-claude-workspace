# YouTube Studio recipe (The Leveraged Agent Shorts)

Verified on the Sept 2026 batch (24 Shorts, all scheduled + linked). claude-in-chrome only. Load tools in ONE ToolSearch:
`select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__find,mcp__claude-in-chrome__file_upload,mcp__claude-in-chrome__get_page_text`

`CH = UCJ_t1LMeHXO2iTx1YLMs1OA`. Every snippet starts with `const sl=ms=>new Promise(r=>setTimeout(r,ms));`.

## The #1 cause of flaky steps: the tab does not render

The Studio tab does not repaint in the background, so overlays (Reuse panel, calendar, time list, Related video picker) never enter the DOM and JS polls / clicks fail. **Take a tiny screenshot (scale 0.1 to 0.2) after every action that opens an overlay, then act via JS.** Keep each JS call under ~40s (CDP times out at 45s).

## Draft IDs

Drafts have no `/video/` link; pull the ID from the thumbnail URL:
```js
[...document.querySelectorAll('ytcp-video-row')].map(r=>{const h=r.innerHTML;const m=h.match(/\/vi\/([A-Za-z0-9_-]{11})\//)||h.match(/video-id="([^"]+)"/);return (m?m[1]:'?')+'|'+r.querySelector('#video-title')?.textContent.trim()}).join('\n')
```
Open a draft: `https://studio.youtube.com/channel/<CH>/videos/short?d=ud&udvid=<ID>`. Drafts open in the 4-step upload dialog.

## First reel of a series (no tagged Short to reuse yet)

1. Title: click the title box, `cmd+a`, type. Description: JS `document.querySelectorAll('ytcp-uploads-dialog #textbox')[1].focus()`, `cmd+a`, type body + footer. (`cmd+a` also clears the channel's default description, which carries Rose Homes contact info and the old -7674 Skool link. It must go.)
2. Show more > Tags > **Delete all** (channel defaults push it to 681/500) > type the series tag list ending with ",".
3. Thumbnail: `find "thumbnail file upload input"` > `file_upload` the **9:16** `covers/cover-NN.png` (Shorts slot is vertical; 16:9 covers are not used).
4. Audience: "No, it's not made for kids". Then schedule (below).

## Every other reel (3 tool calls)

**Call 1 (browser_batch):** navigate to the draft, screenshot 0.2, then:
```js
let btn;for(let i=0;i<30&&!btn;i++){await sl(500);btn=[...document.querySelectorAll('ytcp-uploads-dialog ytcp-button, ytcp-uploads-dialog button')].find(b=>b.innerText.trim()==='Reuse details');}await sl(1500);btn.click();'ok'
```
screenshot 0.2, then pick the series' first (tagged) Short:
```js
let o;for(let i=0;i<20&&!o;i++){await sl(500);o=[...document.querySelectorAll('ytcp-entity-card[role=option]')].find(e=>(e.innerText||'').includes('<SOURCE TITLE>'));}o.click();await sl(2000);'ok'
```
screenshot, then **uncheck Title and Description with coordinate clicks** (they sat at (435,152) and (435,218); confirm on the screenshot). JS clicks on these checkboxes do not stick. Then verify and apply:
```js
const dlg=document.querySelector('ytcp-uploads-reuse-details-selection-dialog');const st=[...dlg.querySelectorAll('ytcp-checkbox-lit')].map(c=>c.hasAttribute('checked'));if(st[0]||st[1]||!st[2])throw new Error('bad state '+st);dlg.querySelector('#select-button').click();await sl(2500);document.querySelectorAll('ytcp-uploads-dialog #textbox')[0].focus();'ok'
```
Expected state `false,false,true,true,true,true`. Reuse copies tags, language, category, remixing.
Then title (`cmd+a`, type), description (JS focus `#textbox`[1], `cmd+a`, type). Verify: click `#toggle-button`, print both textboxes, check tags count with `/\d+\/500/`. Finally `find "thumbnail file upload input"` for the ref.

**Call 2:** `file_upload` the 9:16 cover to that ref.

**Call 3 (browser_batch): schedule.** Next x3, expand Schedule, pick the time:
```js
const TIME='9:00 AM';await sl(2000);const d=document.querySelector('ytcp-uploads-dialog');for(let i=0;i<3;i++){d.querySelector('#next-button').click();await sl(1300);}d.querySelector('#second-container-expand-button').click();await sl(1300);const p=d.querySelector('ytcp-datetime-picker');const ti=[...p.querySelectorAll('input')].find(i=>/AM|PM/.test(i.value));ti.click();let it=[];for(let k=0;k<10&&!it.length;k++){await sl(400);it=[...document.querySelectorAll('tp-yt-paper-item')].filter(i=>i.innerText.trim().replace(/\s/g,' ')===TIME);}if(!it.length)throw new Error('no list');it[0].scrollIntoView({block:'center'});it[0].click();'ok'
```
(`tp-yt-paper-item` sits in a fixed overlay, `offsetParent` is null: do not filter on it. Times are 15-minute steps.)
screenshot 0.2 > `document.querySelector('ytcp-uploads-dialog ytcp-datetime-picker #datepicker-trigger').click()` > wait 1 > screenshot 0.2 (skip it and you get "no month") > pick day, verify, schedule:
```js
const MON='OCT 2026',DAY='7',TIME='2:00 PM',LABEL='Oct 7, 2026';const d=document.querySelector('ytcp-uploads-dialog');const p=d.querySelector('ytcp-datetime-picker');const m=[...document.querySelectorAll('ytcp-scrollable-calendar .calendar-month')].find(x=>x.innerText.trim().toUpperCase().startsWith(MON));if(!m)throw new Error('no month');[...m.querySelectorAll('span.calendar-day')].find(s=>s.innerText.trim()===DAY).click();await sl(1000);const s=p.innerText+' '+[...p.querySelectorAll('input')].map(i=>i.value).join(' ');if(!s.includes(LABEL)||!s.replace(/\s/g,' ').includes(TIME))throw new Error('mismatch '+s);d.querySelector('#done-button').click();let t='';for(let k=0;k<24&&!t;k++){await sl(500);const x=[...document.querySelectorAll('ytcp-dialog, tp-yt-paper-dialog, ytcp-video-share-dialog')].map(e=>e.innerText).find(e=>e.includes('Video scheduled'));t=x?x.replace(/\s+/g,' ').slice(0,110):'';}t||'NOT CONFIRMED'
```
Timezone shows GMT-0700 (local). Do not touch the timezone control.

## Verify all scheduled

```js
const rows=[...document.querySelectorAll('ytcp-video-row')].map(r=>[r.querySelector('#video-title')?.innerText.trim(),r.querySelector('.tablecell-visibility')?.innerText.replace(/\s+/g,' ').trim(),r.querySelector('.tablecell-date')?.innerText.replace(/\s+/g,' ').trim()]);'sched='+rows.filter(r=>r[1]==='Scheduled').length+'\n'+rows.map(r=>r.join(' | ')).join('\n')
```
Scheduled rows now have `a[href*="/video/"]`; `href.split('/')[2]` is the ID.

## Related video (link each Short to its long-form)

Per Short: navigate `studio.youtube.com/video/<ID>/edit`, wait 3, screenshot 0.1, open the field (a button search by aria/innerText FAILS; use the dropdown trigger):
```js
let l;for(let i=0;i<20&&!l;i++){await sl(500);l=[...document.querySelectorAll('ytcp-dropdown-trigger .label-text')].find(e=>e.textContent.includes('Related video'));}const t=l.closest('ytcp-dropdown-trigger');t.scrollIntoView();(t.querySelector('[role=button]')||t).click();'ok'
```
wait 1, screenshot 0.1, then pick (T = text on the long-form card, Q = search fallback), save, verify:
```js
const T='<card text>',Q='<search term>';let c;for(let i=0;i<8&&!c;i++){await sl(500);c=[...document.querySelectorAll('ytcp-entity-card')].find(e=>(e.innerText||'').includes(T));}if(!c){const inp=[...document.querySelectorAll('input')].find(i=>/search your videos/i.test(i.placeholder||i.getAttribute('aria-label')||''));inp.focus();inp.value=Q;inp.dispatchEvent(new Event('input',{bubbles:true}));for(let i=0;i<16&&!c;i++){await sl(500);c=[...document.querySelectorAll('ytcp-entity-card')].find(e=>(e.innerText||'').includes(T));}}if(!c)throw new Error('no card');c.click();await sl(1500);document.querySelector('#save').click();await sl(3000);const s=document.querySelector('#save');const l=[...document.querySelectorAll('ytcp-dropdown-trigger .label-text')].find(e=>e.textContent.includes('Related video'));'saved='+s.hasAttribute('disabled')+' | '+l.closest('ytcp-dropdown-trigger').innerText.replace(/\s+/g,' ')
```
Success = `saved=true | Related video <long-form title>`. 4 Shorts per browser_batch works.
Sept 2026 long-forms: WSU `9aGR8tPyD0A` (card "The Weekly Seller Update That Run..."), OH `ErIMEKoSFPM` (card "Automate My Open House...", search "Open House Follow-Up").

## Failed approaches (do not repeat)

- `document.execCommand('insertText')` into `#textbox`: reports success, DOM keeps old text. Use JS `.focus()` + real `cmd+a` / type.
- Coordinate clicks on overlays with no screenshot before them.
- JS clicks on the Reuse-dialog checkboxes.
- Clicking Schedule right after the calendar closes (click gets eaten). Use `#done-button` + "Video scheduled" check.
- Batching date + time on the first-reel path: did not stick. Time first, then the calendar day, step by step.
- Uploading MP4s through `file_upload` (10 MB cap).
