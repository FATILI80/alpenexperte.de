#!/usr/bin/env python3
"""Baut Tierwelt (content/fauna/index.html) und Pflanzenwelt (content/botanik/index.html) neu.
Nur belegte Angaben; Bilder nur, wenn die Art eindeutig erkennbar ist. Kopf/Fuß von restaurants.html (absolute Pfade)."""
import re, html
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t, sub='': f'<h2 id="{i}" style="color:#14532d;margin:38px 0 6px;scroll-margin-top:140px;">{t}</h2>' + (f'<p style="color:#374151;margin:0 0 12px;line-height:1.6;">{sub}</p>' if sub else '')
P = lambda t: f'<p style="color:#1f2933;line-height:1.65;">{t}</p>'
def BOX(t, farbe='#e8f5e9', rand='#2e7d32'): return f'<div style="background:{farbe};border-left:5px solid {rand};padding:12px 16px;border-radius:10px;margin:14px 0;color:#1f2933;line-height:1.6;">{t}</div>'
def UL(items): return '<ul style="line-height:1.7;color:#1f2933;">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
GRID = lambda cards: '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin:10px 0 6px;">' + ''.join(cards) + '</div>'

class Q:
    def __init__(s): s.l = []
    def __call__(s, titel, url):
        if (titel, url) not in s.l: s.l.append((titel, url))
        n = s.l.index((titel, url)) + 1
        return f'<sup><a href="#q{n}" style="color:#1d4ed8;text-decoration:none;">[{n}]</a></sup>'
    def liste(s): return (H2('quellen', '📚 Quellen') + '<ol style="line-height:1.7;font-size:.92rem;">'
                          + ''.join(f'<li id="q{i}"><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for i, (t, u) in enumerate(s.l, 1)) + '</ol>'
                          + '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026. Genaue Fundorte seltener Arten nennen wir bewusst nicht – auch die amtlichen Managementpläne schwärzen sie.</p>')

def CARD(cid, name, latin, text, rows, img=None, alt='', icon='🐾'):
    top = (f'<img src="/images/{img}" alt="{E(alt or name)}" loading="lazy" style="width:100%;height:170px;object-fit:cover;display:block;">' if img
           else f'<div style="height:70px;display:flex;align-items:center;justify-content:center;font-size:2.2rem;background:#e8f5e9;">{icon}</div>')
    tab = ''.join(f'<tr><th style="text-align:left;padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#14532d;width:34%;vertical-align:top;">{k}</th><td style="padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;">{v}</td></tr>' for k, v in rows)
    return (f'<article id="{cid}" style="background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;scroll-margin-top:140px;">{top}'
            f'<div style="padding:12px 14px;"><h3 style="margin:0 0 2px;color:#14532d;font-size:1.08rem;">{name}</h3>'
            f'<div style="font-style:italic;color:#4b5563;font-size:.85rem;margin-bottom:6px;">{latin}</div>'
            f'<p style="margin:0 0 8px;font-size:.92rem;line-height:1.5;color:#1f2933;">{text}</p>'
            f'<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;"><summary style="color:#14532d;font-weight:600;font-size:.86rem;cursor:pointer;">Steckbrief &amp; Quellen</summary>'
            f'<table style="width:100%;border-collapse:collapse;font-size:.88rem;margin-top:6px;">{tab}</table></details></div></article>')

def seite(pfad, titel, h1, intro, hero, nav, body, desc, crumb, weiter):
    s = open('restaurants.html', encoding='utf-8').read()
    a = s.find('<main'); z = s.find('</main>') + 7
    head, tail = s[:a], s[z:]
    url = 'https://alpenexperte.de/' + pfad
    head = re.sub(r'<title>.*?</title>', f'<title>{E(titel)} | alpenexperte.de</title>', head, count=1, flags=re.S)
    for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(desc) + m.group(2), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(titel) + m.group(2), head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S)
    absol = lambda t: re.sub(r'((?:href|src)=")(?!https?:|/|#|mailto:|tel:|data:|javascript:)([^"]+)"', r'\1/\2"', t)
    head, tail = absol(head), absol(tail)
    m = ['<main id="main"><article class="container" style="max-width:1040px;margin:0 auto;padding:24px 16px 48px;">',
         f'<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">{crumb}</span></nav>',
         f'<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">{h1}</h1><p style="font-size:1.08rem;color:#1f2933;margin:0;line-height:1.6;">{intro}</p></header>', hero,
         '<nav class="kat-nav" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;">'
         + ''.join(f'<a href="#{i}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for i, t in nav) + '</nav>',
         body, f'<p style="margin-top:22px;font-size:.92rem;">{weiter}</p>', '</article></main>']
    open(pfad, 'w', encoding='utf-8').write(head + '\n'.join(m) + tail)
    print('ok', pfad, len(head + ''.join(m) + tail))

HERO = lambda img, alt: f'<img src="/images/{img}" alt="{E(alt)}" loading="lazy" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">'
DAV = 'https://www.alpenverein.de/artikel/'
MPL_HANDOUT = ('Regierung von Oberbayern – Natura 2000 Mangfallgebirge, Handout Runder Tisch 2023', 'https://regierung.oberbayern.bayern.de/mam/dokumente/bereich5/sg51/natura2000/mpl-entwuerfe/8336-371-471_f_mangfallgebirge_handout_rt.pdf')
SPA_VO = ('Bayerische Vogelschutzverordnung – Gebiet DE8336471 Mangfallgebirge (FAOLEX)', 'https://faolex.fao.org/docs/pdf/ger99811.pdf')
LFU_RAUFUSS = ('LfU Bayern – Artenhilfsprogramm Raufußhühner', 'https://www.lfu.bayern.de/natur/artenhilfsprogramme_voegel/raufusshuehner/index.htm')

# =================== TIERWELT ===================
q = Q(); b = []
b.append(H2('schutzgebiet', '🗺️ Ein Schutzgebiet direkt vor der Firstalm')
 + P('Große Teile des Mangfallgebirges sind gleich doppelt geschützt: als Vogelschutzgebiet (SPA 8336-471) und als FFH-Gebiet (8336-371), beide „Mangfallgebirge“ und zu großen Teilen deckungsgleich' + q(*MPL_HANDOUT)
     + '. Das Gebiet berührt die Gemeinden Kreuth, Rottach-Egern, Bayrischzell, Fischbachau und Schliersee' + q(*MPL_HANDOUT) + '.')
 + P('Laut Verordnung ist das Ziel die Erhaltung oder Wiederherstellung der Bestände von Birkhuhn, Auerhuhn, Haselhuhn, Waldschnepfe, Alpenschneehuhn, Steinadler, Wanderfalke, Wespenbussard, Raufußkauz, Sperlingskauz, Uhu und Hohltaube sowie weiterer Arten' + q(*SPA_VO)
     + '. Die Wälder sind zudem Lebensraum für Weißrücken-, Dreizehen-, Schwarz- und Grauspecht' + q(*MPL_HANDOUT) + '.')
 + BOX('Im Managementplan zum FFH-Gebiet sind Fundort- und Nachweisdaten seltener Arten geschwärzt' + q('LfU – Managementplan FFH-Gebiet 8336-371 Mangfallgebirge, Fachgrundlagen (2024)', 'https://lfu.bayern.de/natur/natura2000_managementplaene/8027_8672/doc/8336_371/texte/de8336371_t_fg_ffin_nfin.pdf')
       + '. Wir halten es genauso: Auf dieser Seite stehen keine Horst-, Balz- oder Fundplätze.', '#fff7ed', '#c2410c'))

b.append(H2('raufusshuehner', '🐓 Raufußhühner', 'Die Sorgenkinder des Gebiets – in Bayern gelten Auer- und Birkhuhn als vom Aussterben bedroht, das Alpenschneehuhn als stark gefährdet.' + q(*LFU_RAUFUSS)) + GRID([
 CARD('birkhuhn', 'Birkhuhn', 'Lyrurus tetrix (Syn. Tetrao tetrix)', 'Im Schönfeldkessel an der Rotwand leben laut Gebietsbetreuung noch etwa 20 Tiere – Platz wäre für hundert.' + q('alpinwelt 1/2024 – Interview Gebietsbetreuung Mangfallgebirge', 'https://www.alpenverein-muenchen-oberland.de/alpinwelt/archiv/2024/alpinwelt-1-2024-bergmagazin-alpenverein-muenchen-oberland/alle-gehen-nur-dem-roten-punkt-nach-interview-schwerpunkt-tatort-berg'),
      [('Rote Liste Bayern', 'vom Aussterben bedroht' + q(*LFU_RAUFUSS)), ('Aussehen', 'etwa haushuhngroß, 750–1.600 g; Hahn schwarz-bläulich glänzend, Henne tarnfarben rost-/gelbbraun' + q('Infotafel Wildschutzgebiet Rotwandgebiet (Jägerkamp)', 'https://www.alpenverein-muenchen-oberland.de/uploads/images/Kt0U4tsdl108xPDfZqjfMQ/wsg_rotwandgebiet_schild_2021_tafel_jaegerkamp.pdf')),
       ('Winter', 'gräbt Schneehöhlen – erst ab etwa 30 cm Schneehöhe möglich' + q('Alpenverein München & Oberland – Rückzugsräume für Wildtiere', 'https://www.alpenverein-muenchen-oberland.de/umwelt/naturvertraeglicher-bergsport-im-winter/rueckzugsraeume-fuer-wildtiere-in-den-alpen-wald-wild-schongebiete-und-wildschutzgebiete-bitte-nicht-betreten')),
       ('Schutz', 'Wildschutzgebiet Rotwand: Betretungsverbot 1. Dezember – 14. Juli' + q('Infotafel Wildschutzgebiet Rotwandgebiet (Jägerkamp)', 'https://www.alpenverein-muenchen-oberland.de/uploads/images/Kt0U4tsdl108xPDfZqjfMQ/wsg_rotwandgebiet_schild_2021_tafel_jaegerkamp.pdf'))],
      img='birkhahn-balz.jpg', alt='Birkhahn bei der Balz'),
 CARD('auerhuhn', 'Auerhuhn', 'Tetrao urogallus', 'Die Wälder des Mangfallgebirges sind laut Managementplan ein wertvoller Lebensraum für Auer- und Haselhuhn.' + q(*MPL_HANDOUT),
      [('Rote Liste Bayern', 'vom Aussterben bedroht' + q(*LFU_RAUFUSS)), ('Schutzgebiet', 'Erhaltungsziel im SPA Mangfallgebirge' + q(*SPA_VO)), ('Verhalten', 'sehr störungsempfindlich; Wald-Wild-Schongebiete wurden vor allem für Auer- und Birkhuhn ausgewiesen' + q('DAV – Wald-Wild-Schongebiete', DAV + 'wald-wild-schongebiete-winter-tierschutz_0cd10648-a795-46f8-838d-48d5734b7f37'))],
      img='auerhahn-portrait.jpg', alt='Auerhahn, Kopfporträt'),
 CARD('alpenschneehuhn', 'Alpenschneehuhn', 'Lagopus muta', 'Im Winter bis auf Schwanzfedern, Schnabel und Augen schneeweiß, im Sommer graubraun gefleckt mit weißen Flügeln.' + q(*LFU_RAUFUSS),
      [('Rote Liste Bayern', 'stark gefährdet' + q(*LFU_RAUFUSS)), ('Lebensraum', 'in Bayern die kalkalpine Zone ab etwa 1.600–1.700 m' + q('LfU – Natura 2000 Vogelarten: Raufußhühner (PDF)', 'https://www.lfu.bayern.de/natur/natura_2000/vogelschutzrichtlinie/doc/raufusshuehner.pdf')), ('Klima', 'muss durch den Klimawandel in höhere Lagen ausweichen; der Lebensraum in Bayern wird kleiner' + q(*LFU_RAUFUSS))], icon='❄️'),
 CARD('haselhuhn', 'Haselhuhn', 'Tetrastes bonasia', 'Das heimlichste der vier Raufußhühner – lebt in unterholzreichen Laub- und Mischwäldern, in den Alpen im Bergmischwald.' + q('LfL/LWG – Raufußhühner Teil 2 (PDF)', 'https://lfl.bayern.de/mam/cms04/service/dateien/raufußhuhn_teil_2.pdf'),
      [('Schutzgebiet', 'Erhaltungsziel im SPA Mangfallgebirge' + q(*SPA_VO)), ('Lebensraum', 'Wälder des Mangfallgebirges' + q(*MPL_HANDOUT))], icon='🌲')]))

b.append(H2('greifvoegel', '🦅 Greifvögel & Eulen') + GRID([
 CARD('steinadler', 'Steinadler', 'Aquila chrysaetos', 'In Deutschland lebt der Steinadler nur in den Alpen Bayerns – etwa 50 Brutpaare, mit im weltweiten Vergleich geringem Bruterfolg.' + q('DAV – Der Steinadler', DAV + 'der-steinadler_9e1dc90a-7b64-41fb-9c9f-8962703c8304'),
      [('Monitoring', 'Im Mangfallgebirge erfassen LBV-Kreisgruppe Miesbach und Landratsamt Miesbach die Brutpaare im LfU-Artenhilfsprogramm' + q('LfU – Artenhilfsprogramm Steinadler', 'https://www.lfu.bayern.de/natur/artenhilfsprogramme_voegel/steinadler/projektinhalt/index.htm')),
       ('Schutz', 'Hubschrauber halten 1.000 m Abstand zu besetzten Horsten (freiwillige Vereinbarung)' + q('LfU – Broschüre Steinadler & Hubschrauber', 'https://www.lfu.bayern.de/natur/artenhilfsprogramme_voegel/steinadler/freiwillige_vereinbarungen/doc/broschure_hubschrauber.pdf')),
       ('Schutzgebiet', 'Erhaltungsziel im SPA Mangfallgebirge' + q(*SPA_VO))], img='Steinadler.jpg', alt='Steinadler auf einer Stange'),
 CARD('uhu', 'Uhu', 'Bubo bubo', 'Felsbrüter wie Steinadler, Wanderfalke und Uhu brauchen störungsarme Wände' + q('LfU – Managementplan SPA 8433-471 (Maßnahmen, PDF)', 'https://www.lfu.bayern.de/natur/natura2000_managementplaene/8027_8672/doc/8433_471/texte/de8433471_t_mt_ffin_nfin.pdf') + '; im Mangfallgebirge ist der Uhu ausdrückliches Erhaltungsziel.' + q(*SPA_VO),
      [('Schutzgebiet', 'Erhaltungsziel im SPA Mangfallgebirge' + q(*SPA_VO))], img='uhu.jpg', alt='Uhu auf einem Ast'),
 CARD('sperlingskauz', 'Sperlingskauz & Raufußkauz', 'Glaucidium passerinum · Aegolius funereus', 'Zwei kleine Eulen der Bergwälder, die man eher hört als sieht. Beide sind Erhaltungsziele des Schutzgebiets.' + q(*SPA_VO),
      [('Schutzgebiet', 'beide Erhaltungsziel im SPA Mangfallgebirge' + q(*SPA_VO))], img='sperlingskauz.jpg', alt='Sperlingskauz auf einem Ast'),
 CARD('wanderfalke', 'Wanderfalke & Wespenbussard', 'Falco peregrinus · Pernis apivorus', 'Der Wanderfalke brütet in Felswänden' + q('Regierung von Oberbayern – Managementplan Ammergebirge (Entwurf, PDF)', 'https://www.regierung.oberbayern.bayern.de/mam/dokumente/bereich5/sg51/natura2000/mpl-entwuerfe/8330-471_8431-371_f_ammergebirge_rt.pdf') + '. Wanderfalke und Wespenbussard stehen beide auf der Liste der Erhaltungsziele.' + q(*SPA_VO),
      [('Schutzgebiet', 'beide Erhaltungsziel im SPA Mangfallgebirge' + q(*SPA_VO))], icon='🪶')]))

b.append(H2('wald-bach', '🌲 Wald- & Bachvögel') + GRID([
 CARD('spechte', 'Spechte des Bergwalds', 'Weißrücken-, Dreizehen-, Schwarz- und Grauspecht', 'Alle vier kommen laut Managementplan in den Wäldern des Mangfallgebirges vor. Weißrücken- und Dreizehenspecht gehören zu den charakteristischen Spechten der Alpen.' + q(*MPL_HANDOUT) + q('LBV/DDA – Monitoring von Alpenvögeln (PDF)', 'https://www.lbv.de/files/user_upload/Dokumente/LBV_Infoblaetter_kostenfrei/DDA-Monitoring/Vogel-in-Deutschland-Alpenvoegel.pdf'),
      [], icon='🪵'),
 CARD('wasseramsel', 'Wasseramsel', 'Cinclus cinclus', 'Der einzige heimische Singvogel, der schwimmen und tauchen kann – zu sehen an schnell fließenden Bächen, wo sie knicksend auf Steinen sitzt.' + q('NABU – Wasseramsel', 'https://www.nabu.de/tiere-und-pflanzen/voegel/portraets/wasseramsel/'),
      [('Nest', 'in der Uferböschung oder in Mauerlöchern, hohe Brutplatztreue' + q('NABU – Wasseramsel', 'https://www.nabu.de/tiere-und-pflanzen/voegel/portraets/wasseramsel/'))], icon='💧')]))

b.append(H2('saeugetiere', '🦌 Säugetiere') + GRID([
 CARD('gaemse', 'Gämse', 'Rupicapra rupicapra', 'In den bayerischen Alpen nutzt die Gams den Bergwald, die Almflächen und die Bereiche oberhalb der Baumgrenze.' + q('Bayerischer Landtag – Drucksache 18/18738 (Gamswild)', 'https://www.bayern.landtag.de/www/ElanTextAblage_WP18/Drucksachen/Schriftliche%20Anfragen/18_0018738.pdf'),
      [('Rote Liste Deutschland', 'seit Oktober 2020 auf der Vorwarnliste' + q('Bayerischer Landtag – Drucksache 18/12177 (Gämsen auf der Vorwarnliste)', 'https://www.bayern.landtag.de/www/ElanTextAblage_WP18/Drucksachen/Schriftliche%20Anfragen/18_0012177.pdf')),
       ('Jagdzeit', '1. August bis 15. Dezember' + q('Deutsche Wildtier Stiftung – Schutzwaldsanierung im Gamsrevier (PDF)', 'https://www.deutschewildtierstiftung.de/aktuelles/artikel/schutzwaldsanierung-gams/schutzwaldsanierung-gams_dewist_zielknflikteszah.pdf')),
       ('Forschung', 'Die LWF untersucht Gams-, Rot- und Rehwild im Projekt „Integrales Schalenwildmanagement im Bergwald“' + q('waldwissen.net – Integrales Schalenwildmanagement im Bergwald', 'https://www.waldwissen.net/de/lebensraum-wald/wald-und-wild/integrales-schalenwildmanagement-im-bergwald'))], img='gaemse.jpg', alt='Gämse am Steilhang'),
 CARD('rothirsch', 'Rothirsch', 'Cervus elaphus', 'Das Geweih wird im Februar abgeworfen und ist zur Brunft im September wieder komplett. Der Rothirsch ist Wildtier des Jahres 2026.' + q('NABU – Rothirsch', 'https://www.nabu.de/tiere-und-pflanzen/saeugetiere/sonstige-saeugetiere/30840.html') + q('NABU – Der Rothirsch ist Wildtier des Jahres 2026', 'https://www.nabu.de/natur-und-artenwissen/saeugetiere/portraets-saeugetiere/der-rothirsch-ist-wildtier-des-jahres-2026'),
      [('In Bayern', 'nur in zehn gesetzlich festgelegten Rotwildgebieten' + q('LWF/waldwissen – Rotwild in Bayern: Populationsstrukturen (PDF)', 'https://www.waldwissen.net/assets/wald/wild/oekologie/lwf_rotwild_genetik/a159_s14-17_koenig.pdf')),
       ('Störung', 'Schon eine Person pro Woche, die ein Rotwildgebiet betritt, kann dazu führen, dass die Tiere es um 300–500 m meiden' + q('NABU – Rothirsch', 'https://www.nabu.de/tiere-und-pflanzen/saeugetiere/sonstige-saeugetiere/30840.html'))], img='rothirsch-und-almen.jpg', alt='Rothirsch mit Bastgeweih'),
 CARD('fuchs', 'Rotfuchs, Reh & Co.', 'Vulpes vulpes · Capreolus capreolus', 'Fuchs, Reh, Dachs und Marder sind im Bergwald verbreitet, aber scheu. Der Fuchs ist Hauptwirt des Fuchsbandwurms – mehr dazu bei den Sammelregeln.' + q('ÖKO-TEST – Fuchsbandwurm', 'https://www.oekotest.de/gesundheit-medikamente/Baerlauch-Walderdbeeren-Pilze-So-gefaehrlich-ist-der-Bandwurm-wirklich_12737_1.html'),
      [('Weiter', '<a href="/content/botanik/#sammeln">Beeren, Pilze &amp; Fuchsbandwurm</a>')], img='tier-fuchs.jpg', alt='Rotfuchs'),
 CARD('murmeltier', 'Murmeltier – eher nicht hier', 'Marmota marmota', 'Murmeltiere leben in Deutschland vor allem in den Kalkhochalpen: Berchtesgadener Alpen, Karwendel, Wetterstein und Allgäuer Alpen.' + q('DAV – Das Murmeltier', DAV + 'das-murmeltier_f9a8c3e1-564a-4ef5-b3f7-f1e515cfe005')
      + ' In den Voralpen kommen sie mitunter ab 1.100 m vor' + q('DAV – Das Murmeltier (Kurzführer)', 'https://www.alpenverein.de/natur/naturschutzverband/tiere-der-alpen/das-murmeltier_aid_31841.html') + ' – ein gesichertes Vorkommen im Mangfallgebirge haben wir nicht belegt gefunden.',
      [('Status Bayern', 'nicht gefährdet, unterliegt dem Jagdrecht ohne Jagdzeit' + q('DAV – Das Murmeltier', DAV + 'das-murmeltier_f9a8c3e1-564a-4ef5-b3f7-f1e515cfe005')), ('Hinweis', 'Wer eines sieht: gern melden, z. B. bei Projekten wie Wildes Bayern' + q('DAV – Das Murmeltier (Kurzführer)', 'https://www.alpenverein.de/natur/naturschutzverband/tiere-der-alpen/das-murmeltier_aid_31841.html'))], icon='❓')]))

b.append(H2('reptilien', '🦎 Reptilien & Amphibien') + GRID([
 CARD('kreuzotter', 'Kreuzotter', 'Vipera berus', 'Die einzige Giftschlange Bayerns. Bayernweit stark gefährdet, außerhalb der Alpen sogar vom Aussterben bedroht.' + q('LfU – Kreuzottern: faszinierend und gefährdet (PDF)', 'https://www.lfu.Bayern.de/buerger/doc/uw_114_kreuzottern_faszinierend_und_gefaehrdet.pdf') + q('LfU – Pressemitteilung Kreuzotter (Februar 2026)', 'https://www.lfu.bayern.de/pressemitteilungen/c/2219175/'),
      [('Rote Liste Bayern', '2 – stark gefährdet' + q('LfU – Reptilien in Bayern', 'https://www.lfu.bayern.de/natur/bayaz/artenschutz_tiere/reptilien/index.htm')), ('Begegnung', 'Abstand halten, nicht anfassen; alle heimischen Schlangen stehen unter Naturschutz' + q('LfU – Merkblatt Kreuzotter (via Landkreis Schwandorf, PDF)', 'https://www.landkreis-schwandorf.de/media/custom/727_504_1.PDF'))], img='Kreuzotter.jpg', alt='Kreuzotter im Moos'),
 CARD('alpensalamander', 'Alpensalamander', 'Salamandra atra', 'Pechschwarz und lebendgebärend: Die Weibchen bringen ein bis zwei voll entwickelte, rund vier Zentimeter große Junge zur Welt. Lurch des Jahres 2026.' + q('NABU – Der Alpensalamander ist Lurch des Jahres 2026', 'https://www.nabu.de/natur-und-artenwissen/amphibien-und-reptilien/portraets-amphibien-und-reptilien/der-alpensalamander-ist-lurch-des-jahres-2026'),
      [('Verbreitung', 'in Deutschland im gesamten bayerischen Alpenraum, dazu kleine Vorkommen im Grenzgebiet zu Baden-Württemberg' + q('Rote-Liste-Zentrum – Alpensalamander (PDF)', 'https://www.rote-liste-zentrum.de/detail/pdf/54046')), ('Schutz', 'FFH-Anhang IV, streng geschützt' + q('waldwissen.net – Pechschwarz und einzigartig: der Alpensalamander', 'https://www.waldwissen.net/de/lebensraum-wald/tiere-im-wald/reptilien-amphibien/pechschwarz-und-einzigartig-der-alpensalamander')),
       ('Wann sehen', 'meist erst bei Regenwetter' + q('LWF – Merkblatt 49 Amphibien (PDF)', 'https://www.lwf.bayern.de/mam/cms04/service/dateien/mb49_amphibien_rz_web_bf.pdf'))], icon='🦎'),
 CARD('waldeidechse', 'Waldeidechse', 'Zootoca vivipara', 'Bei der LfU-Kartierung im Landkreis Miesbach die am häufigsten beobachtete Eidechse – im ganzen Landkreis verbreitet.' + q('LfU – Pressemitteilung Naturschutzfachkartierung Landkreis Miesbach (2024)', 'https://www.lfu.bayern.de/pressemitteilungen/c/2021871/'), [], icon='☀️')]))

b.append(H2('verhalten', '🤫 Rücksicht unterwegs')
 + UL(['<strong>Wildschutzgebiete einhalten:</strong> Im Landkreis Miesbach gilt dort ein Betretungsverbot vom 1. Dezember bis 14. Juli – im Winter und während Balz, Brut und Aufzucht.' + q('Alpenverein München & Oberland – Wildschutzgebiet Rotwandgebiet', 'https://www.alpenverein-muenchen-oberland.de/umwelt/naturvertraeglicher-bergsport-im-winter/wildschutzgebiet-rotwandgebiet') + ' Die Gebiete sind in der App alpenvereinaktiv eingezeichnet.' + q('Alpenverein München & Oberland – Was ist ein Wildschutzgebiet?', 'https://www.alpenverein-muenchen-oberland.de/obacht-geben/wald-wild-schongebiete-und-schutzgebiete-in-den-bergen-erkennen/was-ist-ein-wildschutzgebiet'),
       '<strong>Keine Feierabendtouren in der Dämmerung</strong> durch Raufußhuhn-Lebensräume: Genau dann suchen die Tiere Nahrung.' + q('Alpenverein München & Oberland – Rückzugsräume für Wildtiere', 'https://www.alpenverein-muenchen-oberland.de/umwelt/naturvertraeglicher-bergsport-im-winter/rueckzugsraeume-fuer-wildtiere-in-den-alpen-wald-wild-schongebiete-und-wildschutzgebiete-bitte-nicht-betreten'),
       '<strong>Im Winter Energie sparen lassen:</strong> Wiederholtes Aufschrecken kann für Wildtiere auf Dauer lebensbedrohlich werden.' + q('DAV – Wald-Wild-Schongebiete', DAV + 'wald-wild-schongebiete-winter-tierschutz_0cd10648-a795-46f8-838d-48d5734b7f37'),
       '<strong>Gesetzlich:</strong> Wild lebende Tiere mutwillig zu beunruhigen ist verboten (§ 39 BNatSchG).' + q('§ 39 BNatSchG (gesetze-im-internet.de)', 'https://www.gesetze-im-internet.de/bnatschg_2009/__39.html')])
 + P('Mehr zu Wetter und Lawinenlage: <a href="/wetter-webcams.html">Wetter &amp; Webcams</a>.'))
b.append(q.liste())
seite('content/fauna/index.html', 'Tierwelt im Mangfallgebirge – Raufußhühner, Steinadler, Gämse & Co.',
      '🦅 Tierwelt im Mangfallgebirge', 'Welche Tiere rund um Spitzingsee und Rotwand wirklich vorkommen, wie gefährdet sie sind und wie du sie nicht störst – belegt mit Managementplan, LfU, DAV und NABU.',
      HERO('gaemse.jpg', 'Gämse am Steilhang'), [('schutzgebiet', '🗺️ Schutzgebiet'), ('raufusshuehner', '🐓 Raufußhühner'), ('greifvoegel', '🦅 Greifvögel'), ('wald-bach', '🌲 Wald & Bach'), ('saeugetiere', '🦌 Säugetiere'), ('reptilien', '🦎 Reptilien'), ('verhalten', '🤫 Rücksicht'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Tierwelt im Mangfallgebirge mit Quellen: Birkhuhn im Wildschutzgebiet Rotwand, Auerhuhn, Steinadler, Gämse, Rothirsch, Kreuzotter, Alpensalamander – und warum das Murmeltier hier kaum vorkommt.', 'Tierwelt',
      'Weiter: <a href="/content/botanik/">Pflanzenwelt</a> · <a href="/huetten.html">Hüttenführer</a> · <a href="/content/wandern/index.html">Wandern</a>')

# =================== PFLANZENWELT ===================
q = Q(); b = []
b.append(H2('bergwald', '🌲 Bergwald, Latschen & Höhenstufen')
 + P('Der Bergwald der bayerischen Alpen liegt fast ausschließlich in der montanen Höhenstufe. Von Natur aus wächst dort Bergmischwald aus Fichte, Buche und Tanne, dazu Bergahorn und Lärche.' + q('Bayerische Staatsforsten – Grundsätze Bergwald (PDF)', 'https://www.baysf.de/sites/default/files/doc/grunds-2.PDF')
     + ' Die Tanne deckt heute nur noch rund 7 % der Waldfläche im Gebirge ab.' + q('LWF Wissen 49 – Bergwald im Hochgebirge (PDF)', 'https://www.lwf.bayern.de/mam/cms04/service/dateien/w49_bergwald_im_hochgebirge_gesch.pdf'))
 + BOX('<strong>Rekord aus unserem Gebirge:</strong> Die höchste in der Vegetationsdatenbank der bayerischen Alpen gefundene baumförmige Buche steht im Mangfallgebirge – auf 1.530 m.' + q('LWF aktuell 71 – Wo der Wald an Grenzen stößt (PDF)', 'https://lwg.bayern.de/mam/cms04/boden-klima/dateien/a71-wo-der-wald-an-grenzen-stoesst.pdf'))
 + P('Über dem Wald folgen Latschen- und Alpenrosengebüsche (Latsche mit Bewimperter Alpenrose). Sie sind im FFH-Gebiet Mangfallgebirge ein eigener, prioritärer Lebensraumtyp (4070*).' + q('LfU – Erhaltungsziele FFH-Gebiet 8336-371 Mangfallgebirge (PDF)', 'https://www.lfu.bayern.de/natur/natura_2000_vollzugshinweise_erhaltungsziele/8027_8672/doc/8336_371.pdf')))

b.append(H2('wiesen', '🌼 Almwiesen & Rasen')
 + P('Sieben verschiedene Rasengesellschaften der FFH-Richtlinie kommen im Mangfallgebirge vor – darunter alpine und subalpine Kalkrasen; typische Blüten sind Flockenblume, Silberdistel sowie mehrere Enzian- und Orchideenarten.' + q('BUND Naturschutz – Natura-2000-Wanderung Mangfallgebirge/Rotwand (PDF)', 'https://www.bund-naturschutz.de/fileadmin/Bilder_und_Dokumente/Themen/Natur_und_Landschaft/Natura_2000/natura2000wanderungen/Tour_7_Mangfallgebirge_Rotwand.pdf')
     + ' Beweidete Almen zeigen eine besonders hohe Artenvielfalt – die Almwirtschaft ist hier Teil des Naturschutzes.' + q('Vetmeduni Wien / FIWI – Murmeltiere mit Pfiff (PDF)', 'https://www.vetmeduni.ac.at/fileadmin/v/fiwi/Fotos_f%C3%BCr_FIWI_Newsberichte/20190703_Newsmeldung_Murmeltiere_MitPfiff_LL0419-Murmeltier-Hofmann.pdf')))

b.append(H2('arten', '🌸 Typische Arten') + GRID([
 CARD('alpenrose', 'Alpenrosen', 'Rhododendron hirsutum · R. ferrugineum', 'Zwei Arten, die man am Boden unterscheidet: Die Bewimperte Alpenrose wächst ausschließlich auf Kalk, die Rostblättrige braucht sauren Boden.' + q('DAV – Typisch … Rostblättrige Alpenrose', DAV + 'die-rostblattrige-alpenrose_b904b4e5-c1fa-4ef9-81a5-2679d295f4cf'),
      [('Erkennen', 'Bewimperte: kleine Wimpernhaare am Blattrand' + q('hoehenrausch.de – Bewimperte Alpenrose', 'https://www.hoehenrausch.de/alpenblumen/bewimperte-alpenrose/') + '; Rostblättrige: Blattunterseite rostbraun' + q('DAV – Typisch … Rostblättrige Alpenrose', DAV + 'die-rostblattrige-alpenrose_b904b4e5-c1fa-4ef9-81a5-2679d295f4cf')),
       ('Blüte', 'Rostblättrige von Juni bis in den August' + q('DAV – Typisch … Rostblättrige Alpenrose', DAV + 'die-rostblattrige-alpenrose_b904b4e5-c1fa-4ef9-81a5-2679d295f4cf')),
       ('Hier', 'Bewimperte Alpenrose mit Latsche ist geschützter FFH-Lebensraum im Mangfallgebirge' + q('LfU – Erhaltungsziele FFH-Gebiet 8336-371 Mangfallgebirge (PDF)', 'https://www.lfu.bayern.de/natur/natura_2000_vollzugshinweise_erhaltungsziele/8027_8672/doc/8336_371.pdf')), ('Bitte', 'nicht abreißen')],
      img='blume-alpenrose.jpg', alt='Blühende Alpenrose'),
 CARD('enzian', 'Enziane', 'Gentiana spp.', 'Alle Enziane sind besonders geschützt und dürfen nicht gepflückt werden.' + q('NABU – Pflücken verboten?', 'https://www.nabu.de/tiere-und-pflanzen/pflanzen/pflanzen-schuetzen/blumen-pfluecken.html')
      + ' Clusius-Enzian (Kalk) und Koch-Enzian (Silikat) sind ein klassisches Paar, das sich nach dem Untergrund aufteilt.' + q('DAV Wasserburg – Alpenrosen und vikariierende Arten (PDF)', 'https://www.alpenverein-wasserburg.de/wp-content/uploads/2017/06/Alpenrosen.pdf'),
      [('Schnaps', '„Bayerischer Gebirgsenzian“ (geschützte geografische Angabe) wird aus den Wurzeln von Gelbem, Purpur-, Tüpfel- oder Ungarischem Enzian gebrannt' + q('EU – Eintragung „Bayerischer Gebirgsenzian“', 'https://ec.europa.eu/geographical-indications-register/eambrosia-public-api/api/v1/attachments/49185')),
       ('Schutz', 'besonders geschützt – Pflücken und Ausgraben verboten' + q('NABU – Pflücken verboten? (Naturtipps)', 'https://www.nabu.de/natur-erleben/naturtipps/pfluecken-verboten'))], img='blume-enzian.jpg', alt='Stängelloser Enzian am Kalkfels'),
 CARD('arnika', 'Arnika (Bergwohlverleih)', 'Arnica montana', 'Die gelbe Heilpflanze wächst auf bodensauren Magerrasen. Achtung, Verwechslung auf vielen Seiten: „Bergwohlverleih“ ist die Arnika – nicht das Edelweiß.' + q('BfN – Arnika (PDF)', 'https://www.bfn.de/sites/default/files/BfN/natura2000/Dokumente/pfl_arnimont.pdf'),
      [('Rote Liste', 'Bayern und Deutschland: gefährdet (3)' + q('LfU – Merkblatt Artenschutz 42: Echte Arnika (PDF)', 'https://www.lfu.bayern.de/natur/artenhilfsprogramme/merkblaetter_botanik/doc/42blfumerkblatt_echte_arnika.pdf')),
       ('Schutz', 'besonders geschützt' + q('NABU – Pflücken verboten?', 'https://www.nabu.de/tiere-und-pflanzen/pflanzen/pflanzen-schuetzen/blumen-pfluecken.html')), ('Gefährdung', 'u. a. durch unachtsame Pflege von Almen' + q('LfU – Merkblätter Botanik', 'https://www.lfu.bayern.de/natur/artenhilfsprogramme/merkblaetter_botanik/index.htm'))], icon='🌼'),
 CARD('orchideen', 'Orchideen & Frauenschuh', 'Orchidaceae · Cypripedium calceolus', 'Sämtliche wild wachsenden Orchideen sind besonders geschützt.' + q('NABU – Pflücken verboten?', 'https://www.nabu.de/tiere-und-pflanzen/pflanzen/pflanzen-schuetzen/blumen-pfluecken.html')
      + ' Der Frauenschuh ist im FFH-Gebiet Mangfallgebirge als Art des Anhangs II erfasst – sein Fundort wird wegen besonderer Gefährdung nicht dargestellt.' + q('Regierung von Oberbayern – Managementplan FFH 8336-371, Karte 2 Bestand (PDF)', 'https://regierung.oberbayern.bayern.de/mam/dokumente/bereich5/sg51/natura2000/mpl-entwuerfe/8336-371_karte2_4_a1.pdf'),
      [('Bitte', 'auch nicht für ein Foto vom Weg abgehen und niemandem Fundorte weitergeben')], icon='🌺'),
 CARD('edelweiss', 'Edelweiß', 'Leontopodium nivale subsp. alpinum', 'Das Symbol der Alpen ist in den Kalkalpen sehr selten – laut DAV darf man sich äußerst glücklich schätzen, wenn man eines findet.' + q('DAV – Typisch … Edelweiß', DAV + 'das-alpen-edelweiss_249617f9-e31c-4f8c-98bd-f9f4b81c9dcf') + ' Ein Vorkommen im Mangfallgebirge haben wir nicht belegt gefunden.',
      [('Name', 'botanisch Leontopodium nivale subsp. alpinum (oft L. alpinum)' + q('hoehenrausch.de – Edelweiß', 'https://www.hoehenrausch.de/alpenblumen/edelweiss/'))], icon='⭐')]))

b.append(H2('sammeln', '🧺 Sammeln: was erlaubt ist')
 + P('Grundsätzlich ist es verboten, wild wachsende Pflanzen ohne vernünftigen Grund zu entnehmen. Die Ausnahme ist die sogenannte Handstraußregel: Blumen, Gräser, Farne, Moose, Flechten, Früchte, Pilze, Tee- und Heilkräuter dürfen in geringen Mengen für den persönlichen Bedarf pfleglich entnommen werden – an Stellen ohne Betretungsverbot.' + q('§ 39 BNatSchG (gesetze-im-internet.de)', 'https://www.gesetze-im-internet.de/bnatschg_2009/__39.html') + q('anwalt24 – Lexikon Artenschutz', 'https://www.anwalt24.de/lexikon/artenschutz'))
 + UL(['<strong>Wie viel?</strong> So viel, wie man zwischen Daumen und Zeigefinger umfassen kann.' + q('ÖKO-TEST – Blumen pflücken unterwegs', 'https://www.oekotest.de/freizeit-technik/Blumen-pfluecken-unterwegs-Erlaubt-oder-verboten_13977_1.html'),
       '<strong>Nie bei geschützten Arten:</strong> Besonders geschützte Arten dürfen weder ganz noch teilweise abgepflückt oder ausgegraben werden – dazu zählen alle Enziane, Arnika und alle wilden Orchideen.' + q('NABU – Pflücken verboten? (Naturtipps)', 'https://www.nabu.de/natur-erleben/naturtipps/pfluecken-verboten') + q('NABU – Pflücken verboten?', 'https://www.nabu.de/tiere-und-pflanzen/pflanzen/pflanzen-schuetzen/blumen-pfluecken.html'),
       '<strong>Pilze:</strong> Von den geschützten Pilzen sind Steinpilz, alle Pfifferlinge, Schweinsohr, Brätling sowie Birkenpilz und Rotkappe in geringen Mengen für den eigenen Bedarf freigegeben.' + q('Bundesartenschutzverordnung § 2 (via CMS, PDF)', 'https://www.cms.int/cami/sites/default/files/document/cms_nlp_deu_regulation_species_2005.pdf'),
       '<strong>Bärlauch</strong> ist nicht geschützt – nur ein bis zwei Blätter pro Pflanze nehmen und die Knospen stehen lassen.' + q('ANL – Bayern natürlich (PDF)', 'https://www.anl.bayern.de/publikationen/weitere_publikationen/doc/bayern_natuerlich.pdf')])
 + BOX('<strong>Fuchsbandwurm:</strong> Eine Infektion ist selten, aber gefährlich. Waschen von Beeren und Kräutern senkt das Risiko, beseitigt es aber nicht; Erhitzen auf mindestens 60 °C für wenige Minuten tötet die Eier zuverlässig ab.' + q('ÖKO-TEST – Beeren im Wald: Wie gefährlich ist der Fuchsbandwurm? (mit Angaben des LGL)', 'https://www.oekotest.de/gesundheit-medikamente/Beeren-im-Wald-Wie-gefaehrlich-ist-der-Fuchsbandwurm-wirklich_12737_1.html') + q('ÖKO-TEST – Bärlauch und Beeren: Fuchsbandwurm', 'https://www.oekotest.de/gesundheit-medikamente/Baerlauch-und-Beeren-im-Wald-Wie-gefaehrlich-ist-der-Fuchsbandwurm-wirklich_12737_1.html'), '#fff7ed', '#c2410c'))
b.append(q.liste())
seite('content/botanik/index.html', 'Pflanzenwelt im Mangfallgebirge – Bergwald, Alpenrosen, Enzian, Orchideen',
      '🌸 Pflanzenwelt im Mangfallgebirge', 'Vom Bergmischwald über Latschen und Almwiesen bis zu Alpenrose, Enzian, Arnika und Frauenschuh – was hier wächst, was geschützt ist und was du sammeln darfst. Mit Quellen von LfU, LWF, DAV und NABU.',
      HERO('alpenblumen.jpg', 'Alpenrosen an einem Bergsee (Symbolbild)'), [('bergwald', '🌲 Bergwald'), ('wiesen', '🌼 Almwiesen'), ('arten', '🌸 Arten'), ('sammeln', '🧺 Sammeln'), ('quellen', '📚 Quellen')],
      ''.join(b), 'Pflanzenwelt im Mangfallgebirge mit Quellen: Bergmischwald, Latschen-Alpenrosengebüsch, Almwiesen, Alpenrosen, Enziane, Arnika, Frauenschuh, Edelweiß – und die Regeln zum Sammeln.', 'Pflanzenwelt',
      'Weiter: <a href="/content/fauna/">Tierwelt</a> · <a href="/content/wandern/index.html">Wandern</a> · <a href="/huetten.html">Hüttenführer</a>')
