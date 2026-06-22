import os
from ga_style import (svg_open, svg_close, header, text, esc,
                      NAVY, NAVY2, BLUE, TEAL, TEAL_DK, INK, MUTED, LINE,
                      WHITE, PAPER, TINT_NAVY)

W, H = 1600, 1040
p = [svg_open(W, H, PAPER), header(W, "Brand Board", "Sistema visual de marca")]

m = 40

def section(y, label):
    p.append(text(m, y, label, size=13, color=BLUE, weight="800", spacing=1.5))
    p.append(f'<rect x="{m}" y="{y+8}" width="40" height="3" fill="{TEAL}"/>')

def logo_block(x, yb, color_g, color_a, sub_color):
    p.append(text(x, yb, "GLOBAL", size=30, color=color_g, weight="800", spacing=0.5))
    p.append(text(x+148, yb, "ANALYTICS", size=30, color=color_a, weight="800", spacing=0.5))
    p.append(text(x+1, yb+24, "Inteligencia, estrategia y alcance global",
                  size=12.5, color=sub_color, italic=True))

# 01 LOGOTIPO
section(128, "01 · LOGOTIPO")
p.append(f'<rect x="{m}" y="148" width="730" height="150" rx="14" fill="{WHITE}" stroke="{LINE}"/>')
logo_block(m+40, 232, NAVY, BLUE, TEAL_DK)
p.append(f'<rect x="{m+760}" y="148" width="730" height="150" rx="14" fill="{NAVY}"/>')
logo_block(m+800, 232, WHITE, "#7FB0FF", TEAL)

# 02 PALETA
section(338, "02 · PALETA DE COLOR")
swatches = [
    ("Navy", "#0A1D3D"), ("Navy 2", "#10264B"), ("Azul", "#1E5BFF"),
    ("Teal", "#00BFAE"), ("Ink", "#1E2C45"), ("Gris", "#5A6A82"),
    ("Línea", "#DCE5EF"), ("Paper", "#F8FBFF"),
]
sw_w, sw_h, sgap = 178, 110, 8
sx = m
sy = 360
for i, (name, hexv) in enumerate(swatches):
    x = sx + i * (sw_w + sgap)
    border = f' stroke="{LINE}"' if hexv in ("#DCE5EF", "#F8FBFF") else ''
    p.append(f'<rect x="{x}" y="{sy}" width="{sw_w}" height="{sw_h}" rx="10" fill="{hexv}"{border}/>')
    tcol = INK if hexv in ("#DCE5EF", "#F8FBFF") else WHITE
    p.append(text(x+14, sy+sw_h-32, name, size=14, color=tcol, weight="700"))
    p.append(text(x+14, sy+sw_h-12, hexv.upper(), size=12.5, color=tcol))

# 03 TIPOGRAFIA
section(520, "03 · TIPOGRAFÍA")
p.append(f'<rect x="{m}" y="542" width="730" height="150" rx="14" fill="{WHITE}" stroke="{LINE}"/>')
p.append(text(m+30, 588, "Montserrat", size=30, color=NAVY, weight="800"))
p.append(text(m+30, 616, "Títulos y marca · 700–800", size=14, color=MUTED))
p.append(text(m+30, 656, "AaBbCc 0123 — Aa Bb Cc Dd", size=22, color=INK, weight="700"))

p.append(f'<rect x="{m+760}" y="542" width="730" height="150" rx="14" fill="{WHITE}" stroke="{LINE}"/>')
p.append(text(m+790, 588, "Inter", size=30, color=BLUE, weight="700"))
p.append(text(m+790, 616, "Cuerpo de texto · 400–600", size=14, color=MUTED))
p.append(text(m+790, 652, "El software de gestión que se adapta a tu pyme,", size=16, color=INK))
p.append(text(m+790, 674, "ordena tus procesos y te da visibilidad real.", size=16, color=INK))

# 04 TAGLINES
section(722, "04 · TAGLINES")
p.append(f'<rect x="{m}" y="744" width="730" height="120" rx="14" fill="{TINT_NAVY}" stroke="{LINE}"/>')
p.append(text(m+30, 782, "MARCA / INSTITUCIONAL", size=12, color=MUTED, weight="700", spacing=1))
p.append(text(m+30, 812, "“Inteligencia, estrategia y alcance global.”", size=19, color=NAVY, weight="700"))
p.append(text(m+30, 846, "COMERCIAL: “Ordena tu negocio, decide con datos.”", size=15, color=TEAL_DK, weight="600"))

# 05 TONO DE VOZ
section(722 + 0, "")
p.append(text(m+760, 722, "05 · TONO DE VOZ", size=13, color=BLUE, weight="800", spacing=1.5))
p.append(f'<rect x="{m+800}" y="730" width="40" height="3" fill="{TEAL}"/>')
chips = ["Cercano", "Claro y directo", "Profesional", "Orientado a beneficios", "Confiable", "Sin jerga"]
cx, cy = m+760, 760
for ch in chips:
    wch = 22 + len(ch) * 8.6
    p.append(f'<rect x="{cx}" y="{cy}" width="{wch:.0f}" height="34" rx="17" fill="{WHITE}" stroke="{TEAL}" stroke-opacity="0.6"/>')
    p.append(text(cx + wch/2, cy+22, ch, size=13.5, color=TEAL_DK, weight="600", anchor="middle"))
    cx += wch + 12
    if cx > m + 760 + 700 - 120:
        cx = m + 760
        cy += 46
p.append(text(m+760, cy+74, "Hablamos como un asesor de confianza, en lenguaje de pyme:", size=13.5, color=MUTED))
p.append(text(m+760, cy+96, "de tiempo, control y dinero — no de tecnología por la tecnología.", size=13.5, color=MUTED))

p.append(svg_close())
dst = os.path.join(os.path.dirname(__file__), "..", "img", "brand-board.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
