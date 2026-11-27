#!/usr/bin/env python3
"""Baut content/winter/skigebiet/index.html und content/winter/langlauf/index.html neu (nur <main>), mit Quellen."""
import re, html
E=lambda t: html.escape(t, quote=False)
def tab(rows, kopf=None):
    h='<table style="width:100%;border-collapse:collapse;font-size:.95rem;margin:8px 0 14px;">'
    if kopf: h+='<tr>'+''.join(f'<th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">{E(k)}</th>' for k in kopf)+'</tr>'
    for r in rows:
        h+='<tr>'+''.join((f'<th style="text-align:left;padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#14532d;vertical-align:top;width:30%;">{E(c)}</th>' if (i==0 and not kopf) else
                            f'<td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;">{E(c)}</td>') for i,c in enumerate(r))+'</tr>'
    return h+'</table>'
H2=lambda t: f'<h2 style="color:#14532d;margin:30px 0 10px;">{t}</h2>'
P=lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'
LAW=('<div style="background:#fef2f2;border-left:5px solid #b91c1c;padding:12px 16px;border-radius:10px;margin:0 0 20px;color:#1f2933;">'
     'Abseits der Pisten gilt der <a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">Lawinenlagebericht</a>. Notruf <strong>112</strong>.</div>')
def quellen(q): return H2('📚 Quellen')+'<ul style="line-height:1.7;font-size:.92rem;">'+''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t,u in q)+'</ul><p style="font-size:.82rem;color:#4b5563;">Stand: 27. November 2026. Alle Angaben ohne Gewähr.</p>'
def page(crumb, h1, lead, inner):
    return ('<main id="main"><article class="container" style="max-width:900px;margin:0 auto;padding:24px 16px 48px;">'
            f'<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <a href="/content/winter/index.html">Winter-Guide</a> › <span aria-current="page">{E(crumb)}</span></nav>'
            f'<header style="margin-bottom:16px;"><h1 style="color:#14532d;margin:0 0 8px;">{h1}</h1><p style="font-size:1.06rem;color:#1f2933;margin:0;">{lead}</p></header>'
            + LAW + inner + '<p style="margin-top:20px;"><a href="/content/winter/index.html">← Zurück zum Winter-Guide</a></p></article></main>')

