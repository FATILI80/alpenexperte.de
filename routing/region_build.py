#!/usr/bin/env python3
"""Baut die Regionsseite content/regional/index.html neu (Gravel-Schema, belegt).
Ersetzt content/regional/* und /region/* (Weiterleitungen in vercel.json)."""
import re, html, sys
sys.path.insert(0, 'routing')
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t, sub='': f'<h2 id="{i}" style="color:#14532d;margin:38px 0 6px;scroll-margin-top:140px;">{t}</h2>' + (f'<p style="color:#374151;margin:0 0 12px;line-height:1.6;">{sub}</p>' if sub else '')
P = lambda t: f'<p style="color:#1f2933;line-height:1.65;">{t}</p>'
def BOX(t, farbe='#e8f5e9', rand='#2e7d32'): return f'<div style="background:{farbe};border-left:5px solid {rand};padding:12px 16px;border-radius:10px;margin:14px 0;color:#1f2933;line-height:1.6;">{t}</div>'
def UL(items): return '<ul style="line-height:1.7;color:#1f2933;">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
GRID = lambda cards: '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px;margin:10px 0 6px;">' + ''.join(cards) + '</div>'
TH = 'style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;vertical-align:top;"'
TD = 'style="padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;"'
def TAB(kopf, rows): return ('<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:.93rem;margin:8px 0 14px;"><tr>' + ''.join(f'<th {TH}>{k}</th>' for k in kopf) + '</tr>'
                             + ''.join('<tr>' + ''.join(f'<td {TD}>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table></div>')
from naturwelt_build import Q, CARD, seite, HERO

q = Q(); b = []
WV_SP = ('Wikivoyage – Spitzingsee', 'https://de.wikivoyage.org/wiki/Spitzingsee')
WP_SP = ('Wikipedia – Spitzingsee', 'https://en.wikipedia.org/wiki/Spitzingsee')
STAT = ('Statistisches Jahrbuch – Seen (Alpen), Ausgabe 1989 (PDF)', 'https://digi.bib.uni-mannheim.de/fileadmin/statjahrb/514402342_1989/pdf/514402342_0013.pdf')
WP_TEG = ('Wikipedia – Tegernsee (See)', 'https://wikipedia.com/wiki/Lake_Tegernsee')
HDBG = ('Haus der Bayerischen Geschichte – Kollegiatstift St. Sixtus Schliersee', 'https://hdbg.eu/kloster/index.php/detail/geschichte?id=KS0369')
WV_TEG = ('Wikivoyage – Tegernsee', 'https://de.wikivoyage.org/wiki/Tegernsee')
DENKMAL = ('BLfD – Denkmalliste Markt Schliersee (PDF)', 'https://www.geodaten.bayern.de/denkmal_static_data/externe_denkmalliste/pdf/denkmalliste_merge_182131.pdf')
BOCK = ('Wikipedia – Neuhauser Bockerlbahn', 'https://de.wikipedia.org/wiki/Neuhauser_Bockerlbahn')

b.append(H2('vergleich', '🌊 Drei Seen im Vergleich')
 + TAB(['', 'Spitzingsee', 'Schliersee', 'Tegernsee'], [
     ['Höhe', '1.084 m' + q(*WP_SP), '777 m' + q(*STAT), '725 m' + q(*STAT)],
     ['Fläche', 'rund 28 ha' + q(*WP_SP), '2,2 km²' + q(*STAT), '8,9 km²' + q(*STAT)],
     ['größte Tiefe', '16,3 m' + q(*WP_SP), '39 m' + q(*STAT), '72 m (72,6 m)' + q(*STAT) + q(*WP_TEG)],
     ['Abfluss', 'Rote Valepp → Inn' + q(*WV_SP), 'Schlierach → Mangfall' + q('Wikipedia – Schliersee (lake)', 'https://www.wikipedia.org/wiki/Lake_Schliersee'), 'Mangfall' + q('wassertemperatur.org – Tegernsee', 'https://wassertemperatur.org/?p=196')],
     ['Eigentümer', 'Freistaat Bayern (Schlösserverwaltung)' + q(*WV_SP), 'Freistaat Bayern' + q('Bayerische Schlösserverwaltung – Schliersee', 'https://www.schloss.bayern.de/englisch/lakes/objects/schliers.htm'), '–']])
 + BOX('<strong>Wasserscheide vor der Haustür:</strong> Der Spitzingsattel (1.129 m) trennt Mangfall und Inn.' + q(*WV_SP) + ' Schliersee und Tegernsee entwässern nach Norden zur Mangfall, der Spitzingsee über die Rote Valepp und die Brandenberger Ache nach Süden zum Inn.' + q(*WV_SP)))

b.append(H2('orte', '📍 Die Orte') + GRID([
 CARD('spitzingsee', 'Spitzingsee', 'Ortsteil von Schliersee · 1.084 m', 'Der Ort am See besteht im Wesentlichen aus der Kirche, den Hotels und Gaststätten; rund 200 Einwohner.' + q('Wikipedia – Spitzingsee (village)', 'https://en.wikipedia.org/wiki/Spitzingsee_(village)') + q(*WV_SP),
      [('See', '28 ha, max. 16,3 m tief, gespeist von Lochgraben und Firstgraben' + q(*WP_SP) + q(*WV_SP)),
       ('Kirche', 'St. Bernhard, 1937/38 von Friedrich Ferdinand Haindl, Baudenkmal' + q('komoot/Denkmalliste – St. Bernhard (Spitzingsee)', 'https://www.komoot.com/highlight/3633424')),
       ('Anfahrt', 'Spitzingstraße (St 2077) von Neuhaus über den Spitzingsattel' + q(*WV_SP)), ('Bei uns', '<a href="/huetten.html#obere-firstalm">Obere Firstalm</a> · <a href="/content/wandern/index.html">Touren ab der Firstalm</a>')],
      img='spitzingsee-perfekt.jpg', alt='Spitzingsee im Sommer'),
 CARD('schliersee', 'Schliersee', 'Markt · See auf 777 m', 'Der Ort geht auf ein Kloster auf dem Kirchbichl zurück, das am 21. Januar 779 als „Zelle am Slyrse“ erstmals urkundlich erwähnt wird.' + q(*HDBG),
      [('Kloster', '1495 wurde das Stift nach München an die Frauenkirche verlegt' + q(*HDBG) + q('Historisches Lexikon Bayerns – Frauenkirche München', 'https://www.historisches-lexikon-bayerns.de/Lexikon/Frauenkirche,_M%C3%BCnchen')),
       ('Insel Wörth', 'die einzige Insel im See, gut 2 ha, seit 1971 im Besitz des Freistaats; Wirtshaus, Anfahrt mit dem Schiff' + q('Bayerische Schlösserverwaltung – Schliersee', 'https://www.schloss.bayern.de/englisch/lakes/objects/schliers.htm') + q('Wikivoyage – Schliersee', 'https://de.wikivoyage.org/wiki/Schliersee')),
       ('Bauerntheater', '1892 von Konrad Dreher und Xaver Terofal gegründet' + q('ADAC – Schlierseer Bauerntheater', 'https://maps.adac.de/poi/schlierseer-bauerntheater-4')),
       ('Fischerei', 'Fischerei Schliersee (Seestraße 3a) von Marc Fricke und Lukas Müller, Fisch aus eigenem Quellwasser-Weiher im Leitzachtal' + q('smart-travelling – Fischerei Schliersee', 'https://www.smart-travelling.net/locations/fischerei-schliersee'))],
      img='schliersee-see.jpg', alt='Schliersee mit Insel Wörth'),
 CARD('tegernsee', 'Tegernsee', 'Tegernseer Tal · See auf 725 m', 'Das Benediktinerkloster wird traditionell auf 746 datiert, die frühen 760er Jahre gelten heute als wahrscheinlich; aufgehoben am 17. März 1803.' + q(*WV_TEG),
      [('Heute', 'das ehemalige Kloster ist Schloss Tegernsee im Besitz der Wittelsbacher; im Gebäude sitzen das Herzogliche Brauhaus und das Bräustüberl' + q('Wikipedia – Tegernsee Abbey', 'https://en.wikipedia.org/wiki/Tegernsee_Abbey') + q('Wikipedia – Tegernsee', 'https://en.wikipedia.org/wiki/Tegernsee')),
       ('Wallberg', '1.722 m; Wallbergbahn in rund 10 Minuten zur Bergstation auf 1.620 m' + q('muenchen.de – Wallberg', 'https://www.muenchen.de/freizeit/ausflugsziele/wallberg')),
       ('Winter', 'Naturrodelbahn am Wallberg, 6,5 km – eine der längsten Deutschlands' + q('ADAC – Naturrodelbahn am Wallberg', 'https://maps.adac.de/poi/naturrodelbahn-am-wallberg-rottach-egern')),
       ('Einkehr', '<a href="/restaurants.html#braeustueberl-tegernsee">Bräustüberl</a> und weitere im <a href="/restaurants.html">Restaurant-Guide</a>')],
      img='tegernsee-see.jpg', alt='Blick über den Tegernsee'),
 CARD('valepp', 'Valepp', 'Ortsteil von Schliersee · an der Grenze zu Tirol', 'Ein dünn besiedeltes Waldtal, geprägt von Holztrift, Almwirtschaft und Jagd.' + q('gamssteig.de – Geschichte der Valepp', 'https://www.gamssteig.de/lexikon/valepp-kaiserklause'),
      [('Forsthaus', '1841 vom königlichen Salinenamt Reichenhall gebaut; Ensemble mit Kapelle Maria Hilf und Klausenhaus steht unter Denkmalschutz' + q('Schliersee Magazin – Forsthaus Valepp', 'https://magazin.schliersee.de/ein-juwel-forsthaus-valepp-kurz-vor-der-wiedereroeffnung/') + q(*DENKMAL)),
       ('NS-Zeit', 'in den 1930er Jahren entstand ein Jagdhaus für Heinrich Himmler' + q(*DENKMAL)),
       ('Heute', 'seit August 2024 wieder geöffnet, Pächter sind Manuel Neuer und Johannes Rabl (Erbpacht auf 99 Jahre)' + q('Servus Schliersee – Forsthaus Valepp', 'https://servus-schliersee.de/essen-und-trinken/forsthaus-valepp/') + q('Schliersee Magazin – Forsthaus Valepp', 'https://magazin.schliersee.de/ein-juwel-forsthaus-valepp-kurz-vor-der-wiedereroeffnung/')),
       ('Hinkommen', 'zu Fuß ab Spitzingsee in etwa 1,5 h' + q('Schliersee Magazin – Forsthaus Valepp', 'https://magazin.schliersee.de/ein-juwel-forsthaus-valepp-kurz-vor-der-wiedereroeffnung/') + '; Mautstraße von Enterrottach' + q('Tegernsee.com – Forsthaus Valepp', 'https://www.tegernsee.com/a-forsthaus-valepp') + '; Bus 365 Spitzingsee – Valepp – Rottach-Egern' + q('MVV – Fahrplan 365 (PDF)', 'https://mvv-muenchen.de/fileadmin/mediapool/07-Ueber_den_MVV/02-Dokumente/Ausschreibungen/3XX_LK_Miesbach/365__2026_VORAB_Fahrplan.pdf'))],
      img='forsthaus-valepp.jpg', alt='Forsthaus Valepp mit Blumenbalkon')]))

b.append(H2('geschichte', '📜 Geschichte & Geschichten') + GRID([
 CARD('jennerwein', 'Georg Jennerwein', 'Wildschütz · 1848–1877', 'Geboren in Haid bei Holzkirchen, Holzknecht und Wilderer im Grenzgebiet zwischen Bayern und Tirol. Er wurde am 6. November 1877 erschossen, seine Leiche am 15. November am Peißenberg nördlich der Bodenschneid gefunden.' + q('muenchenwiki – Georg Jennerwein', 'https://www.muenchenwiki.de/wiki/Georg_Jennerwein'),
      [('Geburt', 'meist mit 1848 angegeben' + q('Literaturportal Bayern – Georg Jennerwein', 'https://www.literaturportal-bayern.de/themen?task=lpbtheme.default&id=610') + '; laut Taufregister Osterwarngau am 19. April 1849' + q('Wikipedia (via Wikiwand) – Georg Jennerwein', 'https://www.wikiwand.com/de/articles/Georg_Jennerwein')),
       ('Schütze', 'als Täter gilt der Jagdgehilfe Johann Josef Pföderl, ein Kriegskamerad von 1870/71' + q('Literaturportal Bayern – Georg Jennerwein', 'https://www.literaturportal-bayern.de/themen?task=lpbtheme.default&id=610')),
       ('Grab', 'Friedhof Westenhofen (Schliersee)' + q('muenchenwiki – Georg Jennerwein', 'https://www.muenchenwiki.de/wiki/Georg_Jennerwein'))], icon='🎯'),
 CARD('bockerlbahn', 'Neuhauser Bockerlbahn', 'Waldbahn · ab 1919/20', 'Föhnstürme 1919 warfen im Tal der Valepp und um den Spitzingsee Hunderttausende Festmeter Holz. Zum Abtransport baute man eine Schmalspurbahn vom Bahnhof Fischhausen-Neuhaus über den Spitzingsattel bis zur Waitzinger-Alm.' + q(*BOCK) + q('Infotafel 12 „Waldbahn, Bockerlbahn, BB-Trail“ (Markt Schliersee) am Bahnhof Spitzingsattel – eigenes Foto, Nov. 2026', '/images/bockerlbahn-tafel-spitzingsattel.jpg'),
      [('Wikipedia', 'Betrieb 1919–1922; Stürme am 5./6. Januar, 16. März und 8. Juli 1919, rund 290.000 Festmeter; 12 km, 600 mm Spurweite, drei Bremsberge' + q(*BOCK)),
       ('Infotafel vor Ort', 'nennt 1920–1927; am 5./6. Januar 1919 rund 200.000 Festmeter, im Frühjahr 1919 weitere 100.000; gebaut von der Firma Steinbeis (Brannenburg) im Auftrag der Bayerischen Landesforstverwaltung; über 12 km Gleis, über 300 m Höhenunterschied mit 3 Bremsbergen, dazu ein Aufzug über 60 m von der Waitzinger-Alm zum Bleckstein; 7 Dampf- und 2 Benzolloks zogen 170 Doppeltrucks' + q('Infotafel 12 „Waldbahn, Bockerlbahn, BB-Trail“ (Markt Schliersee) am Bahnhof Spitzingsattel – eigenes Foto, Nov. 2026', '/images/bockerlbahn-tafel-spitzingsattel.jpg')),
       ('Unklar', 'Die Betriebsjahre widersprechen sich (1919–1922 bzw. 1920–1927). Wir konnten das nicht klären und zeigen beide Angaben.'), ('Spuren', 'Viele heutige Wege rund um den Spitzingsee folgen der alten Trasse; der Bockerlbahnweg führt von der Valepp nach Neuhaus' + q('gamssteig.de – Bockerlbahnweg', 'https://www.gamssteig.de/touren/bockerlbahnweg-spitzingsee'))], img='bockerlbahn-tafel-header.jpg', alt='Wegweiser Spitzingsattel 1.127 m und Infotafel 12 der Bockerlbahn'),
 CARD('wasmeier', 'Markus Wasmeier & sein Museum', 'Skirennläufer aus Schliersee, * 1963', 'Weltmeister im Riesenslalom 1985, zweifacher Olympiasieger 1994 in Lillehammer: Super-G am 17. Februar, Riesenslalom am 23. Februar.' + q('Wikipedia – Markus Wasmeier', 'https://en.wikipedia.org/wiki/Markus_Wasmeier') + q('the-sports.org – Markus Wasmeier', 'https://www.the-sports.org/markus-wasmeier-alpine-skiing-spf82585.html'),
      [('Museum', 'Freilichtmuseum in Neuhaus, eröffnet am 1. Mai 2007, mehr als 22 historische Gebäude auf 60.000 m²' + q('Wikipedia – Markus Wasmeier Freilichtmuseum', 'https://de.wikipedia.org/wiki/Markus_Wasmeier_Freilichtmuseum_Schliersee')),
       ('Saison', 'Saison 2026 endete am 8. November; für 2027 nennt das Museum 26. März – 7. November. Di–So 10–17 Uhr; Erwachsene laut Museumsseite 11,90 €, Kinder bis einschließlich 15 Jahre frei' + q('wasmeier.de – Öffnungszeiten & Preise', 'https://www.wasmeier.de/informationen/oeffnungszeiten/')),
       ('Anreise', 'gegenüber dem Bahnhof Fischhausen-Neuhaus' + q('Servus Schliersee – Wasmeier Freilichtmuseum', 'https://servus-schliersee.de/sehenswuerdigkeiten/markus-wasmeier-freilichtmuseum/'))], icon='⛷️'),
 CARD('trautwein', 'Theodor Trautwein', 'Mitbegründer des Alpenvereins · 1833–1894', 'Der Münchner Buchhändler gründete am 9. Mai 1869 zusammen mit Franz Senn, Johann Stüdl und Karl Hofmann den Deutschen Alpenverein und seine Sektion München.' + q('Historisches Lexikon Bayerns – Deutscher Alpenverein', 'https://www.historisches-lexikon-bayerns.de/Lexikon/Deutscher_Alpenverein_e._V._(DAV)') + q('Wikipedia – Theodor Trautwein', 'https://de.wikipedia.org/wiki/Theodor_Trautwein'),
      [('Werk', 'Wanderführer für Südbayern und die Alpen, viele Jahre Redakteur der Mitgliederzeitung' + q('muenchenwiki – Theodor Trautwein', 'https://www.muenchenwiki.de/wiki/Theodor_Trautwein')),
       ('Tod', '1894 in München, nach einer Wanderung an einer Lungenentzündung' + q('muenchenwiki – Theodor Trautwein', 'https://www.muenchenwiki.de/wiki/Theodor_Trautwein')),
       ('Gedenktafel', 'Am Spitzingsee erinnert eine Bronzetafel in einer Felswand an ihn: Name, Lebensdaten 1833–1894, gestiftet von der Sektion München des D. u. Ö. Alpenvereins und einem Münchner Alpen-Kränzchen (Inschrift teils von Zweigen verdeckt). Foto: alpenexperte.de, Juni 2026')], img='trautwein-gedenktafel.jpg', alt='Bronzene Gedenktafel für Theodor Trautwein, 1833–1894, in einer Felswand am Spitzingsee'),
 CARD('wilparting', 'Wilparting – nicht am Tegernsee', 'Wallfahrtskirche St. Marinus und Anian · Irschenberg', 'Die markante Kirche an der A8 gehört zu Irschenberg. Sie steht über dem Grab der beiden Heiligen; die Überlieferung lässt die Missionare Marinus und Anian im 7. Jahrhundert hierherkommen.' + q('Wikipedia (via Wikiwand) – Wallfahrtskirche Wilparting', 'https://wikiwand.com/de/articles/Wallfahrtskirche_Wilparting') + q('ausflugsziele.jetzt – Wilparting', 'https://www.ausflugsziele.jetzt/?p=254674'),
      [('Korrektur', 'Auf früheren Seiten stand „oberhalb von Tegernsee“ und „Kapelle von 657“ – beides falsch.')], icon='⛪')]))

b.append(H2('anreise', '🚆 Anreise ohne Auto')
 + UL(['<strong>MVV-Tarif:</strong> Seit dem 10. Dezember 2023 gehört der Landkreis Miesbach zum MVV – ein Fahrschein für Bahn und Bus.' + q('Landratsamt Bad Tölz-Wolfratshausen – MVV-Erweiterung', 'https://lra-toelz.de/mvv-gebiet-waechst-bad-toelz-wolfratshausen-profitiert-von-umfassender-verbundraumerweiterung'),
       '<strong>Zug:</strong> RB 55 München Hbf – Miesbach – Schliersee – Fischhausen-Neuhaus – Bayrischzell.' + q('Alpenverein München & Oberland – Netz Oberland (PDF)', 'https://www.alpenverein-muenchen-oberland.de/uploads/images/mHHnkg3WjZkU16C84XpGng/netz-oberland-2026-05-03.pdf'),
       '<strong>Bus zum Spitzingsee:</strong> Linie 362 Schliersee – Neuhaus – Spitzingsee, mit Halten u. a. am Spitzingsattel, an der Taubensteinbahn und an der Kirche.' + q('DAV – Buslinie 362 zum Spitzingsee', 'https://www.alpenverein.de/artikel/linie-9562-zum-spitzingsee_3d7a35c7-cb46-4106-9e2f-6d5ac5aedd6b'),
       '<strong>Valepp & Tegernsee:</strong> Linie 365 Spitzingsee – Valepp – Moni-Alm – Rottach-Egern.' + q('MVV – Fahrplan 365 (PDF)', 'https://mvv-muenchen.de/fileadmin/mediapool/07-Ueber_den_MVV/02-Dokumente/Ausschreibungen/3XX_LK_Miesbach/365__2026_VORAB_Fahrplan.pdf')])
 + P('Parken, Straßen und Bergbahnen im Detail: <a href="/anreise.html">Anreise &amp; Parken</a>. Fahrpläne vor der Fahrt in der MVV-Auskunft prüfen.'))
b.append(q.liste())
seite('content/regional/index.html', 'Region Spitzingsee, Schliersee & Tegernsee – Seen, Orte, Geschichte',
      '🗺️ Region Spitzingsee · Schliersee · Tegernsee', 'Drei Seen, die Valepp und ihre Geschichte – vom Kloster am „Slyrse“ über den Wildschütz Jennerwein bis zur Bockerlbahn. Alles mit Quellen, geschrieben von der Oberen Firstalm aus.',
      HERO('Schliersee.jpg', 'Schliersee mit Ausflugsschiff'), [('vergleich', '🌊 Seen-Vergleich'), ('orte', '📍 Orte'), ('geschichte', '📜 Geschichte'), ('anreise', '🚆 Anreise'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Region Spitzingsee, Schliersee und Tegernsee mit Quellen: Seen-Vergleich, Valepp, Klostergeschichte, Jennerwein, Bockerlbahn, Wasmeier-Museum, Trautwein und Anreise mit MVV.', 'Region',
      'Weiter: <a href="/huetten.html">Hüttenführer</a> · <a href="/restaurants.html">Restaurants</a> · <a href="/content/fauna/">Tierwelt</a> · <a href="/wetter-webcams.html">Wetter &amp; Webcams</a>')
