#!/usr/bin/env python3
import math, io, time, urllib.request
from PIL import Image, ImageOps, ImageEnhance

Z = 12
TILE = 256
SCALE = 1
# bbox of the Las Vegas valley (west, south, east, north)
WEST, SOUTH, EAST, NORTH = -115.42, 35.94, -114.86, 36.34

def deg2num(lat, lon, z):
    lat_r = math.radians(lat)
    n = 2 ** z
    x = (lon + 180.0) / 360.0 * n
    y = (1.0 - math.asinh(math.tan(lat_r)) / math.pi) / 2.0 * n
    return x, y

# tile index ranges
xw, yn = deg2num(NORTH, WEST, Z)
xe, ys = deg2num(SOUTH, EAST, Z)
xt_min, xt_max = math.floor(xw), math.floor(xe)
yt_min, yt_max = math.floor(yn), math.floor(ys)

ncols = xt_max - xt_min + 1
nrows = yt_max - yt_min + 1
print(f"z={Z} tiles {ncols}x{nrows} = {ncols*nrows}")

canvas = Image.new("RGB", (ncols*TILE, nrows*TILE), (245,245,242))
hdr = {"User-Agent":"RoseHomesLV-RelocationGuide/1.0 (personal real estate guide; ryan@rosehomeslv.com)"}
i = 0
for xt in range(xt_min, xt_max+1):
    for yt in range(yt_min, yt_max+1):
        url = f"https://tile.openstreetmap.org/{Z}/{xt}/{yt}.png"
        req = urllib.request.Request(url, headers=hdr)
        data = urllib.request.urlopen(req, timeout=30).read()
        tile = Image.open(io.BytesIO(data)).convert("RGB")
        canvas.paste(tile, ((xt-xt_min)*TILE, (yt-yt_min)*TILE))
        i += 1
        time.sleep(0.05)
print(f"downloaded {i} tiles")

# crop to exact bbox
origin_x = xt_min * TILE
origin_y = yt_min * TILE
def px(lat, lon):
    gx, gy = deg2num(lat, lon, Z)
    return gx*TILE - origin_x, gy*TILE - origin_y
L, T = px(NORTH, WEST)
R, B = px(SOUTH, EAST)
L, T, R, B = int(L), int(T), int(R), int(B)
crop = canvas.crop((L, T, R, B))
cw, ch = crop.size
print("crop", cw, ch, "aspect", round(cw/ch,3))

# brand duotone: navy features on a warm cream land
gray = ImageOps.grayscale(crop)
# darken mid/dark features (roads casings, highways, labels) so the network reads,
# keep the light land bright
gray = gray.point(lambda v: 0 if v < 120 else min(255, int((v-120)*(255/135))))
gray = ImageEnhance.Contrast(gray).enhance(1.15)
duo = ImageOps.colorize(gray, black=(24,31,48), mid=(120,124,140), white=(244,240,231))

# downscale to display width
outw = 1400
outh = round(outw * ch / cw)
duo = duo.resize((outw, outh), Image.LANCZOS)
duo.save("assets/img/vegas-map.png")
print("saved assets/img/vegas-map.png", duo.size)

# emit label percentages
pts = {
    "strip":        (36.113, -115.173),
    "summerlin":    (36.155, -115.330),
    "centennial":   (36.285, -115.255),
    "northlv":      (36.235, -115.120),
    "downtown":     (36.168, -115.140),
    "springvalley": (36.108, -115.248),
    "henderson":    (36.030, -115.045),
    "lakelv":       (36.108, -114.935),
    "shighlands":   (35.998, -115.190),
}
print("--- percentages (x%, y%) ---")
for k,(la,lo) in pts.items():
    x,y = px(la,lo)
    xp = (x - L)/cw*100
    yp = (y - T)/ch*100
    print(f'{k}: {xp:.1f} {yp:.1f}')