SKI = page('Skigebiet', '⛷️ Skigebiet Spitzingsee-Tegernsee',
 'Kleines, übersichtliches Familienskigebiet zwischen Spitzingsee und Tegernseer Tal – vom Spitzingsee über die Firstalmen, Stümpfling und Roßkopf bis zum Sutten. Die Portale zählen Lifte und Pistenkilometer unterschiedlich; wir nennen deshalb die Spanne mit Quelle.',
 H2('📊 Kennzahlen')+tab([
   ('Höhe','983–1.570 m'),('Lifte','10 Bahnen und Lifte (muenchen.de, wetteronline); schneehoehen.de zählt 11, davon 3 Sessellifte und 6 Schlepplifte'),
   ('Pisten','14–20 km je nach Quelle; schneehoehen.de: 1,7 km leicht, 8,2 km mittel, 4,3 km schwer'),
   ('Hauptbahnen','zwei kuppelbare 4er-Sesselbahnen mit Wetterschutzhauben auf den Stümpfling – vom Spitzingsee und von der Tegernseer Seite (Sutten)'),
   ('Nachtskilauf','Donnerstag und Freitag 18:30–21:30 Uhr auf der über 2 km langen Stümpflingabfahrt'),
   ('Betriebszeit','08:30–16:15 Uhr (bergfex)'),
   ('Saison 2026/27','geplant ab 28.11.2026 (skiinfo, schneehoehen.de) bzw. 05.12.2026 (bergfex) bis Ende März/Anfang April – schneeabhängig'),
   ('Taubenstein','Skibetrieb 2015 eingestellt; die Taubensteinbahn fährt nur im Sommer. Die alte Piste ist heute Tourengelände.')])+
 H2('💶 Skipass')+P('Preise der Saison 2025/26 laut schneehoehen.de; für 2026/27 bitte beim Betreiber prüfen. Ab zwei Tagen gilt der Verbundskipass <strong>Alpen Plus</strong> (Spitzingsee-Tegernsee, Brauneck-Wegscheid, Sudelfeld, Wallberg).')+
 tab([('Halber Tag','43 €','21 €','41 €'),('1 Tag','51 €','24 €','48 €')], kopf=['Gültigkeit','Erwachsene','Kinder','Senioren'])+
 P('Familienskipass laut gleicher Quelle 124 €. Mit Gästekarte gibt es in den Alpen-Plus-Gebieten Ermäßigungen.')+
 H2('🚌 Anreise &amp; Parken')+P('Ohne Auto: BRB bis Fischhausen-Neuhaus oder Schliersee, weiter mit dem MVV-Bus <strong>362</strong> zum Spitzingsee. Parkplätze gibt es am Spitzingsattel, am Kurvenlift und im Ort; an schönen Wochenenden wird es voll, einen Platz findet man meist trotzdem am Sattel oder am Kurvenlift. Details auf der <a href="/anreise.html">Anreise-Seite</a>.')+
 H2('🎿 Tourengehen im Skigebiet')+P('Pistentouren sind am Spitzingsee beliebt – die Liftbetreiber geben dafür eigene Regeln und Routen vor. Ruhigere Alternative ist die ehemalige Taubenstein-Piste: <a href="/content/winter/skitouren/taubenstein.html">Taubenstein-Skitour</a>. Mehr in der <a href="/content/winter/skitouren/index.html">Skitouren-Übersicht</a>.')+
 '<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:16px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
 '<a href="https://www.amazon.de/s?k=Skihelm&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Skihelme</a> · <a href="https://www.amazon.de/s?k=Skibrille&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Skibrillen</a> bei Amazon</aside>'+
 quellen([('skiresort.info – Spitzingsee-Tegernsee (Sesselbahnen mit Wetterschutzhauben, Ausdehnung)','https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/test-result/summary'),
          ('skiresort.info – Taubensteinbahn, geschlossen 2015','https://skiresort.info/ski-resort/spitzingsee-tegernsee/ski-lifts/l1847'),
          ('muenchen.de – Skigebiet Spitzingsee: zehn Bahnen und Lifte','https://www.muenchen.de/freizeit/skigebiete/skigebiet-spitzingsee'),
          ('wetteronline.de – 983–1.570 m, 10 Lifte, 20 km','https://www.wetteronline.de/schneehoehen-gebiet/deutschland/bayerische-voralpen-spitzingsee-tegernsee'),
          ('schneehoehen.de – Skigebietsinfo (11 Lifte, 14,2 km, Saison)','https://www.schneehoehen.de/skigebiete/info/spitzingsee-stuempfling-taubenstein'),
          ('schneehoehen.de – Skipasspreise 2025/26','https://www.schneehoehen.de/skigebiete/preise/spitzingsee-stuempfling-taubenstein'),
          ('bergfex – Betriebszeiten, Nachtskilauf, Taubensteinbahn nur im Sommer','https://www.bergfex.com/spitzingsee-tegernsee/'),
          ('bahn.de – Nachtskilauf auf der über zwei Kilometer langen Stümpflingabfahrt','https://www.bahn.de/angebot/urlaub/bahnreisen/winterrail/deutschland/alpenregion-tegernsee-schliersee-by'),
          ('onthesnow – Alpen Plus Verbund','https://www.onthesnow.co.uk/oberbayern/spitzingsee-tegernsee/skipass')]))

