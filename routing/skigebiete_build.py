#!/usr/bin/env python3
"""Baut content/skigebiete/index.html neu (Gravel-Schema, nur belegte Angaben mit Quelle).

Hauptgebiet Spitzingsee-Tegernsee, Einkehr (Lyra Alm Schirmbar, Angaben von Fatih/Obere Firstalm),
Skipass 2026/27, Anreise, umliegende Gebiete. Kopf und Footer der bestehenden Seite bleiben.
"""
import re, html
F = 'content/skigebiete/index.html'
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:34px 0 10px;scroll-margin-top:140px;">{t}</h2>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'
TH = 'style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;"'
TD = 'style="padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;"'

def tab(kopf, rows):
    return ('<table style="width:100%;border-collapse:collapse;font-size:.94rem;margin:8px 0 14px;">'
            + '<tr>' + ''.join(f'<th {TH}>{E(k)}</th>' for k in kopf) + '</tr>'
            + ''.join('<tr>' + ''.join(f'<td {TD}>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>')

def kv(rows):
    return ('<table style="width:100%;border-collapse:collapse;font-size:.94rem;margin:8px 0 14px;">'
            + ''.join(f'<tr><th style="text-align:left;padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#14532d;width:30%;vertical-align:top;">{E(k)}</th><td {TD}>{v}</td></tr>' for k, v in rows) + '</table>')

def karte(id_, img, kopf, titel, text, fakten, quellen, extra=''):
    q = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{E(n)}</a>' for n, u in quellen)
    return (f'<article id="{id_}" style="background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;scroll-margin-top:140px;">'
            f'<img src="/images/{img}" alt="{E(titel)}" loading="lazy" style="width:100%;height:150px;object-fit:cover;display:block;">'
            f'<div style="padding:12px 14px;"><div style="font-size:.8rem;color:#1d4ed8;font-weight:700;">{E(kopf)}</div>'
            f'<h3 style="margin:4px 0 6px;color:#14532d;font-size:1.05rem;">{E(titel)}</h3>'
            f'<p style="margin:0 0 8px;font-size:.9rem;line-height:1.45;color:#0f2942;">{text}</p>'
            '<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;cursor:pointer;"><summary style="color:#14532d;font-weight:600;font-size:.86rem;">⛷️ Details &amp; Quellen</summary>'
            + kv(fakten) + extra + f'<p style="margin:6px 0 0;font-size:.78rem;color:#4b5563;">Quellen: {q}</p></details></div></article>')

GRID = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;">'
NAV = [('#hauptgebiet', '⛷️ Spitzingsee-Tegernsee'), ('#pisten', '🎿 Pisten & Parks'), ('#einkehr', '🍕 Einkehr'), ('#skipass', '💶 Skipass 2026/27'),
       ('#anreise', '🚌 Anreise'), ('#umgebung', '🗺️ Umliegende Gebiete'), ('#quellen', '📚 Quellen')]

b = []
b.append('<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">')
b.append('<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <a href="/content/winter/index.html">Winter-Guide</a> › <span aria-current="page">Skigebiete</span></nav>')
b.append('<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">⛷️ Skigebiete am Spitzingsee &amp; Tegernsee</h1>'
         '<p style="font-size:1.08rem;color:#1f2933;margin:0;">Das Hausgebiet Spitzingsee-Tegernsee direkt vor der Tür der Oberen Firstalm – mit Pisten, Snowpark, Nachtskilauf, Skipasspreisen 2026/27 und der Einkehr am Pistenende. Dazu die Gebiete in der Umgebung. Die Portale zählen unterschiedlich; wo Zahlen abweichen, steht die Spanne mit Quelle.</p></header>')
b.append('<img src="/images/AusblickWinterunterfirst.jpg" alt="Winterblick über das Skigebiet von der Unteren Firstalm" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">')
b.append('<nav class="kat-nav" aria-label="Skigebiete-Bereiche" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
         + ''.join(f'<a href="{h}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for h, t in NAV) + '</nav>')

# Hauptgebiet
b.append(H2('hauptgebiet', '⛷️ Das Hauptgebiet: Spitzingsee-Tegernsee') +
         P('Das Gebiet rund um Stümpfling und Roßkopf verbindet das Tal am Spitzingsee mit dem Tegernseer Tal. Zwei kuppelbare 4er-Sesselbahnen führen auf den Stümpfling – die Stümpflingbahn von Spitzingsee und die Suttenbahn von der Tegernseer Seite; dazu die 2er-Sesselbahn auf den Roßkopf. Die übrigen Anlagen sind Schlepplifte.') +
         kv([('Höhe', '983–1.570 m (Roßkopf-Gipfel 1.580 m)'),
             ('Lifte', '10–11 Anlagen je nach Zählung'),
             ('Pisten', 'rund 14 km (skiresort.de: 14,2 km – 12 % leicht, 58 % mittel, 30 % schwer); manche Portale nennen bis 20 km'),
             ('Saison 2026/27', 'geplant 28.11.2026 bis 04.04.2027 – schneeabhängig'),
             ('Nachtskilauf', 'Donnerstag und Freitag 18:30–21:30 Uhr auf der Stümpfling-Abfahrt'),
             ('Taubenstein', 'Skibetrieb 2015 eingestellt, heute Tourengebiet – <a href="/content/winter/skitouren/taubenstein.html">Taubenstein-Skitour</a>')]) +
         '<p style="font-size:.88rem;"><a href="https://www.alpenbahnen-spitzingsee.de" target="_blank" rel="noopener">→ Liftstatus und Pistenplan bei den Alpenbahnen Spitzingsee</a></p>')

# Pisten & Parks
b.append(H2('pisten', '🎿 Pisten, Parks &amp; Kinderbereiche') + tab(['Abfahrt / Angebot', 'Daten', 'Charakter'], [
    ['Grünsee-Abfahrt', '3,5 km · 530 Hm', 'lange, anspruchsvolle schwarze Abfahrt vom Roßkopf'],
    ['Roßkopf-Abfahrt', '0,5 km · 150 Hm', 'kurz, aber die schwierigste Piste im Gebiet'],
    ['Sutten-Abfahrt', 'ca. 3,2 km', 'abwechslungsreiche rote Abfahrt hinunter zur Suttenbahn (Tegernseer Seite)'],
    ['Stümpfling-Talabfahrt', 'über 2 km', 'mit Blick auf den See; donnerstags und freitags Flutlicht'],
    ['Snowpark Spitzingsee', 'Untere Firstalm, Nordhanglift', 'Kicker, Rails, Boxen, Jib-Barrels und Wave-Track, täglich geshapt'],
    ['Funslope', 'Osthang bei der Unteren Firstalm', 'Wellenbahnen, Steilkurven und Sprünge – für Einsteiger und Fortgeschrittene; Aufbau erst bei ausreichend Schnee, meist nicht gleich zum Saisonstart'],
    ['Kids-Parks', 'Lyralift und Bayernhanglift', 'Kinderbereiche für die ersten Schwünge']]) +
    '')

# Einkehr
LYRA = karte('lyra-alm', 'Alm-Restaurants.jpg', '⭐ Gehört zur Oberen Firstalm · direkt am Pistenende · nur im Winter',
    'Lyra Alm Schirmbar', 'Die Schirmbar am Lyralift, gleich bei der Talstation der Stümpflingbahn: Einkehrschwung zum Schluss, Après-Ski und an den Nachtskilauf-Abenden bis spät geöffnet. Auf der Karte stehen unter anderem Pizza, Flammkuchen, Leberkassemmel, Germknödel – und das Chili con carne, auf das das Firstalm-Team schwört.',
    [('Adresse', 'Lyraweg 6, 83727 Schliersee (am Lyralift, nahe Talstation Stümpflingbahn)'),
     ('Telefon', '<a href="tel:+4980263959390">08026 3959390</a>'),
     ('E-Mail', '<a href="mailto:info@firstalm.de">info@firstalm.de</a> (Obere Firstalm)'),
     ('Öffnungszeiten', 'laut Google: Samstag bis Mittwoch 9–17 Uhr, Donnerstag und Freitag 9–23 Uhr (Nachtskilauf) – Betrieb nur in der Wintersaison'),
     ('Angebot', 'Getränke, warme Speisen, Sitzplätze im Freien, auch zum Mitnehmen'),
     ('Events', 'Après-Ski und Veranstaltungen – aktuelle Termine auf Instagram und Facebook der Schirmbar'),
     ('Ab Oberer Firstalm', 'zu Fuß oder auf Ski bergab, ca. 3,5 km (Google Maps)')],
    [('Angaben der Oberen Firstalm, Öffnungszeiten laut Google (Stand Nov. 2026)', '#quellen')])
FIRST = karte('obere-firstalm', 'obere-firstalm-terrasse.jpg', 'Obere Firstalm · 1.375 m · täglich 11–22 Uhr',
    'Obere Firstalm', 'Die Alm oberhalb des Skigebiets: Küche 11–21 Uhr, Frühstück 8–10 Uhr, abends Mondscheinrodeln auf der beleuchteten Rodelbahn hinunter zum Spitzingsattel.',
    [('Öffnungszeiten', 'täglich 11–22 Uhr, ab 22 Uhr Hüttenruhe; Küche 11–21 Uhr'),
     ('Frühstück', '8–10 Uhr, 17,50 € pro Person'),
     ('Rodeln', 'Mondscheinrodeln ab 27.11.2026, Bahn bis 22:30 Uhr beleuchtet, Schlitten 7 €'),
     ('Telefon', '<a href="tel:+4980267302">08026 7302</a>')],
    [('Angabe der Hütte, Stand 27.11.2026', '/content/winter/firstalm-rodelbahn.html')],
    '<p style="font-size:.84rem;margin:6px 0 0;"><a href="/content/winter/firstalm-rodelbahn.html">→ Rodelbahn Obere Firstalm</a></p>')
b.append(H2('einkehr', '🍕 Einkehr im Skigebiet') + GRID + LYRA + FIRST + '</div>' +
         P('Weitere Hütten rund um den Spitzingsee: <a href="/content/huetten/index.html">Hütten &amp; Almen</a>.'))

# Skipass
b.append(H2('skipass', '💶 Skipass 2026/27') + tab(['Ticket', 'Erwachsene', 'Jugendliche', 'Kinder'], [
    ['Tageskarte Hauptsaison', '53 €', '46 €', '25 €'],
    ['Mittwochskracher (ab 13.01.2027, nicht am Aschermittwoch)', '39 €', '39 €', '25 €'],
    ['Happy-Hour-Skipass ab 14 Uhr', '24 €', '24 €', '12 €'],
    ['MVV-Skipass inkl. Bahn und Bus ab MVV-Netz', '67 €', '62 €', '32 €']]) +
    P('Alle Preise zzgl. 3 € Kartenpfand. Ab zwei Tagen gelten die Mehrtagespässe von <strong>Alpen Plus</strong> – gültig am Spitzingsee, am Sudelfeld, am Brauneck und am Wallberg. Preise ohne Gewähr, aktuell beim Betreiber prüfen.'))

# Anreise
b.append(H2('anreise', '🚌 Anreise &amp; Parken') +
         P('Mit dem MVV-Skipass ist die Fahrt enthalten: mit der Bahn im MVV-Netz bis Schliersee, dann mit dem Bustransfer zur Talstation. Parkplätze gibt es am Spitzingsattel (8 € pro Tag, Stand November 2026), am Kurvenlift und im Ort. <a href="/anreise.html">Alles zur Anreise</a>'))

# Umgebung
b.append(H2('umgebung', '🗺️ Umliegende Skigebiete') + tab(['Gebiet', 'Ort', 'Kennzahlen', 'Besonderheit', 'Alpen Plus'], [
    ['Skiparadies Sudelfeld', 'Bayrischzell / Oberaudorf', '27 Abfahrten, rund 31 km, 14 Lifte', 'eines der größten zusammenhängenden Skigebiete Deutschlands, rund 70 % beschneibar', 'ja'],
    ['Brauneck-Wegscheid', 'Lenggries', '716–1.712 m, 15 Lifte, knapp 31 km', 'Mischung aus Übungshängen, langen Abfahrten und der schwarzen Weltcupabfahrt; viele Hütten', 'ja'],
    ['Wallberg', 'Rottach-Egern', '1 Kabinenbahn, 3,2 km Skiroute, Bergstation 1.620 m', '6,5 km Naturrodelbahn, eine der längsten Deutschlands; Skiroute am Glaslhang für Freerider', 'ja'],
    ['Oedberg', 'Gmund-Ostin', 'Hauptpiste 1 km · 170 Hm', 'kleines Familiengebiet mit Kinderland, Flutlicht täglich bis 21 Uhr, Rodel- und Snowtubingbahn', 'nein']]))

b.append('<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:22px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
         '<a href="https://www.amazon.de/s?k=Skihelm&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Skihelme</a> · '
         '<a href="https://www.amazon.de/s?k=Skibrille&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Skibrillen</a> · '
         '<a href="https://www.amazon.de/s?k=Skihandschuhe&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Skihandschuhe</a> bei Amazon</aside>')
QUELLEN = [('Alpenbahnen Spitzingsee – Aktionsangebote 2026/27 (Mittwochskracher, Happy Hour, MVV-Skipass, Kartenpfand)', 'https://www.alpenbahnen-spitzingsee.de/de/aktionsangebote.html'),
 ('skiresort.de – Spitzingsee-Tegernsee: Tageskarte, Pisten, Lifttypen, Kids-Parks, Snowpark, Grünsee-Abfahrt', 'https://www.skiresort.de/skigebiet/spitzingsee-tegernsee/'),
 ('schneehoehen.de – Saison, Höhe, Lifte, Osthang- und Nordhanglift', 'https://www.schneehoehen.de/skigebiete/info/spitzingsee-stuempfling-taubenstein'),
 ('Oberbayern.de – Funslope am Osthang', 'https://www.oberbayern.de/en/erleben/ski/winter-abenteuer'),
 ('skiresort.info – Snowpark Spitzingsee an der Unteren Firstalm, Nordhanglift', 'https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/test-result/snow-park'),
 ('skiresort.info – Taubensteinbahn, geschlossen 2015', 'https://skiresort.info/ski-resort/spitzingsee-tegernsee/ski-lifts/l1847'),
 ('bahn.de – Nachtskilauf Stümpflingabfahrt', 'https://www.bahn.de/angebot/urlaub/bahnreisen/winterrail/deutschland/alpenregion-tegernsee-schliersee-by'),
 ('Sudelfeld – Alpen Plus Skipassverbund (vier Gebiete)', 'https://www.sudelfeld.de/?p=4491'),
 ('schneehoehen.de – Sudelfeld', 'https://www.schneehoehen.de/skigebiete/info/skiparadies-sudelfeld'),
 ('schneehoehen.de – Brauneck', 'https://www.schneehoehen.de/skigebiete/info/brauneck'),
 ('skiresort.info – Brauneck Pisten, Weltcupabfahrt', 'https://www.skiresort.info/ski-resort/brauneck-lenggries-wegscheid/slope-offering/'),
 ('schneehoehen.de – Wallberg', 'https://www.schneehoehen.de/skigebiete/info/wallberg'),
 ('mountvacation – Wallberg Skiroute Glaslhang', 'https://mountvacation.co.uk/germany/wallberg'),
 ('schneehoehen.de – Oedberg', 'https://www.schneehoehen.de/skigebiete/info/oedberg'),]
b.append(H2('quellen', '📚 Quellen') + '<ul style="line-height:1.7;font-size:.92rem;">' + ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in QUELLEN) +
         '<li>Lyra Alm Schirmbar und Obere Firstalm: Angaben der Obere Firstalm (Stand November 2026), Öffnungszeiten der Schirmbar laut Google</li></ul>'
         '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Alle Angaben ohne Gewähr – Liftbetrieb, Preise und Öffnungszeiten vor Ort prüfen.</p>')
b.append('</article></main>')

s = open(F, encoding='utf-8').read()
a = s.find('<main'); z = s.find('</main>') + 7
head, tail = s[:a], s[z:]
DESC = 'Skigebiet Spitzingsee-Tegernsee: Pisten, Snowpark, Nachtskilauf, Skipass 2026/27, Lyra Alm Schirmbar am Pistenende – dazu Sudelfeld, Brauneck, Wallberg und Oedberg. Mit Quellen.'
head = re.sub(r'<title>.*?</title>', '<title>Skigebiete am Spitzingsee &amp; Tegernsee – Pisten, Skipass 2026/27, Einkehr | alpenexperte.de</title>', head, count=1, flags=re.S)
for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(DESC) + m.group(2), head)
open(F, 'w', encoding='utf-8').write(head + '\n'.join(b) + tail)
print('ok')
