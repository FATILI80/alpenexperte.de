#!/usr/bin/env python3
"""Baut huetten.html neu: Hüttenführer im Gravel-Schema (Sprungmenü, Bildkarten, Filter, Quellen).
Alm-Restaurants, Hütten-Karte, Wanderwege und alle Hütten-Unterseiten gehen hier auf.
Nur belegte Angaben (bergwelten, hoehenrausch, muenchen.de, DAV-Sektionen, Tourismusportale);
Obere Firstalm und Lyra Alm: Angaben der Oberen Firstalm (Stand 11/2026).
"""
import re, html
F = 'huetten.html'
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:34px 0 8px;scroll-margin-top:140px;">{t}</h2>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'
TD = 'style="padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;"'
BW, HR, MU = 'https://www.bergwelten.com/h/', 'https://www.hoehenrausch.de/huetten/', 'https://www.muenchen.de/freizeit/berge-uebersicht/berghuetten/'
TAGTXT = {'e': '🍽️ Einkehr', 'u': '🛏 Übernachtung', 'w': '❄️ Winter offen', 's': '☀️ nur Sommer', 'b': '🚡 mit Bahn'}

def kv(rows):
    return ('<table style="width:100%;border-collapse:collapse;font-size:.9rem;margin:6px 0 8px;">'
            + ''.join(f'<tr><th style="text-align:left;padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#14532d;width:32%;vertical-align:top;">{E(k)}</th><td {TD}>{v}</td></tr>' for k, v in rows) + '</table>')

def tel(n, show):
    return f'<a href="tel:{n}">{show}</a>'

def karte(h):
    img = h.get('bild', 'huette-alm.jpg')
    sym = h.get('symbol', img in ('huette-alm.jpg', 'huette-berg.jpg', 'huette-berg2.jpg', 'haeuschen-alpen.jpg', 'kleines-sennerhaeuschen.jpg',
                                  'alm-weide.jpg', 'almwirtschaft.jpg', 'Grenze%20%C3%96sterreich.jpg', 'tegernsee-see.jpg', 'spitzingsee-see.jpg', 'Alm-Restaurants.jpg'))
    tags = h['tags']
    badge = ''.join(f'<span style="display:inline-block;font-size:.72rem;background:#e8f5e9;color:#14532d;border-radius:5px;padding:2px 6px;margin:0 4px 4px 0;">{TAGTXT[t]}</span>' for t in tags)
    q = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{E(n)}</a>' if u.startswith('http') else f'<a href="{u}">{E(n)}</a>' for n, u in h['q'])
    rand = '#c2410c' if h.get('top') else '#2e7d32'
    hinweis = f'<p style="margin:0 0 8px;font-size:.84rem;background:#fff7ed;border-left:3px solid #c2410c;padding:5px 8px;color:#7c2d12;">{h["hinweis"]}</p>' if h.get('hinweis') else ''
    return (f'<article id="{h["id"]}" data-tags="{" ".join(tags)}" class="hk" style="background:#fff;border:{"2px" if h.get("top") else "1px"} solid {rand};border-radius:12px;overflow:hidden;scroll-margin-top:140px;">'
            f'<div style="position:relative;"><img src="/images/{img}" alt="{E(h["name"]) + (" (Symbolbild)" if sym else "")}" loading="lazy" style="width:100%;height:150px;object-fit:cover;display:block;">'
            + ('<span style="position:absolute;right:6px;bottom:6px;background:rgba(0,0,0,.55);color:#fff;font-size:.68rem;padding:2px 6px;border-radius:4px;">Symbolbild</span>' if sym else '') + '</div>'
            f'<div style="padding:11px 13px;"><div style="font-size:.78rem;color:#1d4ed8;font-weight:700;">{E(h["kopf"])}</div>'
            f'<h3 style="margin:3px 0 5px;color:#14532d;font-size:1.04rem;">{E(h["name"])} <span style="font-weight:400;color:#4b5563;font-size:.9rem;">· {h["hoehe"]}</span></h3>'
            f'<div>{badge}</div>{hinweis}<p style="margin:0 0 8px;font-size:.9rem;line-height:1.45;color:#0f2942;">{h["text"]}</p>'
            '<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;cursor:pointer;"><summary style="color:#14532d;font-weight:600;font-size:.85rem;">🏠 Details &amp; Quellen</summary>'
            + kv(h['f']) + f'<p style="margin:4px 0 0;font-size:.76rem;color:#4b5563;">Quellen: {q}</p></details></div></article>')

GRID = '<div class="hgrid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:14px;">'

