#!/usr/bin/env python3
"""Baut content/klettern/index.html nach dem Gravel-/Wandern-Schema neu.

Nur belegte Ziele. Jede Angabe stammt aus den je Karte genannten Quellen.
Zustiegskarten ab Oberer Firstalm nutzen die bereits mit BRouter berechneten
Wanderrouten (content/wandern/geojson/W01, W23, W25) – Werte aus routing/ergebnis_wandern.json.
Kopf (Meta, Navigation) und Footer der bestehenden Seite bleiben, Partner-/Affiliate-Blöcke fliegen raus.
"""
import re, html, json
F = 'content/klettern/index.html'
E = lambda t: html.escape(t, quote=False)
ERG = {t['kennung']: t for t in json.load(open('routing/ergebnis_wandern.json', encoding='utf-8'))}
import os
ERGK = {t['kennung']: t for t in json.load(open('routing/ergebnis_klettern.json', encoding='utf-8')) if 'fehler' not in t} if os.path.exists('routing/ergebnis_klettern.json') else {}

def dav(km, hm):
    h = km / 4; v = hm / 300 + hm / 500
    t = max(h, v) + min(h, v) / 2
    m = round((t - int(t)) * 60 / 5) * 5
    return f"{int(t) + (m == 60)}:{0 if m == 60 else m:02d}"

def zustieg(k, text, fallback=None):
    """k = Kletter-Kennung (K..). Ohne Kletter-Ergebnis: bereits berechnete Wanderroute (fallback W..) oder nichts."""
    if k in ERGK:
        t, pfad, art = ERGK[k], 'klettern', ('Strecke' if ERGK[k].get('strecke') else 'Runde')
    elif fallback and fallback in ERG:
        t, pfad, art, k = ERG[fallback], 'wandern', 'Runde', fallback
    else:
        return ''
    km, hm, hab = t['laenge_km_brouter'], t['hm_aufstieg'], t.get('hm_abstieg', t['hm_aufstieg'])
    hmtxt = f"↑↓ {hm:,} Hm".replace(',', '.') if art == 'Runde' else f"↑ {hm:,} / ↓ {hab:,} Hm".replace(',', '.')
    zeit = dav(km, hm) if art == 'Runde' else dav_strecke(km, hm, hab)
    rueck = '' if art == 'Runde' else ' – zurück mit dem Bus'
    return (f'<p style="margin:8px 0 4px;font-size:.84rem;color:#0f2942;"><strong>Zustieg ab Oberer Firstalm (BRouter, hiking-mountain):</strong> {E(text)} – '
            f'{art} {str(km).replace(".", ",")} km · {hmtxt} · ca. {zeit} Std. Gehzeit ohne Kletterzeit (DAV-Formel){rueck}.</p>'
            f'<div class="mini-karte" data-route="{k}" data-pfad="{pfad}" style="height:200px;margin-top:6px;border-radius:8px;"></div>')

def dav_strecke(km, auf, ab):
    h = km / 4; v = auf / 300 + ab / 500
    t = max(h, v) + min(h, v) / 2
    m = round((t - int(t)) * 60 / 5) * 5
    return f"{int(t) + (m == 60)}:{0 if m == 60 else m:02d}"

def karte(id_, img, kopf, titel, text, fakten, hinweis, quellen, zu=None):
    rows = ''.join(f'<tr><th style="text-align:left;padding:5px 8px;color:#14532d;vertical-align:top;width:36%;border-bottom:1px solid #e5e7eb;">{E(a)}</th>'
                   f'<td style="padding:5px 8px;border-bottom:1px solid #e5e7eb;">{E(b)}</td></tr>' for a, b in fakten)
    q = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{E(n)}</a>' for n, u in quellen)
    return (f'<article id="{id_}" style="background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;scroll-margin-top:140px;">'
            f'<img src="/images/{img}" alt="{E(titel)}" loading="lazy" style="width:100%;height:150px;object-fit:cover;display:block;">'
            f'<div style="padding:12px 14px;"><div style="font-size:.8rem;color:#1d4ed8;font-weight:700;">{E(kopf)}</div>'
            f'<h3 style="margin:4px 0 6px;color:#14532d;font-size:1.05rem;">{E(titel)}</h3>'
            f'<p style="margin:0 0 8px;font-size:.9rem;line-height:1.45;color:#0f2942;">{E(text)}</p>'
            '<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;cursor:pointer;"><summary style="color:#14532d;font-weight:600;font-size:.86rem;">🧗 Details, Zustieg &amp; Quellen</summary>'
            f'<table style="width:100%;border-collapse:collapse;font-size:.84rem;color:#0f2942;margin-top:6px;">{rows}</table>'
            f'<p style="margin:8px 0 0;font-size:.84rem;color:#0f2942;">{E(hinweis)}</p>'
            + (zustieg(*zu) if zu else '') +
            f'<p style="margin:8px 0 0;font-size:.78rem;color:#4b5563;">Quellen: {q}</p></details></div></article>')

