import json, os, subprocess
P = json.load(open('paths.json'))

STEEL, STEEL_D = '#B4B7BB', '#C9CCD0'
WOOD, LEATHER = '#A2652C', '#7B3B1D'
INK, PAPER = '#0B0B0B', '#F5F3EF'
WHITE = '#FFFFFF'

# geometry (source px of ikon---logo.png)
MARK = (40, 15, 935, 715)       # x, y, w, h  (mark ~55..958, 27..714)
FULL = (40, 15, 2175, 715)      # mark + wordmark
WORD = (795, 205, 1415, 370)    # KYROX + .STUDIO


def path(d, fill):
    return f'<path fill="{fill}" fill-rule="evenodd" d="{d}"/>'


def mark(steel, wood, leather):
    return path(P['steel'], steel) + path(P['wood'], wood) + path(P['leather'], leather)


def word(c):
    return path(P['kyrox'], c) + path(P['studio'], c)


def svg(vb, body, bg=None, title='Kyrox Studio'):
    x, y, w, h = vb
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
            f'width="{w}" height="{h}"><title>{title}</title>{rect}{body}</svg>\n')


def square(pad_ratio):
    # square box centered on the mark with padding
    x, y, w, h = 55, 27, 903, 687
    side = max(w, h) / (1 - 2 * pad_ratio)
    cx, cy = x + w / 2, y + h / 2
    return (round(cx - side / 2, 2), round(cy - side / 2, 2), round(side, 2), round(side, 2))


os.makedirs('out/svg', exist_ok=True)
F = {}
F['kyrox-logo-renkli.svg'] = svg(FULL, mark(STEEL, WOOD, LEATHER) + word(INK))
F['kyrox-logo-renkli-koyu-zemin.svg'] = svg(FULL, mark(STEEL_D, WOOD, LEATHER) + word(WHITE))
F['kyrox-logo-siyah.svg'] = svg(FULL, mark(INK, INK, INK) + word(INK))
F['kyrox-logo-beyaz.svg'] = svg(FULL, mark(WHITE, WHITE, WHITE) + word(WHITE))
F['kyrox-ikon-renkli.svg'] = svg(MARK, mark(STEEL, WOOD, LEATHER))
F['kyrox-ikon-renkli-koyu-zemin.svg'] = svg(MARK, mark(STEEL_D, WOOD, LEATHER))
F['kyrox-ikon-siyah.svg'] = svg(MARK, mark(INK, INK, INK))
F['kyrox-ikon-beyaz.svg'] = svg(MARK, mark(WHITE, WHITE, WHITE))
F['kyrox-yazi-siyah.svg'] = svg(WORD, word(INK))
F['kyrox-yazi-beyaz.svg'] = svg(WORD, word(WHITE))
# profile / favicon sources (square, with background)
F['kyrox-profil-siyah.svg'] = svg(square(0.17), mark(STEEL_D, WOOD, LEATHER), bg=INK)
F['kyrox-profil-krem.svg'] = svg(square(0.17), mark(STEEL, WOOD, LEATHER), bg=PAPER)
F['favicon.svg'] = svg(square(0.06), mark(STEEL, WOOD, LEATHER))
for k, v in F.items():
    open('out/svg/' + k, 'w').write(v)
print('svgs', len(F))
