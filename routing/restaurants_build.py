#!/usr/bin/env python3
"""Baut restaurants.html neu: Restaurants & Cafés im Tal – nur nachweisbare Lokale mit Quelle.
Die 30 alten Unterseiten unter content/restaurants/ (größtenteils erfunden) entfallen per 301."""
import re, html
F = 'restaurants.html'
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:34px 0 8px;scroll-margin-top:140px;">{t}</h2>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'
TD = 'style="padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;"'
def tel(n, s): return f'<a href="tel:{n}">{s}</a>'
def kv(rows):
    return ('<table style="width:100%;border-collapse:collapse;font-size:.9rem;margin:6px 0 8px;">'
            + ''.join(f'<tr><th style="text-align:left;padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#14532d;width:30%;vertical-align:top;">{E(k)}</th><td {TD}>{v}</td></tr>' for k, v in rows) + '</table>')
def karte(r):
    q = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{E(n)}</a>' for n, u in r['q'])
    img = (f'<img src="/images/{r["bild"]}" alt="{E(r["name"])}" loading="lazy" style="width:100%;height:150px;object-fit:cover;display:block;">' if r.get('bild') else '')
    return (f'<article id="{r["id"]}" style="background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;scroll-margin-top:140px;">{img}'
            f'<div style="padding:11px 13px;"><div style="font-size:.78rem;color:#1d4ed8;font-weight:700;">{E(r["kopf"])}</div>'
            f'<h3 style="margin:3px 0 6px;color:#14532d;font-size:1.04rem;">{E(r["name"])}</h3>'
            f'<p style="margin:0 0 8px;font-size:.9rem;line-height:1.45;color:#0f2942;">{r["text"]}</p>'
            '<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;cursor:pointer;"><summary style="color:#14532d;font-weight:600;font-size:.85rem;">🍽️ Adresse, Zeiten &amp; Quellen</summary>'
            + kv(r['f']) + f'<p style="margin:4px 0 0;font-size:.76rem;color:#4b5563;">Quellen: {q}</p></details></div></article>')
GRID = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:14px;">'

