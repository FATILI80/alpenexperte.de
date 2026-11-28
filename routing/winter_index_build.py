#!/usr/bin/env python3
"""Baut den Inhalt von content/winter/index.html neu (Gravel-Schema: Sprungmenü, Bildkarten, Quellen).
Kopf und Footer der Seite bleiben erhalten. Alle Zahlen mit Quelle."""
import re, html
F='content/winter/index.html'
E=lambda t: html.escape(t, quote=False)

NAV=[('#skitouren','🎿 Skitouren'),('#schneeschuh','👣 Schneeschuh & Winterwandern'),('#rodeln','🛷 Rodeln'),
     ('#skigebiet','⛷️ Skigebiet'),('#langlauf','🎿 Langlauf'),('#lawine','⚠️ Lawine & Notruf'),('#ausruestung','🎒 Ausrüstung'),('#quellen','📚 Quellen')]

def card(img, alt, kopf, titel, text, href):
    return (f'<a href="{href}" style="display:block;background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;text-decoration:none;color:#0f2942;">'
            f'<img src="/images/{img}" alt="{E(alt)}" loading="lazy" style="width:100%;height:150px;object-fit:cover;display:block;">'
            f'<div style="padding:12px 14px;"><div style="font-size:.8rem;color:#1d4ed8;font-weight:700;">{E(kopf)}</div>'
            f'<h3 style="margin:4px 0 6px;color:#14532d;font-size:1.05rem;">{E(titel)}</h3>'
            f'<p style="margin:0;font-size:.9rem;line-height:1.45;">{E(text)}</p>'
            '<span style="display:inline-block;margin-top:8px;color:#14532d;font-weight:700;font-size:.88rem;">Tour ansehen →</span></div></a>')

GRID='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;">'
H2=lambda id_,t: f'<h2 id="{id_}" style="color:#14532d;margin:34px 0 10px;scroll-margin-top:140px;">{t}</h2>'
P=lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'

ski=[card('rotwand-ausblick-im-winter.jpg','Rotwand im Winter','1.884 m · ca. 800 Hm direkt · Reibn 1.200–1.300 Hm · mittel','Rotwand & Rotwand-Reibn',
          'Über die Forststraße zum Rotwandhaus – oder die große Runde über Auerspitz und Miesingsattel.','/content/winter/skitouren/rotwand.html'),
     card('winter-landschaft.jpg','Verschneite Hänge am Taubenstein','1.692 m · ca. 600 Hm · leicht','Taubenstein',
          'Auf der stillgelegten Taubenstein-Piste zum Sattel; der Gipfel ist ein kurzer Felsaufbau.','/content/winter/skitouren/taubenstein.html'),
     card('AusblickWinterunterfirst.jpg','Winterblick von der Unteren Firstalm','ca. 1.630 m Westgipfel · ca. 500 Hm · leicht','Brecherspitz-Westgipfel',
          'Die kurze Tour über Untere und Obere Firstalm – ab unserer Alm nur rund 255 Hm.','/content/winter/skitouren/brecherspitz.html'),
     card('winter-1.jpeg','Winterwald','1.669 m · 560–810 Hm · mittel bis steil','Bodenschneid',
          'Klassisch von Neuhaus übers Bodenschneidhaus oder steil über Firstalm und Bital.','/content/winter/skitouren/bodenschneid.html')]
schuh=[card('schneeschuh.jpg','Schneeschuhwanderer','ca. 3 km · 20–30 Hm · 1 h · leicht','Spitzingsee-Runde',
            'Flach um den See, gut mit Kindern – Schneeschuhe nur nach viel Neuschnee nötig.','/content/winter/schneeschuh/spitzingsee-runde.html'),
       card('rodelpiste.jpg','Weg zur Oberen Firstalm','ca. 250 Hm · 45 min · leicht','Obere Firstalm',
            'Vom Spitzingsattel auf dem Trautweinweg – Verlängerung zum Brecherspitz-Westgipfel möglich.','/content/winter/schneeschuh/firstalm.html'),
       card('rotwandhaus-winter.jpg','Rotwandhaus im Winter','660 Hm Rotwandhaus · 800 Hm Gipfel · 2:30–2:45 h','Rotwand im Winter',
            'Breite, meist gespurte Forststraße zum Rotwandhaus, zum Gipfel deutlich anspruchsvoller.','/content/winter/schneeschuh/rotwand.html')]