GRID = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;">'
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:34px 0 10px;scroll-margin-top:140px;">{t}</h2>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'

SPITZING = [
 karte('krettenburg', 'Klettern.jpg', '⭐ Hausgebiet · 1.414–1.488 m · 120–124 Routen · 5 bis 10- · bis 40 m',
       'Krettenburg – Sportklettern über der Oberen Firstalm', 'Das Sportklettergebiet direkt über der Oberen Firstalm: südseitiger, senkrechter bis überhängender Kalk, gut gebohrt, und die Einkehr liegt auf dem Zustieg. In den letzten Jahren eines der beliebtesten Sportklettergebiete südlich von München.',
       [('Routen', '120 laut Panico 2024, 124 laut theCrag (Stand November 2026)'),
        ('Schwierigkeit', '5 bis 10-, Schwerpunkt im 6. bis 9. Grad'),
        ('Wandhöhe', 'bis 40 m, häufig 12–25 m'),
        ('Sektoren', 'Black Velvet, Pilastro, Parterre, Sonnendeck und Balkon, Antichrist und Block, Wichtelwand (kurze plattige Routen), Séparée'),
        ('Höhe', '1.414–1.488 m (theCrag)'),
        ('Ausrichtung', 'Süd – lange Saison bis in den Herbst'),
        ('Zustieg', 'vom Spitzingsattel ca. 40 min auf der Forststraße zur Oberen Firstalm, von dort wenige Minuten zu den Wänden'),
        ('Einkehr', 'Obere Firstalm 1.375 m'),
        ('Kletterführer', 'Panico „München rockt“')],
       'Helm empfohlen. Im Winter bei wenig Schnee kann man zum Bahnhof Fischhausen-Neuhaus absteigen (ca. 1¼ h, nordseitig) – sonst an der Firstalm eine Rodel leihen.',
       [('Panico Topo des Monats 11/2024 (PDF)', 'https://www.panico.de/media/wysiwyg/Topo_des_Monats/Topo_des_Monats-11_2024.pdf'),
        ('theCrag – Krettenburg', 'https://www.thecrag.com/de/klettern/germany/area/2765345964'),
        ('theCrag – Sektoren', 'https://www.thecrag.com/climbing/germany/oberbayern/area/2765345964/guide'),
        ('alpenvereinaktiv.com', 'https://www.alpenvereinaktiv.com/de/tour/sportklettern-an-der-krettenburg/801954409/'),
        ('stadler-markus.de', 'https://www.stadler-markus.de/klettern/krettenburg-klettergebiet-am-spitzingsee.html')],
       zu=('K01', 'über den Wanderweg zu den Wänden oberhalb der Alm')),
 karte('taubenstein-suedgrat', 'wandern-taubenstein.jpg', 'Taubenstein 1.692 m · III · meist seilfrei · ca. 1 h Kletterei',
       'Taubenstein-Südgrat', 'Kurze, kompakte Gratkletterei direkt über dem Taubensteinhaus – der beliebte „Feierabend-Grat“ am Spitzingsee. Am Taubenstein selbst gibt es dazu über 20 Kletterrouten.',
       [('Schwierigkeit', 'III (eine kurze Abkletterstelle am Gratturm), sonst leichte Schrofenkletterei'),
        ('Charakter', 'meist seilfrei begangen; Fels kompakt'),
        ('Zustieg', 'vom Spitzingsee zum Taubensteinsattel; die Taubensteinbahn fährt nur im Sommer'),
        ('Abstieg', 'über den Normalweg (kurze drahtseilgesicherte Felsrinne)'),
        ('Sektoren am Taubenstein', 'Westwand, Almwandl (theCrag)'),
        ('Einkehr', 'Taubensteinhaus 1.567 m (DAV)')],
       'Gut kombinierbar mit den Ruchenköpfen. Wer seilfrei klettert, muss den III. Grad sicher beherrschen.',
       [('bergsteigen.com', 'https://www.bergsteigen.com/touren/klettern/taubenstein-suedgrat-suedostflanke/'),
        ('via-ferrata.de', 'https://www.via-ferrata.de/touren/gps/taubenstein-suedgrat'),
        ('summitpost (IG Klettern saniert die Routen)', 'https://summitpost.org/taubenstein/463663')],
       zu=('K02', 'Wanderweg zum Taubenstein', 'W25')),
 karte('ruchenkoepfe', 'klettern-wand.jpg', 'Ruchenköpfe 1.805 m · III bis IX · 90 Routen · bis 80 m Wandhöhe',
       'Ruchenköpfe', 'Das Klettergebiet am Spitzingsee: eine Felsbastion zwischen Rotwand und Auerspitz, bei Münchner Kletterern seit Jahrzehnten ein Klassiker – vom leichten Westgrat bis zu modernen Sportkletterrouten.',
       [('Westgrat', 'IV (eine kurze Stelle), meist um II; alpin abgesichert'),
        ('Neue Südwand (Göttner)', 'IV, meist III; Bohrhaken an den schweren Stellen'),
        ('Dülferriss', 'V- (Südwand)'),
        ('Gebiet laut Panico-Kletterführer 2026', '90 Routen im III. bis IX. Grad, Wandhöhe bis 80 m, Ausrichtung NW, W, S'),
        ('Sektoren', 'Obere Westwand, Untere Westwand, Westgrattürme, Südwand (theCrag)'),
        ('Zustieg', 'Spitzingsee – Rotwandhaus ca. 1:30 h, dann Steig zum Wandfuß; im Sommer auch über die Taubensteinbahn'),
        ('Abstieg', 'Abseilen von den Ruchenköpfen'),
        ('Einkehr', 'Rotwandhaus 1.737 m')],
       'Kletterausrüstung und Helm nötig; der Abstieg wird abgeseilt. Topos im Panico-Kletterführer Bayerische Alpen Band 3.',
       [('bergtour-online.de', 'https://www.bergtour-online.de/bergtouren/alpine-bergtouren/alpineklettertouren/mittelschwereklettertouren/alpinklettern-ruchenkoepfe/'),
        ('bergsteigen.com – Westgrat', 'https://www.bergsteigen.com/touren/klettern/ruchenkoepfe-westgrat'),
        ('bergsteigen.com – Neue Südwand', 'https://www.bergsteigen.com/touren/klettern/ruchenkoepfe-neue-suedwand-goettner/'),
        ('via-ferrata.de – Dülferriss', 'https://www.via-ferrata.de/touren/gps/ruchenkoepfe-westgrat?tab=reviews'),
        ('Panico Topo des Monats 6/2026 (PDF)', 'https://www.panico.de/media/wysiwyg/PDF/TopoDMonats/Topo%20des%20Monats-06-2026.pdf')],
       zu=('K03', 'über Spitzingsee und Rotwandhaus zum Wandfuß', 'W23')),
 karte('brecherspitz-ostgrat', 'klettersteig-blick.jpg', 'Brecherspitz 1.683 m · alpine Bergtour · 4 von 6 · 580 Hm · 3 h',
       'Brecherspitz-Ostgrat', 'Kein Klettersteig, sondern ein unmarkierter, ausgesetzter Grat mit kurzen, leichten Felsstufen – direkt über der Oberen Firstalm. Nur für trittsichere, schwindelfreie Bergsteiger mit alpiner Erfahrung.',
       [('Schwierigkeit', '4 von 6 (tourentipp); ausgesetzt, klettertechnisch einfach'),
        ('Höhenmeter / Zeit', 'ca. 580 Hm, insgesamt ca. 3 h'),
        ('Einstieg', 'kleiner, nicht markierter Pfad direkt beim Wegweiser „Brecherspitz“ an der Firstalm'),
        ('Sicherung', 'keine durchgehende Versicherung'),
        ('Abstieg', 'Normalweg über den Südwestrücken zur Oberen Firstalm')],
       'Bei Nässe meiden. Der Normalweg zur Brecherspitz ist auf der Wandern-Seite beschrieben.',
       [('tourentipp.com – Brecherspitz Ostgrat (PDF)', 'https://tourentipp.com/portal/touren/735/pdf/get')],
       zu=('K04', 'Normalweg Firstalm – Brecherspitz (Abstiegsroute)', 'W01')),
]
TEGERNSEE = [
 karte('ross-buchstein', 'klettern-klettersteig.jpg', 'Roß- und Buchstein 1.698 / 1.701 m · II bis 7- · Tegernseer Hütte 1.650 m',
       'Roß- und Buchstein', 'Wander-, Kletter- und Klettersteigziel in einem: Zum Roßstein führt ein kurzer, drahtseilversicherter Steig, der Buchstein verlangt Kletterei – dazwischen thront die Tegernseer Hütte.',
       [('Roßstein', 'kurzer, leichter, drahtseilversicherter Steig zur Tegernseer Hütte; Ausweichroute für Wanderer über die Nordseite'),
        ('Buchstein-Normalweg', 'II, steile und abgespeckte Felsrinne'),
        ('Kletterrouten', 'III–IV+ (z. B. Zwergerlrutschbahn IV) bis 7- (Sahnestückchen); Südwand-Schmankerl 6-'),
        ('Tour gesamt', 'ca. 850 Hm, ca. 4:30 h (Bergtour)'),
        ('Anreise', 'Wanderparkplatz Bayerwald bei Kreuth; Bus ab Tegernsee bis Haltestelle Bayerwald'),
        ('Hütte', 'Tegernseer Hütte (DAV), bewirtschaftet etwa vom zweiten Mai- bis zum ersten Novemberwochenende')],
       'An schönen Wochenenden Stau am Steig und volle Hüttenterrasse – früh losgehen. Bei Nässe sind die Felsen glatt.',
       [('tourentipp.com – Ross- und Buchstein (PDF)', 'https://tourentipp.com/portal/touren/32/pdf/get'),
        ('bergtour-online.de – Klettern (III–IV+)', 'https://www.bergtour-online.de/bergtouren/alpine-bergtouren/alpineklettertouren/mittelschwereklettertouren/ross-buchstein/'),
        ('bergsteigen.com – Südwand Schmankerl', 'https://www.bergsteigen.com/touren/klettern/suedwand-schmankerl-buchstein/'),
        ('bergsteigen.com – Sahnestückchen', 'https://www.bergsteigen.com/touren/klettern/sahnestueckchen-buchstein/'),
        ('tourentipp.com – Tegernseer Hütte (PDF)', 'https://www.tourentipp.com/portal/huetten/5/pdf/get'),
        ('bergfex – Anreise Bayerwald', 'https://www.bergfex.com/sommer/bayern/touren/wanderung/59503,ross-und-buchstein')],
       zu=('K05', 'zu Fuß zur Tegernseer Hütte')),
 karte('blankenstein', 'felsformation.jpg', 'Blankenstein 1.768 m · II+ bis IV+ · Direkter Ostgrat 5 SL',
       'Blankenstein (Plankenstein)', 'Einer der wenigen richtig felsigen Berge der Bayerischen Voralpen, südlich des Tegernsees zwischen Wallberg und Risserkogel.',
       [('Normalweg', 'II+ (eine Stelle in der 17 m langen Kaminrinne), sonst leichter; stark abgespeckt'),
        ('Direkter Ostgrat', 'IV+ (eine Stelle), 5 Seillängen, ca. 140 m; gut mit Normal- und Bohrhaken gesichert'),
        ('Zustieg', 'über die Wallbergbahn oder vom Parkplatz Kistenwinterstube (950 m)'),
        ('Abstieg', 'über den Normalweg, die obere Kaminrinne wird meist abgeseilt')],
       'Kombinierbar mit dem Risserkogel. Klemmkeile braucht es am Ostgrat laut bergsteigen.com nicht.',
       [('bergsteigen.com – Direkter Ostgrat', 'https://www.bergsteigen.com/touren/klettern/direkter-ostgrat-plankenstein/'),
        ('bergsteigen.com – Normalweg', 'https://www.bergsteigen.com/touren/klettern/normalweg-plankenstein-blankenstein/'),
        ('via-ferrata.de – Blankenstein', 'https://www.via-ferrata.de/gipfeldatenbank/bergtour/blankenstein'),
        ('climbing.place – 140 m', 'https://climbing.place/climbing/detail/blankenstein/direkter-ostgrat-blankenstein-plankenstein-114023')],
       zu=('K06', 'zu Fuß zum Blankenstein')),
 karte('leonhardstein', 'klettersteig-seil.jpg', 'Leonhardstein 1.452 m · Sportklettern 6 bis 7- · Kreuth',
       'Leonhardstein', 'Markanter Felszacken über Kreuth: als Gipfel eine kurze, spritzige Bergtour, in der Südwand gut gebohrte Mehrseillängen im VI. Grad.',
       [('Gipfel zu Fuß', 'ca. 700 Hm, 3:20–3:30 h, Schwierigkeit 3 von 6; Kraxelei am Gipfel'),
        ('Kletterrouten', 'u. a. Flora Bohra 6/6+, Für Andi 6, Hey Leoni 6, Überholspur 7-'),
        ('Absicherung', 'gut: 2 Bohrhaken an den Ständen, 4–7 pro Seillänge (Überholspur)'),
        ('Ausgangspunkt', 'Kreuth (ca. 780 m) oder Parkplatz Schwarztennalm'),
        ('Sperrzeit', 'Sektor Westpfeiler vom 1. März bis 31. Juli gesperrt – Schilder vor Ort beachten')],
       'Die Platten mit Graseinlagen sind bei Nässe unangenehm; nach Regen ein bis zwei trockene Tage abwarten.',
       [('tourentipp.com – Leonhardstein (PDF)', 'https://www.tourentipp.com/portal/touren/30/pdf/get'),
        ('bergsteigen.com – Flora Bohra', 'https://www.bergsteigen.com/touren/klettern/flora-bohra-leonhardstein/'),
        ('bergsteigen.com – Überholspur', 'https://www.bergsteigen.com/touren/klettern/ueberholspur/'),
        ('bergsteigen.com – Hey Leoni', 'https://www.bergsteigen.com/touren/klettern/hey-leoni-leonhardstein/'),
        ('theCrag – Sperrung Westpfeiler', 'https://www.thecrag.com/de/klettern/germany/area/2567648919')],
       zu=('K07', 'zu Fuß zum Leonhardstein')),
]
WEITERE = [
 karte('loechelwand', 'felsenschwalbe.jpg', 'Löchelwand · 1.208–1.252 m · 25 Routen · Sportklettern',
       'Löchelwand', 'Kleiner, ruhiger und noch junger Klettergarten im Mangfallgebirge – Überhang, Rampe und senkrechter Fels.',
       [('Routen', '25 (theCrag), Wandhöhe bis ca. 19 m'),
        ('Sektoren', 'Feste + Biere, Tage'),
        ('Fels', 'teils noch locker – Helm wird dringend empfohlen; leichtere Routen stellenweise bemoost'),
        ('Wandfuß', 'meist geneigt, Waldboden kann rutschig sein'),
        ('Unterstützung', 'Spendenbox im Sektor Tage für die Erschließung')],
       'Im Panico-Kletterführer Bayerische Alpen Band 2 als kleiner, ruhiger Klettergarten beschrieben.',
       [('theCrag – Löchelwand', 'https://www.thecrag.com/de/klettern/germany/area/6731659860'),
        ('Panico Leseprobe Bayerische Alpen Band 2 (PDF)', 'https://www.panico.de/media/wysiwyg/PDF/Leseproben/Leseprobe_BayerischeAlpen_Band2_2025-2.pdf')],
       zu=('K08', 'zu Fuß zur Löchelwand')),
]

