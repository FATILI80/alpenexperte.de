#!/usr/bin/env python3
"""Baut die vier Ratgeber-Hauptseiten neu (Gravel-Schema, belegt):
content/ausruestung/ (inkl. Wanderstöcke + Fehlkäufe), content/layering/, content/fitness/, content/sicherheit/.
Kopf/Fuß von restaurants.html; Unterseiten entfallen per 301 (siehe Abschnitt REDIRECTS)."""
import re, html, json
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:36px 0 10px;scroll-margin-top:140px;">{t}</h2>'
H3 = lambda t: f'<h3 style="color:#14532d;margin:18px 0 6px;font-size:1.05rem;">{t}</h3>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.65;">{t}</p>'
TH = 'style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;vertical-align:top;"'
TD = 'style="padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;"'
def UL(items): return '<ul style="line-height:1.7;color:#1f2933;">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def TAB(kopf, rows): return ('<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:.93rem;margin:8px 0 14px;"><tr>'
                             + ''.join(f'<th {TH}>{E(k)}</th>' for k in kopf) + '</tr>' + ''.join('<tr>' + ''.join(f'<td {TD}>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table></div>')
def BOX(t, farbe='#e8f5e9', rand='#2e7d32'): return f'<div style="background:{farbe};border-left:5px solid {rand};padding:12px 16px;border-radius:10px;margin:14px 0;color:#1f2933;line-height:1.6;">{t}</div>'
def IMG(src, alt): return f'<img src="/images/{src}" alt="{E(alt)}" loading="lazy" style="width:100%;max-height:280px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">'
def AFF(links): return ('<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:18px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
                        + ' · '.join(f'<a href="https://www.amazon.de/s?k={q}&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">{t}</a>' for t, q in links) + ' bei Amazon</aside>')

class Q:  # nummerierte Quellen je Seite
    def __init__(s): s.l = []
    def __call__(s, titel, url):
        if (titel, url) not in s.l: s.l.append((titel, url))
        n = s.l.index((titel, url)) + 1
        return f'<sup><a href="#q{n}" style="color:#1d4ed8;text-decoration:none;">[{n}]</a></sup>'
    def liste(s): return (H2('quellen', '📚 Quellen') + '<ol style="line-height:1.7;font-size:.92rem;">'
                          + ''.join(f'<li id="q{i}"><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for i, (t, u) in enumerate(s.l, 1)) + '</ol>'
                          + '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Allgemeine Informationen, keine medizinische oder individuelle Beratung.</p>')

def seite(pfad, titel, h1, intro, hero, nav, body, desc, crumb):
    s = open('restaurants.html', encoding='utf-8').read()
    a = s.find('<main'); z = s.find('</main>') + 7
    head, tail = s[:a], s[z:]
    url = 'https://alpenexperte.de/' + pfad
    head = re.sub(r'<title>.*?</title>', f'<title>{html.escape(titel)} | alpenexperte.de</title>', head, count=1, flags=re.S)
    for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(desc) + m.group(2), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(titel) + m.group(2), head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S)
    absol = lambda t: re.sub(r'((?:href|src)=")(?!https?:|/|#|mailto:|tel:|data:|javascript:)([^"]+)"', r'\1/\2"', t)
    head, tail = absol(head), absol(tail)
    m = ['<main id="main"><article class="container" style="max-width:960px;margin:0 auto;padding:24px 16px 48px;">',
         f'<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">{crumb}</span></nav>',
         f'<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">{h1}</h1><p style="font-size:1.08rem;color:#1f2933;margin:0;line-height:1.6;">{intro}</p></header>', hero,
         '<nav class="kat-nav" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
         + ''.join(f'<a href="#{i}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for i, t in nav) + '</nav>',
         body, '<p style="margin-top:22px;font-size:.92rem;">Weiter: <a href="/content/ausruestung/">Ausrüstung</a> · <a href="/content/layering/">Layering</a> · <a href="/content/fitness/">Fitness</a> · <a href="/content/sicherheit/">Sicherheit</a> · <a href="/wetter-webcams.html">Wetter &amp; Webcams</a></p>',
         '</article></main>']
    open(pfad, 'w', encoding='utf-8').write(head + '\n'.join(m) + tail)
    print('ok', pfad)

DAV = 'https://www.alpenverein.de/artikel/'
# ============ AUSRÜSTUNG ============
q = Q()
b = []
b.append(H2('schuhe', '🥾 Schuhe: die Kategorien A bis D')
 + P('Wander- und Bergschuhe lassen sich nach ihrem Einsatzbereich in die Kategorien A bis D einordnen' + q('Bergzeit – Kategorien Wander- und Bergschuhe', 'https://www.bergzeit.de/magazin/kategorie-wanderschuhe-bergschuhe-info/')
     + '. Das System stammt ursprünglich vom Hersteller Meindl und wurde von vielen, aber nicht allen Herstellern übernommen' + q('travelbook – Wanderschuh-Ratgeber', 'https://www.travelbook.de/news/wanderschuh-ratgeber') + '. Das System ist nicht genormt, die Übergänge sind fließend – entscheidend ist das Gelände, nicht das Etikett.')
 + TAB(['Kategorie', 'Typ', 'Sohle / Schaft', 'Gelände', 'Steigeisen'], [
     ['A, A/B', 'Freizeit- und Wanderschuh', 'weich, niedrig bis mittel', 'gute Wege, Forst- und Almwege', 'nein'],
     ['B', 'Wander- und Trekkingschuh', 'mittelfest, knöchelhoch', 'Bergwege abseits befestigter Wege, Geröll, Wurzeln', 'nein'],
     ['B/C', 'Trekkingstiefel', 'härtere Zwischensohle, hoher Schaft', 'anspruchsvolle Trekking- und leichte Hochtouren', 'bedingt (Körbchen)'],
     ['C', 'Bergstiefel', 'steif, hoher Schaft, Geröllschutz', 'wegloses Hochgebirge, Klettersteige, Gletscher', 'bedingt'],
     ['D', 'Hochtouren-/Expeditionsstiefel', 'maximal steif', 'Eis, Firn, Hochtouren', 'voll']])
 + P('Zusammengefasst nach Bergzeit und Sport Conrad' + q('Bergzeit – Kategorien Wander- und Bergschuhe', 'https://www.bergzeit.de/magazin/kategorie-wanderschuhe-bergschuhe-info/') + q('Sport Conrad – Kategorien', 'https://www.sport-conrad.com/blog/de/kategorien-wanderschuhe-bergschuhe/')
     + '. Trekkingstiefel der Kategorie B haben meist keine Lippe für Steigeisen an der Sohle' + q('travelbook – Wanderschuh-Ratgeber', 'https://www.travelbook.de/news/wanderschuh-ratgeber') + '; Steigeisen gehen erst ab B/C bedingt.')
 + BOX('<strong>Für unsere Touren ab der Oberen Firstalm</strong> (Brecherspitz, Bodenschneid, Rotwand, Taubenstein): Das sind Bergwege mit Wurzeln, Geröll und steilen Passagen – dafür ist ein knöchelhoher Schuh der Kategorie B die passende Wahl. Für die Forststraßen zur Unteren Firstalm oder zum Spitzingsee reicht ein Schuh der Kategorie A/B.'))
b.append(H2('rucksack', '🎒 Rucksack &amp; Packliste')
 + P('Für Tagestouren reicht in der Regel ein Rucksack mit 25 bis 30 Litern' + q('DAV – Ausrüstung beim Bergwandern', DAV + 'ausruestung-beim-bergwandern_54393172-b5e7-42fa-b84e-1525920a0ba0')
     + '. Wichtig sind eine anatomische Form, gepolsterte Schultergurte und eine Rückenbelüftung' + q('DAV – Der richtig gepackte Wanderrucksack', DAV + 'das-ist-der-richtig-gepackte-wanderrucksack_633664a0-ba50-4eb1-8251-470355129173') + '.')
 + H3('Was laut DAV in den Tagesrucksack gehört')
 + UL(['Erste-Hilfe-Set (Heft- und Blasenpflaster, Mullbinde, Desinfektion, Pinzette)', 'regelmäßig einzunehmende Medikamente', 'Handy/Smartphone', 'Regen- und Sonnenschutz',
       'Proviant und Trinkflasche – mindestens 1 Liter pro Person', 'Ersatzwäsche, je nach Jahreszeit Mütze und Handschuhe', 'Rettungsdecke bzw. Biwaksack',
       'UV-Schutz: Kopfbedeckung, Sonnenbrille, Sonnencreme' + q('DAV – Der richtig gepackte Wanderrucksack', DAV + 'das-ist-der-richtig-gepackte-wanderrucksack_633664a0-ba50-4eb1-8251-470355129173')])
 + P('Packen: Schweres körpernah, Erste-Hilfe-Set und Wetterschutz gut erreichbar. Biwaksack und Erste-Hilfe-Set dürfen unten liegen – man braucht sie hoffentlich nicht' + q('DAV – Packliste Frühjahr', DAV + 'packliste-fur-wanderungen-im-fruhjahr_c1c01d77-76a2-49bf-84f0-e5784bc546d9') + '.'))
b.append(H2('stoecke', '🥢 Wanderstöcke: Länge, Einsatz, Grenzen')
 + H3('Die richtige Länge')
 + P('Steht der Stock senkrecht auf dem Boden, sollte der Ellbogen etwa im rechten Winkel (90°) gebeugt sein' + q('DAV – Trekkingstöcke richtig einsetzen', DAV + 'so-geht-das-trekkingstocke-richtig-einsetzen_d294025d-018e-4cb3-b1ab-d12c1311476b') + q('Stiftung Warentest – Wanderstöcke', 'https://www.test.de/Wanderstoecke-im-Test-5623087-6084170/')
     + '. Als grobe Faustformel gilt Körpergröße × 0,7 – bei 1,80 m also rund 1,26 m. Bergauf kürzer, bergab länger einstellen; Stiftung Warentest nennt für steile Abstiege 5 bis 10 cm mehr und rät, dann die Hände aus den Schlaufen zu nehmen' + q('Stiftung Warentest – Wanderstöcke', 'https://www.test.de/Wanderstoecke-im-Test-5623087-6084170/') + q('news.at / dpa – Wanderstöcke', 'https://www.news.at/gesundheit/darauf-kommt-es-bei-wanderstocken-wirklich-an') + '.')
 + TAB(['Körpergröße', 'Stocklänge (× 0,7)', 'bergauf', 'bergab'], [[f'{k} cm', f'ca. {round(k*0.7)} cm', f'ca. {round(k*0.7)-5} cm', f'ca. {round(k*0.7)+5} cm'] for k in (160, 170, 180, 190)])
 + H3('Entlasten Stöcke wirklich die Knie?')
 + P('Hersteller und Händler nennen gern Werte wie „bis zu 30 Prozent“ – diese Zahlen sind nicht einheitlich belegt. Eine Studie der Universität Innsbruck fand auf mäßig abfallenden Wegen (bis 20 % Gefälle) <em>keine</em> Entlastung des Bewegungsapparats; die Stöcke verleiteten eher zu größeren Schritten' + q('Universität Innsbruck – Über Stock und Stein', 'https://www.uibk.ac.at/archive/ipoint/news/uni_und_forschung/20021106.html')
     + '. Sinnvoll sind Stöcke vor allem gezielt: bergauf parallel gesetzt als Schub an hohen Absätzen, steil bergab vor dem Körper zum Abfedern, und auf langen Touren, weil sie die Last auf Arme und Beine verteilen und die Ermüdung verzögern können' + q('news.at / dpa – Wanderstöcke', 'https://www.news.at/gesundheit/darauf-kommt-es-bei-wanderstocken-wirklich-an') + '.')
 + BOX('<strong>Praxis am Spitzingsee:</strong> Beim langen Abstieg von der Rotwand oder der Bodenschneid und im Winter auf festgetretenem Schnee sind Stöcke Gold wert. Auf den kurzen Wegen um den See und zur Unteren Firstalm kannst du sie getrost im Rucksack lassen.'))
b.append(H2('fehlkauf', '⚠️ Fehlkäufe vermeiden')
 + UL(['<strong>Schuh nach Gelände kaufen, nicht nach Optik:</strong> Entscheidend ist der Einsatzzweck – ein weicher A-Schuh ist auf Geröll zu weich, ein steifer C-Stiefel auf Forstwegen unnötig schwer.' + q('Bergzeit – Kategorien Wander- und Bergschuhe', 'https://www.bergzeit.de/magazin/kategorie-wanderschuhe-bergschuhe-info/'),
       '<strong>„Wasserdicht“ prüfen:</strong> Laut DAV gilt ein Stoff ab 1.300 mm Wassersäule als wasserdicht; für Regenjacken empfehlen Fachportale eher 10.000 mm, mit schwerem Rucksack 20.000 mm.' + q('DAV – Wetterschutzbekleidung', DAV + 'wie-klappt-das-wetterschutzbekleidung_92524e64-3fc4-4f8d-aee3-d3c3b140dcfb') + q('Bergzeit – Wasserdicht oder wasserabweisend?', 'https://www.bergzeit.de/magazin/wasserdicht-wasserabweisend/') + ' Mehr dazu unter <a href="/content/layering/#shell">Layering</a>.',
       '<strong>Rucksack nicht zu groß:</strong> 25–30 Liter reichen für den Tag; ein großer Rucksack verleitet zum Überladen.' + q('DAV – Ausrüstung beim Bergwandern', DAV + 'ausruestung-beim-bergwandern_54393172-b5e7-42fa-b84e-1525920a0ba0'),
       '<strong>Stöcke mit sicherem Verschluss:</strong> Die Längenfixierung mit Druck testen – rutscht der Stock beim Draufstützen zusammen, ist das gefährlich.' + q('DAV – Trekkingstöcke richtig einsetzen', DAV + 'so-geht-das-trekkingstocke-richtig-einsetzen_d294025d-018e-4cb3-b1ab-d12c1311476b'),
       '<strong>Daune nicht für nasses Wetter:</strong> Wird Daune nass, verliert sie fast ihre gesamte Isolationskraft – für feuchte Tage ist Kunstfaser die robustere Wahl.' + q('bergwelten – Daune vs. Kunstfaser', 'https://www.bergwelten.com/a/daunenjacke-vs-kunstfaserjacke')])
 + AFF([('Wanderschuhe Kategorie B', 'Wanderschuhe+Kategorie+B'), ('Wanderrucksäcke 25–30 l', 'Wanderrucksack+30+Liter'), ('Teleskop-Wanderstöcke', 'Teleskop+Wanderst%C3%B6cke')]))
b.append(q.liste())
seite('content/ausruestung/index.html', 'Ausrüstung fürs Bergwandern – Schuhe, Rucksack, Wanderstöcke, Fehlkäufe',
      '🎒 Ausrüstung fürs Bergwandern', 'Welcher Schuh für welches Gelände, was in den Rucksack gehört, wie lang die Stöcke sein sollten – und welche Fehlkäufe du dir sparen kannst. Alles mit Quellen, bezogen auf die Touren rund um Spitzingsee und Obere Firstalm.',
      IMG('ausruestung-schuhe.jpg', 'Wanderschuhe'), [('schuhe', '🥾 Schuhe'), ('rucksack', '🎒 Rucksack'), ('stoecke', '🥢 Wanderstöcke'), ('fehlkauf', '⚠️ Fehlkäufe'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Bergwander-Ausrüstung mit Quellen: Schuhkategorien A–D, Rucksack und DAV-Packliste, Wanderstöcke richtig einstellen und die häufigsten Fehlkäufe.', 'Ausrüstung')

# ============ LAYERING ============
q = Q(); b = []
b.append(H2('prinzip', '🧅 Das Zwiebelprinzip')
 + P('Statt einer dicken Jacke trägt man mehrere dünne Schichten, die sich einzeln an- und ausziehen lassen. Der Vorteil laut DAV: Zwischen den Schichten wird Luft eingeschlossen, die isoliert' + q('DAV – Fleece & Midlayer', DAV + 'fleece-oberteile-midlayer-bergsport_0ac100e2-6a46-4a0f-8327-352cd6b73fb6')
     + '. Klassisch sind drei Lagen: Funktionsunterwäsche (Base), wärmende Schicht (Mid) und Wetterschutz (Shell).')
 + TAB(['Schicht', 'Aufgabe', 'Typische Materialien'], [['1 · Baselayer', 'Feuchtigkeit von der Haut wegleiten', 'Merino, Polyester, Mischgewebe'], ['2 · Midlayer', 'Wärme halten', 'Fleece, Merino, Daune, Kunstfaser'], ['3 · Shell', 'Regen und Wind abhalten, Dampf rauslassen', 'Membran-Hardshell, Softshell']]))
b.append(H2('base', '👕 Baselayer: Merino oder Synthetik?')
 + P('Funktionsunterwäsche darf nicht einschneiden, scheuern oder die Bewegung einschränken' + q('DAV – Funktionsunterwäsche', DAV + 'wie-funktioniert-das-funktionsunterwasche_1e074d5e-8d7a-497f-8dee-579850baffc2') + '. Beide Fasern haben ihre Stärken:')
 + TAB(['', 'Merino', 'Synthetik (Polyester u. a.)'], [
     ['Geruch', 'lüftet gut aus, nimmt kaum Geruch an', 'kann bei starkem Schwitzen Geruch annehmen'],
     ['Trocknung', 'langsamer als Kunstfaser', 'schnell'],
     ['Haltbarkeit', 'weniger strapazier- und reißfest', 'robust'],
     ['Gefühl bei Nässe', 'wärmt auch feucht', 'fühlt sich feucht kühler an']])
 + P('Zusammengestellt nach Bergzeit, outdoor-magazin und Patagonia' + q('Bergzeit – Merinowolle Materialkunde', 'https://www.bergzeit.de/magazin/merinowolle-materialkunde-die-funktion-der-faser-im-ueberblick/') + q('outdoor-magazin – Funktionsunterwäsche', 'https://www.outdoor-magazin.com/outdoorbekleidung/funktionsunterwaesche/') + q('Patagonia – Zwiebelprinzip', 'https://eu.patagonia.com/ch/de/guides/cold-weather-layering/')
     + '. Mischgewebe aus Merino und Kunstfaser gleichen die Schwächen der reinen Wolle teilweise aus' + q('Bergzeit – Merinowolle Materialkunde', 'https://www.bergzeit.de/magazin/merinowolle-materialkunde-die-funktion-der-faser-im-ueberblick/') + '.')
 + BOX('<strong>Faustregel:</strong> Für Mehrtagestouren mit Hüttenübernachtung ohne Waschgelegenheit spielt Merino seine Geruchsvorteile aus. Für schweißtreibende Tagestouren, Skitouren oder MTB trocknet Synthetik schneller.'))
b.append(H2('mid', '🧥 Midlayer: Fleece, Daune, Kunstfaser')
 + P('Fleece und Merino gehören zur Midlayer-Schicht, die auch aus mehreren Lagen bestehen kann' + q('DAV – Fleece & Midlayer', DAV + 'fleece-oberteile-midlayer-bergsport_0ac100e2-6a46-4a0f-8327-352cd6b73fb6') + '. Für Pausen und kalte Tage kommt eine Isolationsjacke dazu.')
 + TAB(['', 'Daune', 'Kunstfaser'], [['Wärme pro Gewicht', 'sehr hoch, kleines Packmaß', 'gut, aber schwerer und größer'], ['bei Nässe', 'verliert fast die gesamte Isolationskraft', 'wärmt auch nass'], ['Pflege', 'aufwendig', 'pflegeleicht'], ['sonst', 'tierisches Produkt', 'Mikroplastik']])
 + P('Nach bergwelten' + q('bergwelten – Daune vs. Kunstfaser', 'https://www.bergwelten.com/a/daunenjacke-vs-kunstfaserjacke') + '. Die Qualität von Daune wird in <strong>cuin</strong> (Bauschkraft) angegeben: Je höher, desto wärmer bei gleichem Gewicht. Laut DAV gelten 550 cuin als Minimum, Expeditionsjacken haben 900 cuin; wärmer macht aber auch die Füllmenge' + q('DAV – Daune oder Kunstfaser?', DAV + 'wie-funktioniert-das-daune-oder-kunstfaser_44f44be1-c542-4cd0-b2b7-8f28774f025d') + '.'))
b.append(H2('shell', '🌧️ Shell: Wassersäule und Atmungsaktivität')
 + P('Beim Bergsteigen wird man durch Schwitzen von innen oft nässer als vom Regen – deshalb muss die äußere Schicht nicht nur dicht, sondern auch dampfdurchlässig sein' + q('DAV – Wetterschutzbekleidung', DAV + 'wie-klappt-das-wetterschutzbekleidung_92524e64-3fc4-4f8d-aee3-d3c3b140dcfb') + '.')
 + TAB(['Kennwert', 'Was er misst', 'Einordnung'], [
     ['Wassersäule (mm)', 'Wasserdruck, bis das Material durchlässt', 'ab 1.300 mm „wasserdicht“ laut DIN (400–1.300 mm: wasserabweisend)' + q('DAV – Wetterschutzbekleidung', DAV + 'wie-klappt-das-wetterschutzbekleidung_92524e64-3fc4-4f8d-aee3-d3c3b140dcfb') + '; EN 343 Klasse 3: 1.325 mm, Klasse 4: 2.039 mm' + q('Bergzeit – Wasserdicht oder wasserabweisend?', 'https://www.bergzeit.de/magazin/wasserdicht-wasserabweisend/')],
     ['Empfehlung Regenjacke', 'Praxiswert der Fachportale', 'ca. 10.000 mm; mit schwerem Rucksack eher 20.000 mm' + q('Bergzeit – Wasserdicht oder wasserabweisend?', 'https://www.bergzeit.de/magazin/wasserdicht-wasserabweisend/') + q('bergwelten – Wassersäule', 'https://www.bergwelten.com/a/wie-dicht-ist-meine-regenjacke')],
     ['RET', 'Widerstand gegen Wasserdampf (je niedriger, desto atmungsaktiver)', 'unter RET 6 sehr gut, Top-Materialien unter 0,5' + q('DAV – Wetterschutzbekleidung', DAV + 'wie-klappt-das-wetterschutzbekleidung_92524e64-3fc4-4f8d-aee3-d3c3b140dcfb') + '; gemessen nach ISO 11092 („Hohenstein-Test“)' + q('Bergzeit – Atmungsaktivität MVTR/RET', 'https://www.bergzeit.de/magazin/atmungsaktiv-mvtr-ret/')]])
 + P('Wassersäule und Atmungsaktivität sind ein Zielkonflikt: Je dichter ein Material gegen Wasser von außen ist, desto schwerer lässt es in der Regel Dampf nach außen' + q('Sport Conrad – Wassersäule bei Regenjacken', 'https://www.sport-conrad.com/blog/de/wassersaeule-bei-regenjacken/') + '. Laut Bergzeit reichen ohne Rucksack meist 10.000 mm, mit schwerem Rucksack sollten es 20.000 mm sein' + q('Bergzeit – Wasserdicht oder wasserabweisend?', 'https://www.bergzeit.de/magazin/wasserdicht-wasserabweisend/') + '.'))
b.append(H2('praxis', '🏔️ Kombinationen für unsere Region')
 + TAB(['Situation', 'Base', 'Mid', 'Shell'], [
     ['Sommer, Brecherspitz ab Firstalm', 'kurzes Synthetik- oder Merino-Shirt', 'dünnes Fleece im Rucksack', 'leichte Regenjacke'],
     ['Herbst, Rotwand-Runde', 'langärmelig', 'Fleece; Isojacke für den Gipfel', 'Regenjacke, Mütze, Handschuhe'],
     ['Winter, Rodeln an der Firstalm', 'lang, warm', 'Fleece + Kunstfaserjacke', 'wind- und wasserdichte Jacke und Hose'],
     ['Skitour Taubenstein', 'dünn, schnell trocknend', 'leichtes Fleece; Isojacke für Abfahrt/Pause', 'Hardshell im Rucksack']])
 + P('Die Tabelle ist eine Orientierung der Redaktion – entscheidend sind Wetter und eigenes Wärmeempfinden. Das aktuelle Bergwetter steht unter <a href="/wetter-webcams.html">Wetter &amp; Webcams</a>.')
 + AFF([('Merino-Funktionsshirts', 'Merino+Funktionsshirt'), ('Fleecejacken', 'Fleecejacke+Wandern'), ('Regenjacken 20.000 mm', 'Regenjacke+20000+mm+Wassers%C3%A4ule')]))
b.append(q.liste())
seite('content/layering/index.html', 'Layering & Zwiebelprinzip – Baselayer, Midlayer, Shell erklärt',
      '🧅 Layering: das Zwiebelprinzip fürs Bergwandern', 'Merino oder Synthetik, Daune oder Kunstfaser, wie viel Wassersäule und welcher RET-Wert – die drei Schichten verständlich erklärt, mit Quellen und Kombinationen für Touren am Spitzingsee.',
      IMG('wanderpfad-im-nebel.jpeg', 'Wanderweg im Nebel'), [('prinzip', '🧅 Prinzip'), ('base', '👕 Baselayer'), ('mid', '🧥 Midlayer'), ('shell', '🌧️ Shell'), ('praxis', '🏔️ Praxis'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Zwiebelprinzip mit Quellen: Merino vs. Synthetik, Daune vs. Kunstfaser (cuin), Wassersäule nach DIN/EN 343 und RET-Wert – plus Kombinationen für Touren am Spitzingsee.', 'Layering')

# ============ FITNESS ============
q = Q(); b = []
b.append(H2('warum', '❤️ Warum Fitness am Berg zählt')
 + P('Bergwandern ist Ausdauersport – die Belastung für Herz und Kreislauf setzt Gesundheit und eine realistische Selbsteinschätzung voraus' + q('DAV – Bergwandern: 10 DAV-Empfehlungen', 'https://www.alpenverein.de/bergsport/sicherheit/10-empfehlungen/wandern-bergwandern-10-dav-empfehlungen_aid_11737.html')
     + '. Der DAV schreibt, dass der überwältigende Teil der Wanderunfälle auf mangelnde körperliche Fitness zurückgeht' + q('DAV – Fit in die Wandersaison', 'https://alpenverein.de/bergsport/aktiv-sein/bergwandern-so-geht-das/so-geht-das-fit-in-die-wandersaison_aid_36521.html')
     + '. Die häufigste Unfallursache beim Wandern ist der Sturz – 2021 bei 60 Prozent aller Meldungen' + q('DAV – Bergunfallstatistik 2021', 'https://www.alpenverein.de/verband/bergsport/sicherheitsforschung/bergunfallstatistik/bergunfallstatistik-2021') + '. Müde Beine stolpern eher.'))
b.append(H2('umfang', '📏 Wie viel Training?')
 + P('Die WHO empfiehlt Erwachsenen pro Woche 150 bis 300 Minuten moderate Ausdauerbewegung (oder 75 bis 150 Minuten intensive) und an mindestens zwei Tagen muskelkräftigende Übungen' + q('WHO – Guidelines on physical activity (2020)', 'https://www.who.int/europe/publications/i/item/9789240014886') + q('TUM – WHO-Richtlinien 2020 im Vergleich', 'https://www.hs.mh.tum.de/fileadmin/w00bbr/exercisebiology/downloads/2020_episode015_who_richtlinien.pdf')
     + '. Das ist eine gute Basis auch für die Berge.')
 + TAB(['Baustein', 'Beispiele laut DAV', 'Wozu am Berg'], [
     ['Ausdauer', 'Laufen, Spazierengehen, Nordic Walking, Hometrainer', 'lange Aufstiege ohne Einbruch'],
     ['Kraft', 'sportliches Treppensteigen, Fitnessstudio', 'kontrollierte Abstiege, Stufen'],
     ['Kraftausdauer', 'Radfahren', 'gleichmäßiges Tempo über Stunden'],
     ['Koordination', 'Gehen und Walken abseits von Wegen im Gelände', 'Trittsicherheit auf Wurzeln und Geröll']])
 + P('Trainingsbeispiele nach DAV' + q('DAV – Start der Bergwandersaison', 'https://www.alpenverein.de/verband/presse/pressemeldungen/start-der-bergwandersaison-tipps-zur-richtigen-vorbereitung-ausruestung-und-tourenplanung') + q('DAV – Fit in die Wandersaison', DAV + 'so-geht-das-fit-in-die-wandersaison_cbb2a951-df80-453c-b1e2-75799bfc755e') + '.'))
b.append(H2('plan', '🗓️ 8-Wochen-Aufbau (Beispiel)')
 + P('Ein Vorschlag der Redaktion, der den WHO-Umfang Schritt für Schritt erreicht. Wer Vorerkrankungen hat oder lange inaktiv war, klärt das Training vorher ärztlich ab.')
 + TAB(['Woche', 'Ausdauer', 'Kraft &amp; Koordination', 'Am Berg'], [
     ['1–2', '3 × 30 min zügig gehen oder radeln', '2 × 15 min: Kniebeugen, Ausfallschritte, Wadenheben', 'Runde Untere Firstalm – Spitzingsee (7,7 km, 281 Hm)'],
     ['3–4', '3 × 40 min, eine Einheit mit Steigung', '2 × 20 min, dazu Einbeinstand', 'Spitzingsee & Wurzhütte ab Firstalm (8,2 km, 281 Hm)'],
     ['5–6', '2 × 45 min + 1 × 60–90 min', '2 × 20 min, Treppensteigen', 'Blecksteinhaus-Runde (11,1 km, 343 Hm)'],
     ['7–8', '2 × 45 min + 1 × 2 h im Gelände', '2 × 25 min', 'erster Gipfel ab Firstalm: Brecherspitz (3,6 km, 373 Hm) oder Bodenschneid (3,4 km, 296 Hm)']])
 + P('Die Runden ab der Oberen Firstalm sind mit BRouter nachgerechnet – Details und Karten unter <a href="/content/wandern/index.html">Wandern</a>.'))
b.append(H2('gehzeit', '⏱️ Selbstcheck: die DAV-Gehzeit')
 + P('Mit der Gehzeitformel des DAV kannst du prüfen, ob du im „Normaltempo“ bist: 4 km pro Stunde in der Ebene, 300 Höhenmeter pro Stunde bergauf, 500 Höhenmeter pro Stunde bergab. Der größere Wert aus Strecken- und Höhenzeit plus die Hälfte des kleineren ergibt die Gehzeit ohne Pausen. Wer deutlich langsamer ist, sollte kürzere Touren wählen oder mehr Zeit einplanen.')
 + BOX('Beispiel: 8 km und 400 Hm auf und ab → Strecke 2 h, Höhe 1:20 + 0:48 = 2:08 h → 2:08 + 1:00 = <strong>ca. 3:10 h</strong>.')
 + AFF([('Fitnessbänder', 'Fitnessband+Set'), ('Pulsuhren', 'Pulsuhr+Wandern')]))
b.append(q.liste())
seite('content/fitness/index.html', 'Fit fürs Bergwandern – Training, Umfang, 8-Wochen-Plan',
      '💪 Fit fürs Bergwandern', 'Wie viel Training sinnvoll ist, welche Bausteine der DAV empfiehlt und ein 8-Wochen-Aufbau mit Touren ab der Oberen Firstalm – mit Quellen von WHO und Alpenverein.',
      IMG('wandern-brecherspitz.jpg', 'Blick vom Weg zur Brecherspitz auf den Spitzingsee'), [('warum', '❤️ Warum'), ('umfang', '📏 Umfang'), ('plan', '🗓️ 8-Wochen-Plan'), ('gehzeit', '⏱️ Gehzeit'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Training fürs Bergwandern mit Quellen: WHO-Bewegungsempfehlung, DAV-Trainingsbausteine, 8-Wochen-Plan mit Touren ab der Oberen Firstalm und DAV-Gehzeitformel.', 'Fitness')

# ============ SICHERHEIT ============
q = Q(); b = []
b.append(H2('regeln', '✅ Die 10 Empfehlungen der Alpenvereine')
 + P('Die alpinen Vereine haben zehn Empfehlungen formuliert, damit Bergwanderungen möglichst sicher und genussvoll werden' + q('DAV – Bergwandern: 10 DAV-Empfehlungen', 'https://www.alpenverein.de/bergsport/sicherheit/10-empfehlungen/wandern-bergwandern-10-dav-empfehlungen_aid_11737.html') + q('10 DAV-Empfehlungen (PDF, via Pfronten)', 'https://www.pfronten.de/fileadmin/user_upload/Tourismus/Flyer_Plakate_Homepage/Die_10_DAV_Empfehlungen_zum_Wandern.pdf') + '. In Kurzform:')
 + '<ol style="line-height:1.8;color:#1f2933;"><li>Gesund in die Berge</li><li>Sorgfältige Planung</li><li>Vollständige Ausrüstung</li><li>Passendes Schuhwerk</li><li>Trittsicherheit ist der Schlüssel</li><li>Auf markierten Wegen bleiben</li><li>Regelmäßige Pausen</li><li>Verantwortung für Kinder</li><li>Kleine Gruppen</li><li>Respekt für Natur und Umwelt</li></ol>'
 + P('Die vollständigen Texte stehen beim DAV. Passende Ausrüstung findest du unter <a href="/content/ausruestung/">Ausrüstung</a>, die Fitness-Grundlagen unter <a href="/content/fitness/">Fitness</a>.'))
b.append(H2('unfaelle', '📊 Was passiert wirklich?')
 + P('Die meisten Schadensmeldungen an die DAV-Versicherung kommen vom Wandern; die häufigste Ursache sind Stürze ohne Fremdeinwirkung' + q('DAV – Bergunfallstatistik 2021', 'https://www.alpenverein.de/verband/bergsport/sicherheitsforschung/bergunfallstatistik/bergunfallstatistik-2021') + '. Die Ursachen beim Wandern laut DAV-Fact-Sheets:')
 + TAB(['Ursache beim Wandern', '2021', '2022'], [['Sturz', '60 %', '58 %'], ['Blockierung (verstiegen, erschöpft, nicht mehr weiter)', '25 %', '23 %'], ['körperliche Probleme', '11 %', '14 %'], ['Sturz oder Kreislaufprobleme', '2 %', '1 %'], ['Sonstiges', '2 %', '4 %']])
 + P('Quellen: DAV-Bergunfallstatistik 2021 und 2022' + q('DAV – Unfallstatistik Fact Sheet 2021', 'https://alpenverein.de/files/DAV-Unfallstatistik-Fact-Sheet-2021_32935.pdf') + q('DAV – Unfallstatistik Fact Sheet 2022', 'https://alpenverein.de/files/unfallstatistik-fact-sheet-2022.pdf') + '. Die Statistik erfasst nur gemeldete Fälle von DAV-Mitgliedern. Bei älteren Mitgliedern steigen die Todesfälle vor allem durch Herz-Kreislauf-Versagen' + q('DAV Panorama 2/2010 – Wie riskant ist Bergsport?', 'https://www.alpenverein.de/chameleon/public/181a2714-e66c-15d5-f9f4-e9f625ed1dd3/Wie-riskant-ist-Bergsport_18535.pdf') + '.')
 + BOX('<strong>Daraus folgt:</strong> Trittsicherheit üben, Touren passend zur Kondition wählen, rechtzeitig umkehren – und beim Abstieg konzentriert bleiben, wenn die Beine müde werden.'))
b.append(H2('notruf', '🆘 Notruf &amp; alpines Notsignal')
 + BOX('<strong>Notruf 112</strong> – europaweit; in Österreich zusätzlich Alpin-Notruf 140' + q('DAV – Notruf und Rettung in den Alpen', DAV + 'notruf-und-rettung-in-den-alpen_3802c636-0bd1-4f83-a33a-e9b266bd51d8') + '. Die 112 hat den Vorteil, in jedem verfügbaren Netz durchzukommen' + q('oesterreich.gv.at – Verhalten bei Bergunfällen', 'https://www.oesterreich.gv.at/themen/notfaelle_unfaelle_und_kriminalitaet/katastrophenfaelle/1/Seite.29500327.html') + '.', '#fef2f2', '#b91c1c')
 + H3('Die 5 W beim Notruf')
 + UL(['Wer meldet? (Rückrufnummer)', 'Was ist passiert?', 'Wo genau ist der Unfallort?', 'Wie viele Verletzte?', 'Welche Verletzungen?' + q('DAV – Tipps & Infos (PDF)', 'https://www.alpenverein.de/files/BBS_tippinfos_10240.pdf')])
 + P('Danach das Handy eingeschaltet lassen und nicht mehr telefonieren, damit die Leitstelle zurückrufen kann' + q('DAV – Erste Hilfe für Bergsportler (PDF)', 'https://www.forststeig.sachsen.de/download/Erste_Hilfe_2012_DAV.pdf') + '. In Bayern, Tirol und Südtirol übermittelt die kostenlose App „SOS EU ALP“ beim Notruf die GPS-Position an die zuständige Leitstelle' + q('DAV – Notfall-App SOS EU ALP', DAV + 'notfall-app-sos-eu-alp_69098d79-169b-40df-8bca-daa419eeced6') + '.')
 + H3('Kein Empfang? Das alpine Notsignal')
 + UL(['eine Minute lang alle 10 Sekunden ein Zeichen geben (6 × pro Minute) – Rufen, Pfeifen, Licht', 'eine Minute Pause, dann wiederholen', 'Antwort der Retter: 3 × pro Minute' + q('DAV – Wie funktioniert das: Notruf', DAV + 'wie-funktioniert-das-notruf_29889ad0-4363-4b8f-b52e-a5d0fecd7168')]))
b.append(H2('erstehilfe', '⛑️ Erste Hilfe unterwegs')
 + P('In abgelegenen Bergregionen und bei schlechten Verhältnissen kann es Stunden dauern, bis organisierte Rettung eintrifft – deshalb hat die Erste Hilfe oberste Priorität' + q('DAV – Tipps und Infos: Wetter, Notruf, Erste Hilfe (PDF)', 'https://magazin.alpenverein.de/files/1801-tipps_und_infos_ol.pdf') + '.')
 + UL(['<strong>Ruhe bewahren</strong>, Lage beurteilen, dann nötigenfalls Notruf absetzen.' + q('DAV – Erste Hilfe für Bergsportler (PDF)', 'https://www.forststeig.sachsen.de/download/Erste_Hilfe_2012_DAV.pdf'),
       '<strong>Aus der Gefahrenzone bringen</strong> und vor Unterkühlung schützen – Rettungsdecke oder Biwaksack.' + q('DAV – Tipps und Infos: Wetter, Notruf, Erste Hilfe (PDF)', 'https://magazin.alpenverein.de/files/1801-tipps_und_infos_ol.pdf'),
       '<strong>Ins Erste-Hilfe-Set</strong> gehören mindestens Heft- und Blasenpflaster, Mullbinde, Desinfektion und Pinzette – dazu Rettungsdecke bzw. Biwaksack.' + q('DAV – Der richtig gepackte Wanderrucksack', DAV + 'das-ist-der-richtig-gepackte-wanderrucksack_633664a0-ba50-4eb1-8251-470355129173'),
       '<strong>In Sicht- oder Hörweite</strong> von Tal oder Hütte alarmiert das alpine Notsignal.' + q('DAV – So geht das: Notfall alpin', DAV + 'so-geht-das-notfall-alpin_62bc1334-e9c7-4d8b-8a02-89dd681cbb83')]))
b.append(H2('wetter', '⛈️ Wetter &amp; Lawinen')
 + P('Regen, Wind und Kälte erhöhen das Unfallrisiko – der Wetterbericht gehört zu jeder Tourenplanung' + q('AVS – Fit fürs Bergwandern (PDF)', 'https://alpenverein.it/wp-content/uploads/2025/12/avs-cf-bergwandern-1-auflage-anpassung-7.10.2025.pdf') + '. Live-Wetter, Webcams und den Lawinenlagebericht findest du gebündelt unter <a href="/wetter-webcams.html">Wetter &amp; Webcams</a>; für Wintertouren die <a href="/content/winter/lawinenkunde-grundlagen.html">Lawinen-Grundlagen</a>.')
 + AFF([('Erste-Hilfe-Sets Outdoor', 'Erste+Hilfe+Set+Outdoor'), ('Biwaksäcke', 'Biwaksack'), ('Notfallpfeifen', 'Notfallpfeife')]))
b.append(q.liste())
seite('content/sicherheit/index.html', 'Sicherheit beim Bergwandern – DAV-Empfehlungen, Notruf, Erste Hilfe',
      '🛟 Sicher am Berg', 'Die 10 Empfehlungen der Alpenvereine, was die DAV-Unfallstatistik zeigt, wie Notruf und alpines Notsignal funktionieren und was ins Erste-Hilfe-Set gehört – mit Quellen.',
      IMG('wanderer-bayern.jpg', 'Wanderer auf einer Felsstufe'), [('regeln', '✅ 10 Empfehlungen'), ('unfaelle', '📊 Unfälle'), ('notruf', '🆘 Notruf'), ('erstehilfe', '⛑️ Erste Hilfe'), ('wetter', '⛈️ Wetter'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Sicherheit beim Bergwandern mit Quellen: 10 Empfehlungen der Alpenvereine, DAV-Unfallstatistik, Notruf 112, alpines Notsignal, Erste Hilfe.', 'Sicherheit')
