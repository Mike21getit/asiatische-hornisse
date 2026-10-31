#!/usr/bin/env python3
"""Erzeugt die selbst gezeichneten SVG-Illustrationen (keine Fremdbilder).
Aufruf: python3 tools/make_svgs.py  -> schreibt nach img/"""
import os
OUT = os.path.join(os.path.dirname(__file__), '..', 'img')

def hornet(kind):
    v = kind == 'velutina'
    if v:
        head_top, face, thorax, thorax_mark = '#1a1614', '#e8a63a', '#141110', '#2a2220'
        leg, tarsus = '#1d1816', '#f2c14e'
        seg = ['#1b1715', '#1b1715', '#1e1917', '#e9a53c', '#241b16', '#5e3d1f']
        edge = '#d99a3a'
        wing = 'rgba(120,96,70,.30)'
    else:
        head_top, face, thorax, thorax_mark = '#8a3b1f', '#e9c247', '#5a2615', '#2a130b'
        leg, tarsus = '#7a3519', '#8a3e1d'
        seg = ['#6b2d18', '#e8c040', '#e8c040', '#e8c040', '#e8c040', '#e8c040']
        edge = None
        wing = 'rgba(170,120,80,.26)'
    p = []
    a = p.append
    a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 560" role="img">')
    a(f'<title>{"Asiatische Hornisse (Vespa velutina), Illustration" if v else "Europäische Hornisse (Vespa crabro), Illustration"}</title>')
    a('<defs>')
    a('<clipPath id="abd"><path d="M200 262 C 262 266 286 330 280 392 C 274 452 236 512 200 540 C 164 512 126 452 120 392 C 114 330 138 266 200 262 Z"/></clipPath>')
    a('<radialGradient id="sh" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></radialGradient>')
    a('</defs>')
    # Beine (hinter Körper)
    legs = [  # (Ansatz y, Knie, Fuß) für rechte Seite, gespiegelt links
        (175, (262, 150), (292, 108)),
        (200, (270, 222), (318, 248)),
        (225, (262, 286), (300, 352)),
    ]
    for side in (1, -1):
        for y, knee, foot in legs:
            x0 = 200 + side * 30
            kx = 200 + side * (knee[0] - 200)
            fx = 200 + side * (foot[0] - 200)
            # Unterschenkel bis kurz vor Fuß, dann Tarsus
            tx = kx + (fx - kx) * .62
            ty = knee[1] + (foot[1] - knee[1]) * .62
            a(f'<path d="M{x0} {y} L{kx} {knee[1]} L{tx:.1f} {ty:.1f}" fill="none" stroke="{leg}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>')
            a(f'<path d="M{tx:.1f} {ty:.1f} L{fx} {foot[1]}" fill="none" stroke="{tarsus}" stroke-width="7" stroke-linecap="round"/>')
    # Flügel
    for side in (1, -1):
        sx = lambda x: 200 + side * (x - 200)
        a(f'<path d="M{sx(222)} 170 C {sx(300)} 190 {sx(352)} 300 {sx(330)} 400 C {sx(318)} 440 {sx(282)} 420 {sx(262)} 360 C {sx(244)} 300 {sx(228)} 230 {sx(216)} 182 Z" fill="{wing}" stroke="rgba(255,240,220,.35)" stroke-width="1.5"/>')
        a(f'<path d="M{sx(220)} 190 C {sx(268)} 220 {sx(300)} 290 {sx(300)} 350" fill="none" stroke="rgba(255,240,220,.22)" stroke-width="1.2"/>')
        a(f'<path d="M{sx(222)} 196 C {sx(270)} 240 {sx(282)} 300 {sx(268)} 330 C {sx(258)} 300 {sx(240)} 250 {sx(218)} 206 Z" fill="{wing}" stroke="rgba(255,240,220,.25)" stroke-width="1.2"/>')
    # Hinterleib
    a('<g clip-path="url(#abd)">')
    ys = [262, 300, 336, 372, 410, 452, 540]
    for i in range(6):
        a(f'<rect x="100" y="{ys[i]}" width="200" height="{ys[i+1]-ys[i]+1}" fill="{seg[i]}"/>')
        if v and i in (0, 1, 2, 4):
            a(f'<rect x="100" y="{ys[i+1]-6}" width="200" height="6" fill="{edge}"/>')
        if not v and i >= 1:
            y = ys[i]
            h = (ys[i+1] - ys[i]) * .42
            a(f'<path d="M100 {y} H300 V{y+h*.5:.0f} C 262 {y+h*.5:.0f} 250 {y+h:.0f} 236 {y+h*1.25:.0f} C 222 {y+h:.0f} 214 {y+h*.6:.0f} 200 {y+h*.6:.0f} C 186 {y+h*.6:.0f} 178 {y+h:.0f} 164 {y+h*1.25:.0f} C 150 {y+h:.0f} 138 {y+h*.5:.0f} 100 {y+h*.5:.0f} Z" fill="#2a1a10"/>')
    a('<rect x="100" y="262" width="200" height="280" fill="url(#sh)"/>')
    a('</g>')
    # Stielchen
    a(f'<ellipse cx="200" cy="256" rx="16" ry="12" fill="{thorax}"/>')
    # Brust
    a(f'<ellipse cx="200" cy="198" rx="48" ry="62" fill="{thorax}"/>')
    a(f'<path d="M170 170 C 185 158 215 158 230 170 C 222 200 178 200 170 170 Z" fill="{thorax_mark}" opacity=".9"/>')
    if not v:
        a('<path d="M168 214 C 180 232 220 232 232 214" fill="none" stroke="#c9832e" stroke-width="5" stroke-linecap="round" opacity=".8"/>')
    a('<ellipse cx="200" cy="198" rx="48" ry="62" fill="url(#sh)"/>')
    # Kopf
    a(f'<ellipse cx="200" cy="112" rx="42" ry="34" fill="{head_top}"/>')
    a(f'<path d="M168 118 C 176 146 224 146 232 118 C 222 128 178 128 168 118 Z" fill="{face}"/>')
    a(f'<path d="M180 128 C 190 150 210 150 220 128 C 212 136 188 136 180 128 Z" fill="{face}"/>')
    for side in (1, -1):
        a(f'<ellipse cx="{200+side*33}" cy="108" rx="13" ry="22" transform="rotate({side*-18} {200+side*33} 108)" fill="#0c0a09"/>')
        a(f'<ellipse cx="{200+side*30}" cy="100" rx="4" ry="7" fill="#fff" opacity=".18"/>')
    a('<ellipse cx="200" cy="112" rx="42" ry="34" fill="url(#sh)"/>')
    # Fühler
    ant = '#1a1512' if v else '#5a2a16'
    for side in (1, -1):
        a(f'<path d="M{200+side*10} 84 C {200+side*16} 52 {200+side*40} 34 {200+side*72} 22" fill="none" stroke="{ant}" stroke-width="6" stroke-linecap="round"/>')
        if not v:
            a(f'<path d="M{200+side*10} 84 C {200+side*14} 66 {200+side*20} 56 {200+side*26} 48" fill="none" stroke="#c8902e" stroke-width="6" stroke-linecap="round"/>')
    a('</svg>')
    return '\n'.join(p)