NAV = [('#krettenburg', '⭐ Krettenburg'), ('#hinweis', 'ℹ️ Gut zu wissen'), ('#spitzingsee', '🏔️ Spitzingsee'), ('#tegernsee', '🌊 Tegernsee'), ('#weitere', '🪨 Weitere Felsen'), ('#klettersteige', '🪢 Klettersteige'),
       ('#ausruestung', '🎒 Ausrüstung'), ('#sicherheit', '⚠️ Sicherheit'), ('#kompendium', '🔬 Kompendium'), ('#quellen', '📚 Quellen')]

KOMP = [('/content/klettern/angstmanagement.html', '1. Angstmanagement', 'Sturzangst und Atemtechnik'),
        ('/content/klettern/neuromuskulaere-rekrutierung.html', '2. Rekrutierung', 'Wie das Nervensystem Fingerkraft steuert'),
        ('/content/klettern/uiaa-skala.html', '3. UIAA-Skala', 'Schwierigkeitsgrade und Normen'),
        ('/content/klettern/erstbegehung.html', '4. Erstbegehung', 'Wie neue Routen entstehen'),
        ('/content/klettern/vertikale-architektur.html', '5. Felsästhetik', 'Kalkstein als Kletterfels')]

QUELLEN = [('bergtour-online.de – Alpine Bergtouren am Spitzingsee', 'https://www.bergtour-online.de/beschreibungen/bergtouren-spitzingsee/'),
           ('via-ferrata.de – Dr.-Julius-Mayr-Klettersteig (Brünnstein, A/B)', 'https://www.via-ferrata.de/klettersteige/topo/dr-julius-mayr-klettersteig/reviews'),
           ('bergwelten.com – Roß- und Buchstein, drahtseilversicherter Steig', 'https://www.bergwelten.com/t/w/7044'),
           ('Panico Alpinverlag – Topo des Monats 11/2024: Krettenburg (PDF)', 'https://www.panico.de/media/wysiwyg/Topo_des_Monats/Topo_des_Monats-11_2024.pdf'),
           ('tourentipp.com – Brecherspitz Ostgrat (PDF)', 'https://tourentipp.com/portal/touren/735/pdf/get'),
           ('Panico Alpinverlag – Topo des Monats 6/2026: Ruchenköpfe (PDF)', 'https://www.panico.de/media/wysiwyg/PDF/TopoDMonats/Topo%20des%20Monats-06-2026.pdf'),
           ('theCrag – Leonhardstein, Sperrung Westpfeiler', 'https://www.thecrag.com/de/klettern/germany/area/2567648919'),
           ('theCrag – Mangfallgebirge (Routenzahlen)', 'https://www.thecrag.com/de/klettern/germany/area/2537059515')]

