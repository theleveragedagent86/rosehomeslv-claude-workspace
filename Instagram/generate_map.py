#!/usr/bin/env python3
"""Generate annotated satellite map of Las Vegas showing all 7 community locations."""

import urllib.request
from PIL import Image, ImageDraw, ImageFont
import os
import math

BASE_DIR = "/Users/ryanrose/Downloads/Claude/Instagram"
OUTPUT = os.path.join(BASE_DIR, "vegas_community_map.png")

# ── Bounding box for Las Vegas valley (west, south, east, north) ──
# Focused on the south valley where all communities are located
BBOX_W, BBOX_S, BBOX_E, BBOX_N = -115.38, 35.92, -114.98, 36.18
IMG_W, IMG_H = 900, 750


def download_esri_image(service, transparent=False):
    """Download a map image from ESRI ArcGIS REST services."""
    trans = "&transparent=true" if transparent else ""
    url = (
        f"https://server.arcgisonline.com/arcgis/rest/services/{service}/MapServer/export"
        f"?bbox={BBOX_W},{BBOX_S},{BBOX_E},{BBOX_N}"
        f"&bboxSR=4326&size={IMG_W},{IMG_H}&imageSR=4326"
        f"&format=png{trans}&f=image"
    )
    path = os.path.join(BASE_DIR, f"_temp_{service.replace('/', '_')}.png")
    print(f"  Downloading {service}...")
    urllib.request.urlretrieve(url, path)
    return Image.open(path).convert("RGBA")


def geo_to_pixel(lon, lat):
    """Convert longitude/latitude to pixel coordinates on the map image."""
    x = (lon - BBOX_W) / (BBOX_E - BBOX_W) * IMG_W
    y = (1 - (lat - BBOX_S) / (BBOX_N - BBOX_S)) * IMG_H
    return int(x), int(y)


def get_font(size, bold=True):
    """Try to load a system font, falling back to default."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for fp in font_paths:
        try:
            return ImageFont.truetype(fp, size, index=1 if bold and fp.endswith('.ttc') else 0)
        except Exception:
            continue
    return ImageFont.load_default()


def draw_marker(draw, x, y, num, color, radius=20):
    """Draw a numbered circle marker with white border and drop shadow."""
    # Drop shadow
    shadow_offset = 2
    draw.ellipse(
        [x - radius + shadow_offset, y - radius + shadow_offset,
         x + radius + shadow_offset, y + radius + shadow_offset],
        fill=(0, 0, 0, 80)
    )
    # White border
    draw.ellipse(
        [x - radius - 3, y - radius - 3, x + radius + 3, y + radius + 3],
        fill=(255, 255, 255, 240)
    )
    # Colored circle
    draw.ellipse(
        [x - radius, y - radius, x + radius, y + radius],
        fill=color
    )
    # Number
    font = get_font(22, bold=True)
    text = str(num)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x - tw / 2, y - th / 2 - 2), text, fill=(255, 255, 255), font=font)


def draw_label(draw, x, y, text, size=14, color=(255, 255, 255, 200)):
    """Draw a text label with semi-transparent background."""
    font = get_font(size, bold=False)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    padding = 4
    # Background box
    draw.rounded_rectangle(
        [x - padding, y - padding, x + tw + padding, y + th + padding],
        radius=3,
        fill=(0, 0, 0, 120)
    )
    draw.text((x, y), text, fill=color, font=font)


def main():
    print("Generating Las Vegas community map...")

    # Step 1: Download satellite base map
    try:
        satellite = download_esri_image("World_Imagery")
        print(f"  Satellite image: {satellite.size}")
    except Exception as e:
        print(f"  Failed to download satellite: {e}")
        print("  Falling back to terrain...")
        try:
            satellite = download_esri_image("World_Topo_Map")
        except Exception as e2:
            print(f"  Also failed: {e2}")
            return

    # Step 2: Download road/label overlay
    try:
        roads = download_esri_image("Reference/World_Transportation", transparent=True)
        satellite = Image.alpha_composite(satellite, roads)
        print("  Road overlay applied")
    except Exception as e:
        print(f"  Road overlay failed (continuing without): {e}")

    # Step 3: Download place name labels overlay
    try:
        labels = download_esri_image("Reference/World_Boundaries_and_Places", transparent=True)
        satellite = Image.alpha_composite(satellite, labels)
        print("  Labels overlay applied")
    except Exception as e:
        print(f"  Labels overlay failed (continuing without): {e}")

    # Step 4: Add community markers
    draw = ImageDraw.Draw(satellite, "RGBA")

    # Community data: (number, name, longitude, latitude, color_rgb)
    communities = [
        (1, "Lexington Chase",       -115.279, 36.028, (198, 40, 40)),     # Red
        (2, "Ironwood",              -115.278, 36.048, (21, 101, 192)),    # Blue
        (3, "Delamar",               -115.170, 35.985, (46, 125, 50)),     # Green
        (4, "Southwind",             -115.302, 36.012, (123, 31, 162)),    # Purple
        (5, "Hinson Hills",          -115.222, 36.033, (230, 81, 0)),      # Orange
        (6, "Lucere at Inspirada",   -115.082, 35.962, (0, 131, 143)),     # Teal
        (7, "Sienna Ridge",          -115.298, 36.108, (93, 64, 55)),      # Brown
    ]

    for num, name, lon, lat, color in communities:
        px, py = geo_to_pixel(lon, lat)
        draw_marker(draw, px, py, num, color, radius=20)
        print(f"  Marker {num} ({name}): pixel ({px}, {py})")

    # Step 5: Add small community name labels next to markers
    label_font = get_font(11, bold=True)
    for num, name, lon, lat, color in communities:
        px, py = geo_to_pixel(lon, lat)
        # Position label to the right of the marker, slightly above
        label_x = px + 25
        label_y = py - 8
        # For markers on the right side, put label to the left
        if px > IMG_W * 0.7:
            bbox = draw.textbbox((0, 0), name, font=label_font)
            tw = bbox[2] - bbox[0]
            label_x = px - tw - 30
        draw_label(draw, label_x, label_y, name, size=11)

    # Step 6: Convert to RGB and save
    final = satellite.convert("RGB")
    final.save(OUTPUT, quality=95)
    print(f"\nMap saved: {OUTPUT}")
    print(f"File size: {os.path.getsize(OUTPUT):,} bytes")

    # Clean up temp files
    for f in os.listdir(BASE_DIR):
        if f.startswith("_temp_"):
            os.remove(os.path.join(BASE_DIR, f))


if __name__ == "__main__":
    main()
