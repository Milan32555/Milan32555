"""Genera header-dark.svg y header-light.svg: "Misael." hecho de caracteres de código,
como el hero del portfolio, con un escaneo sutil (desactivado con prefers-reduced-motion)."""
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 300
STEP = 6  # separación de la grilla de glifos
GLYPHS = "{}[]()<>;:=+-*/_&|!?$#%01"
random.seed(7)

# DM Serif Display, from github.com/google/fonts (OFL), downloaded next to this script.
font = ImageFont.truetype("DMSerifDisplay.ttf", 250)
mask = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(mask)
text = "Misael."
bbox = d.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
ox = (W - tw) // 2 - bbox[0]
oy = 18 - bbox[1]
d.text((ox, oy), text, font=font, fill=255)
# El punto final va en el color de acento, como en el sitio.
dot_x0 = ox + d.textbbox((0, 0), "Misael", font=font)[2]

# Filas de glifos por clase: 0-2 base (parpadean con distinto desfase), 3 acento.
rows: dict[tuple[int, int], list[tuple[int, str]]] = {}
for y in range(0, H - STEP, STEP):
    for x in range(0, W - STEP, STEP):
        if mask.getpixel((x + STEP // 2, y + STEP // 2)) < 128:
            continue
        cls = 3 if x >= dot_x0 else (3 if random.random() < 0.09 else random.randrange(3))
        rows.setdefault((y, cls), []).append((x, random.choice(GLYPHS)))

def esc(c: str) -> str:
    return c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def build(theme: str) -> str:
    if theme == "dark":
        base, accent, sub, scan = "#9bbcf0", "#4f8ef7", "#8b949e", "#f5b84a"
    else:
        base, accent, sub, scan = "#1b3a7a", "#1a5df5", "#57606a", "#c77d00"
    texts = []
    for (y, cls), cells in sorted(rows.items()):
        xs = " ".join(str(x) for x, _ in cells)
        chars = "".join(esc(c) for _, c in cells)
        texts.append(f'<text class="g c{cls}" x="{xs}" y="{y + STEP}">{chars}</text>')
    body = "\n".join(texts)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Misael — developer and code security reviewer">
<style>
  .g {{ font: 600 7.5px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {base}; }}
  .c3 {{ fill: {accent}; }}
  .sub {{ font: 500 17px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {sub}; letter-spacing: .04em; }}
  .sub b {{ fill: {accent}; }}
  .c0 {{ animation: f 6s ease-in-out infinite; }}
  .c1 {{ animation: f 6s ease-in-out 2s infinite; }}
  .c2 {{ animation: f 6s ease-in-out 4s infinite; }}
  @keyframes f {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .55; }} }}
  .scan {{ animation: s 7.5s cubic-bezier(.4,0,.2,1) infinite; }}
  @keyframes s {{ 0% {{ transform: translateX(-160px); opacity: 0; }} 8% {{ opacity: 1; }} 55% {{ opacity: 1; }} 70%,100% {{ transform: translateX({W + 40}px); opacity: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{ .c0,.c1,.c2,.scan {{ animation: none; }} .scan {{ opacity: 0; }} }}
</style>
<defs>
  <linearGradient id="sg" x1="0" x2="1">
    <stop offset="0" stop-color="{scan}" stop-opacity="0"/>
    <stop offset=".8" stop-color="{scan}" stop-opacity=".1"/>
    <stop offset="1" stop-color="{scan}" stop-opacity=".38"/>
  </linearGradient>
  <clipPath id="name"><rect x="0" y="0" width="{W}" height="{H - 50}"/></clipPath>
</defs>
{body}
<g clip-path="url(#name)"><rect class="scan" x="0" y="0" width="70" height="{H - 50}" fill="url(#sg)"/></g>
<text class="sub" x="{W // 2}" y="{H - 16}" text-anchor="middle">// developer · <tspan fill="{accent}">code security reviewer</tspan></text>
</svg>
'''

for theme in ("dark", "light"):
    svg = build(theme)
    open(f"assets/header-{theme}.svg", "w", encoding="utf-8").write(svg)
    print(theme, len(svg) // 1024, "KB,", sum(len(v) for v in rows.values()), "glifos")
