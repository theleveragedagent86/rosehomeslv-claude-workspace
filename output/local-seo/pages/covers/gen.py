import subprocess, os

PLATE = "plate.png"

VARIANTS = [
  # name, w, h, layout, headline, hsize, subsize, eyesize, show_sub, show_cta
  ("facebook-cover",  1640, 624, "center", "New Construction<br>Homes in Las Vegas", 88, 26, 15, True,  True),
  ("linkedin-banner", 1584, 396, "left",   "New Construction Homes<br>in Las Vegas",  60, 21, 13, True,  True),
  ("x-header",        1500, 500, "center", "New Construction<br>Homes in Las Vegas", 72, 22, 13, True,  False),
  ("og-share",        1200, 630, "left",   "New Construction<br>Homes in Las Vegas", 68, 24, 14, True,  True),
]

TPL = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@600;700&family=Inter:wght@400;500&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{w}px;height:{h}px;overflow:hidden}}
.wrap{{position:relative;width:{w}px;height:{h}px;overflow:hidden}}
.plate{{position:absolute;inset:0;background:url('{plate}') center/cover no-repeat}}
.scrim{{position:absolute;inset:0;background:{scrim}}}
.grain{{position:absolute;inset:0;opacity:.06;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/></filter><rect width='120' height='120' filter='url(%23n)'/></svg>")}}
.rule{{position:absolute;left:0;right:0;top:0;height:5px;background:#C9A86E}}
.content{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
  align-items:{align};text-align:{talign};padding:0 {pad}px;{extra}}}
.eyebrow{{font-family:Montserrat,sans-serif;font-weight:700;font-size:{eyesize}px;letter-spacing:.22em;
  color:#C9A86E;text-transform:uppercase;margin-bottom:{eb}px}}
h1{{font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:{hsize}px;line-height:1.06;
  letter-spacing:-.02em;color:#fff;text-shadow:0 2px 24px rgba(12,20,35,.55)}}
.sub{{font-family:Inter,system-ui,sans-serif;font-weight:400;font-size:{subsize}px;line-height:1.5;
  color:rgba(255,255,255,.90);margin-top:{sm}px;max-width:{smax}px;text-shadow:0 1px 12px rgba(12,20,35,.5)}}
.cta{{display:flex;align-items:center;gap:14px;margin-top:{cm}px;font-family:Montserrat,sans-serif;
  font-weight:600;font-size:{eyesize}px;letter-spacing:.14em;color:#fff;text-transform:uppercase}}
.dot{{width:6px;height:6px;border-radius:50%;background:#C9A86E;flex:none}}
</style>
<div class="wrap">
  <div class="plate"></div><div class="scrim"></div><div class="grain"></div><div class="rule"></div>
  <div class="content">
    <div class="eyebrow">Rose Homes LV &nbsp;&middot;&nbsp; Real Broker, LLC</div>
    <h1>{headline}</h1>
    {sub}
    {cta}
  </div>
</div>"""

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

for name, w, h, layout, headline, hsize, subsize, eyesize, show_sub, show_cta in VARIANTS:
    if layout == "center":
        scrim = "linear-gradient(180deg,rgba(28,35,51,.62) 0%,rgba(28,35,51,.50) 55%,rgba(28,35,51,.70) 100%)"
        align, talign, pad, extra = "center", "center", int(w*0.10), ""
        smax = int(w*0.62)
    else:
        scrim = ("linear-gradient(90deg,rgba(28,35,51,.92) 0%,rgba(28,35,51,.86) 46%,"
                 "rgba(28,35,51,.62) 72%,rgba(28,35,51,.22) 100%)")
        align, talign, pad, extra = "flex-start", "left", int(w*0.055), ""
        smax = int(w*0.80)

    sub = f'<div class="sub">The agent in the model home works for the builder.<br>I work for you.</div>' if show_sub else ""
    cta = ('<div class="cta">rosehomeslv.com <span class="dot"></span> 702 747 5921</div>') if show_cta else ""

    html = TPL.format(w=w, h=h, plate=os.path.abspath(PLATE), scrim=scrim, align=align, talign=talign,
                      pad=pad, extra=extra, eyesize=eyesize, hsize=hsize, subsize=subsize,
                      headline=headline, sub=sub, cta=cta,
                      eb=max(10, int(h*0.035)), sm=max(10, int(h*0.038)), cm=max(12, int(h*0.055)),
                      smax=smax)
    f = f"_{name}.html"
    open(f, "w").write(html)
    out = f"{name}-{w}x{h}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", f"--window-size={w},{h}",
                    "--virtual-time-budget=12000", f"--screenshot={out}",
                    f"file://{os.path.abspath(f)}"],
                   capture_output=True)
    print(name, os.path.exists(out))
