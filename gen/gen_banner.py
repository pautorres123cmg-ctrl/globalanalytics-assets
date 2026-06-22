import os
from ga_style import (svg_open, svg_close, text, NAVY, NAVY2, BLUE, TEAL, WHITE)

# Banner ancho para portada (ratio Notion ~ 1500x600)
W, H = 1600, 600
p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
# fondo degradado navy
p.append(f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#020918"/>
  <stop offset="0.5" stop-color="#0A1D3D"/>
  <stop offset="1" stop-color="#0B2B49"/>
</linearGradient>
<radialGradient id="glow" cx="0.78" cy="0.35" r="0.5">
  <stop offset="0" stop-color="#1E5BFF" stop-opacity="0.45"/>
  <stop offset="1" stop-color="#1E5BFF" stop-opacity="0"/>
</radialGradient>
</defs>''')
p.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
p.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')

# grid sutil
for gx in range(0, W, 60):
    p.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="#1E5BFF" stroke-opacity="0.05"/>')
for gy in range(0, H, 60):
    p.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="#1E5BFF" stroke-opacity="0.05"/>')

# globo + arco (isotipo estilizado) a la derecha
cx, cy, r = 1230, 300, 150
p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BLUE}" stroke-opacity="0.55" stroke-width="2.5"/>')
p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="58" fill="none" stroke="{BLUE}" stroke-opacity="0.4" stroke-width="2"/>')
p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="62" ry="{r}" fill="none" stroke="{BLUE}" stroke-opacity="0.4" stroke-width="2"/>')
p.append(f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="{BLUE}" stroke-opacity="0.4" stroke-width="2"/>')
# arco/flecha ascendente teal->azul
p.append(f'''<defs><linearGradient id="ar" x1="0" y1="1" x2="1" y2="0">
<stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>''')
p.append(f'<path d="M {cx-180} {cy+150} Q {cx-40} {cy+120} {cx+130} {cy-150}" fill="none" stroke="url(#ar)" stroke-width="12" stroke-linecap="round"/>')
p.append(f'<path d="M {cx+130} {cy-150} l -42 12 l 30 30 z" fill="{BLUE}"/>')

# Texto principal
p.append(text(90, 250, "GLOBAL", size=76, color=WHITE, weight="800", spacing=1))
p.append(text(90+352, 250, "ANALYTICS", size=76, color="#3D7BFF", weight="800", spacing=1))
p.append(f'<rect x="93" y="282" width="520" height="3" fill="{TEAL}"/>')
p.append(text(95, 326, "Inteligencia, estrategia y alcance global", size=24, color="#9FB4D6", italic=True))
p.append(text(95, 408, "Software de gestión a la medida de tu pyme.", size=30, color=WHITE, weight="600"))
# chips
chips = ["Automatiza", "Integra", "Visualiza"]
chx = 95
for ch in chips:
    w = 40 + len(ch)*15
    p.append(f'<rect x="{chx}" y="445" width="{w}" height="44" rx="22" fill="none" stroke="{TEAL}" stroke-opacity="0.7"/>')
    p.append(text(chx + w/2, 473, ch, size=18, color=TEAL, weight="600", anchor="middle"))
    chx += w + 16

p.append('</svg>')
dst = os.path.join(os.path.dirname(__file__), "..", "img", "banner.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
