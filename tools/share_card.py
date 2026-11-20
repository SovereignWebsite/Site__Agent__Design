#!/usr/bin/env python3
"""Make site/share-card.jpg, the 1200x630 link-preview card (under 300 KB). Needs Pillow and DejaVu fonts.
Run from the repository root: python3 tools/share_card.py"""
from PIL import Image, ImageDraw, ImageFont
import pathlib
W, H = 1200, 630
BG, FG, MUTED, ACCENT, LINE = "#fbf6ee", "#2a1f17", "#5e5148", "#a5432a", "#eadccd"
F = "/usr/share/fonts/truetype/dejavu/"
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
serif, sans, mono = (ImageFont.truetype(F + n, s) for n, s in (("DejaVuSerif-Bold.ttf", 92), ("DejaVuSans.ttf", 34), ("DejaVuSansMono.ttf", 28)))
# five panels: five designs, the owner picks one
x0, y0, w, h, g = 80, 380, 196, 150, 24
for i in range(5):
    x = x0 + i * (w + g)
    d.rounded_rectangle((x, y0, x + w, y0 + h), 14, outline=ACCENT if i == 2 else LINE, width=8 if i == 2 else 4, fill="#fffdf9")
    d.text((x + 18, y0 + 14), str(i + 1), font=mono, fill=ACCENT if i == 2 else MUTED)
d.rounded_rectangle((80, 80, 132, 132), 12, outline=ACCENT, width=6)
d.line([(92, 118), (102, 98), (110, 112), (114, 106), (120, 118)], fill=ACCENT, width=6, joint="curve")
d.text((152, 84), "design.b", font=mono.font_variant(size=40), fill=FG)
d.text((80, 170), "Five designs, always.", font=serif, fill=FG)
d.text((80, 290), "Guidelines, ratings and reviews for every site.", font=sans, fill=MUTED)
d.text((80, 560), "design.agents.sovereignweb.site", font=mono, fill=ACCENT)
out = pathlib.Path(__file__).resolve().parent.parent / "site" / "share-card.jpg"
im.save(out, "JPEG", quality=86, optimize=True, progressive=True)
print(out, out.stat().st_size // 1024, "KB")
