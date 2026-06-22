import os
from ga_style import (svg_open, svg_close, header, text,
                      NAVY, BLUE, TEAL, TEAL_DK, INK, MUTED, WHITE, LINE, PAPER)

W, H = 1600, 1000
p = [svg_open(W, H, PAPER), header(W, "Por qué Global Analytics", "Comparativa de soluciones")]

m = 40
cols = ["Criterio", "Excel /\nplanillas", "ERP\ngrande", "Global\nAnalytics"]
rows = [
    ("Costo accesible",        "mid", "no", "yes"),
    ("Personalización al rubro","no",  "mid","yes"),
    ("Rápido de implementar",  "yes", "no", "yes"),
    ("Soporte cercano",        "no",  "mid","yes"),
    ("Dashboards y visibilidad","no", "yes","yes"),
    ("Automatización",         "no",  "yes","yes"),
    ("Escala con tu negocio",  "no",  "yes","yes"),
]
# layout
tx = m
ty = 140
crit_w = 520
ccw = (W - 2*m - crit_w) / 3
col_x = [tx, tx+crit_w, tx+crit_w+ccw, tx+crit_w+2*ccw]
header_h = 70
row_h = (H - ty - header_h - m) / len(rows)

# encabezado de columnas
hdr_fill = [PAPER, "#EEF1F6", "#EEF1F6", NAVY]
for i, c in enumerate(cols):
    x = col_x[i]
    w = crit_w if i == 0 else ccw
    p.append(f'<rect x="{x}" y="{ty}" width="{w}" height="{header_h}" rx="10" fill="{hdr_fill[i]}"/>')
    lines = c.split("\n")
    tc = WHITE if i == 3 else INK
    oy = ty + header_h/2 - (len(lines)-1)*10 + 5
    for ln in lines:
        p.append(text(x + w/2, oy, ln, size=16, color=tc, weight="800", anchor="middle"))
        oy += 20

def icon(x, y, kind):
    if kind == "yes":
        p.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{TEAL}"/>')
        p.append(f'<path d="M {x-7} {y} L {x-2} {y+6} L {x+8} {y-6}" stroke="{WHITE}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    elif kind == "no":
        p.append(f'<circle cx="{x}" cy="{y}" r="15" fill="#E0564B"/>')
        p.append(f'<path d="M {x-6} {y-6} L {x+6} {y+6} M {x+6} {y-6} L {x-6} {y+6}" stroke="{WHITE}" stroke-width="3" stroke-linecap="round"/>')
    else:  # mid
        p.append(f'<circle cx="{x}" cy="{y}" r="15" fill="#D9A21A"/>')
        p.append(f'<rect x="{x-7}" y="{y-2}" width="14" height="4" rx="2" fill="{WHITE}"/>')

ry = ty + header_h
for r, (crit, a, b, c) in enumerate(rows):
    yc = ry + row_h/2
    if r % 2 == 0:
        p.append(f'<rect x="{tx}" y="{ry}" width="{W-2*m}" height="{row_h}" fill="{WHITE}"/>')
    p.append(text(col_x[0]+24, yc+6, crit, size=17, color=INK, weight="600"))
    # resaltar columna GA
    p.append(f'<rect x="{col_x[3]}" y="{ry}" width="{ccw}" height="{row_h}" fill="{TEAL}" fill-opacity="0.07"/>')
    for ci, kind in enumerate([a, b, c]):
        icon(col_x[ci+1] + ccw/2, yc, kind)
    ry += row_h
# borde columna GA
p.append(f'<rect x="{col_x[3]}" y="{ty}" width="{ccw}" height="{H-ty-m}" rx="10" fill="none" stroke="{TEAL}" stroke-width="2.5"/>')

p.append(svg_close())
dst = os.path.join(os.path.dirname(__file__), "..", "img", "comparativa.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