LAW=('<div style="background:#fef2f2;border-left:5px solid #b91c1c;padding:16px 18px;border-radius:10px;color:#1f2933;">'
     '<p style="margin:0 0 8px;"><strong style="color:#991b1b;">Kein Hang ist „lawinensicher“.</strong> Der Lawinenlagebericht für die Bayerischen Alpen erscheint im Winter täglich um 18 Uhr und gilt als Prognose für die nächsten 24 Stunden – er ersetzt nicht die eigene Einschätzung vor Ort.</p>'
     '<ul style="margin:0 0 8px 18px;line-height:1.6;"><li>LVS-Gerät (eingeschaltet), Sonde und Schaufel bei jeder Skitour und jeder Schneeschuhtour abseits geräumter Wege.</li>'
     '<li>Notruf: <strong>112</strong> – die Leitstelle alarmiert die Bergwacht. (Die 140 ist der Alpin-Notruf in Österreich.)</li>'
     '<li>Notfall-App <strong>SOS EU ALP</strong>: übermittelt beim Notruf den GPS-Standort an die Leitstelle in Bayern, Tirol oder Südtirol.</li></ul>'
     '<p style="margin:0;"><a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">→ Lawinenwarndienst Bayern</a> · '
     '<a href="/content/winter/lawinenkunde-grundlagen.html">Lawinenkunde-Grundlagen</a></p></div>')

SKIG=[('Höhe','983–1.570 m'),('Lifte','10 Bahnen und Lifte (manche Portale zählen 11)'),
      ('Pisten','je nach Quelle 14–20 km (schneehoehen.de 14,2 km, planetoutdoor 14,7 km, wetteronline 20 km)'),
      ('Bereiche','Spitzingsee/Firstalm, Stümpfling, Roßkopf, Sutten (Tegernseer Seite)'),
      ('Bahnen','zwei kuppelbare 4er-Sesselbahnen mit Wetterschutzhauben auf den Stümpfling – von Spitzingsee und vom Tegernseer Tal (Sutten)'),
      ('Taubenstein','Skibetrieb 2015 eingestellt, heute Tourengebiet'),
      ('Tageskarte','51 € Erwachsene (laut skiresort.info / schneehoehen.de – aktuellen Preis beim Betreiber prüfen)')]
tab='<table style="width:100%;border-collapse:collapse;font-size:.95rem;margin:8px 0;">'+''.join(
    f'<tr><th style="text-align:left;padding:7px 10px;border-bottom:1px solid #e5e7eb;width:28%;color:#14532d;vertical-align:top;">{E(k)}</th><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;color:#1f2933;">{E(v)}</td></tr>' for k,v in SKIG)+'</table>'

QUELLEN=[('skiresort.info – Skigebiet Spitzingsee-Tegernsee','https://www.skiresort.info/ski-resort/spitzingsee-tegernsee'),
 ('skiresort.info – Taubensteinbahn, geschlossen 2015','https://skiresort.info/ski-resort/spitzingsee-tegernsee/ski-lifts/l1847'),
 ('muenchen.de – Skigebiet Spitzingsee: zehn Bahnen und Lifte','https://www.muenchen.de/freizeit/skigebiete/skigebiet-spitzingsee'),
 ('wetteronline.de – Spitzingsee-Tegernsee: 983–1.570 m, 10 Lifte, 20 km','https://www.wetteronline.de/schneehoehen-gebiet/deutschland/bayerische-voralpen-spitzingsee-tegernsee'),
 ('schneehoehen.de – Spitzingsee-Tegernsee: 14,2 km Pisten','https://www.schneehoehen.de/skigebiete/info/spitzingsee-stuempfling-taubenstein'),
 ('planetoutdoor.de – Pistenplan 14,7 km','https://planetoutdoor.de/wissen/winterwissen/skigebiet-spitzingsee-tegernsee'),
 ('destination.one / Alpenregion Tegernsee Schliersee – Valepper-Almen-Loipe 6,5 km','https://web.destination.one/en/tour/valepper-almen-trails'),
 ('skiresort.info – Langlauf an den Valepper Almen, Langlaufzentrum an der Albert-Link-Hütte','https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/test-result/cross-country'),
 ('snowtrex – rund 33 km Loipen um Schliersee und Spitzingsee','https://snowtrex.co.uk/germany/schliersee/cross-country.html'),
 ('hoehenrausch.de – Winterwandern und Rodeln an der Oberen Firstalm','https://www.hoehenrausch.de/wandern/kinder/obere-firstalm'),
 ('hoehenrausch.de – Rotwandhaus: Forstweg nicht als Rodelbahn präpariert','https://www.hoehenrausch.de/wandern/rodeln/rotwandhaus-spitzingsee'),
 ('alpinwelt 1/24 – Lagebericht täglich 18 Uhr (Lawinenwarndienst Bayern, PDF)','https://lawinenwarndienst.bayern.de/wp-content/uploads/2024/03/Beitrag_alpinwelt_01-24_Reisner.pdf'),
 ('DAV – Notfall-App SOS EU ALP','https://www.alpenverein.de/artikel/notfall-app-sos-eu-alp_69098d79-169b-40df-8bca-daa419eeced6'),
 ('DAV – Notrufnummern in den Alpen (112, Österreich 140)','https://www.alpenverein.de/services/dav-services/gut-informiert-in-den-bergen-unterwegs-notruf-und-rettung-in-den-alpen_aid_10705.html')]