LL = page('Langlauf', '🎿 Langlauf am Spitzingsee &amp; Schliersee',
 'Die Loipen am Spitzingsee liegen auf gut 1.000 m an den Valepper Almen und gelten als schneesicher; weitere Loipen gibt es rund um Schliersee und Neuhaus. Insgesamt nennt muenchen.de rund 20 km in Schliersee und Spitzingsee.',
 H2('📋 Loipen im Überblick')+tab([
   ('Valepper-Almen-Loipe','6,5 km','klassisch & Skating','Spitzingsee, Roßkopfweg (ca. 1.100 m) – abwechslungsreich, teils an der Roten Valepp; schwer'),
   ('Loipe Valepp–Spitzing','5 km','–','Spitzingsee'),
   ('Loipe Heimatsau–Spitzing','2 km','–','Spitzingsee'),
   ('Loipe Neuhaus–Geitau','8 km','–','Neuhaus'),
   ('Beleuchtete Loipe Schliersee–Hausham','4,5 km','–','Schliersee'),
   ('Fischhausen-Loipe','2,6 km','–','Fischhausen-Neuhaus, ca. 800 m, familienfreundlich')],
   kopf=['Loipe','Länge','Stil','Start / Charakter'])+
 P('„–“ = Stil in der Quelle nicht angegeben. Die Namen der Loipen unterscheiden sich je nach Portal; die Valepper-Almen-Loipe und die Loipe Valepp–Spitzing beschreiben dasselbe Gebiet.')+
 H2('📍 Am Spitzingsee')+P('Das Langlaufzentrum mit Ski- und Wachsservice liegt an der <strong>Albert-Link-Hütte</strong>. Die Valepper-Almen-Loipe hat eine schwarze Schleife (Blecksteinloipe) mit einer recht steilen, mehrstufigen Abfahrt am Umkehrpunkt. Den aktuellen Spurzustand meldet der Loipenbericht der Alpenregion Tegernsee Schliersee.')+
 H2('🚌 Anreise')+P('BRB bis Fischhausen-Neuhaus – die Fischhausen-Loipe beginnt direkt im Ort. Zum Spitzingsee weiter mit dem MVV-Bus <strong>362</strong>. <a href="/anreise.html">Anreise &amp; Parken</a>')+
 '<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:16px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
 '<a href="https://www.amazon.de/s?k=Langlaufski+Set&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Langlauf-Sets bei Amazon</a></aside>'+
 quellen([('destination.one / Alpenregion Tegernsee Schliersee – Valepper-Almen-Loipe 6,5 km','https://web.destination.one/en/tour/valepper-almen-trails'),
          ('destination.one – Fischhausen-Loipe 2,56 km','https://web.destination.one/en/tour/fischhausen-trail'),
          ('muenchen.de – Loipen in Schliersee und Spitzingsee (20 km)','https://www.muenchen.de/freizeit/berge-uebersicht/skigebiete/tegernseer-tal.html'),
          ('skiresort.info – Langlauf Spitzingsee, Langlaufzentrum Albert-Link-Hütte','https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/test-result/cross-country'),
          ('DAV München & Oberland – Tourenbericht Loipe Valepper Almen (Blecksteinloipe)','https://www.alpenverein-muenchen-oberland.de/seniorenkreis/2025-tourenberichte2/12.02.2025-loipe-valepper-almen'),
          ('snow-online – Loipen Schliersee–Spitzingsee','https://www.snow-online.com/cross-country/spitzingsee_trailmap.html')]))