# ---------------- Daten ----------------
FIRSTALM = [
 dict(id='obere-firstalm', top=True, name='Obere Firstalm', hoehe='1.375 m', kopf='⭐ Unsere Alm · Berggasthof · Spitzingsee', bild='obere-firstalm-terrasse.jpg', tags='euwb',
      text='Der Berggasthof oberhalb des Spitzingsees, direkt an der beleuchteten 2,5-km-Rodelbahn. Bayerische Küche, Zimmer und Lager, im Winter Mondscheinrodeln bis 22:30 Uhr.',
      f=[('Geöffnet', 'täglich 11–22 Uhr, ab 22 Uhr Hüttenruhe; Küche 11–21 Uhr'), ('Frühstück', '8–10 Uhr, 17,50 € pro Person'),
         ('Übernachtung', '42 Betten in Zimmern, 30 Lagerplätze (bergwelten)'), ('Zustieg', 'ca. 40 min ab Spitzingsattel, 246 Hm (bergwelten)'),
         ('Winter', 'Rodelbahn bis 22:30 Uhr beleuchtet, Schlitten 7 €, Parken am Sattel 8 €/Tag'), ('Kontakt', tel('+4980267302', '08026 7302') + ' · info@firstalm.de')],
      q=[('Angaben der Oberen Firstalm, Stand 27.11.2026', '/content/winter/firstalm-rodelbahn.html'), ('bergwelten', BW + 'obere-firstalm')]),
 dict(id='lyra-alm', top=True, name='Lyra Alm Schirmbar', hoehe='Talstation Stümpflingbahn', kopf='⭐ Gehört zur Oberen Firstalm · nur im Winter', bild='Alm-Restaurants.jpg', tags='ew',
      text='Die Schirmbar am Lyralift direkt am Pistenende: Pizza, Flammkuchen, Leberkassemmel, Germknödel, Chili con carne und Après-Ski. Donnerstag und Freitag zum Nachtskilauf bis 23 Uhr.',
      f=[('Adresse', 'Lyraweg 6, 83727 Schliersee'), ('Geöffnet', 'nur in der Wintersaison; laut Google Sa–Mi 9–17, Do–Fr 9–23 Uhr'),
         ('Kontakt', tel('+4980263959390', '08026 3959390') + ' · info@firstalm.de')],
      q=[('Angaben der Oberen Firstalm', '/content/skigebiete/#lyra-alm')]),
]
SPITZING = [
 dict(id='untere-firstalm', name='Untere Firstalm', hoehe='1.318 m', kopf='Berggasthof · Firstgraben', bild='untere-firstalm.jpg', tags='ew',
      text='Wenige Minuten unterhalb der Oberen Firstalm im Firstgraben zwischen Brecherspitz, Bodenschneid und Suttenstein. Am schnellsten vom Parkplatz Kurvenlift.',
      f=[('Geöffnet', 'ganzjährig; laut hoehenrausch Mi–Mo 9–17 Uhr, Di Ruhetag'), ('Übernachtung', 'nein (komoot)'), ('Web', 'unterefirstalm.de')],
      q=[('hoehenrausch', HR + 'untere-firstalm/')]),
 dict(id='jagahuettn', name="Jagahütt'n am Stümpfling", hoehe='ca. 1.485 m', kopf='Berghütte · Bergstation Stümpflingbahn', bild='jagahuettn.jpg', tags='ewb',
      text='Die Hütte an der Bergstation der Stümpflingbahn – im Winter mitten im Skigebiet, im Sommer mit der Bahn oder zu Fuß erreichbar.',
      f=[('Lage', 'Bergstation Stümpflingbahn (Webcam-Standort 1.486 m, skiresort.info 1.484 m)'), ('Adresse', 'Am Stümpfling, 83727 Schliersee')],
      q=[('skiresort.info – Gastronomie', 'https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/test-result/gastronomy'), ('snow-online Webcam', 'https://www.snow-online.com/ski-resort/spitzingsee/webcam/mountain-hut-jagahuettn-.htm')]),
 dict(id='albert-link-huette', name='Albert-Link-Hütte', hoehe='1.053 m', kopf='DAV Sektion München · Kategorie II', bild='albert-link-huette.jpg', tags='euw',
      text='Familien-Stützpunkt auf der Valepper Alm südlich des Spitzingsees, knapp 20 Minuten ab der Kirche. Eigenes Brot, Mitglied bei „So schmecken die Berge“, Langlaufzentrum nebenan.',
      f=[('Geöffnet', 'ganzjährig, Montag Ruhetag (außer Feiertage); Betriebsferien beachten'), ('Übernachtung', 'Zimmer und Lager, 64–65 Plätze'),
         ('Zustieg', 'knapp 20 min ab Kirche Spitzingsee'), ('Hüttenruhe', '23 Uhr, striktes Rauchverbot'), ('Kontakt', tel('+4980267126 4'.replace(' ', ''), '08026 71264'))],
      q=[('Alpenverein München & Oberland', 'https://www.alpenverein-muenchen-oberland.de/huetten/alpenvereinshuetten/albert-link-huette'), ('muenchen.de', MU + 'spitzingsee')]),
 dict(id='blecksteinhaus', name='Blecksteinhaus', hoehe='1.022 m', kopf='DAV Sektion Männer-Turnverein München', bild='Blecksteinhausfrontansicht.jpg', tags='euw',
      text='An der Roten Valepp, rund 2 km bzw. 30 Minuten vom Spitzingsee. Großer Biergarten; entstand nach dem Föhnsturm 1919 als Teil der Waldbahn.',
      f=[('Geöffnet', 'Mi–Mo, Dienstag Ruhetag (muenchen.de)'), ('Übernachtung', '22 Betten, 22 Lagerplätze (bergwelten)'), ('Zustieg', 'ca. 30 min ab Parkplatz Kirche Spitzingsee'),
         ('Kontakt', tel('+498026712 04'.replace(' ', ''), '08026 71204'))],
      q=[('bergwelten', BW + 'blecksteinhaus'), ('hoehenrausch', HR + 'blecksteinhaus/'), ('muenchen.de', MU + 'spitzingsee')]),
 dict(id='rotwandhaus', name='Rotwandhaus', hoehe='1.737 m', kopf='DAV Sektion Turner-Alpenkränzchen · höchste Hütte der Gegend', bild='rotwandhaus.jpg', tags='euw',
      text='Unter dem Gipfel der Rotwand, von dort 30 Minuten zum Kreuz. Kürzester Zustieg über den Fahrweg ab der Alten Wurzhütte (2:30 h), bequemer mit der Taubensteinbahn.',
      f=[('Geöffnet', 'ganzjährig, im November/Dezember eingeschränkt'), ('Übernachtung', 'Zimmer und Matratzenlager'), ('Zustieg', '2:30 h ab Wurzhütte (654 Hm); ab Bergstation Taubensteinbahn ca. 1 h'),
         ('Kontakt', tel('+498026395988 0'.replace(' ', ''), '08026 3959880') + ' · rotwandhaus.de')],
      q=[('bergwelten', BW + 'rotwandhaus'), ('hoehenrausch', HR + 'rotwandhaus/'), ('muenchen.de', MU + 'spitzingsee')]),
 dict(id='taubensteinhaus', name='Taubensteinhaus', hoehe='1.567 m', kopf='DAV Sektion München · Kategorie II', bild='taubensteinhaus.jpg', tags='eub',
      text='Aussichtsloge zwischen Aiplspitz und Rotwand, 15 Minuten von der Bergstation der Taubensteinbahn. Stützpunkt für Taubenstein, Jägerkamp, Hochmiesing und Rotwand. 2022 von der Sektion Bergbund an die Sektion München übergegangen.',
      f=[('Geöffnet', 'Sommersaison ab Mitte Mai; 2026 bis 7. November'), ('Übernachtung', '15 Betten, 35 Lagerplätze (bergwelten)'), ('Zustieg', '15 min ab Bergstation; 1:30 h ab Spitzingsee'),
         ('Kontakt', tel('+491712255033', '0171 2255033') + ' · info@taubensteinhaus.de')],
      q=[('Alpenverein München & Oberland', 'https://www.alpenverein-muenchen-oberland.de/taubensteinhaus'), ('bergwelten', BW + 'taubensteinhaus'),
         ('Saisonende 2026', 'https://www.alpenverein-muenchen-oberland.de/presse/medieninfos-2026/2026-09-10-saisonende-auf-den-huetten-des-alpenvereins-muenchen-oberland')]),
 dict(id='schoenfeldhuette', name='Schönfeldhütte', hoehe='1.410 m', kopf='DAV Sektion München · Kategorie II', bild='schoenfeldhuette.jpg', tags='eu',
      text='„Basislager“ am Fuß des Jägerkamps, gut eine Stunde vom Spitzingsattel. Erste Nacht der Drei-Seen-Tour, ideal für Familien mit älteren Kindern.',
      f=[('Geöffnet', 'Mai bis Anfang November; 2026 bis 7. November'), ('Übernachtung', '26 Betten, 10 Lager'), ('Zustieg', 'ca. 1 h ab Spitzingsattel; im Sommer auch über die Taubensteinbahn'),
         ('Hinweis', 'kein Handyempfang, kein WLAN'), ('Kontakt', tel('+4980267496', '08026 7496'))],
      q=[('Alpenverein München & Oberland', 'https://www.alpenverein-muenchen-oberland.de/huetten/alpenvereinshuetten/schoenfeldhuette'), ('tourentipp.com', 'https://www.tourentipp.com/portal/huetten/11/pdf/get')]),
 dict(id='bodenschneidhaus', name='Bodenschneidhaus', hoehe='1.365 m', kopf='DAV Sektion Bodenschneid · Rettenbeck-Alm', bild='huette-berg.jpg', tags='euw',
      text='Auf der Rettenbeck-Alm zwischen Tegernsee und Spitzingsee unter der Bodenschneid. Ganzjährig offen, im Winter Ziel für Schneeschuh- und Skitourengeher. Von der Oberen Firstalm in rund 45 Minuten.',
      f=[('Geöffnet', 'ganzjährig'), ('Übernachtung', '17 Betten, 31 Lagerplätze'), ('Zustieg', '1,5 h ab Fischhausen-Neuhaus oder Hennerer, ca. 3 h ab Spitzingsee'),
         ('Kontakt', tel('+491723735798', '0172 3735798'))],
      q=[('bergwelten', BW + 'bodenschneidhaus'), ('muenchen.de', MU + 'spitzingsee')]),
 dict(id='obere-maxlraineralm', name='Obere Maxlraineralm', hoehe='1.520 m', kopf='Privat · am Taubenstein', bild='huette-alm.jpg', tags='euwb',
      text='Sonniger Wiesenboden unter dem Taubenstein, privat geführt. Im Sommer 10 Minuten von der Taubensteinbahn, sonst 1¼ h ab der Alten Wurzhütte.',
      f=[('Geöffnet', 'ganzjährig, eventuell Betriebsferien'), ('Übernachtung', '44 Plätze im Bettenlager (hoehenrausch)'), ('Zustieg', 'ca. 1:15 h ab Alter Wurzhütte über den Schwarzenkopfweg, 435 Hm')],
      q=[('muenchen.de', MU + 'spitzingsee'), ('hoehenrausch', HR + 'obere-maxlraineralm/')]),
 dict(id='dav-haus-spitzingsee', name='DAV-Haus Spitzingsee', hoehe='1.124 m', kopf='Selbstversorgerhaus · Alpenverein München & Oberland', bild='spitzingsee-see.jpg', tags='uw',
      text='Leicht erhöht über dem Nordende des Sees, für Gruppen, Familien und Schulklassen. Selbstversorgung; Essen auf Wunsch von der Albert-Link-Hütte.',
      f=[('Geöffnet', 'ganzjährig; Hüttenruhe 8.11.–13.12.2026'), ('Übernachtung', 'Mehrbett-, Doppel- und Familienzimmer'), ('Kontakt', tel('+4980269209349', '08026 9209349'))],
      q=[('Alpenverein München & Oberland', 'https://www.alpenverein-muenchen-oberland.de/selbstversorgerhuetten/haus-spitzingsee'), ('bergwelten', BW + 'dav-haus-spitzingsee')]),
 dict(id='wurzhuette', name='Alte Wurzhütte', hoehe='ca. 1.100 m', kopf='Gasthof · Südufer Spitzingsee', bild='spitzingsee-see.jpg', tags='euw',
      text='Der historische Gasthof am Südufer, 1720 errichtet und früher Enzianbrennerei – Ausgangspunkt für Rotwand, Maxlraineralm und die Valepp.',
      f=[('Adresse', 'Roßkopfweg 1, 83727 Spitzingsee'), ('Übernachtung', 'Hotelzimmer')],
      q=[('Marriott – Geschichte Spitzingsee', 'https://www.marriott.com/hotels/travel/mucsb/'), ('speisekarte.de', 'https://www.speisekarte.de/schliersee/restaurant/alte_wurzhuette/bewertung')]),
 dict(id='forsthaus-valepp', name='Forsthaus Valepp', hoehe='ca. 880 m', kopf='Gasthaus · Valepp, nahe der Tiroler Grenze', bild='forsthaus-valepp.jpg', tags='eu',
      text='Das Forsthaus von 1841 zwischen Spitzingsee und Tiroler Grenze, nach Jahren Leerstand renoviert und seit August 2024 wieder offen. Beliebt bei Radlern im Valepptal.',
      f=[('Adresse', 'Valepp 1, 83727 Schliersee'), ('Geöffnet', 'laut Schlemmer Atlas täglich 11–19 Uhr'), ('Übernachtung', 'möglich'), ('Zustieg', 'ca. 1½–2 h ab Albert-Link-Hütte'),
         ('Kontakt', tel('+4980267809580', '08026 7809580'))],
      q=[('Schlemmer Atlas', 'https://www.schlemmer-atlas.de/restaurants/deutschland/schliersee/forsthaus-valepp/'), ('komoot (Wiedereröffnung 2024)', 'https://www.komoot.com/highlight/820029')]),
]
SCHLIERSEE = [
 dict(id='schliersbergalm', name='Schliersbergalm', hoehe='1.061 m', kopf='Alpenhotel · Schliersee', bild='Schliersbergalmausblickschliersee.jpg', tags='euwb',
      text='Direkt über dem Schliersee, mit der Schliersbergbahn in rund 2 Minuten oder zu Fuß in unter einer Stunde ab Bahnhof. Sommerrodelbahn (rund 1 km), Spielplatz und Freibad.',
      f=[('Adresse', 'Schliersberg 1, 83727 Schliersee'), ('Übernachtung', 'Hotelzimmer'), ('Bahn', 'täglich 8:30–22 Uhr, für Hotelgäste frei')],
      q=[('motorradundreisen.de', 'https://www.motorradundreisen.de/motorradhotel/oberbayern-tegernsee-schliersee/5946_schliersberg-alm.html'), ('hotel.info', 'https://www.hotel.info/en/hotel/143453'), ('coaster.cloud – Sommerrodelbahn', 'https://coaster.cloud/en/attractions/4787a2f1-sommerrodelbahn')]),
 dict(id='gindelalm', name='Gindelalm', hoehe='1.242 m', kopf='Drei bewirtschaftete Hütten · zwischen Schliersee und Tegernsee', bild='alm-weide.jpg', tags='eus',
      text='Am Sattel zwischen Gindelalmschneid und Auerberg stehen drei Hütten, alle bewirtschaftet. Am Prinzenweg vom Schliersee zum Tegernsee; Kreuzbergalm und Neureuth in der Nähe.',
      f=[('Übernachtung', 'größte Hütte: 19 Betten, 15 Lagerplätze (bergwelten)'), ('Zustieg', 'ca. 1:30 h ab Hausham oder Schliersee (Hennererstraße)'), ('Kontakt', tel('+491739439384', '0173 9439384') + ' · gindelalm.de')],
      q=[('bergwelten', BW + 'gindelalm'), ('hoehenrausch', HR + 'gindelalm/')]),
 dict(id='kreuzbergalm', name='Kreuzbergalm', hoehe='1.223 m', kopf='Alm · zwischen Schliersee und Tegernsee', bild='almwirtschaft.jpg', tags='es',
      text='Freistehende Alm mit Rundumblick. Zur Weidesaison Brotzeiten, kleine Gerichte und hausgemachte Kuchen; am schnellsten ab dem Hennerer.',
      f=[('Zustieg', 'ca. 1:30 h ab Parkplatz Café Hennerer über den Prinzenweg')],
      q=[('bergwelten', BW + 'kreuzbergalm'), ('hoehenrausch', HR + 'kreuzbergalm')]),
 dict(id='freudenreichalm', name='Freudenreichalm', hoehe='ca. 1.300 m', kopf='Alm · unter der Bodenschneid', bild='Freudenreich%20Alm.jpg', tags='es',
      text='Bewirtschaftete Alm mit Blick auf die Bodenschneid, beliebt bei Mountainbikern. Über den Freudenreichsattel (Schiebe- und Tragestück) geht es hinüber zur Oberen Firstalm.',
      f=[('Zustieg', 'aus Richtung Fischhausen-Neuhaus/Josefsthal, Teil der Bodenschneid-Runden')],
      q=[('komoot', 'https://www.komoot.com/highlight/997075')]),
 dict(id='ankelalm', name='Ankelalm', hoehe='1.311 m', kopf='Brotzeitalm · am Brecherspitz', bild='Ankelalm.jpg', tags='es',
      text='Kleine Alm im Kessel unter dem Brecherspitz, 2019 neu aufgebaut. Brotzeiten, Kuchen, Käse und Milch von der Alm – gute Rast vor dem Gipfel.',
      f=[('Geöffnet', 'Almsaison Anfang Juni bis Ende September; laut hoehenrausch Mo–Do 9–21, Fr 9–18 Uhr, Sa/So Ruhetag'), ('Zustieg', 'ca. 1:30 h ab Neuhaus; ab Oberer Firstalm über den Brecherspitz ca. 2 h')],
      q=[('hoehenrausch', HR + 'ankelalm'), ('servus-schliersee', 'https://servus-schliersee.de/?p=6657')]),
 dict(id='almbad-huberspitz', name='Almbad Huberspitz', hoehe='1.050 m', kopf='Berggasthaus · über Hausham', bild='huette-berg2.jpg', tags='e',
      text='Über dem Schliersee mit Blick bis zum Wendelstein, barrierearm zertifiziert.',
      f=[('Adresse', 'Huberspitzweg 1, 83734 Hausham'), ('Kontakt', tel('+498026929676 0'.replace(' ', ''), '08026 9296760') + ' · almbad.de')],
      q=[('Bayern Tourismus – Reisen für Alle', 'https://bavaria.travel/accessible-holidays/almbad-huberspitz/')]),
]
BAYRISCHZELL = [
 dict(id='wendelsteinhaus', name='Wendelsteinhaus', hoehe='1.724 m', kopf='Berggasthaus · an Zahnrad- und Seilbahn', bild='huette-berg.jpg', tags='ewb',
      text='Rund 100 m unter dem Gipfel, 1882/83 erbaut, direkt an beiden Bergstationen. Die höchste Einkehr der Region; übernachten ist aus Brandschutzgründen nicht mehr möglich.',
      f=[('Geöffnet', 'gekoppelt an die Bahnbetriebszeiten (wendelsteinbahn.de)'), ('Übernachtung', 'nein')],
      q=[('muenchen.de', MU + 'berghuetten-am-wendelstein')]),
 dict(id='mitteralm', name='Mitteralm', hoehe='1.200 m', kopf='DAV Sektion Bergbund Rosenheim · Wendelstein', bild='huette-alm.jpg', tags='euwb',
      text='Zwischen Brannenburg und Wendelsteingipfel, mit eigener Bedarfshaltestelle der Zahnradbahn. Die einzige Wendelstein-Hütte mit Übernachtung.',
      f=[('Geöffnet', 'ganzjährig; Mo/Di Ruhetag, So ab 17 Uhr geschlossen'), ('Übernachtung', 'bis 55 Plätze in Zimmern und Lagern'), ('Zustieg', 'ca. 1:30 h ab Brannenburg-St. Margarethen'),
         ('Kontakt', tel('+4980342760', '08034 2760'))],
      q=[('muenchen.de', MU + 'berghuetten-am-wendelstein'), ('bergwelten', BW + 'mitteralm')]),
 dict(id='wendelsteinalm', name='Wendelsteinalm', hoehe='ca. 1.420 m', kopf='Alm · privat', bild='alm-weide.jpg', tags='es',
      text='1923 erbaut, nur zur Almsaison bewirtschaftet; am kürzesten vom Sudelfeldpass.',
      f=[('Übernachtung', 'nein')], q=[('muenchen.de', MU + 'berghuetten-am-wendelstein')]),
 dict(id='walleralm', name='Walleralm', hoehe='1.412 m', kopf='Berggasthof · Oberes Sudelfeld', bild='huette-alm.jpg', tags='ew',
      text='Mitten im Wander- und Skigebiet Sudelfeld, ganzjährig offen; Ausgangspunkt für Kleinen und Großen Traithen.',
      f=[('Adresse', 'Oberes Sudelfeld 1, 83735 Bayrischzell'), ('Kontakt', tel('+498023722', '08023 722') + ' · walleralm.de')],
      q=[('Bayern Tourismus – Reisen für Alle', 'https://bavaria.travel/accessible-holidays/berggasthof-walleralm-restaurant/'), ('bergtour-online', 'https://www.bergtour-online.de/beschreibungen/wanderungen-bayrischzell/huettenwanderungen/')]),
 dict(id='kesselalm', name='Kesselalm', hoehe='1.285 m', kopf='Alm · am Breitenstein (Fischbachau)', bild='almwirtschaft.jpg', tags='euw',
      text='Fast ganzjährig offen; im Winter ist der Fahrweg von Birkenstein die Rodelbahn (rund 3 km, teils steil und vereist). Ruhetage vorher prüfen.',
      f=[('Übernachtung', 'nach Voranmeldung im Schlaflager'), ('Zustieg', 'ab Birkenstein, ca. 433 Hm')],
      q=[('hoehenrausch', HR + 'kesselalm/'), ('bergwelten – Rodeltour', 'https://www.bergwelten.com/t/r/9171')]),
]
TEGERNSEE = [
 dict(id='neureuth', name='Berggasthof Neureuth', hoehe='1.264 m', kopf='Berggasthof · Hausberg von Tegernsee', bild='tegernsee-see.jpg', tags='euw',
      text='Riesige Sonnenterrasse mit Blick über den ganzen Tegernsee; viele Aufstiege, auch für Kinder. Im Winter Rodeln.',
      f=[('Geöffnet', 'ganzjährig; Sommer Mo Ruhetag, Winter Mo/Di Ruhetag; Betriebsurlaub im Spätherbst'), ('Übernachtung', 'Bettenlager'), ('Zustieg', '1 h ab Parkplatz Neureuth, 1:30 h ab Bahnhof Tegernsee')],
      q=[('muenchen.de', MU + 'tegernsee'), ('hoehenrausch', HR + 'berggasthof-neureuth')]),
 dict(id='riederstein', name='Berggasthaus Riederstein am Galaun', hoehe='1.060 m', kopf='Berggasthaus · unter der Riederstein-Kapelle', bild='huette-berg2.jpg', tags='euw',
      text='Sonnenterrasse über dem Tegernsee, 30 Minuten unter der Kapelle auf dem Riederstein. Im Winter Rodelbahn ins Tal.',
      f=[('Geöffnet', 'fast ganzjährig, Ruhetage laut Homepage'), ('Übernachtung', 'möglich'), ('Zustieg', 'ca. 1 h ab Tegernsee, 45 min ab Rottach-Egern'), ('Kontakt', tel('+498022273022', '08022 273022'))],
      q=[('hoehenrausch', HR + 'riedersteinhaus-am-galaun/'), ('tourentipp.com', 'https://tourentipp.com/portal/huetten/35/pdf/get')]),
 dict(id='aueralm', name='Aueralm', hoehe='1.266 m', kopf='Alm · über Bad Wiessee', bild='alm-weide.jpg', tags='ew',
      text='Eine der bekanntesten Almen am Tegernsee, ganzjährig bewirtschaftet; im Winter Rodeln ins Söllbachtal.',
      f=[('Geöffnet', 'ganzjährig, Montag Ruhetag; Betriebsurlaub im Spätherbst'), ('Übernachtung', 'nein'), ('Zustieg', 'ca. 1:30 h ab Bad Wiessee (Parkplatz Sonnenbichl)'),
         ('Kontakt', tel('+49802283600', '08022 83600') + ' · aueralm.de')],
      q=[('muenchen.de', MU + 'tegernsee'), ('bergwelten', BW + 'aueralm')]),
 dict(id='hirschberghaus', name='Hirschberghaus', hoehe='1.511 m', kopf='Privat · unter dem Hirschberg', bild='huette-berg.jpg', tags='',
      hinweis='Derzeit geschlossen – Pächtersuche (hoehenrausch, komoot 07/2025).',
      text='Klassiker am Tegernsee unterhalb des Hirschberg-Gipfels, Aufstieg meist ab Scharling (ca. 2,5 h).',
      f=[('Status', 'geschlossen, Wiedereröffnung offen')], q=[('hoehenrausch', HR + 'hirschberghaus/'), ('komoot', 'https://www.komoot.com/ja-jp/highlight/114857')]),
 dict(id='altes-wallberghaus', name='Altes Wallberghaus', hoehe='1.512 m', kopf='Berghotel · Wallberg', bild='huette-berg2.jpg', tags='eub',
      text='Seit 1899 zwischen Wallberg und Setzberg; mit der Wallbergbahn oder in ca. 2 h zu Fuß.',
      f=[('Geöffnet', 'Mo/Di Ruhetag; geschlossen während der Bahn-Revision (April, Mitte Nov.–Anf. Dez.)'), ('Übernachtung', 'Zimmer (muenchen.de)'), ('Kontakt', tel('+498022278523', '08022 278523'))],
      q=[('muenchen.de', MU + 'tegernsee'), ('bergwelten', BW + 'wallberghaus')]),
 dict(id='wallbergmoosalm', name='Wallbergmoosalm', hoehe='1.117 m', kopf='Berggasthaus · Wallberg', bild='huette-alm.jpg', tags='ew',
      text='An der Wallberg-Rodelbahn, eine der längsten Naturrodelbahnen Deutschlands (6,5 km).',
      f=[], q=[('Der Tegernsee', 'https://www.tegernsee.com/en/a-wallbergmoos-alm')]),
 dict(id='moni-alm', name='Moni-Alm', hoehe='987 m', kopf='Berggasthof · Sutten (Rottach-Egern)', bild='huette-alm.jpg', tags='ew',
      text='Traditioneller Berggasthof mit großer Sonnenterrasse in der Sutten, zwischen Tegernsee und Spitzingsee. Spezialitäten: Linsensuppe, Spinatknödel, Kaiserschmarrn. Von hier ist die Obere Firstalm zu Fuß in rund einer Stunde erreichbar.',
      f=[('Geöffnet', 'ganzjährig täglich ab 9 Uhr (servus-tegernsee)'), ('Adresse', 'Sutten 42, 83700 Rottach-Egern'), ('Anfahrt', 'Mautstraße Enterrottach; RVO-Bus 9560 bis „Parkplatz Moni-Alm“'),
         ('Kontakt', tel('+498022664154', '08022 664154') + ' · moni-alm.de')],
      q=[('servus-tegernsee', 'https://servus-tegernsee.de/en/eating-out/moni-alm-2/'), ('Tegernsee-Flyer „Sutten – Natur pur“', 'https://www.tegernsee.com/flyer-sutten-natur-pur-1'), ('bergwelten – Winterwanderung', 'https://www.bergwelten.com/t/ww/7552')]),
 dict(id='lukas-alm', name='Lukas-Alm', hoehe='ca. 1.100 m', kopf='Alm · Sutten (Rottach-Egern)', bild='alm-weide.jpg', tags='eu',
      text='Gemütliche Alm oberhalb der Sutten mit Blick zu Wallberg und Risserkogel; Übernachtung möglich. Vom Parkplatz Moni-Alm steil auf Asphalt hinauf, Radler nehmen besser die Schotterauffahrt.',
      f=[('Ruhetage', 'Montag und Dienstag (komoot)'), ('Zustieg', 'ca. 1:15 h ab Mautstation Enterrottach bzw. kurz ab Parkplatz Moni-Alm'), ('Web', 'lukas-alm.de')],
      q=[('komoot', 'https://www.komoot.com/highlight/159373'), ('bergtour-online', 'https://www.bergtour-online.de/bergtouren/bergwanderungen/leicht/lukas-alm/')]),
 dict(id='schwaigeralm', name='Schwaigeralm', hoehe='Kreuth', kopf='Alm · Kreuth', bild='almwirtschaft.jpg', tags='e',
      text='Bayerische Almhütte, nur rund 10 Minuten vom Wanderparkplatz in Kreuth – gut mit einer Tour in die umliegenden Berge oder durchs Langenautal Richtung Valepp zu verbinden.',
      f=[], q=[('Der Tegernsee', 'https://www.tegernsee.com/en/a-schwaigeralm')]),
 dict(id='buchsteinhuette', name='Buchsteinhütte', hoehe='1.260 m', kopf='Hüttenverein Buchstein · unter Roß- und Buchstein', bild='huette-berg.jpg', tags='euw',
      text='Ganzjährig bewirtschaftet, gehört dem Hüttenverein Buchstein (kein DAV). Im Winter Rodeln zur Winterstube; im Sommer Zwischenstation zur Tegernseer Hütte.',
      f=[('Geöffnet', 'ganzjährig; Sommer Mo, Winter Mo/Di Ruhetag'), ('Übernachtung', 'Bettenlager'), ('Zustieg', 'ca. 1:45 h ab Parkplatz Winterstube')],
      q=[('muenchen.de', MU + 'tegernsee'), ('hoehenrausch', HR + 'buchsteinhuette/')]),
 dict(id='tegernseer-huette', name='Tegernseer Hütte', hoehe='1.650 m', kopf='DAV Sektion Tegernsee · zwischen Roß- und Buchstein', bild='tegernseer-huette.jpg', tags='eus',
      text='Spektakulär in der Scharte zwischen Roßstein und Buchstein. Trittsicherheit nötig; kürzester Weg ab Bayerwald über die Sonnbergalm.',
      f=[('Geöffnet', 'zweites Mai-Wochenende bis erstes November-Wochenende'), ('Übernachtung', 'Matratzenlager, rund 38–40 Plätze'), ('Zustieg', 'ca. 2:15 h ab Bayerwald; ca. 800 Hm ab Klamm'),
         ('Kontakt', tel('+491754115813', '0175 4115813'))],
      q=[('muenchen.de', MU + 'tegernsee'), ('hoehenrausch', HR + 'tegernseer-huette/'), ('bergwelten', 'https://www.bergwelten.com/a/tegernseer-huette')]),
 dict(id='siebenhuetten', name='Siebenhütten', hoehe='ca. 840 m', kopf='Jausenstation · Wildbad Kreuth', bild='alm-weide.jpg', tags='es',
      text='Von einst sieben Hütten stehen noch vier; heute beliebte Jausenstation, 35–45 Minuten ab Wildbad Kreuth – ideal mit Kindern.',
      f=[('Geöffnet', 'je nach Schnee ab Ostern oder Mai bis Ende Oktober, ohne Ruhetag'), ('Übernachtung', 'nein'), ('Kontakt', tel('+4980299975983', '08029 9975983'))],
      q=[('hoehenrausch', HR + 'siebenhuettenalm')]),
 dict(id='koenigsalm', name='Königsalm', hoehe='1.114 m', kopf='Alm · Kreuth', bild='almwirtschaft.jpg', tags='es',
      text='Mit 46 m langer Almhütte und dem Kavaliershaus von König Max I. Joseph. In der Weidezeit bewirtschaftet, hausgemachter Kuchen.',
      f=[('Geöffnet', 'Mitte Juni bis Ende der Weidezeit'), ('Zustieg', 'ab Parkplatz Siebenhütten oder Klamm')],
      q=[('Alpenverein München & Oberland – Tourenblatt', 'https://www.alpenverein-muenchen-oberland.de/uploads/images/AAXvRfWUuc01cpRmtKvPYw/koenigsalm.pdf'), ('bergwelten', 'https://www.bergwelten.com/t/w/17443')]),
]
LENGGRIES = [
 dict(id='lenggrieser-huette', name='Lenggrieser Hütte', hoehe='1.338 m', kopf='DAV Sektion Lenggries · am Seekarkreuz', bild='huette-berg2.jpg', tags='euw',
      text='Hoch über Lenggries am Fuß des Seekarkreuzes, ganzjährig bewirtschaftet; donnerstags Radl-Stammtisch.',
      f=[('Geöffnet', 'ganzjährig; Ruhetag laut Sektion Dienstag'), ('Übernachtung', '52 Lagerplätze, Winterraum 7'), ('Zustieg', '1:30 h ab Lenggries über den Grasleitensteig'),
         ('Kontakt', tel('+491714849349', '0171 4849349'))],
      q=[('bergwelten', BW + 'lenggrieser-huette'), ('DAV-Flyer', 'https://magazin.alpenverein.de/files/broschueren/2201-lenggrieser-huette-flyer_ol_30217.pdf')]),
 dict(id='brauneck-gipfelhaus', name='Brauneck-Gipfelhaus', hoehe='1.540 m', kopf='DAV Alpiner Ski-Club München · Brauneck', bild='huette-berg.jpg', tags='euwb',
      text='Mit großer Panoramaterrasse über Lenggries, im Winter mitten im Skigebiet Brauneck.',
      f=[('Übernachtung', '38 Betten, 42 Lagerplätze'), ('Kontakt', tel('+4980428786', '08042 8786'))], q=[('bergwelten', BW + 'brauneck-gipfelhaus')]),
]
TIROL = [
 dict(id='blaubergalm', name='Blaubergalm', hoehe='1.540 m', kopf='🇦🇹 Alm · Südseite der Blauberge (Achenkirch)', bild='Grenze%20%C3%96sterreich.jpg', tags='eus',
      text='Kleine Alm knapp hinter der Grenze; Bio-Käse und Speck aus eigener Herstellung. Aufstieg von Wildbad Kreuth durch die Wolfsschlucht (Trittsicherheit, Schwindelfreiheit).',
      f=[('Geöffnet', 'Ende Mai bis Anfang Oktober'), ('Übernachtung', 'nach Reservierung'), ('Zustieg', 'ca. 2:30 h ab Wildbad Kreuth, 760 Hm'), ('Kontakt', tel('+436642306719', '+43 664 2306719'))],
      q=[('hoehenrausch', HR + 'blaubergalm/'), ('Alpenverein München & Oberland – Tourenblatt', 'https://www.alpenverein-muenchen-oberland.de/uploads/images/tcS7233ibeQMmade4jtI0A/blaubergalm.pdf')]),
 dict(id='erzherzog-johann-klause', name='Erzherzog-Johann-Klause', hoehe='814 m', kopf='🇦🇹 Jausenstation · Brandenberger Ache', bild='Grenze%20%C3%96sterreich.jpg', tags='s',
      hinweis='Status widersprüchlich: Achensee-Tourismus meldet „geschlossen“, Alpbachtal „wieder geöffnet“ – unbedingt vorher prüfen.',
      text='Die historische Triftklause an der Brandenberger Ache, über die Valepp mit Rad oder zu Fuß erreichbar; im Winter geschlossen.',
      f=[('Zustieg', 'aus der Valepp bzw. von Brandenberg (Kaiserhaus) ca. 7,5 km')],
      q=[('hoehenrausch', HR + 'erzherzog-johann-klause/'), ('Alpbachtal', 'https://www.alpbachtal.at/en/summer/hiking/huts/erzherzog-johann-klause_az_9110'), ('Achensee', 'https://www.achensee.com/en/map-detail/jausenstation-erzherzog-johann-klause-122258381/')]),
 dict(id='gufferthuette', name='Gufferthütte', hoehe='1.475 m', kopf='🇦🇹 DAV Sektion Mühldorf · Brandenberger Alpen', bild='Grenze%20%C3%96sterreich.jpg', tags='eus',
      text='Auf Almwiesen zwischen Blaubergen und Rofan, Umweltgütesiegel und „So schmecken die Berge“. Seit 2014 bzw. 2024 bei der Sektion Mühldorf.',
      f=[('Geöffnet', 'Mitte Mai bis Ende Oktober'), ('Übernachtung', 'Zimmer und Lager (rund 57–64 Plätze), Winterraum 6'), ('Zustieg', 'ab Steinberg am Rofan bzw. Köglboden nördlich des Achensees, ca. 2:30 h')],
      q=[('hoehenrausch', HR + 'gufferthuette/'), ('Tirol Werbung', 'https://www.tirol.at/reisefuehrer/sport/wandern/alpenvereinshuetten/a-gufferthuette')]),
 dict(id='erfurter-huette', name='Erfurter Hütte', hoehe='1.834 m', kopf='🇦🇹 DAV Sektion Ettlingen · Rofan', bild='Grenze%20%C3%96sterreich.jpg', tags='euwb',
      text='Direkt an der Bergstation der Rofanseilbahn auf dem Mauritzköpfl, mit Blick auf Achensee und Karwendel. Stützpunkt am Adlerweg.',
      f=[('Geöffnet', 'Sommer und Winter (Zeiten auf der Hütten-Website)'), ('Übernachtung', '26 Betten, 58 Lager (Tirol Werbung)'), ('Zustieg', 'Rofanseilbahn ab Maurach oder ca. 2:15 h zu Fuß'),
         ('Kontakt', tel('+4352435517', '+43 5243 5517'))],
      q=[('Tirol Werbung', 'https://www.tirol.at/aktivitaeten/sport/wandern/av-huetten/alle-huetten/erfurter-huette'), ('hoehenrausch', HR + 'erfurter-huette/')]),
 dict(id='dalfazalm', name='Dalfazalm', hoehe='1.693 m', kopf='🇦🇹 Alm · Rofan über dem Achensee', bild='Grenze%20%C3%96sterreich.jpg', tags='eus',
      text='Urige Alm mit Kühen, Schafen und Achensee-Blick, seit vier Generationen von Familie Moser bewirtschaftet. Rund 45 Minuten von der Rofanseilbahn.',
      f=[('Geöffnet', 'Mitte Mai bis Anfang November'), ('Übernachtung', 'ja (Lager und Betten)'), ('Kontakt', tel('+436649159807', '+43 664 9159807'))],
      q=[('bergwelten', BW + 'dalfaz-alm'), ('hoehenrausch', HR + 'dalfazalm/')]),
 dict(id='berggasthof-rofan', name='Berggasthof Rofan', hoehe='1.840 m', kopf='🇦🇹 Berggasthof · Bergstation Rofanseilbahn', bild='Grenze%20%C3%96sterreich.jpg', tags='eb',
      text='Familie Hollaus, große Terrasse direkt an der Bergstation; Tiroler Küche, Wildspezialitäten.',
      f=[], q=[('Achensee Tourismus', 'https://www.achensee.com/en/map-detail/berggasthof-rofan-1'), ('Tirol Werbung', 'https://www.tirol.at/aktivitaeten/kulinarik/gastronomie/berggasthof-rofan')]),
 dict(id='bayreuther-huette', name='Bayreuther Hütte', hoehe='1.576 m', kopf='🇦🇹 DAV Sektion Bayreuth · Rofan-Südseite', bild='Grenze%20%C3%96sterreich.jpg', tags='eus',
      text='Sonnige Aussichtslage über Inntal, Alpbachtal und Zillertal; familiengeeignet, kein Absturzgelände direkt an der Hütte.',
      f=[('Geöffnet', 'Mai bis Oktober (2026 bis 10. Oktober)'), ('Übernachtung', '24 Betten, 28 Lager'), ('Zustieg', 'ca. 3 h ab Kramsach, 2,5 h ab Münster'), ('Kontakt', tel('+436643425103', '+43 664 3425103'))],
      q=[('bergwelten', 'https://www.bergwelten.com/huetten/bayreuther-huette'), ('Achensee', 'https://www.achensee.com/en/map-detail/bayreuther-huette-122210954/')]),
 dict(id='ruebezahl-alm', name='Rübezahl-Alm', hoehe='1.172 m', kopf='🇦🇹 Alm · Ellmau am Wilden Kaiser', bild='Grenze%20%C3%96sterreich.jpg', tags='ew',
      text='1778 als Kuhstall erbaut, Blick auf den Wilden Kaiser, an der Hartkaiser-Abfahrt; Schnitzfiguren-Wanderweg.',
      f=[('Geöffnet', 'Sommer und Winter, Zeiten laut SkiWelt/TVB'), ('Übernachtung', 'nein'), ('Kontakt', tel('+4353582646', '+43 5358 2646'))],
      q=[('bergwelten', BW + 'ruebezahlalm'), ('SkiWelt', 'https://skiwelt.at/cz/info/ruebezahl-alm')]),
]
WEITERE = [
 dict(id='priener-huette', name='Priener Hütte', hoehe='1.410 m', kopf='DAV Sektion Prien · Geigelstein (Chiemgau)', bild='huette-berg.jpg', tags='euw',
      text='Im Naturschutzgebiet Geigelstein, fast ganzjährig offen; Station der Chiemgau-Tour.',
      f=[('Übernachtung', '36 Betten, 35 Lager; Hüttenschlafsack Pflicht'), ('Kontakt', tel('+498057428', '08057 428'))], q=[('bergwelten', BW + 'priener-huette'), ('hoehenrausch', HR + 'priener-huette/')]),
 dict(id='hochrieshuette', name='Hochrieshütte', hoehe='1.569 m', kopf='DAV Sektion Rosenheim · Hochries (Chiemgau)', bild='huette-berg2.jpg', tags='euwb',
      text='Auf dem Gipfel der Hochries, ganzjährig bewirtschaftet; Hochriesbahn von Ende März bis Anfang November.',
      f=[('Übernachtung', 'rund 35–37 Betten'), ('Kontakt', tel('+4980328210', '08032 8210'))], q=[('hoehenrausch', HR + 'hochrieshuette/'), ('bergwelten', BW + 'hochrieshuette')]),
 dict(id='tutzinger-huette', name='Tutzinger Hütte', hoehe='1.327 m', kopf='DAV · Benediktenwand', bild='huette-alm.jpg', tags='euw',
      text='Moderner Neubau von 2000 unter der Benediktenwand-Nordwand, Steinböcke in den Felsen darüber.',
      f=[('Geöffnet', 'je nach Schnee Mitte/Ende April bis Anfang November, dazu Weihnachten/Dreikönig und Ostern'), ('Zustieg', 'ca. 2:30 h ab Benediktbeuern (Gschwend)')],
      q=[('planetoutdoor', 'https://planetoutdoor.de/wissen/auf-huettentour/die-schoensten-berghuetten-im-fruehling'), ('bergwelten', 'https://www.bergwelten.com/a/8-huetten-in-den-bayerischen-voralpen-und-chiemgauer-alpen')]),
]
SEKTIONEN = [('firstalm', '⭐ Unsere Alm', FIRSTALM), ('spitzingsee', '🏔️ Spitzingsee & Valepp', SPITZING), ('schliersee', '🌊 Schliersee & Hausham', SCHLIERSEE),
             ('bayrischzell', '⛰️ Wendelstein & Sudelfeld', BAYRISCHZELL), ('tegernsee', '🏞️ Tegernsee & Kreuth', TEGERNSEE), ('lenggries', '🌲 Lenggries & Isarwinkel', LENGGRIES),
             ('tirol', '🇦🇹 Grenzgänger Tirol', TIROL), ('weitere', '🧭 Weiter weg', WEITERE)]
