#!/usr/bin/env python3
"""Baut die Winter-Tourenseiten (Skitouren + Schneeschuh) neu auf.

Kopf (Meta, CSS, Navigation) und Footer der bestehenden Seiten bleiben erhalten.
Der Inhalt von <main> wird durch verifizierte Tourendaten mit Quellen ersetzt.
Alle Zahlen stammen aus den unten je Tour verlinkten Quellen; Höhenmeter ab der
Oberen Firstalm (1.375 m) sind Gipfelhöhe minus 1.375 m (reine Differenz).
"""
import re, html

FIRSTALM = 1375

LAWINE = ('<div style="background:#fef2f2;border-left:5px solid #b91c1c;padding:14px 16px;border-radius:10px;margin:0 0 24px;color:#1f2933;">'
          '<strong style="color:#991b1b;">Lawinen: vor jeder Tour den aktuellen Lagebericht lesen.</strong> '
          'Kein Hang ist „lawinensicher“ – die Gefahr hängt von Neuschnee, Wind, Temperatur und Exposition des Tages ab. '
          'LVS-Gerät, Sonde und Schaufel gehören bei jeder Skitour und jeder Schneeschuhtour abseits geräumter Wege in den Rucksack. '
          '<a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">Lawinenwarndienst Bayern</a> · '
          'Notruf <strong>112</strong> (Bergwacht).</div>')

SKITOUR_AFF = ('Tourenski & Felle', 'https://www.amazon.de/s?k=Tourenski+Felle&linkCode=ll2&tag=bb8ozi-21')
SCHNEESCHUH_AFF = ('Schneeschuhe', 'https://www.amazon.de/s?k=Schneeschuhe+Wandern&linkCode=ll2&tag=bb8ozi-21')