RODEL = page('Rodelbahn Obere Firstalm', '🛷 Rodelbahn Obere Firstalm',
 'Die Familien-Rodelbahn am Spitzingsee: vom Spitzingsattel hinauf zur Oberen Firstalm (1.375 m), oben einkehren, auf rund 2,5 km wieder hinunter. Keine scharfen Kurven, keine Steilstücke – und abends beleuchtet. Die Alm ist unser Zuhause – Öffnungszeiten und Preise kommen direkt von der Hütte, die Streckendaten aus den unten genannten Quellen.',
 H2('📋 Eckdaten')+tab([
   ('Länge','ca. 2,5–2,6 km'),('Höhe','Spitzingsattel ca. 1.130 m → Obere Firstalm 1.375 m (ca. 250 Hm)'),
   ('Aufstieg','ca. 40–45 min zu Fuß auf der Bahn (für Autos gesperrter Fahrweg)'),
   ('Schwierigkeit','leicht, gut mit Kindern'),('Beleuchtung','Mondscheinrodeln ab 27.11.2026 – Bahn bis 22:30 Uhr beleuchtet'),
   ('Rodelverleih','an der Oberen Firstalm, 7 € pro Schlitten'),
   ('Alternative','vom Parkplatz Kurvenlift über die Untere Firstalm (1.318 m) hinauf'),
   ('Anreise','Bus 362 bis Haltestelle Spitzingsattel; Parkplatz am Sattel 8 € pro Tag')])+
 H2('🕒 Öffnungszeiten (Winter 2026/27)')+'<div style="background:#f0fdf4;border-left:5px solid #2d8a56;padding:12px 16px;border-radius:10px;color:#1f2933;"><strong>Aus erster Hand – Obere Firstalm, Stand 27.11.2026:</strong>''<ul style="margin:8px 0 0 18px;line-height:1.7;"><li>Geöffnet täglich 11–22 Uhr, ab 22 Uhr Hüttenruhe</li><li>Küche 11–21 Uhr</li>''<li>Frühstück 8–10 Uhr, 17,50 € pro Person</li><li>Mondscheinrodeln ab 27.11.2026, Bahn bis 22:30 Uhr beleuchtet</li><li>Schlitten-Verleih 7 €</li></ul>''<p style="margin:8px 0 0;">Telefon <strong>08026 7302</strong>.</p></div>'+
 H2('⚠️ Hinweise')+'<ul style="line-height:1.7;color:#1f2933;"><li>Bergauf am Rand gehen – die Bahn ist gleichzeitig Aufstiegsweg.</li><li>Bei harter, vereister Bahn langsam fahren; Grödel für den Aufstieg helfen.</li><li>Den aktuellen Zustand der Bahn vorab erfragen, besonders am Saisonanfang.</li></ul>'+
 '<p><a href="/content/winter/schneeschuh/firstalm.html">Obere Firstalm als Winterwanderung</a> · <a href="/content/winter/rodeln-familie.html">Rodeln mit Familie</a></p>'+
 quellen([('bergtour-online.de – Obere Firstalm Rodeln: 2,5 km, 250 Hm, beleuchtet bis 22:30, Rodelverleih','https://www.bergtour-online.de/bergtouren/wintertouren/rodeltouren/obere-firstalm-rodeln/'),
          ('hoehenrausch.de – Obere Firstalm: 2,5 km vom Spitzingsattel, Öffnungszeiten, Telefon','https://www.hoehenrausch.de/huetten/obere-firstalm/huettenbuch.php'),
          ('mux.de – Rodelbahn Obere Firstalm 2.600 m, 1.130–1.375 m','https://www.mux.de/info/die-schoensten-rodelbahnen-im-muenchner-umland/'),
          ('bergtour-online.de – Rodelverleih 7 € (Stand 2024/2025)','https://www.bergtour-online.de/bergtouren/wintertouren/rodeltouren/schoenste-rodeltouren-bayerische-alpen/'),
          ('bergwelten.com – Obere Firstalm (1.375 m), Gehzeit 40 min, Alternative über Untere Firstalm','https://www.bergwelten.com/h/obere-firstalm')]))

