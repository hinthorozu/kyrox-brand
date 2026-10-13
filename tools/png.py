from playwright.sync_api import sync_playwright
import os
os.makedirs('out/png', exist_ok=True)
jobs = [(f, f.replace('.svg', '.png'), 2400) for f in os.listdir('out/svg') if f.startswith(('kyrox-logo', 'kyrox-yazi'))]
jobs += [(f, f.replace('.svg', '.png'), 1024) for f in os.listdir('out/svg') if f.startswith('kyrox-ikon')]
jobs += [('kyrox-profil-siyah.svg', 'kyrox-profil-siyah-1080.png', 1080), ('kyrox-profil-krem.svg', 'kyrox-profil-krem-1080.png', 1080),
         ('favicon.svg', 'favicon-32.png', 32), ('favicon.svg', 'favicon-512.png', 512), ('kyrox-profil-krem.svg', 'apple-touch-icon-180.png', 180)]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for src, out, w in jobs:
        svg = open('out/svg/' + src).read()
        pg.set_content(f"<html><body style='margin:0;background:transparent'><div id=w style='width:{w}px'>{svg}</div><style>svg{{width:100%;height:auto;display:block}}</style></body></html>")
        pg.locator('#w').screenshot(path='out/png/' + out, omit_background=True)
    b.close()
print(len(jobs))
