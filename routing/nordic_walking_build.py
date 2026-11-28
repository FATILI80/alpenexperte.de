#!/usr/bin/env python3
"""Baut content/nordic-walking/index.html neu (Gravel-Schema).
Offizielle Strecken: Daten der Alpenregion Tegernsee Schliersee (destination.one).
Runden ab Oberer Firstalm: BRouter-Ergebnisse aus ergebnis_wandern.json (W05, W07, W24), Gehzeit nach DAV-Formel.
"""
import re, html, json
F = 'content/nordic-walking/index.html'
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:34px 0 10px;scroll-margin-top:140px;">{t}</h2>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'
TD = 'style="padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;"'
def kv(rows):
    return ('<table style="width:100%;border-collapse:collapse;font-size:.92rem;margin:8px 0 10px;">'
            + ''.join(f'<tr><th style="text-align:left;padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#14532d;width:36%;vertical-align:top;">{E(k)}</th><td {TD}>{v}</td></tr>' for k, v in rows) + '</table>')
def dav(km, auf, ab):
    h = km / 4; v = auf / 300 + ab / 500
    t = max(h, v) + min(h, v) / 2; m = int(round(t * 60 / 5) * 5)
    return f'{m // 60}:{m % 60:02d} h'
def kmf(x): return f'{x:.2f}'.replace('.', ',').rstrip('0').rstrip(',')
def karte(id_, kopf, titel, text, fakten, quellen, route=None):
    q = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{E(n)}</a>' for n, u in quellen)
    mk = f'<div class="mini-karte" data-route="{route}" data-pfad="wandern" style="height:200px;margin-top:6px;border-radius:8px;"></div>' if route else ''
    return (f'<article id="{id_}" style="background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;scroll-margin-top:140px;">'
            f'<div style="padding:12px 14px;"><div style="font-size:.8rem;color:#1d4ed8;font-weight:700;">{E(kopf)}</div>'
            f'<h3 style="margin:4px 0 6px;color:#14532d;font-size:1.05rem;">{E(titel)}</h3>'
            f'<p style="margin:0 0 8px;font-size:.9rem;line-height:1.45;color:#0f2942;">{text}</p>'
            '<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;cursor:pointer;"><summary style="color:#14532d;font-weight:600;font-size:.86rem;">🥢 Details, Karte &amp; Quellen</summary>'
            + kv(fakten) + mk + f'<p style="margin:6px 0 0;font-size:.78rem;color:#4b5563;">Quellen: {q}</p></details></div></article>')
GRID = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;">'
DO = 'https://web.destination.one/en/tour/'
ERG = {x['kennung']: x for x in json.load(open('routing/ergebnis_wandern.json', encoding='utf-8'))}

b = ['<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">',
     '<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">Nordic Walking</span></nav>',
     '<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">🥢 Nordic Walking am Spitzingsee &amp; Schliersee</h1>'
     '<p style="font-size:1.08rem;color:#1f2933;margin:0;">Drei Runden direkt ab der Oberen Firstalm – mit BRouter nachgerechnet – und die ausgeschilderten Nordic-Walking-Strecken der Alpenregion Tegernsee Schliersee am Spitzingsee und am Schliersee. Alle Zahlen mit Quelle.</p></header>',
     '<img src="/images/nordic-walking.jpg" alt="Nordic Walking in den Bayerischen Voralpen" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">']
