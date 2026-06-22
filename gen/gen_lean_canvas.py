import os
from ga_style import (svg_open, svg_close, header, box,
                      NAVY, BLUE, TEAL_DK, TINT_NAVY, TINT_BLUE, TINT_TEAL)

W, H = 1600, 1040
m, gap, cw = 40, 12, 0
# 5 columnas
usable = W - 2 * m
cw = (usable - 4 * gap) / 5
cols = [m + i * (cw + gap) for i in range(5)]

gy = 112                      # inicio grid
strip_h = 150
grid_bottom = H - m - strip_h - gap
gh = grid_bottom - gy         # alto total grid (boxes altas)
rh = (gh - gap) / 2           # alto media fila
row2y = gy + rh + gap

parts = [svg_open(W, H), header(W, "Lean Canvas", "Modelo de negocio en una página")]

# Caja alta col1: Problema
parts.append(box(cols[0], gy, cw, gh, 1, "Problema", [
    "• Procesos desordenados en Excel o herramientas aisladas",
    "• Tareas manuales que consumen tiempo",
    "• Sin visibilidad de sus datos: ventas, stock, clientes, facturación",
], NAVY, TINT_NAVY))

# col2 fila1: Solución
parts.append(box(cols[1], gy, cw, rh, 2, "Solución", [
    "• SaaS de gestión personalizado",
    "• Automatiza procesos y muestra dashboards",
    "• Integra herramientas existentes",
    "• Atención y soporte cercano",
], BLUE, TINT_BLUE))

# col2 fila2: Métricas clave
parts.append(box(cols[1], row2y, cw, rh, 8, "Métricas clave", [
    "• Clientes activos",
    "• MRR (ingreso recurrente)",
    "• Tiempo de implementación",
    "• Renovación y referidos",
], TEAL_DK, TINT_TEAL))

# col3 alta: Propuesta de valor única (destacada)
parts.append(box(cols[2], gy, cw, gh, 3, "Propuesta de valor única", [
    "Implementamos sistemas de gestión personalizados y accesibles para que tu empresa ordene sus procesos sin pagar por software complejo que no se adapta a tu realidad.",
    "",
    "“Ordena tu negocio, decide con datos.”",
], TEAL_DK, TINT_TEAL))

# col4 fila1: Ventaja competitiva
parts.append(box(cols[3], gy, cw, rh, 9, "Ventaja competitiva", [
    "• Cercanía con el cliente",
    "• Personalización rápida",
    "• Menor costo que un ERP grande",
    "• Conocimiento del negocio",
], BLUE, TINT_BLUE))

# col4 fila2: Canales
parts.append(box(cols[3], row2y, cw, rh, 5, "Canales", [
    "• Referidos (canal principal)",
    "• LinkedIn y networking",
    "• Visitas comerciales directas",
    "• Web + WhatsApp",
], NAVY, TINT_NAVY))

# col5 alta: Segmento de clientes
parts.append(box(cols[4], gy, cw, gh, 4, "Segmento de clientes", [
    "• Pymes y negocios en crecimiento",
    "• Pequeñas (10-50 empleados) al inicio",
    "• Comercios, distribuidoras y servicios",
    "• Chile primero, expansión a LATAM",
], NAVY, TINT_NAVY))

# Strip inferior
sy = grid_bottom + gap
half = (usable - gap) / 2
parts.append(box(m, sy, half, strip_h, 7, "Estructura de costes", [
    "Desarrollo · Hosting/servidores · Herramientas de software · Diseño · Soporte · Ventas y marketing · Administración y asesorías",
], NAVY, TINT_NAVY))
parts.append(box(m + half + gap, sy, half, strip_h, 6, "Estructura de ingresos", [
    "Setup inicial de implementación (one-time)  +  Mensualidad recurrente (MRR)  +  Soporte  +  Capacitación",
], TEAL_DK, TINT_TEAL))

parts.append(svg_close())

out = "\n".join(parts)
dst = os.path.join(os.path.dirname(__file__), "..", "img", "lean-canvas.svg")
with open(dst, "w") as f:
    f.write(out)
print("ok", os.path.abspath(dst))