def nest_secondary():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 520" role="img">
<title>Sekundärnest hoch in einer Baumkrone, Illustration</title>
<defs><radialGradient id="n" cx=".38" cy=".35" r=".75"><stop offset="0" stop-color="#c9a27a"/><stop offset=".7" stop-color="#8a6a4c"/><stop offset="1" stop-color="#5a4432"/></radialGradient></defs>
<g fill="none" stroke="#3f4a33" stroke-linecap="round">
<path d="M0 60 C 120 70 220 40 400 30" stroke-width="14"/><path d="M200 50 C 205 80 200 100 198 120" stroke-width="8"/>
<path d="M60 64 C 40 20 20 10 0 6" stroke-width="6"/><path d="M300 40 C 340 80 370 90 400 96" stroke-width="6"/>
</g>
<g fill="#2f3b27" opacity=".9"><ellipse cx="70" cy="50" rx="40" ry="16" transform="rotate(-12 70 50)"/><ellipse cx="320" cy="30" rx="44" ry="15" transform="rotate(10 320 30)"/><ellipse cx="140" cy="76" rx="30" ry="11" transform="rotate(18 140 76)"/><ellipse cx="370" cy="86" rx="32" ry="12" transform="rotate(24 370 86)"/></g>
<path d="M198 112 C 290 120 338 220 330 320 C 322 420 270 490 200 500 C 130 490 78 420 70 320 C 62 220 110 120 198 112 Z" fill="url(#n)"/>
<g fill="none" stroke="#f1dcc0" stroke-opacity=".28" stroke-width="2.2">
<path d="M96 200 C 150 186 250 186 304 200"/><path d="M80 250 C 150 234 250 234 320 250"/><path d="M72 300 C 150 284 250 284 328 300"/><path d="M72 350 C 150 334 250 334 328 350"/><path d="M80 400 C 150 386 250 386 320 400"/><path d="M98 448 C 150 436 250 436 302 448"/><path d="M128 160 C 170 150 230 150 272 160"/>
</g>
<g fill="none" stroke="#3b2c20" stroke-opacity=".35" stroke-width="1.6"><path d="M110 226 C 150 214 190 222 230 214"/><path d="M180 276 C 220 266 260 274 300 266"/><path d="M96 326 C 140 316 180 324 220 316"/><path d="M200 376 C 240 366 270 372 306 366"/></g>
<ellipse cx="292" cy="318" rx="13" ry="16" fill="#1c140e"/>
<g fill="#1a1512"><ellipse cx="318" cy="300" rx="7" ry="3.5" transform="rotate(-30 318 300)"/><ellipse cx="342" cy="282" rx="7" ry="3.5" transform="rotate(-20 342 282)"/></g>
<g fill="#e9a53c"><rect x="315" y="300" width="4" height="3" transform="rotate(-30 318 300)"/><rect x="339" y="282" width="4" height="3" transform="rotate(-20 342 282)"/></g>
</svg>'''

def nest_primary():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 320" role="img">
<title>Primärnest unter einem Dachüberstand, Illustration</title>
<defs><radialGradient id="p" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#d2ad84"/><stop offset=".7" stop-color="#93714f"/><stop offset="1" stop-color="#604836"/></radialGradient></defs>
<path d="M0 40 L400 40 L400 64 L0 64 Z" fill="#3a332e"/><path d="M0 64 L400 64 L400 74 L0 74 Z" fill="#26211e"/>
<g fill="#4a413a"><rect x="40" y="74" width="22" height="18"/><rect x="190" y="74" width="22" height="18"/><rect x="340" y="74" width="22" height="18"/></g>
<path d="M200 92 L200 110" stroke="#7a5d43" stroke-width="5"/>
<path d="M200 108 C 252 108 272 150 268 186 C 262 236 232 262 200 262 C 168 262 138 236 132 186 C 128 150 148 108 200 108 Z" fill="url(#p)"/>
<g fill="none" stroke="#f1dcc0" stroke-opacity=".3" stroke-width="2"><path d="M144 150 C 180 140 220 140 256 150"/><path d="M134 186 C 180 176 220 176 266 186"/><path d="M140 222 C 180 212 220 212 260 222"/></g>
<ellipse cx="200" cy="254" rx="12" ry="7" fill="#1c140e"/>
<g fill="#1a1512"><ellipse cx="240" cy="284" rx="7" ry="3.5" transform="rotate(-25 240 284)"/></g>
</svg>'''