RODELN = page('Rodeln', '🛷 Rodeln am Spitzingsee &amp; Tegernsee',
 'Die Familien-Rodelbahn am Spitzingsee ist die an der Oberen Firstalm – leicht, schneesicher und abends beleuchtet. Darunter alle weiteren belegten Bahnen der Region, vom kurzen Stück an der Unteren Firstalm bis zur 6,5 km langen Wallberg-Bahn.',
 '<div style="background:linear-gradient(135deg,#14532d,#2d8a56);color:#fff;border-radius:14px;padding:20px 22px;margin:0 0 22px;">'
 '<div style="font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;opacity:.9;">Unsere Hausbahn · Familien-Tipp</div>'
 '<h2 style="color:#fff;margin:6px 0 8px;">⭐ Rodelbahn Obere Firstalm</h2>'
 '<ul style="margin:0 0 12px 18px;line-height:1.7;"><li>ca. 2,5 km, leicht – auch mit kleinen Kindern</li><li>Aufstieg ca. 40–45 min vom Spitzingsattel, rund 250 Hm</li>'
 '<li>Mondscheinrodeln ab 27.11.2026 – Bahn bis 22:30 Uhr beleuchtet</li><li>Schlitten-Verleih an der Alm: 7 €</li>'
 '<li>Hütte täglich 11–22 Uhr, Küche 11–21 Uhr, Frühstück 8–10 Uhr (17,50 € p. P.)</li><li>Bus 362 bis Spitzingsattel · Parken am Sattel 8 €</li></ul>'
 '<a href="/content/winter/firstalm-rodelbahn.html" style="display:inline-block;background:#fff;color:#14532d;font-weight:700;padding:9px 16px;border-radius:8px;text-decoration:none;">Alle Infos zur Firstalm-Rodelbahn →</a></div>'+
 H2('🏔️ Weitere Bahnen am Spitzingsee &amp; Schliersee')+tab([
   ('Untere Firstalm','ca. 1,5 km','leicht','geräumter Fahrweg hinab Richtung Spitzingsee'),
   ('Rotwandhaus','ca. 4,5 km','mittel','keine offizielle Rodelbahn, Forststraße nicht präpariert, kein Verleih – nur mit eigenem Schlitten bei guter Schneelage')],
   kopf=['Bahn','Länge','Anspruch','Hinweis'])+
 H2('🌊 Tegernseer Tal')+tab([
   ('Neureuth → Tegernsee','ca. 2,1 km','für Fortgeschrittene','ab Berggasthof Neureuth (1.259 m), 363 Hm Abfahrt, steile Passagen und enge Kurven; Aufstieg ca. 1 h ab Parkplatz Neureuthstraße'),
   ('Neureuth → Gmund (Oberbuchberg)','ca. 3,7 km','nur für Geübte','schnelle Geraden, enge Kurven'),
   ('Riederstein','ca. 1,7 km','mittel','Start auf 1.062 m, 264 Hm Abfahrt'),
   ('Galaun (Tegernsee)','ca. 2 km','leicht bis mittel','Aufstieg gut 1 h'),
   ('Aueralm (Bad Wiessee)','ca. 4,3–4,5 km','mittel','Aufstieg ca. 1,5 h'),
   ('Hirschberg (Kreuth)','ca. 4,5–5 km','anspruchsvoll','Start Ortsteil Scharling, für geübte Rodler'),
   ('Wallberg (Rottach-Egern)','ca. 6,5 km','sportlich','mit der Wallbergbahn auf 1.620 m, rund 825 Hm; nicht für Kleinkinder')],
   kopf=['Bahn','Länge','Anspruch','Hinweis'])+
 H2('⚠️ Sicher rodeln')+'<ul style="line-height:1.7;color:#1f2933;"><li>Helm, vor allem für Kinder.</li><li>Beim Aufstieg am Rand gehen – Rodelbahnen sind oft zugleich der Aufstiegsweg.</li><li>Abstand halten, nicht im Auslauf stehen bleiben.</li><li>Zustand der Bahn vorab beim Betreiber oder der Hütte erfragen.</li></ul>'+
 quellen([('Obere Firstalm – Öffnungszeiten, Preise, Mondscheinrodeln (Angabe der Hütte, 27.11.2026)','/content/winter/firstalm-rodelbahn.html'),
          ('bergtour-online.de – Obere Firstalm: ca. 2,5 km, Rodelverleih an der Alm','https://www.bergtour-online.de/bergtouren/wintertouren/rodeltouren/schoenste-rodeltouren-bayerische-alpen/'),
          ('in-muenchen.de – Firstalm: beleuchtet bis 22:30 Uhr, schneesicher','https://www.in-muenchen.de/stadtleben/schlittenfahren-rodeln.html'),
          ('karwendel-urlaub.de – Untere Firstalm ca. 1,5 km; Neureuth, Galaun, Aueralm, Hirschberg','https://www.karwendel-urlaub.de/umgebung/tegernsee/rodeln/'),
          ('bergwelten.com – Von der Neureuth nach Tegernsee: 2,1 km','https://www.bergwelten.com/t/r/7559'),
          ('bergwelten.com – Von der Neureuth nach Gmund: 3,7 km','https://www.bergwelten.com/t/r/7560'),
          ('bergwelten.com – Riederstein: 1,7 km','https://www.bergwelten.com/t/r/7562'),
          ('bergwelten.com – Aueralm: 4,3 km','https://www.bergwelten.com/touren/aueralm'),
          ('bergwelten.com – Vom Hirschberg nach Kreuth-Scharling: 4,5 km','https://www.bergwelten.com/t/r/7563'),
          ('DAV – Schlemmen und Rodeln (Rotwandhaus nicht präpariert)','https://www.alpenverein.de/artikel/schlemmen-und-rodeln_0248a1d2-9810-4987-8e1c-ad83a741c8e8'),
          ('karwendel-urlaub.de – Wallberg: 6,5 km, ca. 825 Hm','https://www.karwendel-urlaub.de/?p=2832')]))

