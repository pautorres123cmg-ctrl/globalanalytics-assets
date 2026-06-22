import os
from ga_style import (svg_open, svg_close, header, box, text,
                      NAVY, BLUE, TEAL_DK, TEAL, WHITE, MUTED,
                      TINT_NAVY, TINT_BLUE, TINT_TEAL)

W, H = 1600, 1040
p = [svg_open(W, H), header(W, "Value Proposition Canvas", "Encaje entre oferta y necesidad")]

# Dos paneles
pw = 700
lx, rx = 40, W - 40 - pw          # left 40, right 860
py, ph = 130, 860

# Contenedores
p.append(f'<rect x="{lx}" y="{py}" width="{pw}" height="{ph}" rx="20" fill="{TINT_TEAL}" stroke="{TEAL}" stroke-opacity="0.4"/>')
p.append(f'<rect x="{rx}" y="{py}" width="{pw}" height="{ph}" rx="20" fill="{TINT_NAVY}" stroke="{NAVY}" stroke-opacity="0.25"/>')

# Títulos de panel + icono (cuadrado / círculo)
p.append(f'<rect x="{lx+28}" y="{py+26}" width="26" height="26" rx="5" fill="{TEAL_DK}"/>')
p.append(text(lx+68, py+46, "MAPA DE VALOR", size=18, color=TEAL_DK, weight="800", spacing=0.5))
p.append(text(lx+68, py+66, "Lo que ofrecemos", size=12.5, color=MUTED))

p.append(f'<circle cx="{rx+41}" cy="{py+39}" r="14" fill="{NAVY}"/>')
p.append(text(rx+68, py+46, "PERFIL DEL CLIENTE", size=18, color=NAVY, weight="800", spacing=0.5))
p.append(text(rx+68, py+66, "Lo que el cliente necesita", size=12.5, color=MUTED))

# Sub-cajas
inner_w = pw - 56
bx_l = lx + 28
bx_r = rx + 28
top = py + 86
bh = (ph - 86 - 2*14 - 24) / 3   # 3 cajas
def yy(i): return top + i*(bh+14)

# Izquierda: Mapa de valor
p.append(box(bx_l, yy(0), inner_w, bh, None, "Productos y servicios", [
    "SaaS de gestión personalizado, dashboards, integraciones, soporte y capacitación.",
], TEAL_DK, WHITE))
p.append(box(bx_l, yy(1), inner_w, bh, None, "Aliviadores de dolor", [
    "• Automatizan tareas manuales → menos tiempo y errores",
    "• Centralizan la información → visibilidad real",
    "• Precio accesible y a medida → sin pagar de más",
], TEAL_DK, WHITE))
p.append(box(bx_l, yy(2), inner_w, bh, None, "Creadores de alegría", [
    "• Personalización rápida al rubro del cliente",
    "• Soporte humano y cercano",
    "• Mejora continua del sistema",
], TEAL_DK, WHITE))

# Derecha: Perfil del cliente
p.append(box(bx_r, yy(0), inner_w, bh, None, "Trabajos del cliente", [
    "• Gestionar ventas, stock, clientes y facturación",
    "• Decidir con información confiable",
    "• Profesionalizar la operación al crecer",
], NAVY, WHITE))
p.append(box(bx_r, yy(1), inner_w, bh, None, "Dolores (pains)", [
    "• Procesos manuales y duplicados en Excel",
    "• Sin visibilidad en tiempo real",
    "• ERPs grandes caros y complejos",
], BLUE, WHITE))
p.append(box(bx_r, yy(2), inner_w, bh, None, "Alegrías (gains)", [
    "• Ahorro de tiempo y menos errores",
    "• Dashboards claros para decidir",
    "• Soporte que responde rápido",
], NAVY, WHITE))

# Conector "Encaje" al centro
cxc = (lx + pw + rx) / 2
cyc = py + ph/2
p.append(f'<circle cx="{cxc}" cy="{cyc}" r="44" fill="{WHITE}" stroke="{BLUE}" stroke-width="2.5"/>')
p.append(text(cxc, cyc-4, "ENCAJE", size=13, color=BLUE, weight="800", anchor="middle"))
p.append(text(cxc, cyc+15, "(fit)", size=12, color=MUTED, anchor="middle"))
p.append(f'<path d="M {cxc-70} {cyc} L {cxc-46} {cyc}" stroke="{TEAL_DK}" stroke-width="3" marker-end="url(#ar)"/>')
p.append(f'<path d="M {cxc+70} {cyc} L {cxc+46} {cyc}" stroke="{NAVY}" stroke-width="3" marker-end="url(#ar)"/>')
p.insert(1, f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{NAVY}"/></marker></defs>')

p.append(svg_close())
dst = os.path.join(os.path.dirname(__file__), "..", "img", "value-proposition-canvas.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