TOUREN = {
 'content/winter/skitouren/taubenstein.html': dict(
  title='Taubenstein (1.692 m) – Skitour vom Spitzingsee',
  desc='Taubenstein-Skitour vom Spitzingsee: ca. 600 Hm über die ehemalige Taubenstein-Piste zum Taubensteinsattel, Taubensteinhaus 1.567 m. Daten mit Quellen.',
  crumb=('Skitouren','/content/winter/skitouren/index.html'), name='Taubenstein', icon='🏔️',
  lead='Seit die Taubensteinbahn im Winter nicht mehr fährt (Skibetrieb am Taubenstein 2015 eingestellt), gehört die alte Piste den Tourengehern. Leichte, beliebte Tour – der Gipfel selbst ist ein kleiner Felskopf, im Winter bleibt man meist am Sattel.',
  fakten=[('Gipfel','Taubenstein 1.692 m'),('Start','Spitzingsee, Parkplatz Taubensteinbahn (ca. 1.100 m)'),
          ('Höhenmeter','ca. 600 Hm bis zum Gipfel, ca. 490 Hm bis zum Taubensteinsattel (1.592 m)'),
          ('Aufstieg','ca. 2 h'),('Schwierigkeit','leicht (Gipfelaufbau zu Fuß, drahtseilgesicherte Felsrinne)'),
          ('Einkehr','Taubensteinhaus 1.567 m (DAV), im Winter etwa ab Ende Dezember geöffnet'),
          ('Ab Oberer Firstalm','Gipfel liegt 317 m über der Alm; Zustieg über Spitzingsattel/Spitzingsee')],
  route=['Vom Parkplatz an der Talstation der Taubensteinbahn auf der ehemaligen Piste aufsteigen – der DAV weist die Strecke als Pisten- bzw. Nachtroute aus.',
         'Durch den Lochgraben hinauf zum Taubensteinsattel (1.592 m). Fünf Minuten entfernt liegt das Taubensteinhaus.',
         'Der Gipfelaufbau ist eine kurze, drahtseilgesicherte Felsrinne. Im Winter meist Skidepot am Sattel und nur bei sicheren, griffigen Verhältnissen zu Fuß hinauf – sonst ist der Sattel das Ziel.',
         'Abfahrt wie Aufstieg über die alte Piste.'],
  hinweis='Die Taubensteinbahn fährt nur im Sommer. Wer die Strecke kombinieren will: Vom Taubensteinsattel lässt sich die Rotwand-Reibn anschließen.',
  aff=SKITOUR_AFF,
  quellen=[('skiresort.info – Taubensteinbahn: „lift closed and not replaced“, Schließung 2015','https://skiresort.info/ski-resort/spitzingsee-tegernsee/ski-lifts/l1847'),
           ('hoehenrausch.de – Taubenstein (1.692 m) ab Talstation Taubensteinbahn (1.100 m)','https://www.hoehenrausch.de/berge/taubenstein/talstation-taubensteinbahn/'),
           ('hoehenrausch.de – Rotwand-Reibn (Taubensteinsattel 1.592 m, Taubensteinhaus 1.567 m)','https://www.hoehenrausch.de/berge/rotwand/reibn-skitour/'),
           ('DAV München & Oberland – Pistentouren Taubenstein (PDF)','https://www.alpenverein-muenchen-oberland.de/uploads/images/quXDtdW8KTYAmijoMd1CJQ/pistentouren_taubenstein.pdf'),
           ('tourentipp.com – Gipfelanstieg durch drahtseilgesicherte Felsrinne','https://www.tourentipp.com/portal/touren/1837/pdf/get')]),
 'content/winter/skitouren/rotwand.html': dict(
  title='Rotwand (1.884 m) – Skitour & Rotwand-Reibn',
  desc='Rotwand-Skitour vom Spitzingsee: ca. 800 Hm zum Gipfel, als Rotwand-Reibn 1.200–1.300 Hm in 5–6 h. Rotwandhaus 1.737 m. Daten mit Quellen.',
  crumb=('Skitouren','/content/winter/skitouren/index.html'), name='Rotwand', icon='⛰️',
  lead='Der höchste Gipfel im Landkreis Miesbach. Direkt über die Forststraße zum Rotwandhaus und auf den Gipfel – oder als Rotwand-Reibn, der große Skitourenklassiker am Spitzingsee mit mehrmaligem Auf- und Abfellen.',
  fakten=[('Gipfel','Rotwand 1.884 m'),('Start','Spitzingsee (ca. 1.085–1.095 m), Bushaltestelle Spitzingsee Kirche'),
          ('Höhenmeter','direkt ca. 800 Hm · Reibn ca. 1.200–1.300 Hm'),
          ('Zeit','direkt: gut 2 h zum Rotwandhaus, ca. 2,5 h zum Gipfel · Reibn: 5–6 h gesamt'),
          ('Strecke Reibn','ca. 14–15,5 km'),('Schwierigkeit','mittel; Nebelrinne anspruchsvoll, bei Vereisung den Gipfel auslassen'),
          ('Einkehr','Rotwandhaus 1.737 m, Taubensteinhaus 1.567 m'),
          ('Ab Oberer Firstalm','Gipfel liegt 509 m über der Alm; Zustieg über Spitzingsee')],
  route=['Von der Kirche in Spitzingsee Richtung Valepp, kurz darauf links der Forststraße Richtung Rotwand folgen. Beim Bergwachthaus rechts über die Brücke, weiter auf der Forststraße zum Rotwandhaus (1.737 m).',
         'Vom Rotwandhaus die letzten rund 150 Hm zum Gipfel, oft mit Skidepot und einem kurzen Stück zu Fuß.',
         'Reibn-Runde: Rotwand – Auerspitz (1.811 m) – Abfahrt zur Großtiefentalalm – Miesingsattel (1.704 m) – Taubensteinhaus – Taubensteinsattel – Abfahrt zum Spitzingsee.',
         'Direkte Variante: Abfahrt wie Aufstieg.'],
  hinweis='Die Forststraße zum Rotwandhaus wird vom Versorgungsfahrzeug befahren und ist normalerweise gut gespurt; im Winter nutzen sie auch Rodler.',
  aff=SKITOUR_AFF,
  quellen=[('DAV – Klassiker Rotwand-Reibn (Start Spitzingsee Kirche, Bus 362)','https://www.alpenverein.de/artikel/klassiker-rotwand-reibn_bc7eb889-8a3c-4d7c-b38c-c0e48ee299d8'),
           ('hoehenrausch.de – Rotwand-Reibn: 1.250 Hm, 15,5 km, mittelschwierig','https://www.hoehenrausch.de/berge/rotwand/reibn-skitour/'),
           ('tourentipp.com – Rotwand-Reibe: ca. 1.300 Hm, 14 km, 5–6 h','https://www.tourentipp.com/portal/touren/101/pdf/get'),
           ('bergtour-online.de – Rotwand-Reibn: 1.200 Hm, mittel','https://www.bergtour-online.de/skitouren/mittlereskitouren/rotwand-reibn/'),
           ('hoehenrausch.de – Rotwand als Winterwanderung (800 Hm)','https://www.hoehenrausch.de/berge/rotwand/winterwanderung/')]),
 'content/winter/skitouren/brecherspitz.html': dict(
  title='Brecherspitz-Westgipfel – Skitour über die Firstalmen',
  desc='Skitour auf den Brecherspitz-Westgipfel (ca. 1.630 m) vom Kurvenlift über Untere und Obere Firstalm: ca. 500 Hm, leicht. Hauptgipfel 1.683 m nur über Grat. Mit Quellen.',
  crumb=('Skitouren','/content/winter/skitouren/index.html'), name='Brecherspitz', icon='🗻',
  lead='Die kurze Hausrunde direkt an der Oberen Firstalm. Ziel ist im Winter der Westgipfel mit der Windmessstation des Lawinenwarndienstes; der ausgesetzte Grat zum Hauptgipfel wird selten begangen.',
  fakten=[('Ziel','Brecherspitz-Westgipfel ca. 1.630 m (Angaben 1.620–1.643 m); Hauptgipfel 1.683 m'),
          ('Start','Parkplatz Kurvenlift (ca. 1.120 m) oder Spitzingsattel (1.127 m)'),
          ('Höhenmeter','ca. 500 Hm'),('Aufstieg','ca. 1:15–1:45 h'),('Schwierigkeit','leicht (Westgipfel); Grat zum Hauptgipfel ausgesetzt'),
          ('Einkehr','Untere Firstalm 1.318 m, Obere Firstalm 1.375 m'),
          ('Ab Oberer Firstalm','ca. 255 Hm bis zum Westgipfel – die kürzeste Skitour ab der Alm')],
  route=['Vom Parkplatz Kurvenlift am rechten Pistenrand hinauf, dann über einen Ziehweg parallel zum Firstgraben zur Unteren Firstalm (1.318 m).',
         'Weiter nach Norden zur Oberen Firstalm (1.375 m). Vom Spitzingsattel führt alternativ der für Autos gesperrte Fahrweg (Trautweinweg) herauf – das ist auch die Rodelbahn, also auf Schlittenfahrer achten.',
         'Von der Oberen Firstalm über den breiten Südwesthang zum Westgipfel mit der Windmessstation.',
         'Abfahrt über den Südwesthang, zurück zu den Firstalmen und zum Ausgangspunkt.'],
  hinweis='Der Westgipfel eignet sich auch gut für Schneeschuhe. Der Grat zum Hauptgipfel ist im Winter oft vereist und nichts für Einsteiger.',
  aff=SKITOUR_AFF,
  quellen=[('hoehenrausch.de – Brecherspitz-Westgipfel (1.630 m) als Skitour: 500 Hm, leicht','https://www.hoehenrausch.de/berge/brecherspitz/skitour/'),
           ('tourentipp.com – Brecherspitz Skitour: 500 Hm, Windmessstation am Westgipfel','https://www.tourentipp.com/portal/touren/1569/pdf/get'),
           ('planetoutdoor.de – Brecherspitz Wintergipfel (1.643 m): 520 Hm, leicht','https://planetoutdoor.de/touren/skitouren/alpenregion-spitzingsee-brecherspitz-wintergipfel-1643-m'),
           ('hoehenrausch.de – Brecherspitz (1.683 m), Untere Firstalm 1.318 m, Obere Firstalm 1.375 m','https://www.hoehenrausch.de/berge/brecherspitz/')]),
 'content/winter/skitouren/bodenschneid.html': dict(
  title='Bodenschneid (1.669 m) – Skitour',
  desc='Bodenschneid-Skitour: von Neuhaus übers Bodenschneidhaus ca. 810 Hm, oder steil vom Spitzingsee über Firstalm und Bital ca. 560 Hm. Daten mit Quellen.',
  crumb=('Skitouren','/content/winter/skitouren/index.html'), name='Bodenschneid', icon='🌄',
  lead='Ruhiger als die Berge rund um den Spitzingsee. Zwei verifizierte Anstiege: der klassische von Neuhaus durchs Dürnbachtal über das Bodenschneidhaus – und eine kurze, steile Variante von der Unteren Firstalm aus.',
  fakten=[('Gipfel','Bodenschneid 1.669 m'),
          ('Variante A','Neuhaus, Parkplatz Dürnbachstraße (850 m) – Bodenschneidhaus (1.365 m) – Gipfel: ca. 810 Hm, Aufstieg ca. 2,5 h, mittel'),
          ('Variante B','Spitzingsee – Untere Firstalm (1.318 m) – Bital – Gipfel: ca. 560 Hm, Aufstieg ca. 1:20 h, steil (4 von 6)'),
          ('Einkehr','Bodenschneidhaus 1.365 m (DAV, ganzjährig geöffnet) · Untere Firstalm'),
          ('Bahn','Variante A: ca. 10 Minuten zu Fuß vom Bahnhof Fischhausen-Neuhaus'),
          ('Ab Oberer Firstalm','Gipfel liegt 294 m über der Alm; Variante B beginnt an der Unteren Firstalm')],
  route=['Variante A: Vom Wanderparkplatz im Dürnbachtal auf Forststraßen durch den Wald zum Bodenschneidhaus auf der Rettenböckalm.',
         'Vom Bodenschneidhaus durch freies Gelände zum Gipfel (ca. 300 Hm).',
         'Variante B: Hinter der Unteren Firstalm den Weg nach Norden verlassen und über das Bital steil zum Gipfel – nur bei sicheren Verhältnissen.',
         'Abfahrt jeweils wie Aufstieg; im Frühjahr müssen die Ski bei Variante A unten oft getragen werden.'],
  hinweis='Die Bodenschneid wird nicht mit einer Bahn erschlossen – Start ist immer im Tal bzw. am Spitzingsee.',
  aff=SKITOUR_AFF,
  quellen=[('tourentipp.com – Bodenschneid Skitour: 810 Hm, Aufstieg 2:30 h','https://www.tourentipp.com/portal/touren/764/pdf/get'),
           ('tourentipp.com – Bodenschneid über Firstalm und Bital: 560 Hm, 1:20 h','https://www.tourentipp.com/portal/touren/1436/pdf/get'),
           ('hoehenrausch.de – Bodenschneid von Neuhaus (850 m) übers Bodenschneidhaus (1.365 m)','https://www.hoehenrausch.de/berge/bodenschneid/'),
           ('bergwelten.com – Bodenschneid Skitour, Anreise mit der Bahn','https://www.bergwelten.com/t/s/7793')]),
 'content/winter/schneeschuh/spitzingsee-runde.html': dict(
  title='Spitzingsee-Runde im Winter – leichte Seeumrundung',
  desc='Winterrunde um den Spitzingsee: knapp 3 km, rund 20–30 Hm, ca. 1 h. Familienfreundlich, mit Einkehr an der Wurzhütte. Daten mit Quellen.',
  crumb=('Schneeschuh','/content/winter/schneeschuh/index.html'), name='Spitzingsee-Runde', icon='❄️',
  lead='Der See hat einen Umfang von rund 3,3 km. Die Runde auf dem Uferweg ist flach, auch im Winter leicht und gut mit Kindern machbar – Schneeschuhe braucht es nur nach viel Neuschnee, sonst reichen Winterschuhe und Grödel.',
  fakten=[('Länge','ca. 2,8–3 km'),('Höhenmeter','ca. 20–30 Hm'),('Zeit','ca. 1 h'),
          ('Start','Ort Spitzingsee, z. B. Parkplatz Taubensteinbahn am Ostufer'),
          ('Schwierigkeit','leicht'),('Einkehr','u. a. Alte Wurzhütte, Albert-Link-Hütte (kurzer Abstecher)'),
          ('Ab Oberer Firstalm','Abstieg zum See ca. 290 Hm; die Runde selbst ist flach')],
  route=['Im Ort Spitzingsee starten und dem Uferweg rund um den See folgen.',
         'Am Südende Richtung Valepp liegt die Alte Wurzhütte; wer verlängern will, geht zur Albert-Link-Hütte weiter (Runde dann ca. 4 km, ca. 60 Hm).',
         'Auf der anderen Seeseite zurück zum Ausgangspunkt.'],
  hinweis='Den zugefrorenen See nur betreten, wenn die Eisfläche offiziell freigegeben ist.',
  aff=SCHNEESCHUH_AFF, lawine=False,
  quellen=[('hoehenrausch.de – Wanderung rund um den Spitzingsee: 2,8 km, 28 Hm','https://www.hoehenrausch.de/wandern/kinder/spitzingsee/wanderbuch.php'),
           ('phototravellers.de – Spitzingsee Winterwanderung: 3 km, 20 Hm, 1 h','https://phototravellers.de/wanderung-spitzingsee/'),
           ('ich-geh-wandern.de – Umfang des Spitzingsees 3,33 km','https://www.ich-geh-wandern.de/runde-um-den-spitzingsee-und-zur-albert-link-h%C3%BCtte'),
           ('bergwelten.com – Runde um den Spitzingsee und zur Albert-Link-Hütte: 4 km, 60 Hm','https://www.bergwelten.com/t/w/6241')]),
 'content/winter/schneeschuh/firstalm.html': dict(
  title='Obere Firstalm im Winter – Schneeschuh- und Winterwanderung',
  desc='Winterwanderung zur Oberen Firstalm (1.375 m): ca. 250 Hm, 45 Minuten vom Spitzingsattel. Verlängerung zum Brecherspitz-Westgipfel. Daten mit Quellen.',
  crumb=('Schneeschuh','/content/winter/schneeschuh/index.html'), name='Obere Firstalm', icon='🏡',
  lead='Die Obere Firstalm ist das Ziel der bekanntesten Rodelbahn am Spitzingsee – und unser Zuhause. Hinauf geht es in einer Dreiviertelstunde; mit Schneeschuhen lässt sich die Tour bis zum Brecherspitz-Westgipfel verlängern.',
  fakten=[('Ziel','Obere Firstalm 1.375 m'),('Start','Spitzingsattel (1.127 m, Bus 362) oder Parkplatz Kurvenlift'),
          ('Höhenmeter','ca. 250 Hm'),('Zeit','ca. 45 min Aufstieg'),('Schwierigkeit','leicht'),
          ('Verlängerung','Brecherspitz-Westgipfel ca. 1.630 m: weitere ca. 255 Hm, auch mit Schneeschuhen'),
          ('Einkehr','Obere Firstalm, Untere Firstalm 1.318 m')],
  route=['Vom Spitzingsattel auf dem für Autos gesperrten Fahrweg (Trautweinweg) zur Oberen Firstalm. Das ist zugleich die Rodelbahn – am Rand gehen und auf Schlittenfahrer achten.',
         'Alternative vom Parkplatz Kurvenlift: über die Untere Firstalm (1.318 m) weiter zur Oberen Firstalm.',
         'Mit Schneeschuhen: von der Oberen Firstalm über den Südwesthang zum Brecherspitz-Westgipfel; zurück wie Aufstieg.'],
  hinweis='Öffnungszeiten der Hütte und den Zustand der Rodelbahn vor dem Aufbruch prüfen – bei guten Rodelverhältnissen ist abends länger geöffnet.',
  aff=SCHNEESCHUH_AFF,
  quellen=[('hoehenrausch.de – Obere Firstalm (1.375 m): 45 min, 250 Hm vom Spitzingsattel','https://www.hoehenrausch.de/huetten/obere-firstalm/huettenbuch.php'),
           ('hoehenrausch.de – Winterwandern und Rodeln an der Oberen Firstalm: 249 Hm','https://www.hoehenrausch.de/wandern/kinder/obere-firstalm'),
           ('hoehenrausch.de – Brecherspitz-Westgipfel, auch für Schneeschuhe geeignet','https://www.hoehenrausch.de/berge/brecherspitz/skitour/'),
           ('bergwelten.com – Trautweinweg vom Spitzingsattel zur Oberen Firstalm','https://www.bergwelten.com/t/w/10293')]),
 'content/winter/schneeschuh/rotwand.html': dict(
  title='Rotwand im Winter – Schneeschuh- und Winterwanderung',
  desc='Winterwanderung vom Spitzingsee zum Rotwandhaus (1.737 m) und auf die Rotwand (1.884 m): ca. 800 Hm, 2:45 h Aufstieg, 15 km. Daten mit Quellen.',
  crumb=('Schneeschuh','/content/winter/schneeschuh/index.html'), name='Rotwand', icon='⛄',
  lead='Bis zum Rotwandhaus führt eine breite, meist gut gespurte Forststraße – das schafft man mit Grödeln oder Schneeschuhen. Die letzten rund 150 Hm zum Gipfel folgen dem Sommerweg und sind deutlich anspruchsvoller.',
  fakten=[('Gipfel','Rotwand 1.884 m'),('Start','Spitzingsee (ca. 1.095 m), Alte Wurzhütte'),
          ('Höhenmeter','ca. 660 Hm zum Rotwandhaus · ca. 800 Hm zum Gipfel'),
          ('Zeit','ca. 2:30 h zum Rotwandhaus · ca. 2:45 h zum Gipfel, Abstieg ca. 2:15 h'),
          ('Strecke','ca. 13,6 km (Rotwandhaus) bzw. 15 km (Gipfel) hin und zurück'),
          ('Schwierigkeit','bis Rotwandhaus leicht bis mittel, Gipfelanstieg mittel'),
          ('Einkehr','Rotwandhaus 1.737 m'),('Ab Oberer Firstalm','Gipfel liegt 509 m über der Alm; Zustieg über Spitzingsee')],
  route=['Vom Ort Spitzingsee zur Alten Wurzhütte und an der Schranke geradeaus Richtung Valepp; kurz danach links (Wegweiser Rotwand). Bis zur Bergwachthütte ist der Fahrweg asphaltiert und geräumt.',
         'Weiter auf der Forststraße zum Rotwandhaus. Bei passender Schneelage kürzt ein Pfad die Serpentinen ab.',
         'Vom Rotwandhaus auf dem Sommerweg zum Gipfel (ca. 150 Hm) – bei Vereisung oder schlechter Sicht am Haus umkehren.',
         'Zurück wie Aufstieg; mit eigenem Schlitten lässt sich bei guter Schneelage bis zur Bergwachthütte abfahren. Die Forststraße ist keine präparierte Rodelbahn.'],
  hinweis='Die Forststraße wird vom Versorgungsfahrzeug des Rotwandhauses befahren – Augen und Ohren offen halten.',
  aff=SCHNEESCHUH_AFF,
  quellen=[('hoehenrausch.de – Rotwand als Winterwanderung: 800 Hm, 15 km, 2:45 h','https://www.hoehenrausch.de/berge/rotwand/winterwanderung/'),
           ('hoehenrausch.de – Rotwandhaus, Winterwandern und Rodeln: 660 Hm, 13,6 km','https://www.hoehenrausch.de/wandern/rodeln/rotwandhaus-spitzingsee'),
           ('bergwelten.com – Rotwandhaus (1.737 m)','https://www.bergwelten.com/h/rotwandhaus')]),
}