SCHLIERSEE = [
 dict(id='ratskeller-schliersee', name='Ratskeller Schliersee', kopf='Bayerisches Wirtshaus · Ortsmitte', text='Rustikales Wirtshaus am Rathaus mit großem Biergarten – laut wanderlog einer der beliebtesten Gasthöfe im Ort.',
      f=[('Adresse', 'Rathausstraße 1a, 83727 Schliersee'), ('Kontakt', tel('+4980269205800', '08026 9205800') + ' · ratskeller-schliersee.de')],
      q=[('wanderlog', 'https://wanderlog.com/list/geoCategory/202248/')]),
 dict(id='xaver-terofal', name='Xaver Restaurant + Bar im Terofal', kopf='Bayerisch-modern · am Bauerntheater', text='Im Haus von Xaver Terofal, der 1892 mit Konrad Dreher das Schlierseer Bauerntheater gründete. Bayerische Küche neu interpretiert, Stuben, Terrasse und einer der größten Biergärten am See.',
      f=[('Adresse', 'Xaver-Terofal-Platz 2, 83727 Schliersee'), ('Kontakt', tel('+498026929210', '08026 929210')), ('Parken', 'kostenlos, vier Parkplätze rund um den Platz')],
      q=[('Terofal Schliersee', 'https://www.terofal-schliersee.de/en/xaver-restaurant-schliersee'), ('ADAC – Bauerntheater', 'https://maps.adac.de/poi/schlierseer-bauerntheater-gemeinde-schliersee')]),
 dict(id='cafe-milchhaeusl', name='Café Milchhäusl am See', kopf='Café · Seeufer', bild='cafe-milchhaeusl-schliersee.jpg', text='Direkt am Ufer, aus einer Hütte von 1923 entstanden, Café seit 1937. Kuchen, Brotzeiten, mittags Kasspatz’n und Bauerngröstl – klassische Einkehr bei der Seerunde.',
      f=[('Adresse', 'Kurweg 4, 83727 Schliersee'), ('Geöffnet', 'laut Gelbe Seiten Mo–Do ab 10:30 Uhr – aktuell beim Café prüfen'), ('Kontakt', tel('+4980264676', '08026 4676') + ' · milchhaeusl-schliersee.de')],
      q=[('komoot', 'https://www.komoot.com/highlight/6055453'), ('smart-travelling', 'https://smart-travelling.net/locations/cafe-milchhaeusl')]),
 dict(id='cafe-mesner', name='Café Mesner', kopf='Café · Ortsmitte', text='Traditionscafé mit Kaffee, Kuchen und Gebäck.',
      f=[('Adresse', 'Lautererstraße 2, 83727 Schliersee'), ('Geöffnet', 'laut Telefonbuch Di–Fr 9–18 Uhr'), ('Kontakt', tel('+4980266436', '08026 6436'))],
      q=[('Das Telefonbuch', 'https://adresse.dastelefonbuch.de/Schliersee/1-Cafe-Mesner-Schliersee-Lautererstr.html')]),
]
NEUHAUS = [
 dict(id='zum-wofen', name='Wirtshaus „Zum Wofen“ im Wasmeier-Museum', kopf='Altbayerisches Wirtshaus · Neuhaus', bild='wasmeier-freilichtmuseum.jpg', text='Bauernhaus von 1734 im Markus Wasmeier Freilichtmuseum, heute Wirtshaus mit hauseigener Schöpfbrauerei und großem Biergarten. Bayerische Klassiker und Fisch aus dem See.',
      f=[('Adresse', 'Brunnbichl 5, 83727 Schliersee'), ('Geöffnet', 'Di–So 10–17 Uhr, Montag Ruhetag'), ('Kontakt', tel('+498026929220', '08026 929220'))],
      q=[('servus-schliersee', 'https://servus-schliersee.de/en/eating-out/restaurant-zum-wofen/'), ('museum.com', 'https://www.museum.com/museums/markus-wasmeier-freilichtmuseum-schliersee-schliersee')]),
 dict(id='slyrs-caffee', name='SLYRS Caffee & Lunchery', kopf='Café & Lunch · Whisky-Destillerie', bild='Slyrs%20Whiskey%20Tasting.jpg', text='Café der SLYRS-Destillerie am Ortsende von Neuhaus, mit Seeblick. Fisch von der Fischerei Schliersee, Nudeln und Marmeladen vom Hennererhof, Mehl aus der Leitzachmühle.',
      f=[('Adresse', 'Bayrischzeller Straße 13, 83727 Schliersee'), ('Anfahrt', 'BRB bis Fischhausen-Neuhaus, dann ca. 1 km zu Fuß; Parkplätze vor dem Eingang'), ('Kontakt', 'Destillerie ' + tel('+4980269209 20'.replace(' ', ''), '08026 920920'))],
      q=[('servus-schliersee', 'https://servus-schliersee.de/en/sightseeing/slyrs-distillery/'), ('about-drinks – Eröffnung', 'https://www.about-drinks.com/feierliche-neueroeffnung-bei-slyrs/')]),
]
SPITZING = [
 dict(id='spitzing-alm', name='Spitzing Alm am See', kopf='Almhütten-Gaststätte · Spitzingsee', bild='spitzingsee-see.jpg', text='Direkt am See auf rund 1.100 m, gehört zum Arabella Alpenhotel. Mittwochs Grill- bzw. Hüttenabend.',
      f=[('Adresse', 'Seeweg 7a, 83727 Spitzingsee'), ('Geöffnet', 'Mi 12–22, Do–So 12–20 Uhr, Mo/Di Ruhetag (Prospekt)')],
      q=[('Spitzing Alm Prospekt', 'https://www.conferencehotelgroup.com/img/hotels/files/7328/Spitzing%20Alm%20Prospekt.pdf'), ('cylex', 'https://web2.cylex.de/firma-home/spitzing-alm-13424849.html')]),
 dict(id='alte-wurzhuette', name='Alte Wurzhütte', kopf='Gasthof · Südufer Spitzingsee', text='Historischer Gasthof von 1720, früher Enzianbrennerei. Mehr im <a href="/huetten.html#wurzhuette">Hüttenführer</a>.',
      f=[('Adresse', 'Roßkopfweg 1, 83727 Spitzingsee')], q=[('speisekarte.de', 'https://www.speisekarte.de/schliersee/restaurant/alte_wurzhuette/bewertung')]),
]
TEGERNSEE = [
 dict(id='braeustueberl-tegernsee', name='Herzogliches Bräustüberl Tegernsee', kopf='Bräustüberl · im Schloss Tegernsee', bild='tegernsee-see.jpg', text='Seit 1675 im ehemaligen Kloster, Bier aus dem benachbarten Herzoglichen Brauhaus. Rund 750 Plätze innen und 760 im Biergarten, Schiffsanleger direkt vor der Tür.',
      f=[('Adresse', 'Schlossplatz 1, 83684 Tegernsee'), ('Geöffnet', 'täglich 10–22 Uhr, warme Küche bis 21:30 Uhr'), ('Reservierung', 'ab 4 Personen'), ('Kontakt', tel('+4980224141', '08022 4141'))],
      q=[('Bräustüberl Tegernsee', 'https://braustuberl.de/en'), ('Schlemmer Atlas', 'https://www.schlemmer-atlas.de/restaurants/deutschland/tegernsee/braeustueberl-tegernsee/'), ('in-muenchen', 'https://www.in-muenchen.de/?p=1105185')]),
 dict(id='schlosswirtschaft-tegernsee', name='Schlosswirtschaft Tegernsee', kopf='Bayerisch · im Schloss Tegernsee', text='Seit April 2023 die „Schwester“ des Bräustüberls, ebenfalls von Peter und Caterina Hubert geführt.',
      f=[('Lage', 'Schloss Tegernsee')], q=[('Bräustüberl – Chronik 2023', 'https://braustuberl.de/en/blogs/geschichte/tagged/2023'), ('Schlemmer Atlas', 'https://www.schlemmer-atlas.de/restaurants/deutschland/tegernsee/')]),
 dict(id='leeberghof', name='Leeberghof', kopf='Bayerisch & Crossover · über dem See', text='Hotel-Restaurant mit Terrasse hoch über dem Tegernsee, dazu Wuidara Bar & Biergarten. Bayerische Klassiker und internationale Crossover-Küche.',
      f=[('Adresse', 'Ellingerstraße 10, 83684 Tegernsee'), ('Geöffnet', 'laut Schlemmer Atlas Di–Fr ab 17 Uhr – Zeiten schwanken je nach Quelle'), ('Kontakt', tel('+498022188090', '08022 188090'))],
      q=[('Der Tegernsee', 'https://tegernsee.com/en/a-restaurant-leeberghof-wuidara-bar-biergarten'), ('Schlemmer Atlas', 'https://www.schlemmer-atlas.de/restaurants/deutschland/tegernsee/leeberghof/')]),
 dict(id='ueberfahrt', name='Restaurant Überfahrt', kopf='Fine Dining · 1 Michelin-Stern · Rottach-Egern', text='Gourmetrestaurant im Althoff Seehotel Überfahrt, Küchenchefin Cornelia Fischer; zwei Menüs mit vier bis sechs Gängen, eines davon vegetarisch.',
      f=[('Adresse', 'Überfahrtstraße 10, 83700 Rottach-Egern'), ('Geöffnet', 'abends; Ruhetage und Zeiten laut Guide Michelin vorab prüfen')],
      q=[('Guide Michelin', 'https://guide.michelin.com/en/bayern/rottach-egern/restaurant/restaurant-uberfahrt')]),
]
LEITZACH = [
 dict(id='cafe-winklstueberl', name='Café Winklstüberl', kopf='Ausflugscafé · Fischbachau', text='Familiengeführt seit 1950 am Fuß des Breitensteins, deutschlandweit bekannt für seine Torten – allen voran die Bayerische Vanillecremetorte. Terrasse und Kinderspielplatz.',
      f=[('Adresse', 'Leitzachtalstraße 68, 83730 Fischbachau')],
      q=[('speisekarte.de', 'https://www.speisekarte.de/fischbachau/restaurant/cafe_winklstueberl/speisekarte'), ('bridebook', 'https://bridebook.com/de/wedding-venues/caf-winklst-berl-fischbachau-upper-bavaria-deWXRMxK8d')]),
]
SEK = [('schliersee', '🌊 Schliersee', SCHLIERSEE), ('neuhaus', '🥃 Neuhaus', NEUHAUS), ('spitzingsee', '🏔️ Spitzingsee', SPITZING),
       ('tegernsee', '🏞️ Tegernsee & Rottach-Egern', TEGERNSEE), ('leitzachtal', '🍰 Leitzachtal', LEITZACH)]