def hero():
    hv = hornet('velutina').split('\n', 1)[1].rsplit('</svg>', 1)[0]
    hv = hv.replace('<title>Asiatische Hornisse (Vespa velutina), Illustration</title>', '')
    hexes = []
    import math
    r = 46
    for row in range(-1, 13):
        for col in range(-1, 11):
            cx = col * r * 1.5 * 1.0 + 40
            cy = row * r * math.sqrt(3) + (col % 2) * r * math.sqrt(3) / 2
            pts = ' '.join(f'{cx + r*math.cos(math.radians(60*k)):.1f},{cy + r*math.sin(math.radians(60*k)):.1f}' for k in range(6))
            hexes.append(f'<polygon points="{pts}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1200" role="img">
<title>Asiatische Hornisse über Wabenmuster, Illustration</title>
<defs><radialGradient id="glow" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#e09a3a" stop-opacity=".32"/><stop offset="1" stop-color="#0b0b0c" stop-opacity="0"/></radialGradient></defs>
<rect width="900" height="1200" fill="#0e0d0c"/>
<g fill="none" stroke="#e0a24a" stroke-opacity=".10" stroke-width="2">{''.join(hexes)}</g>
<rect width="900" height="1200" fill="url(#glow)"/>
<g transform="translate(450 600) rotate(-16) scale(1.55) translate(-200 -285)">{hv}</g>
</svg>'''

def favicon():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0b0b0c"/>
<polygon points="32,6 54,19 54,45 32,58 10,45 10,19" fill="none" stroke="#e0a24a" stroke-width="3"/>
<clipPath id="c"><path d="M32 22 C 44 22 46 36 32 50 C 18 36 20 22 32 22 Z"/></clipPath>
<circle cx="32" cy="17" r="5" fill="#efe6da"/>
<g clip-path="url(#c)"><rect x="16" y="20" width="32" height="32" fill="#efe6da"/><rect x="16" y="33" width="32" height="7" fill="#e9a53c"/></g></svg>'''

files = {
    'hornisse-velutina.svg': hornet('velutina'),
    'hornisse-crabro.svg': hornet('crabro'),
    'nest-sekundaer.svg': nest_secondary(),
    'nest-primaer.svg': nest_primary(),
    'hero-hornisse.svg': hero(),
    '../favicon.svg': favicon(),
}
for name, svg in files.items():
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(svg + '\n')
print('ok')