def esc(t): return html.escape(t, quote=False)

def build_main(d):
    out=['<main id="main">','<article class="container" style="max-width:860px;margin:0 auto;padding:24px 16px 48px;">',
         '<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <a href="/content/winter/index.html">Winter-Guide</a> › '
         f'<a href="{d["crumb"][1]}">{esc(d["crumb"][0])}</a> › <span aria-current="page">{esc(d["name"])}</span></nav>',
         f'<header style="margin-bottom:20px;"><h1 style="color:#14532d;margin:0 0 10px;">{d["icon"]} {esc(d["title"])}</h1>',
         f'<p style="font-size:1.08rem;color:#1f2933;margin:0;">{esc(d["lead"])}</p></header>']
    if d.get('lawine',True): out.append(LAWINE)
    out.append('<section style="margin-bottom:28px;"><h2 style="color:#14532d;">📋 Tourdaten</h2><table style="width:100%;border-collapse:collapse;font-size:.97rem;">')
    for k,v in d['fakten']:
        out.append(f'<tr><th style="text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid #e5e7eb;width:34%;color:#14532d;">{esc(k)}</th>'
                   f'<td style="padding:8px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;">{esc(v)}</td></tr>')
    out.append('</table><p style="font-size:.85rem;color:#4b5563;margin-top:6px;">Zahlen aus den unten genannten Quellen; Höhenangaben je nach Quelle ±10 m. „Ab Oberer Firstalm“ = Gipfelhöhe minus 1.375 m.</p></section>')
    out.append('<section style="margin-bottom:28px;"><h2 style="color:#14532d;">🗺️ Route</h2><ol style="color:#1f2933;line-height:1.6;">')
    out+= [f'<li style="margin-bottom:8px;">{esc(r)}</li>' for r in d['route']]
    out.append(f'</ol><p style="background:#f0fdf4;border-left:4px solid #2d8a56;padding:10px 14px;border-radius:8px;color:#1f2933;">{esc(d["hinweis"])}</p></section>')
    n,u=d['aff']
    out.append(f'<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;margin-bottom:28px;font-size:.95rem;color:#1f2933;">'
               f'<span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>Ausrüstung: <a href="{u}" target="_blank" rel="sponsored noopener">{esc(n)} bei Amazon ansehen</a>. '
               'Mehr in der <a href="/content/winter/ausruestung-winter.html">Winter-Ausrüstungsliste</a>.</aside>')
    out.append('<section style="margin-bottom:28px;"><h2 style="color:#14532d;">🔗 Weitere Wintertouren</h2><ul style="line-height:1.8;">'
               '<li><a href="/content/winter/skitouren/index.html">Alle Skitouren am Spitzingsee</a></li>'
               '<li><a href="/content/winter/schneeschuh/index.html">Schneeschuh-Touren</a></li>'
               '<li><a href="/content/winter/index.html">Winter-Guide</a> · <a href="/anreise.html">Anreise &amp; Parken</a></li></ul></section>')
    out.append('<section class="quellen-section"><h2 style="color:#14532d;">📚 Quellen</h2><ul style="line-height:1.7;font-size:.93rem;">')
    out+= [f'<li><a href="{u}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t,u in d['quellen']]
    out.append('<li><a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">Lawinenwarndienst Bayern</a></li></ul>'
               '<p style="font-size:.82rem;color:#4b5563;">Stand: November 2026. Alle Angaben ohne Gewähr – Verhältnisse vor Ort prüfen.</p></section>')
    out.extend(['</article>','</main>'])
    return '\n'.join(out)

for f,d in TOUREN.items():
    s=open(f,encoding='utf-8').read()
    a=s.find('<main id="main">'); b=s.find('</main>')+len('</main>')
    head, tail = s[:a], s[b:]
    # Kopf: Titel/Beschreibung aktualisieren
    head=re.sub(r'<title>.*?</title>', f'<title>{esc(d["title"])} | alpenexperte.de</title>', head, count=1, flags=re.S)
    head=re.sub(r'(<meta name="description"\s+content=")[^"]*(")', lambda m: m.group(1)+html.escape(d['desc'])+m.group(2), head, count=1)
    head=re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1)+html.escape(d['title'])+m.group(2), head)
    head=re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1)+html.escape(d['desc'])+m.group(2), head)
    head=re.sub(r'"headline": "[^"]*"', '"headline": '+repr(d['title']).replace("'",'"'), head)
    head=re.sub(r'"description": "[^"]*"', '"description": '+repr(d['desc']).replace("'",'"'), head)
    head=re.sub(r'"dateModified": "[^"]*"', '"dateModified": "2026-11-27"', head)
    # Nach </main>: BRB-Box, alte Quellen, Partner-Kommentare, Urwahn-Affiliate raus
    tail=re.sub(r'<!-- ===== BRB ECHTZEIT-FAHRPLAN.*?</div>\s*', '', tail, flags=re.S)
    tail=re.sub(r'<!-- ===== QUELLEN & EXPERTISE \(E-E-A-T\) ===== -->\s*', '', tail)
    tail=re.sub(r'<section class="quellen-section".*?</section>\s*', '', tail, flags=re.S)
    tail=re.sub(r'(<!-- ===== PARTNER-HUB-BOX \(Allgemein\) ===== -->)+', '', tail)
    tail=re.sub(r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*', '', tail, flags=re.S)
    open(f,'w',encoding='utf-8').write(head+build_main(d)+tail)
    print('ok',f)