body=[]
body.append('<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">')
body.append('<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">Winter-Guide</span></nav>')
body.append('<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">❄️ Winter am Spitzingsee</h1>'
            '<p style="font-size:1.08rem;color:#1f2933;margin:0;">Skitouren, Schneeschuh- und Winterwanderungen, Rodeln, Pisten und Loipen rund um den Spitzingsee – mit Tourdaten aus nachprüfbaren Quellen. Geschrieben von der Oberen Firstalm (1.375 m), mitten im Gebiet.</p></header>')
body.append('<img src="/images/Winter%20Guide.jpg" alt="Winterlandschaft am Spitzingsee" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">')
body.append('<nav class="kat-nav" aria-label="Winter-Bereiche" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'+
            ''.join(f'<a href="{h}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for h,t in NAV)+'</nav>')
body.append('<div style="background:#fef2f2;border-left:5px solid #b91c1c;padding:10px 14px;border-radius:10px;color:#1f2933;margin-bottom:8px;"><strong style="color:#991b1b;">Vor jeder Tour:</strong> <a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">Lawinenlagebericht Bayern</a> lesen · Notruf 112 · <a href="#lawine">mehr zu Lawine &amp; Notruf</a></div>')
body.append(H2('skitouren','🎿 Skitouren')+P('Vier Gipfel, alle mit Start am Spitzingsee oder an den Firstalmen. Schwierigkeiten nach den angegebenen Tourenportalen; Höhenmeter jeweils vom genannten Startpunkt.')+GRID+''.join(ski)+'</div>')
body.append('<p style="margin-top:10px;"><a href="/content/winter/skitouren/index.html">→ Skitouren-Übersicht</a> · <a href="/content/winter/skitouren-anfaenger.html">Skitouren für Einsteiger</a></p>')
body.append(H2('schneeschuh','👣 Schneeschuh &amp; Winterwandern')+P('Bei festgetretener Spur reichen oft Winterschuhe mit Grödeln; Schneeschuhe lohnen sich nach Neuschnee und abseits der Wege.')+GRID+''.join(schuh)+'</div>')
body.append('<p style="margin-top:10px;"><a href="/content/winter/schneeschuh/index.html">→ Schneeschuh-Übersicht</a> · <a href="/content/winter/winterwandern-groedel.html">Winterwandern mit Grödeln</a></p>')
body.append(H2('rodeln','🛷 Rodeln')+P('Die bekannteste Rodelbahn am Spitzingsee führt vom Spitzingsattel zur <strong>Oberen Firstalm</strong>: hinauf etwa 45 Minuten und 250 Hm auf dem für Autos gesperrten Trautweinweg, hinunter auf derselben Bahn. '
            'Zum <strong>Rotwandhaus</strong> führt eine breite Forststraße, die aber nicht als Rodelbahn präpariert ist – mit eigenem Schlitten nur bei passender Schneelage.')+
            '<p><a href="/content/winter/firstalm-rodelbahn.html">→ Rodelbahn Obere Firstalm</a> · <a href="/content/winter/rodeln-familie.html">Rodeln mit Familie</a></p>')
body.append(H2('skigebiet','⛷️ Skigebiet Spitzingsee-Tegernsee')+P('Das Skigebiet reicht vom Spitzingsee über die Firstalmen, Stümpfling und Roßkopf bis zum Sutten auf der Tegernseer Seite. Die Portale zählen unterschiedlich – deshalb hier die Spanne mit Quelle:')+tab+
            '<p><a href="/content/skigebiete/">→ Skigebiet-Guide</a> · Saisonzeiten und Liftstatus tagesaktuell bei den <a href="https://www.alpenbahnen-spitzingsee.de" target="_blank" rel="noopener">Alpenbahnen Spitzingsee</a>.</p>')
body.append(H2('langlauf','🎿 Langlauf')+P('Am Spitzingsee liegen die Loipen an den <strong>Valepper Almen</strong>: die Valepper-Almen-Loipe ist rund 6,5 km lang, startet am Roßkopfweg (ca. 1.100 m), ist klassisch und für Skating gespurt und läuft teils entlang der Roten Valepp. Das Langlaufzentrum liegt an der Albert-Link-Hütte. '
            'Rund um Schliersee und Spitzingsee kommen je nach Portal etwa 22–33 km Loipen zusammen.')+'<p><a href="/content/winter/langlauf/index.html">→ Langlauf-Guide</a></p>')
body.append(H2('lawine','⚠️ Lawine &amp; Notruf')+LAW)
body.append(H2('ausruestung','🎒 Ausrüstung')+'<ul style="line-height:1.7;color:#1f2933;">'
            '<li><strong>Lawinen-Notfallausrüstung</strong> – LVS, Sonde, Schaufel</li><li><strong>Felle und Harscheisen</strong> für Skitouren</li>'
            '<li><strong>Schneeschuhe</strong> mit Steighilfe oder <strong>Grödel</strong> für gespurte Wege</li><li><strong>Stöcke mit Schneetellern</strong></li>'
            '<li><strong>Zwiebelprinzip</strong> – Funktionsunterwäsche, Fleece, winddichte Jacke, Mütze, Handschuhe</li><li><strong>Thermoskanne, Stirnlampe, geladenes Handy</strong></li></ul>'
            '<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
            '<a href="https://www.amazon.de/s?k=LVS+Set+Sonde+Schaufel&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">LVS-Sets</a> · '
            '<a href="https://www.amazon.de/s?k=Schneeschuhe+Wandern&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Schneeschuhe</a> · '
            '<a href="https://www.amazon.de/s?k=Gr%C3%B6del&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Grödel</a> bei Amazon · '
            '<a href="/content/winter/ausruestung-winter.html">Ausführliche Winter-Ausrüstung</a></aside>')
body.append(H2('mehr','📖 Weitere Winterthemen')+'<ul style="line-height:1.8;">'
            '<li><a href="/content/winter/firstalm-rodelbahn.html">Rodelbahn Obere Firstalm</a> · <a href="/content/winter/rodeln-familie.html">Rodeln mit Familie</a></li>'
            '<li><a href="/content/winter/skitouren-anfaenger.html">Skitouren für Einsteiger</a> · <a href="/content/winter/ausruestung-winter.html">Winter-Ausrüstung</a></li>'
            '<li><a href="/anreise.html">Anreise &amp; Parken</a></li></ul>')
body.append(H2('quellen','📚 Quellen')+'<ul style="line-height:1.7;font-size:.92rem;">'+''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t,u in QUELLEN)+
            '</ul><p style="font-size:.82rem;color:#4b5563;">Stand: 27. November 2026. Alle Angaben ohne Gewähr – Verhältnisse, Liftbetrieb und Hütten-Öffnungszeiten vor Ort prüfen.</p>')
body.append('</article></main>')

s=open(F,encoding='utf-8').read()
a=s.find('<main'); b=s.find('</main>')+7
head,tail=s[:a],s[b:]
tail=re.sub(r'<!-- ===== BRB ECHTZEIT-FAHRPLAN.*?</div>\s*','',tail,flags=re.S)
tail=re.sub(r'<section class="quellen-section".*?</section>\s*','',tail,flags=re.S)
tail=re.sub(r'(<!-- ===== PARTNER-HUB-BOX \(Allgemein\) ===== -->)+','',tail)
tail=re.sub(r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*','',tail,flags=re.S)
head=re.sub(r'(<meta name="description"\s+content=")[^"]*(")',lambda m:m.group(1)+'Winter am Spitzingsee: Skitouren, Schneeschuh- und Winterwanderungen, Rodeln, Skigebiet und Loipen – Tourdaten mit Quellen, geschrieben von der Oberen Firstalm.'+m.group(2),head,count=1)
open(F,'w',encoding='utf-8').write(head+'\n'.join(body)+tail)
print('ok', len(head+''.join(body)+tail))