ALLE = [r for _, _, l in SEK for r in l]

b = ['<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">',
     '<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">Restaurants im Tal</span></nav>',
     f'<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">🍽️ Restaurants &amp; Cafés im Tal</h1>'
     f'<p style="font-size:1.08rem;color:#1f2933;margin:0;">{len(ALLE)} Lokale in Schliersee, Neuhaus, am Spitzingsee, am Tegernsee und im Leitzachtal – nur Adressen, die sich belegen lassen, jede mit Quelle. Hütten und Almen am Berg stehen im <a href="/huetten.html">Hüttenführer</a>. Öffnungszeiten ändern sich: vorher beim Lokal prüfen.</p></header>',
     '<img src="/images/Schliersee.jpg" alt="Schliersee" style="width:100%;max-height:280px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">',
     '<nav class="kat-nav" aria-label="Orte" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 10px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
     + ''.join(f'<a href="#{i}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for i, t, _ in SEK) + '</nav>']
for i, t, l in SEK:
    b.append(H2(i, t) + GRID + ''.join(karte(r) for r in l) + '</div>')
b.append(H2('hinweis', 'ℹ️ Warum so wenige?') + P('Die frühere Liste enthielt viele Lokale, die sich nirgends nachweisen ließen. Hier steht nur, was wir mit einer Quelle belegen können. Weitere Tipps aus der Region nehmen wir gern auf, sobald sie belegt sind.')
         + '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Alle Angaben ohne Gewähr.</p></article></main>')

s = open(F, encoding='utf-8').read()
a = s.find('<main'); z = s.find('</main>') + 7
head, tail = s[:a], s[z:]
DESC = f'Restaurants und Cafés in Schliersee, Neuhaus, Spitzingsee, Tegernsee und Fischbachau: {len(ALLE)} belegte Adressen mit Öffnungszeiten und Quellen – vom Bräustüberl bis zum Café Milchhäusl.'
head = re.sub(r'<title>.*?</title>', '<title>Restaurants &amp; Cafés Schliersee, Spitzingsee &amp; Tegernsee – mit Quellen | alpenexperte.de</title>', head, count=1, flags=re.S)
for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(DESC) + m.group(2), head)
for pat in [r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*', r'<!-- DS24-AFFILIATE -->.*?<!-- /DS24-AFFILIATE -->\s*',
            r'<aside class="urwahn-affiliate".*?</aside>\s*', r'<aside class="ds24-affiliate".*?</aside>\s*']:
    tail = re.sub(pat, '', tail, flags=re.S)
i = tail.find('<footer')
if re.search(r'amazon|awin|urwahn|lucky|digistore', tail[:i], re.I): tail = tail[i:]
open(F, 'w', encoding='utf-8').write(head + '\n'.join(b) + tail)
print('ok', len(ALLE))
