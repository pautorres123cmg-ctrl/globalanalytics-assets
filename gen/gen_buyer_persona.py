import os
from ga_style import (svg_open, svg_close, header, box, text,
                      NAVY, BLUE, TEAL, TEAL_DK, INK, MUTED, WHITE, LINE,
                      PAPER, TINT_NAVY, TINT_BLUE, TINT_TEAL)

W, H = 1600, 1040
p = [svg_open(W, H, PAPER), header(W, "Buyer Persona", "Cliente ideal de Global Analytics")]

m = 40
# Tarjeta perfil (izquierda)
px, pw = m, 480
py, ph = 128, 866
p.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18" fill="{NAVY}"/>')
# avatar
ax, ay = px + pw/2, py + 120
p.append(f'<circle cx="{ax}" cy="{ay}" r="68" fill="{BLUE}"/>')
p.append(text(ax, ay+16, "DP", size=48, color=WHITE, weight="800", anchor="middle"))
p.append(text(ax, py+232, "“Don Pablo”", size=26, color=WHITE, weight="800", anchor="middle"))
p.append(text(ax, py+262, "El dueño de pyme", size=15, color=TEAL, anchor="middle"))

# datos rápidos
data = [
    ("Rol", "Dueño / gerente que decide"),
    ("Empresa", "Pyme pequeña (10-50 empleados)"),
    ("Rubro", "Comercio, distribución o servicios"),
    ("Ubicación", "Chile"),
    ("Digitalización", "Baja — vive en Excel"),
]
dy = py + 312
for k, v in data:
    p.append(text(px+34, dy, k.upper(), size=11.5, color="#8FA6C8", weight="700", spacing=0.8))
    p.append(text(px+34, dy+22, v, size=14.5, color=WHITE))
    dy += 56
# cita
p.append(f'<rect x="{px+28}" y="{dy+6}" width="{pw-56}" height="120" rx="12" fill="#10264B"/>')
p.append(text(px+46, dy+44, "“Sé que vendo, pero no", size=16, color=WHITE, italic=True))
p.append(text(px+46, dy+70, "tengo idea de mis números", size=16, color=WHITE, italic=True))
p.append(text(px+46, dy+96, "hasta fin de mes.”", size=16, color=WHITE, italic=True))

# Columna derecha: cajas
rx = px + pw + 24
rw = W - rx - m
gap = 16
bh = (ph - 3*gap) / 4
def by(i): return py + i*(bh+gap)

p.append(box(rx, by(0), rw, bh, None, "Objetivos", [
    "• Ordenar y profesionalizar la operación",
    "• Tener información confiable para decidir",
    "• Crecer sin perder el control del negocio",
], TEAL_DK, TINT_TEAL))
p.append(box(rx, by(1), rw, bh, None, "Dolores / frustraciones", [
    "• Todo en Excel y planillas duplicadas",
    "• No sabe en tiempo real qué pasa en su negocio",
    "• Los ERP grandes son caros y no se adaptan",
], BLUE, TINT_BLUE))
p.append(box(rx, by(2), rw, bh, None, "Gatillos de compra", [
    "• Un dolor concreto: perdió stock, error de factura, no sabe cuánto vende",
    "• Recomendación de alguien de confianza",
], NAVY, TINT_NAVY))
p.append(box(rx, by(3), rw, bh, None, "¿Dónde lo encuentro?", [
    "• Referidos y boca a boca (principal)",
    "• LinkedIn y networking local",
    "• Búsquedas / web + WhatsApp",
], TEAL_DK, TINT_TEAL))

p.append(svg_close())
dst = os.path.join(os.path.dirname(__file__), "..", "img", "buyer-persona.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