EINSTEIGER = page('Skitouren für Einsteiger', '🎿 Skitouren für Einsteiger am Spitzingsee',
 'Wer sicher Parallelschwung fährt, kann am Spitzingsee mit kurzen, leichten Touren beginnen. Lawinenwissen und Notfallausrüstung gehören von Anfang an dazu – am besten lernt man beides in einem Kurs, etwa bei einer DAV-Sektion.',
 H2('🟢 Leichte Einstiegstouren')+tab([
   ('Brecherspitz-Westgipfel','ca. 500 Hm','leicht','Kurvenlift – Firstalmen – Westgipfel; breiter Südwesthang'),
   ('Taubenstein / Taubensteinsattel','ca. 490–600 Hm','leicht','ehemalige Taubenstein-Piste, vom DAV als Pisten- und Nachtroute beschrieben'),
   ('Rotwand (direkt)','ca. 800 Hm','mittel','Forststraße zum Rotwandhaus – lang, aber technisch moderat')],
   kopf=['Tour','Höhenmeter','Schwierigkeit','Charakter'])+
 '<p><a href="/content/winter/skitouren/brecherspitz.html">Brecherspitz</a> · <a href="/content/winter/skitouren/taubenstein.html">Taubenstein</a> · <a href="/content/winter/skitouren/rotwand.html">Rotwand</a></p>'+
 H2('✅ Vor der ersten Tour')+'<ul style="line-height:1.7;color:#1f2933;"><li>Lawinenlagebericht lesen – er erscheint im Winter täglich um 18 Uhr für den Folgetag.</li>'
 '<li>LVS-Gerät, Sonde, Schaufel mitnehmen und die Verschüttetensuche vorher üben.</li><li>Felle, Harscheisen, Stöcke, warme Wechselkleidung, Stirnlampe.</li>'
 '<li>Pistentouren nur nach den Regeln der Liftbetreiber; die alte Taubenstein-Piste ist die ruhige Alternative.</li><li>Notruf 112, Notfall-App SOS EU ALP.</li></ul>'+
 '<p><a href="/content/winter/lawinenkunde-grundlagen.html">Lawinenkunde-Grundlagen</a> · <a href="/content/winter/ausruestung-winter.html">Winter-Ausrüstung</a></p>'+
 quellen([('hoehenrausch.de – Brecherspitz-Westgipfel als Skitour (leicht, 500 Hm)','https://www.hoehenrausch.de/berge/brecherspitz/skitour/'),
          ('DAV München & Oberland – Pistentouren Taubenstein (PDF)','https://www.alpenverein-muenchen-oberland.de/uploads/images/quXDtdW8KTYAmijoMd1CJQ/pistentouren_taubenstein.pdf'),
          ('hoehenrausch.de – Rotwand als Winterwanderung (800 Hm)','https://www.hoehenrausch.de/berge/rotwand/winterwanderung/'),
          ('alpinwelt 1/24 – Lagebericht täglich 18 Uhr (PDF)','https://lawinenwarndienst.bayern.de/wp-content/uploads/2024/03/Beitrag_alpinwelt_01-24_Reisner.pdf'),
          ('DAV – Notfall-App SOS EU ALP','https://www.alpenverein.de/artikel/notfall-app-sos-eu-alp_69098d79-169b-40df-8bca-daa419eeced6')]))

