import json, sys
from textpath import text_path
P = json.load(open('paths.json'))
def studio(size, base=None, right=2192):
    base = base if base else 566 + (size - 112) * 0.3
    d, w = text_path('.studio', 'Medium', size, track=-0.01)
    d, w = text_path('.studio', 'Medium', size, x=right - w, baseline=base, track=-0.01)
    return d
mark = ''.join(f'<path fill="{c}" d="{P[k]}"/>' for k, c in [('steel', '#B4B7BB'), ('wood', '#A2652C'), ('leather', '#7B3B1D')])
def full(st, bg):
    fg = '#0B0B0B' if bg != '#0B0B0B' else '#FFFFFF'
    m = mark.replace('#B4B7BB', '#C9CCD0') if fg == '#FFFFFF' else mark
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -20 2250 790"><rect x="0" y="-20" width="2250" height="790" fill="{bg}"/>{m}<path fill="{fg}" fill-rule="evenodd" d="{P["kyrox"]}"/><path fill="{fg}" fill-rule="evenodd" d="{st}"/></svg>'
if __name__ == '__main__':
    for size in map(int, sys.argv[1:]):
        st = studio(size)
        open(f's{size}_l.svg', 'w').write(full(st, '#FFFFFF'))
        open(f's{size}_d.svg', 'w').write(full(st, '#0B0B0B'))