INTRO = {'firstalm': 'Unsere Alm über dem Spitzingsee – und die Schirmbar am Pistenende, die dazugehört.',
         'spitzingsee': 'Alles, was rund um den Spitzingsee und hinunter in die Valepp einkehren lässt.',
         'schliersee': 'Almen und Berggasthäuser zwischen Schliersee, Hausham und dem Brecherspitz.',
         'bayrischzell': 'Rund um Wendelstein und Sudelfeld.',
         'tegernsee': 'Von der Neureuth über die Sutten bis zu den Kreuther Almen.',
         'lenggries': 'Über Lenggries und am Brauneck.',
         'tirol': 'Knapp hinter der Grenze: über Valepp und Blauberge oder mit der Rofanseilbahn erreichbar.',
         'weitere': 'Beliebte Ziele außerhalb des Mangfallgebirges.'}
ALLE = [h for _, _, l in SEKTIONEN for h in l]

# ---------------- Seite ----------------
b = ['<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">',
     '<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">Hüttenführer</span></nav>',
     f'<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">🏠 Hüttenführer Spitzingsee, Schliersee &amp; Tegernsee</h1>'
     f'<p style="font-size:1.08rem;color:#1f2933;margin:0;">{len(ALLE)} Hütten, Almen und Berggasthöfe – vom Spitzingsee über Schliersee, Wendelstein und Tegernsee bis zu den Grenzgängern in Tirol. Mit Höhe, Übernachtung, Öffnungszeiten und Zustieg, jede Angabe mit Quelle. Öffnungszeiten ändern sich: vor der Tour bei der Hütte prüfen.</p></header>',
     '<img src="/images/huetten-hero.jpg" alt="Berghütte in den Bayerischen Voralpen" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">',
     '<nav class="kat-nav" aria-label="Regionen" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 10px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
     + ''.join(f'<a href="#{i}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for i, t, _ in SEKTIONEN)
     + '<a href="#tipps" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">🎒 Hütten-Tipps</a></nav>',
     '<div id="hfilter" style="display:flex;flex-wrap:wrap;gap:6px;margin:0 0 6px;align-items:center;"><span style="font-size:.85rem;color:#4b5563;margin-right:4px;">Filter:</span>'
     + ''.join(f'<button type="button" data-f="{k}" style="border:1px solid #2e7d32;background:#fff;color:#14532d;border-radius:16px;padding:4px 10px;font-size:.82rem;cursor:pointer;">{v}</button>' for k, v in [('', 'Alle')] + [(k, TAGTXT[k]) for k in 'euwb'])
     + '</div><p id="hcount" style="font-size:.8rem;color:#4b5563;margin:0 0 6px;"></p>']
for i, t, l in SEKTIONEN:
    b.append(f'<section class="hsek">{H2(i, t)}{P(INTRO[i])}{GRID}{"".join(karte(h) for h in l)}</div></section>')

b.append(H2('tipps', '🎒 Hütten-Tipps') + '<ul style="line-height:1.7;color:#1f2933;">'
         '<li><strong>Reservieren:</strong> Übernachtungen vorab buchen – viele Alpenvereinshütten über das Online-Reservierungssystem der AV-Hütten; kurzfristig hilft das „Last-Minute-Hüttenbett“ des DAV.</li>'
         '<li><strong>Mitglieder:</strong> Alpenvereinsmitglieder zahlen ermäßigte Übernachtung und haben Anspruch auf ein preiswertes Bergsteigeressen.</li>'
         '<li><strong>Hüttenschlafsack</strong> ist auf DAV-Hütten Pflicht, Hüttenruhe meist 22 oder 23 Uhr.</li>'
         '<li><strong>Bargeld</strong> mitnehmen – auf manchen Hütten ist keine Kartenzahlung möglich.</li>'
         '<li><strong>Rodeln:</strong> die Hütten mit Rodelbahn – allen voran die Obere Firstalm – im <a href="/content/winter/rodeln-familie.html">Rodel-Überblick</a>.</li>'
         '<li><strong>Touren zu den Hütten</strong> ab der Oberen Firstalm, mit BRouter nachgerechnet: <a href="/content/wandern/index.html">Wandern</a> · <a href="/content/mtb/index.html">MTB</a> · <a href="/content/winter/index.html">Winter</a> · <a href="/content/skigebiete/">Skigebiete</a></li></ul>'
         '<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:16px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
         '<a href="https://www.amazon.de/s?k=H%C3%BCttenschlafsack&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Hüttenschlafsäcke</a> · '
         '<a href="https://www.amazon.de/s?k=Stirnlampe&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Stirnlampen</a> bei Amazon</aside>')
b.append(H2('quellen', '📚 Quellen') + P('Die Quellen stehen bei jeder Hütte unter „Details &amp; Quellen“. Übergreifend genutzt: '
         f'<a href="{MU}spitzingsee" target="_blank" rel="noopener">muenchen.de Spitzingsee</a>, <a href="{MU}tegernsee" target="_blank" rel="noopener">Tegernsee</a>, '
         f'<a href="{MU}berghuetten-am-wendelstein" target="_blank" rel="noopener">Wendelstein</a>; <a href="https://www.bergwelten.com" target="_blank" rel="noopener">bergwelten</a>; '
         '<a href="https://www.hoehenrausch.de" target="_blank" rel="noopener">hoehenrausch</a>; Alpenverein München &amp; Oberland; '
         '<a href="https://www.alpenverein.de/artikel/oeffnungstermine-der-dav-huetten-im-sommer-2026_eb1fadf9-64a1-4733-89be-d70d47caa33b" target="_blank" rel="noopener">DAV-Öffnungstermine 2026</a>. '
         'Obere Firstalm und Lyra Alm: Angaben der Hütte. Bilder ohne Hinweis zeigen die jeweilige Hütte, sonst ist „Symbolbild“ vermerkt.')
         + '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Alle Angaben ohne Gewähr.</p></article></main>')

JS = '''<script>
(function(){var bt=document.querySelectorAll('#hfilter button'),k=document.querySelectorAll('.hk'),c=document.getElementById('hcount');
function f(t){var n=0;k.forEach(function(e){var ok=!t||(' '+e.dataset.tags.split('').join(' ')+' ').indexOf(' '+t+' ')>-1;e.style.display=ok?'':'none';if(ok)n++;});
document.querySelectorAll('.hsek').forEach(function(s){var v=[].some.call(s.querySelectorAll('.hk'),function(e){return e.style.display!=='none'});s.style.display=v?'':'none';});
bt.forEach(function(b){var a=b.dataset.f===t;b.style.background=a?'#14532d':'#fff';b.style.color=a?'#fff':'#14532d';});c.textContent=n+' Hütten angezeigt';}
bt.forEach(function(b){b.addEventListener('click',function(){f(b.dataset.f);});});f('');})();
</script>
'''
s = open(F, encoding='utf-8').read()
a = s.find('<main'); z = s.find('</main>') + 7
head, tail = s[:a], s[z:]
DESC = f'Hüttenführer Spitzingsee, Schliersee, Tegernsee & Tirol: {len(ALLE)} Hütten und Almen mit Höhe, Übernachtung, Öffnungszeiten und Zustieg – jede Angabe mit Quelle. Mit Obere Firstalm und Lyra Alm.'
head = re.sub(r'<title>.*?</title>', '<title>Hüttenführer Spitzingsee, Schliersee &amp; Tegernsee – Hütten &amp; Almen mit Quellen | alpenexperte.de</title>', head, count=1, flags=re.S)
for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(DESC) + m.group(2), head)
for pat in [r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*', r'<!-- DS24-AFFILIATE -->.*?<!-- /DS24-AFFILIATE -->\s*',
            r'<aside class="urwahn-affiliate".*?</aside>\s*', r'<aside class="ds24-affiliate".*?</aside>\s*', r'<section class="quellen-section".*?</section>\s*']:
    tail = re.sub(pat, '', tail, flags=re.S)
i = tail.find('<footer')
if re.search(r'amazon|awin|urwahn|lucky|digistore', tail[:i], re.I): tail = tail[:0] + tail[i:]
tail = tail.replace('</body>', JS + '</body>', 1)
open(F, 'w', encoding='utf-8').write(head + '\n'.join(b) + tail)
print('ok', len(ALLE))