LAWINE = page('Lawinenkunde', '⚠️ Lawinenkunde – die Grundlagen',
 'Der Lawinenlagebericht ist die wichtigste Planungsgrundlage für jede Wintertour abseits gesicherter Pisten. Hier steht, wie er aufgebaut ist und was die Gefahrenstufen bedeuten – ein Kurs ersetzt das nicht.',
 H2('📊 Die fünf Gefahrenstufen (europaweit einheitlich)')+tab([
   ('1','gering','Schneedecke allgemein gut verfestigt; Auslösung vor allem bei großer Zusatzbelastung an sehr wenigen, extremen Steilhängen'),
   ('2','mäßig','an einigen Steilhängen nur mäßig verfestigt; schon deutlich gefährlicher als Stufe 1'),
   ('3','erheblich','an vielen Steilhängen mäßig bis schwach verfestigt; Auslösung bereits bei geringer Zusatzbelastung möglich – laut DAV etwa viermal so viele Gefahrenstellen wie bei Stufe 2'),
   ('4','groß','an den meisten Steilhängen schwach verfestigt; Auslösung schon bei geringer Zusatzbelastung wahrscheinlich, spontane Lawinen'),
   ('5','sehr groß','Katastrophenfall – auf Touren im Gelände unbedingt verzichten')], kopf=['Stufe','Bezeichnung','Bedeutung (verkürzt)'])+
 H2('🧭 So liest man den Lagebericht')+'<ol style="line-height:1.7;color:#1f2933;"><li><strong>Gefahrenstufe</strong> – wie groß ist die Gefahr?</li><li><strong>Lawinenproblem</strong> – was ist das Problem (z. B. Triebschnee, Altschnee, Nassschnee, Gleitschnee)?</li>'
 '<li><strong>Gefahrenstellen</strong> – wo: Höhenlage und Exposition (Windrose).</li><li><strong>Details</strong> – warum: Schneedeckenaufbau und Wetter.</li></ol>'+
 P('Der Bericht für die Bayerischen Alpen erscheint im Winter täglich um 18 Uhr und gilt als Prognose für die folgenden 24 Stunden; gültig ist er jeweils von 17 bis 17 Uhr.')+
 H2('🎒 Notfallausrüstung &amp; Notruf')+'<ul style="line-height:1.7;color:#1f2933;"><li>LVS-Gerät (beim Losgehen Gruppencheck), Sonde, Schaufel – jede Person.</li><li>Notruf <strong>112</strong>; die App <strong>SOS EU ALP</strong> übermittelt den Standort an die Leitstelle in Bayern, Tirol oder Südtirol.</li></ul>'+
 '<p><a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">→ Aktueller Lawinenlagebericht Bayern</a></p>'+
 quellen([('EAWS – Europäische Lawinengefahrenskala (PDF)','https://www.avalanches.org/wp-content/uploads/2022/09/Europaische_Lawinengefahrenskala-EAWS.pdf'),
          ('DAV – Was steckt hinter dem Lawinenlagebericht?','https://www.alpenverein.de/artikel/was-steckt-hinter-dem-lawinenlagebericht_bb0542ff-585f-48f5-bdc6-1476865386f6'),
          ('Panorama 6/2019 – Der optimierte Lawinenlagebericht (Wie? Was? Wo? Warum?, PDF)','https://lawinenwarndienst.bayern.de/wp-content/uploads/2023/08/Panorama-6-2019-LLB.pdf'),
          ('alpinwelt 1/24 – Veröffentlichung täglich 18 Uhr (PDF)','https://lawinenwarndienst.bayern.de/wp-content/uploads/2024/03/Beitrag_alpinwelt_01-24_Reisner.pdf'),
          ('DAV – Notfall-App SOS EU ALP','https://www.alpenverein.de/artikel/notfall-app-sos-eu-alp_69098d79-169b-40df-8bca-daa419eeced6')]))

