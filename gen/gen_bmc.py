import os
from ga_style import (svg_open, svg_close, header, box,
                      NAVY, BLUE, TEAL_DK, TINT_NAVY, TINT_BLUE, TINT_TEAL)

W, H = 1600, 1040
m, gap = 40, 12
usable = W - 2 * m
cw = (usable - 4 * gap) / 5
cols = [m + i * (cw + gap) for i in range(5)]
gy = 112
strip_h = 150
grid_bottom = H - m - strip_h - gap
gh = grid_bottom - gy
rh = (gh - gap) / 2
row2y = gy + rh + gap

p = [svg_open(W, H), header(W, "Business Model Canvas", "Los 9 bloques de Osterwalder")]

p.append(box(cols[0], gy, cw, gh, 1, "Socios clave", [
    "• Proveedores de hosting / cloud",
    "• Herramientas SaaS de terceros (integraciones)",
    "• Contadores y asesores que refieren",
    "• Desarrolladores freelance",
], NAVY, TINT_NAVY))

p.append(box(cols[1], gy, cw, rh, 2, "Actividades clave", [
    "• Desarrollo de software",
    "• Implementación / onboarding",
    "• Soporte técnico",
    "• Levantamiento de requerimientos",
    "• Venta consultiva",
], BLUE, TINT_BLUE))

p.append(box(cols[1], row2y, cw, rh, 3, "Recursos clave", [
    "• Equipo de desarrollo",
    "• Base de código reutilizable",
    "• Conocimiento del negocio del cliente",
    "• Marca e infraestructura cloud",
], TEAL_DK, TINT_TEAL))

p.append(box(cols[2], gy, cw, gh, 4, "Propuesta de valor", [
    "Sistemas de gestión personalizados, accesibles y con soporte cercano. Automatizan procesos y dan visibilidad con dashboards.",
    "",
    "“Ordena tu negocio, decide con datos.”",
], TEAL_DK, TINT_TEAL))

p.append(box(cols[3], gy, cw, rh, 5, "Relación con clientes", [
    "• Atención cercana y personalizada",
    "• Soporte continuo (WhatsApp / reuniones)",
    "• Mejora continua del sistema",
], BLUE, TINT_BLUE))

p.append(box(cols[3], row2y, cw, rh, 6, "Canales", [
    "• Referidos (canal principal)",
    "• LinkedIn y networking",
    "• Visitas comerciales directas",
    "• Web + WhatsApp",
], NAVY, TINT_NAVY))

p.append(box(cols[4], gy, cw, gh, 7, "Segmentos de clientes", [
    "• Pymes y negocios en crecimiento",
    "• Pequeñas (10-50) al inicio",
    "• Comercios, distribuidoras y servicios",
    "• Chile primero, expansión a LATAM",
], NAVY, TINT_NAVY))

sy = grid_bottom + gap
half = (usable - gap) / 2
p.append(box(m, sy, half, strip_h, 8, "Estructura de costos", [
    "Desarrollo · Hosting · Herramientas de software · Diseño · Soporte · Ventas y marketing · Administración",
], NAVY, TINT_NAVY))
p.append(box(m + half + gap, sy, half, strip_h, 9, "Fuentes de ingreso", [
    "Setup inicial de implementación (one-time)  +  Mensualidad recurrente (MRR)  +  Soporte  +  Capacitación",
], TEAL_DK, TINT_TEAL))

p.append(svg_close())
dst = os.path.join(os.path.dirname(__file__), "..", "img", "business-model-canvas.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
