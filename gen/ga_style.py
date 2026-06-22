"""Estilo de marca compartido para los gráficos de Global Analytics.
Helpers para generar SVG on-brand (canvas, infografías, etc.).
"""

# Paleta de marca
NAVY = "#0A1D3D"
NAVY2 = "#10264B"
BLUE = "#1E5BFF"
TEAL = "#00BFAE"
TEAL_DK = "#0B9B8E"
INK = "#1E2C45"
BODY = "#2A3A53"
MUTED = "#5A6A82"
LINE = "#DCE5EF"
PAPER = "#F8FBFF"
WHITE = "#FFFFFF"

# Tints suaves para fondos de caja
TINT_NAVY = "#F2F5FB"
TINT_BLUE = "#EEF3FF"
TINT_TEAL = "#E9FBF8"

FONT = "Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif"


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def wrap(text, max_chars):
    """Word-wrap simple por número aproximado de caracteres."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, size=14, color=BODY, weight="400", anchor="start",
         italic=False, spacing=None):
    style = (f'font-family:{FONT};font-size:{size}px;font-weight:{weight};'
             f'fill:{color};')
    if italic:
        style += "font-style:italic;"
    if spacing:
        style += f"letter-spacing:{spacing}px;"
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
            f'style="{style}">{esc(s)}</text>')


def box(x, y, w, h, num, title, body_lines, accent, bg, *,
        rx=14, title_size=15, body_size=14, lh=22, big_value=None):
    """Dibuja una caja de canvas con número, título y cuerpo."""
    out = []
    # sombra suave + caja
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
               f'fill="{bg}" stroke="{accent}" stroke-opacity="0.35" '
               f'stroke-width="1.5"/>')
    # franja de acento superior
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" '
               f'fill="{accent}"/>')
    pad = 18
    if num is not None:
        # badge número
        cx, cy = x + pad + 11, y + 34
        out.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{accent}"/>')
        out.append(text(cx, cy + 5, str(num), size=14, color=WHITE,
                        weight="700", anchor="middle"))
        tx = x + pad + 32
    else:
        tx = x + pad
    # título
    out.append(text(tx, y + 39, title.upper(), size=title_size,
                    color=accent, weight="700", spacing=0.5))
    # cuerpo
    ty = y + 66
    inner = int((w - 2 * pad) / (body_size * 0.5))
    if big_value:
        out.append(text(x + pad, ty + 6, big_value, size=22, color=accent,
                        weight="700"))
        ty += 34
    for raw in body_lines:
        bullet = raw.startswith("•")
        content = raw[1:].strip() if bullet else raw
        wrapped = wrap(content, inner - (2 if bullet else 0))
        for i, ln in enumerate(wrapped):
            prefix = ("•  " if (bullet and i == 0) else ("   " if bullet else ""))
            out.append(text(x + pad, ty, prefix + ln, size=body_size,
                            color=BODY))
            ty += lh
        if bullet:
            ty += 3
    return "\n".join(out)


def header(width, title, subtitle=None):
    """Cabecera de marca: logotipo textual + título de la pieza."""
    out = []
    out.append(text(40, 50, "GLOBAL", size=27, color=NAVY, weight="800",
                    spacing=0.5))
    # ancho aprox de "GLOBAL " a 27px
    out.append(text(40 + 132, 50, "ANALYTICS", size=27, color=BLUE,
                    weight="800", spacing=0.5))
    out.append(text(41, 74, "Inteligencia, estrategia y alcance global",
                    size=12.5, color=TEAL_DK, italic=True, spacing=0.3))
    out.append(text(width - 40, 52, title, size=30, color=NAVY, weight="800",
                    anchor="end", spacing=1))
    if subtitle:
        out.append(text(width - 40, 75, subtitle, size=13, color=MUTED,
                        anchor="end"))
    out.append(f'<rect x="40" y="90" width="{width-80}" height="3" rx="1.5" '
               f'fill="{TEAL}"/>')
    return "\n".join(out)


def svg_open(width, height, bg=WHITE):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
            f'height="{height}" viewBox="0 0 {width} {height}">\n'
            f'<rect width="{width}" height="{height}" fill="{bg}"/>')


def svg_close():
    return "</svg>"