for f,body,title,desc in [
  ('content/winter/skigebiet/index.html',SKI,'Skigebiet Spitzingsee-Tegernsee – Lifte, Pisten, Skipass','Skigebiet Spitzingsee-Tegernsee: 983–1.570 m, 10 Lifte, 14–20 km Pisten, Nachtskilauf Do/Fr, Skipass und Anreise – mit Quellen.'),
  ('content/winter/firstalm-rodelbahn.html',RODEL,'Rodelbahn Obere Firstalm – 2,5 km, beleuchtet','Rodelbahn Obere Firstalm am Spitzingsee: ca. 2,5 km, 250 Hm, abends beleuchtet, Rodelverleih an der Alm – Eckdaten mit Quellen.'),
  ('content/winter/rodeln-familie.html',RODELN,'Rodeln am Spitzingsee & Tegernsee – Bahnen im Überblick','Rodeln am Spitzingsee: Familien-Rodelbahn Obere Firstalm (2,5 km, bis 22:30 Uhr beleuchtet) – dazu Neureuth, Riederstein, Aueralm, Hirschberg, Wallberg mit Quellen.'),
  ('content/winter/skitouren-anfaenger.html',EINSTEIGER,'Skitouren für Einsteiger am Spitzingsee','Leichte Einstiegs-Skitouren am Spitzingsee: Brecherspitz-Westgipfel, Taubenstein, Rotwand – plus Checkliste vor der ersten Tour, mit Quellen.'),
  ('content/winter/lawinenkunde-grundlagen.html',LAWINE,'Lawinenkunde – Gefahrenstufen und Lagebericht','Lawinenkunde-Grundlagen: die fünf europäischen Gefahrenstufen, Aufbau des Lawinenlageberichts Bayern, Notfallausrüstung und Notruf – mit Quellen.'),
  ('content/winter/langlauf/index.html',LL,'Langlauf am Spitzingsee & Schliersee – Loipen','Loipen am Spitzingsee und Schliersee: Valepper-Almen-Loipe 6,5 km, Langlaufzentrum Albert-Link-Hütte, Loipen in Neuhaus und Schliersee – mit Quellen.')]:
    s=open(f,encoding='utf-8').read(); a=s.find('<main'); b=s.find('</main>')+7
    head,tail=s[:a],s[b:]
    head=re.sub(r'<title>.*?</title>',f'<title>{E(title)} | alpenexperte.de</title>',head,count=1,flags=re.S)
    head=re.sub(r'(<meta name="description"\s+content=")[^"]*(")',lambda m:m.group(1)+html.escape(desc)+m.group(2),head,count=1)
    head=re.sub(r'(<meta property="og:title" content=")[^"]*(")',lambda m:m.group(1)+html.escape(title)+m.group(2),head)
    head=re.sub(r'(<meta property="og:description" content=")[^"]*(")',lambda m:m.group(1)+html.escape(desc)+m.group(2),head)
    for pat in [r'<!-- ===== BRB ECHTZEIT-FAHRPLAN.*?</div>\s*',r'<section class="quellen-section".*?</section>\s*',r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*']:
        tail=re.sub(pat,'',tail,flags=re.S)
    tail=re.sub(r'(<!-- ===== PARTNER-HUB-BOX \(Allgemein\) ===== -->)+','',tail)
    open(f,'w',encoding='utf-8').write(head+body+tail); print('ok',f)