NAV = [('#firstalm', '🏠 Ab Oberer Firstalm'), ('#spitzingsee', '🏞️ Spitzingsee'), ('#schliersee', '🌊 Schliersee'), ('#tegernsee', '⛰️ Tegernsee'), ('#hinweise', 'ℹ️ Hinweise'), ('#quellen', '📚 Quellen')]
b.append('<nav class="kat-nav" aria-label="Nordic-Walking-Bereiche" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
         + ''.join(f'<a href="{h}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for h, t in NAV) + '</nav>')

# Ab Oberer Firstalm (BRouter)
FA = [('W07', 'Große Firstalm – Untere Firstalm – Spitzingsee-Runde', 'Die kürzeste Runde: über die Firstalmen hinunter an den Spitzingsee und zurück. Der Rückweg zur Alm ist der Anstieg des Tages.'),
      ('W05', 'Firstalm-Runde: Spitzingsee & Wurzhütte', 'Hinunter zum Spitzingsee, am See entlang zur Alten Wurzhütte und wieder hinauf zur Oberen Firstalm.'),
      ('W24', 'Firstalm-Runde: Blecksteinhaus', 'Die längste der drei: zum Blecksteinhaus und zurück – für Nordic Walker mit Kondition.')]
cards = []
for k, t, txt in FA:
    r = ERG[k]
    cards.append(karte('fa-' + k.lower(), f'Start & Ziel Obere Firstalm · Runde · BRouter', t, txt,
        [('Strecke', f'{kmf(r["laenge_km_brouter"])} km'), ('Höhenmeter', f'↑ {r["hm_aufstieg"]} · ↓ {r["hm_abstieg"]} Hm'),
         ('Gehzeit', f'ca. {dav(r["laenge_km_brouter"], r["hm_aufstieg"], r["hm_abstieg"])} (DAV-Formel, ohne Pausen)')],
        [('BRouter-Berechnung alpenexperte.de', '/content/wandern/index.html')], k))
b.append(H2('firstalm', '🏠 Runden ab der Oberen Firstalm') + P('Die Alm liegt auf 1.375 m, der Spitzingsee rund 290 m tiefer – jede Runde beginnt also bergab und endet mit dem Anstieg zurück zur Alm. Genau das macht sie zum guten Stocktraining.') + GRID + ''.join(cards) + '</div>')

# Spitzingsee
SP = [karte('eon-spitzingsee', 'Spitzingsee · Runde · mittel, Kondition leicht', 'E.ON Bayern Trail Spitzingsee',
            'Rund um den Spitzingsee und weiter ins Valepptal, vorbei an Albert-Link-Hütte und Blecksteinhaus. Gut zu kombinieren mit einer Einkehr.',
            [('Strecke', '7,00 km'), ('Höhenmeter', '65 Hm'), ('Höhe', '1.026–1.091 m'), ('Gehzeit', 'ca. 1:45 h'), ('Einkehr', 'Albert-Link-Hütte, Blecksteinhaus')],
            [('Alpenregion Tegernsee Schliersee / destination.one', DO + 'eon-bayern-trail-at-spitzingsee')]),
      karte('petrusquelle-spitzingsee', 'Spitzingsee · Runde · leicht', 'Siegsdorfer Petrusquelle Trail Spitzingsee',
            'Die kurze Einsteigerrunde rund um den See – fast flach, mit mehreren Einkehrmöglichkeiten und im Sommer einer Badegelegenheit.',
            [('Strecke', '2,80 km'), ('Höhenmeter', '8 Hm'), ('Höhe', '1.083–1.091 m'), ('Gehzeit', 'ca. 0:45 h')],
            [('Alpenregion Tegernsee Schliersee / destination.one', DO + 'siegsdorfer-petrusquelle-trail-at-spitzingsee')]),
      karte('seerundweg', 'Spitzingsee · barrierearm', 'Rundweg um den Spitzingsee',
            'Flacher Seerundweg ohne nennenswerte Höhenunterschiede, zertifiziert als teilweise barrierefrei für Menschen mit Gehbehinderung – ideal für die ersten Versuche mit Stöcken.',
            [('Strecke', '2,81 km'), ('Belag', 'wassergebunden und Asphalt, ein kurzer Holzbohlenweg, ein Viehgitter'), ('Ziel', 'Parkplatz Ostufer Spitzingsee')],
            [('Bayern Tourismus – Reisen für Alle', 'https://bavaria.travel/accessible-holidays/wanderweg-um-den-spitzingsee'), ('destination.one', DO + 'accessible-hiking-trail-around-spitzingsee')])]
b.append(H2('spitzingsee', '🏞️ Ausgeschilderte Strecken am Spitzingsee') + GRID + ''.join(SP) + '</div>')

# Schliersee
SC = [karte('haas-fertigbau-trail', 'Schliersee · Runde · mittel', 'HAAS Fertigbau Trail Schliersee',
            'Die anspruchsvolle Runde am Westufer: aus Schliersee hinauf in den Wald am Westerberg und über Schliersee und das Ufer zurück. Fast 16 km brauchen gute Ausdauer.',
            [('Strecke', '15,76 km'), ('Höhenmeter', '380 Hm'), ('Höhe', '776–1.154 m'), ('Gehzeit', 'ca. 3:00 h')],
            [('Alpenregion Tegernsee Schliersee / destination.one', DO + 'haas-prefabricated-construction-trail-at-schliersee')]),
      karte('eon-schliersee', 'Schliersee · Runde · Kondition leicht · barrierefrei', 'E.ON Bayern Trail Schliersee',
            'Flache Uferrunde am Schliersee, vorbei am Campingplatz, an Badeplätzen und Bootshütten, am Ende durch den Ort.',
            [('Strecke', '7,27 km'), ('Höhenmeter', '↑ 17 · ↓ 23 Hm'), ('Höhe', '776–793 m'), ('Gehzeit', 'ca. 1:45 h')],
            [('Alpenregion Tegernsee Schliersee / destination.one', DO + 'eon-bayern-trail-at-schliersee')]),
      karte('petrusquelle-schliersee', 'Schliersee · Runde · leicht', 'Siegsdorfer Petrusquelle Trail Schliersee',
            'Die kurze, flache Runde in Schliersee – zum Kennenlernen der Technik.',
            [('Strecke', '2,11 km'), ('Höhenmeter', '7 Hm'), ('Höhe', '777–783 m'), ('Gehzeit', 'ca. 0:25 h')],
            [('Alpenregion Tegernsee Schliersee / destination.one', DO + 'siegsdorfer-petrusquelle-trail-at-schliersee')])]
b.append(H2('schliersee', '🌊 Ausgeschilderte Strecken am Schliersee') + GRID + ''.join(SC) + '</div>' +
         P('Anreise: Schliersee erreichst du mit der BRB; von der Oberen Firstalm aus ist der Bahnhof Schliersee über die Schliersbergalm zu Fuß erreichbar – siehe <a href="/content/wandern/index.html">Wandern</a>.'))

b.append(H2('tegernsee', '⛰️ Tegernseer Tal') +
         P('Im Tegernseer Tal sind insgesamt 18 Nordic-Walking-Strecken vom Deutschen Skiverband (DSV) zertifiziert. Übersicht und Karten bei <a href="https://tegernsee.com/en/nordic-walking-tegernsee-mountain" target="_blank" rel="noopener">Der Tegernsee</a>.'))

b.append(H2('hinweise', 'ℹ️ Hinweise') + '<ul style="line-height:1.7;color:#1f2933;">'
         '<li>Die Quellen der ausgeschilderten Strecken sagen nichts über Winterräumung. Im Winter vorher prüfen oder auf geräumte Wege ausweichen – Ideen im <a href="/content/winter/index.html">Winter-Guide</a>.</li>'
         '<li>Gehzeiten der Firstalm-Runden nach der DAV-Formel (4 km/h, 300 Hm/h bergauf, 500 Hm/h bergab), ohne Pausen.</li>'
         '<li>GPX-Tracks der offiziellen Strecken gibt es auf den verlinkten Seiten der Alpenregion.</li></ul>'
         '<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:16px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
         '<a href="https://www.amazon.de/s?k=Nordic+Walking+St%C3%B6cke&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Nordic-Walking-Stöcke</a> · '
         '<a href="https://www.amazon.de/s?k=Nordic+Walking+Schuhe&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Nordic-Walking-Schuhe</a> bei Amazon</aside>')

Q = [('destination.one / Alpenregion Tegernsee Schliersee – E.ON Bayern Trail Spitzingsee', DO + 'eon-bayern-trail-at-spitzingsee'),
     ('destination.one – Siegsdorfer Petrusquelle Trail Spitzingsee', DO + 'siegsdorfer-petrusquelle-trail-at-spitzingsee'),
     ('destination.one – Barrierefreier Rundweg Spitzingsee', DO + 'accessible-hiking-trail-around-spitzingsee'),
     ('Bayern Tourismus – Wanderweg um den Spitzingsee (Belag, Zertifizierung)', 'https://bavaria.travel/accessible-holidays/wanderweg-um-den-spitzingsee'),
     ('destination.one – HAAS Fertigbau Trail Schliersee', DO + 'haas-prefabricated-construction-trail-at-schliersee'),
     ('destination.one – E.ON Bayern Trail Schliersee', DO + 'eon-bayern-trail-at-schliersee'),
     ('destination.one – Siegsdorfer Petrusquelle Trail Schliersee', DO + 'siegsdorfer-petrusquelle-trail-at-schliersee'),
     ('tegernsee.com – 18 DSV-zertifizierte Nordic-Walking-Strecken', 'https://tegernsee.com/en/active')]
b.append(H2('quellen', '📚 Quellen') + '<ul style="line-height:1.7;font-size:.92rem;">' + ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in Q) +
         '<li>Firstalm-Runden: eigene Routenberechnung mit BRouter (OpenStreetMap-Daten)</li></ul>'
         '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Alle Angaben ohne Gewähr.</p></article></main>')

kl = open('routing/klettern_seite_build.py', encoding='utf-8').read()
MAPJS = kl.split("MAPJS = '''", 1)[1].split("'''", 1)[0]
s = open(F, encoding='utf-8').read()
a = s.find('<main'); z = s.find('</main>') + 7
head, tail = s[:a], s[z:]
DESC = 'Nordic Walking am Spitzingsee und Schliersee: drei Runden ab der Oberen Firstalm (BRouter) und die ausgeschilderten Trails der Alpenregion – E.ON, HAAS Fertigbau, Petrusquelle – mit Quellen.'
head = re.sub(r'<title>.*?</title>', '<title>Nordic Walking am Spitzingsee &amp; Schliersee – Strecken mit Karte | alpenexperte.de</title>', head, count=1, flags=re.S)
for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(DESC) + m.group(2), head)
if 'leaflet.css' not in head:
    head = head.replace('</head>', '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>\n'
                        '<style id="mini-karte-fix">.mini-karte{position:relative;isolation:isolate;overflow:hidden;}.mini-karte .leaflet-container{width:100%!important;height:100%!important;}</style>\n</head>', 1)
for pat in [r'\s*<!-- ===== FEEDBACK-BOX.*?</section>', r'<section class="section section--lounge".*?</section>\s*',
            r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*', r'<section class="section section--lounge-alt".*?</section>\s*',
            r'<section class="quellen-section".*?</section>\s*', r'<!-- ===== BRB ECHTZEIT-FAHRPLAN.*?</div>\s*',
            r'<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>\s*<script>.*?</script>\s*']:
    tail = re.sub(pat, '', tail, flags=re.S)
i = tail.find('<footer')
pre = tail[:i]
if re.search(r'amazon|awin|urwahn|lucky', pre, re.I): tail = tail[i:]
tail = tail.replace('</body>', MAPJS + '</body>', 1)
open(F, 'w', encoding='utf-8').write(head + '\n'.join(b) + tail)
print('ok')