b = []
b.append('<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">')
b.append('<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">Klettern</span></nav>')
b.append('<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">🧗 Klettern am Spitzingsee &amp; Tegernsee</h1>'
         '<p style="font-size:1.08rem;color:#1f2933;margin:0;">Grate, Wände und kurze versicherte Steige zwischen Spitzingsee und Tegernsee – acht belegte Ziele vom III. Grad bis zum Sportklettern im 10. Grad – allen voran die Krettenburg direkt über der Oberen Firstalm, mit Quellen zu jeder Angabe. Die Zustiege am Spitzingsee sind ab der Oberen Firstalm (1.375 m) berechnet.</p></header>')
b.append('<img src="/images/klettern-hero.jpg" alt="Kletterer am Kalkfels" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">')
b.append('<nav class="kat-nav" aria-label="Klettern-Bereiche" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
         + ''.join(f'<a href="{h}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for h, t in NAV) + '</nav>')
b.append(H2('hinweis', 'ℹ️ Gut zu wissen') + '<div style="background:#fffbeb;border-left:5px solid #b45309;padding:14px 18px;border-radius:10px;color:#1f2933;">'
         '<p style="margin:0 0 6px;"><strong>Am Spitzingsee gibt es keinen ausgebauten Klettersteig.</strong> Taubenstein, Rotwand, Brecherspitz und Bodenschneid sind Wander- und Klettergipfel – kurze Drahtseile am Gipfelaufbau machen daraus noch keinen Klettersteig.</p>'
         '<p style="margin:0;">Die nächsten versicherten Steige: der kurze Steig auf den <a href="#ross-buchstein">Roßstein</a> bei Kreuth und der Dr.-Julius-Mayr-Klettersteig auf den Brünnstein (A/B).</p></div>')
b.append(H2('spitzingsee', '🏔️ Spitzingsee') + P('Vier Ziele, alle mit Zustieg ab der Oberen Firstalm – die Krettenburg liegt nur wenige Minuten über der Alm. Die Karten zeigen die mit BRouter berechnete Wanderroute; die Kletterei selbst ist nicht eingezeichnet.') + GRID + ''.join(SPITZING) + '</div>')
b.append(H2('tegernsee', '🌊 Tegernseer Berge') + P('Für diese Ziele fährt man besser ins Tegernseer Tal – ab der Firstalm sind sie zu Fuß zu weit für einen Klettertag.') + GRID + ''.join(TEGERNSEE) + '</div>')
b.append(H2('weitere', '🪨 Weitere Felsen im Mangfallgebirge') + GRID + ''.join(WEITERE) + '</div>' +
         '<table style="width:100%;border-collapse:collapse;font-size:.93rem;color:#1f2933;margin-top:14px;"><tr><th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">Fels</th><th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">Routen (theCrag)</th><th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">Hinweis</th></tr>'
         '<tr><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Sebaldstein</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">10</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">1.594–1.678 m</td></tr>'
         '<tr><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Kleintiefental</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">10</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">bis ca. 20 m</td></tr>'
         '<tr><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Rotwandkopf</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">4</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">–</td></tr>'
         '<tr><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Platte</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">3</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">bis ca. 12 m</td></tr></table>'
         + P('Zu diesen kleinen Felsen gibt es kaum belegte Beschreibungen – Details im Panico-Kletterführer Bayerische Alpen Band 3 und auf <a href="https://www.thecrag.com/de/klettern/germany/area/2537059515" target="_blank" rel="noopener">theCrag</a>.'))
b.append(H2('klettersteige', '🪢 Klettersteige in der Nähe') +
         '<table style="width:100%;border-collapse:collapse;font-size:.93rem;color:#1f2933;"><tr><th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">Steig</th><th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">Schwierigkeit</th><th style="text-align:left;padding:7px 10px;background:#e8f5e9;color:#14532d;">Hinweis</th></tr>'
         '<tr><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Roßstein (Kreuth)</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">leicht, kurz</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">drahtseilversichert durch die Südwand zur Tegernseer Hütte; Trittsicherheit und Schwindelfreiheit nötig</td></tr>'
         '<tr><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Dr.-Julius-Mayr-Klettersteig (Brünnstein)</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">A/B</td><td style="padding:7px 10px;border-bottom:1px solid #e5e7eb;">Start in Mühlau bei Oberaudorf, ca. 5 h; leichte Tour mit kurzer Klettersteig-Einlage</td></tr></table>'
         + P('Größere Klettersteige gibt es erst im Wetterstein, im Karwendel oder in Tirol.'))
b.append(H2('ausruestung', '🎒 Ausrüstung') + '<ul style="line-height:1.7;color:#1f2933;">'
         '<li><strong>Helm</strong> – auf allen Touren, wegen Steinschlag</li><li><strong>Gurt, Seil, Expressschlingen</strong> – z. B. 60 m Seil und 12 Expressen am Leonhardstein, 60 m Seil zum Abseilen an Roß- und Buchstein</li>'
         '<li><strong>Abseilgerät und Bandschlingen</strong> – Ruchenköpfe und Blankenstein werden abgeseilt</li><li><strong>Klettersteigset</strong> nur für versicherte Steige</li>'
         '<li><strong>Zustiegsschuhe</strong> mit griffiger Sohle, Wetterschutz, Getränke</li></ul>'
         '<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
         '<a href="https://www.amazon.de/s?k=Kletterhelm&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Kletterhelme</a> · '
         '<a href="https://www.amazon.de/s?k=Klettergurt&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Klettergurte</a> · '
         '<a href="https://www.amazon.de/s?k=Klettersteigset&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">Klettersteigsets</a> bei Amazon</aside>')
b.append(H2('sicherheit', '⚠️ Sicherheit') + '<ul style="line-height:1.7;color:#1f2933;">'
         '<li>Bei Gewittergefahr und Nässe nicht einsteigen – Kalk und abgespeckte Rinnen werden glatt.</li>'
         '<li>Sperrzeiten zum Vogelschutz beachten, z. B. Leonhardstein-Westpfeiler 1. März bis 31. Juli.</li>'
         '<li>Hütten-Saison prüfen: Rotwandhaus, Taubensteinhaus und Tegernseer Hütte haben eigene Öffnungszeiten; die Taubensteinbahn fährt nur im Sommer.</li>'
         '<li>Notruf <strong>112</strong> – die Leitstelle alarmiert die Bergwacht.</li></ul>')
b.append(H2('kompendium', '🔬 Kletter-Kompendium') + GRID + ''.join(
    f'<a href="{u}" style="display:block;background:#fff;border:1px solid #2e7d32;border-radius:10px;padding:12px 14px;text-decoration:none;color:#0f2942;"><strong style="color:#14532d;">{E(t)} →</strong><br><span style="font-size:.88rem;">{E(d)}</span></a>' for u, t, d in KOMP) + '</div>')
b.append(H2('quellen', '📚 Quellen') + P('Die Quellen zu jedem Ziel stehen in der jeweiligen Karte unter „Details“. Übergreifend:') + '<ul style="line-height:1.7;font-size:.92rem;">'
         + ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in QUELLEN) +
         '</ul><p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Alle Angaben ohne Gewähr – Grade, Absicherung und Sperrzeiten vor Ort und im aktuellen Kletterführer prüfen.</p>')
b.append('</article></main>')

MAPJS = '''<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".mini-karte").forEach(function (el) {
    var det = el.closest("details"), geladen = false;
    function init() {
      if (geladen || typeof L === "undefined") return;
      geladen = true;
      var m = L.map(el, { attributionControl: false });
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 18 }).addTo(m);
      var pf = el.getAttribute("data-pfad") || "wandern"; fetch("/content/" + pf + "/geojson/" + el.getAttribute("data-route") + "_" + pf + ".geojson")
        .then(function (r) { return r.json(); })
        .then(function (g) { var l = L.geoJSON(g, { style: { color: "#ea580c", weight: 4 } }).addTo(m); m.fitBounds(l.getBounds(), { padding: [10, 10] }); setTimeout(function () { m.invalidateSize(); }, 50); })
        .catch(function () { el.style.display = "none"; });
    }
    if (det) det.addEventListener("toggle", function () { if (det.open) init(); });
  });
});
</script>
'''

s = open(F, encoding='utf-8').read()
a = s.find('<main id="main">'); bb = s.find('</main>') + 7
head, tail = s[:a], s[bb:]
DESC = 'Klettern am Spitzingsee und Tegernsee: Krettenburg über der Oberen Firstalm, Taubenstein-Südgrat, Ruchenköpfe, Brecherspitz-Ostgrat, Roß- und Buchstein, Blankenstein, Leonhardstein – belegt mit Quellen.'
head = re.sub(r'<title>.*?</title>', '<title>Klettern am Spitzingsee &amp; Tegernsee – Grate, Wände, Steige | alpenexperte.de</title>', head, count=1, flags=re.S)
for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(DESC) + m.group(2), head)
if 'leaflet.css' not in head:
    head = head.replace('</head>', '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>\n'
                        '<style id="mini-karte-fix">.mini-karte{position:relative;isolation:isolate;overflow:hidden;}.mini-karte .leaflet-container{width:100%!important;height:100%!important;}</style>\n</head>', 1)
for pat in [r'\s*<!-- ===== FEEDBACK-BOX.*?</section>', r'<section class="section section--lounge".*?</section>\s*',
            r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*', r'<section class="section section--lounge-alt".*?</section>\s*',
            r'<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>\s*<script>.*?</script>\s*']:
    tail = re.sub(pat, '', tail, flags=re.S)
i = tail.find('<footer'); j = tail.find('<div style="background:linear-gradient(135deg,#1c2826')
if 0 <= j < i: tail = tail[:j] + tail[i:]
tail = tail.replace('</body>', MAPJS + '</body>', 1)
open(F, 'w', encoding='utf-8').write(head + '\n'.join(b) + tail)
print('ok')
