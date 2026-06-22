import os
from ga_style import (svg_open, svg_close, header, box, text,
                      NAVY, BLUE, TEAL_DK, MUTED)

W, H = 1600, 1040
GREEN = "#0E9E6E"
RED = "#E0564B"
AMBER = "#D98A14"
T_GREEN = "#EAFBF3"
T_RED = "#FDEEEC"
T_BLUE = "#EEF3FF"
T_AMBER = "#FDF4E5"

p = [svg_open(W, H), header(W, "Análisis FODA", "Fortalezas · Oportunidades · Debilidades · Amenazas")]

m, gap = 40, 14
top = 150
labw = 34                      # franja para etiquetas de eje
gx = m + labw
gw = (W - gx - m - gap) / 2
gh = (H - top - m - gap) / 2

def quad(col, row): return (gx + col*(gw+gap), top + row*(gh+gap))

# Etiquetas de eje (rotadas vía transform)
p.append(f'<text x="{m+18}" y="{top+gh*0.6}" text-anchor="middle" transform="rotate(-90 {m+18} {top+gh*0.6})" style="font-family:Montserrat,Arial,sans-serif;font-size:12px;font-weight:700;fill:{MUTED};letter-spacing:1px">INTERNO</text>')
p.append(f'<text x="{m+18}" y="{top+gh+gap+gh*0.6}" text-anchor="middle" transform="rotate(-90 {m+18} {top+gh+gap+gh*0.6})" style="font-family:Montserrat,Arial,sans-serif;font-size:12px;font-weight:700;fill:{MUTED};letter-spacing:1px">EXTERNO</text>')
p.append(text(gx+gw*0.5, top-10, "POSITIVO", size=12, color=MUTED, weight="700", anchor="middle", spacing=1))
p.append(text(gx+gw+gap+gw*0.5, top-10, "NEGATIVO", size=12, color=MUTED, weight="700", anchor="middle", spacing=1))

x, y = quad(0, 0)
p.append(box(x, y, gw, gh, None, "Fortalezas", [
    "• Cercanía y trato directo con el cliente",
    "• Personalización rápida y flexible",
    "• Menor costo que un ERP grande",
    "• Conocimiento del negocio del cliente",
    "• Producto + acompañamiento continuo",
], GREEN, T_GREEN))

x, y = quad(1, 0)
p.append(box(x, y, gw, gh, None, "Debilidades", [
    "• Equipo pequeño / capacidad limitada",
    "• Marca aún poco conocida",
    "• Dependencia de pocos clientes al inicio",
    "• Procesos internos por formalizar",
    "(propuesta — ajustar con tu realidad)",
], RED, T_RED))

x, y = quad(0, 1)
p.append(box(x, y, gw, gh, None, "Oportunidades", [
    "• Muchas pymes aún operan en Excel",
    "• Tendencia a digitalización y datos",
    "• Demanda de software a medida accesible",
    "• Expansión futura a LATAM",
], BLUE, T_BLUE))

x, y = quad(1, 1)
p.append(box(x, y, gw, gh, None, "Amenazas", [
    "• ERPs y soluciones no-code bajando precios",
    "• Nuevos competidores / freelancers",
    "• Ciclos económicos que afectan a las pymes",
    "• Cambios tecnológicos rápidos",
], AMBER, T_AMBER))

p.append(svg_close())
dst = os.path.join(os.path.dirname(__file__), "..", "img", "foda.svg")
open(dst, "w").write("\n".join(p))
print("ok", dst)
