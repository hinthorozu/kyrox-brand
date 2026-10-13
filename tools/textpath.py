from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FONTDIR = '/usr/share/fonts/opentype/inter/'
def text_path(text, weight='Medium', size=100, x=0, baseline=0, track=0.0):
    f = TTFont(FONTDIR + f'Inter-{weight}.otf')
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    cx = 0
    for ch in text:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (s, 0, 0, -s, x + cx, baseline))
        gs[g].draw(tp)
        cx += gs[g].width * s + track * size
    return pen.getCommands(), cx - track * size
def metrics(weight='Medium'):
    f = TTFont(FONTDIR + f'Inter-{weight}.otf'); os2 = f['OS/2']
    return f['head'].unitsPerEm, os2.sCapHeight, os2.sxHeight
