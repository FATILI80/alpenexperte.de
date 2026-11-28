#!/usr/bin/env python3
"""Naturwissenschaften: Geologie, Limnologie (Seen), Moore, Forstwirtschaft – kompakte, belegte Seiten. Meteorologie wird auf die Wetter-Seite geleitet."""
import sys; sys.path.insert(0, 'routing')
from kern import Q, CARD, seite, H2, P, BOX, GRID, FIG, UL, TAB

WEITER = 'Weiter: <a href="/content/geologie/">Geologie</a> · <a href="/content/limnologie/">Seen</a> · <a href="/content/moore/">Moore</a> · <a href="/content/forstwirtschaft/">Bergwald</a> · <a href="/wetter-webcams.html">Wetter</a>'

# ---------------- GEOLOGIE ----------------
q = Q()
TUM = ('Nickmann & Thuro (TUM): Kössener Mergel als Schlüsselhorizont für Hangbewegungen im Spitzingseegebiet (PDF)', 'https://mediatum.ub.tum.de/download/1138103/1138103.pdf')
PLO = ('Plöchinger: Die Nördlichen Kalkalpen, in: Der geologische Aufbau Österreichs (1980, PDF)', 'https://opac.geologie.ac.at/ais312/dokumente/Oberhauser_1980_218_264.pdf')
DAC = ('Dacqué (1912): Geologische Aufnahme des Gebietes um den Schliersee und Spitzingsee (PDF)', 'https://opac.geologie.ac.at/ais312/dokumente/Dacque_1912_Schliersee.pdf')
KIR = ('Kirsch: Kalkgraben-Schichten vom Schliersee – Mitt. Bayer. Staatsslg. Paläont. 40 (PDF)', 'https://www.zobodat.at/pdf/Mitt-Bayer-Staatsslg-Pal-hist-Geol_40_0003-0079.pdf')
USP = ('unser-stadtplan.de – Schliersee (Geologie der Seeschwelle)', 'https://m.unser-stadtplan.de/Stadtplan/Schliersee/map/Stadtplan-Schliersee.map')
LFU35 = ('Bayer. Geologische Landesuntersuchung (1935) – Eiszeitliche Gletscher im Tegernseer Gebiet (PDF)', 'https://www.lfu.bayern.de/geologie/geo_karten_schriften/historische_schriften/doc/1935_18.pdf')
BNH = ('BN Miesbach – Deglaziationschronologie Raum Holzkirchen (PDF)', 'https://miesbach.bund-naturschutz.de/fileadmin/kreisgruppen/miesbach/Holzkirchen/dateien/gemeindeblatt/2005_gb-ergaenzung-Deglaziationschronologie_Raum_Holzkirchen.pdf')
GEO = ('Geologica Bavarica 73 – Die oberbayerische Pechkohle (1975, PDF)', 'https://www.stmwi.bayern.de/fileadmin/user_upload/stmwi/Energie/Bodensch%C3%A4tze/1975-Die_oberbayerische_Peckkohle_Geologica_Bavarica_Nr_73.pdf')
b = []
b.append(H2('zonen', '🪨 Drei Zonen auf wenigen Kilometern', 'Von Hausham bis zur Rotwand quert man drei völlig verschiedene Gesteinswelten.'))
b.append(TAB(['Zone', 'Wo', 'Was man wissen sollte'], [
    ('Faltenmolasse', 'Hausham, Miesbach', 'Hier lag die oberbayerische Pechkohle, die bis 1966 bzw. 1971 abgebaut wurde' + q(*GEO) + ' – siehe <a href="/content/kultur_geschichte/#bergbau">Bergbau</a>'),
    ('Flysch', 'um den Schliersee', 'Die Kalkgraben-Schichten des Flysches am Schliersee stammen aus der Oberkreide (Campan)' + q(*KIR) + '; Seeschwelle und Insel Wörth bestehen aus diesem Material, Typlokalität ist der ehemalige Steinbruch Kalkgraben' + q(*USP)),
    ('Nördliche Kalkalpen', 'Spitzingsee, Rotwand, Brecherspitz', 'Typisch ist die Hauptdolomit-Fazies mit Hauptdolomit, Plattenkalk, Kössener Schichten und Oberrhätkalk' + q(*PLO)),
]))
b.append(GRID([
 CARD('koessen', 'Kössener Schichten', 'Trias · weit verbreitet am Spitzingsee',
      'Im Spitzingseegebiet steht die Kössen-Formation weit verbreitet an; vor allem die weichen Kössener Mergel sind eng mit Hangbewegungen verknüpft.' + q(*TUM),
      [('Für Wanderer', 'Wo die Mergel anstehen, sind Wege nach Regen oft rutschig und Hänge kriechen – nicht wegen schlechter Pflege, sondern wegen des Gesteins' + q(*TUM))], icon='⛰️'),
 CARD('dacque', 'Erste genaue Karte', '1912',
      'Edgar Dacqué veröffentlichte 1912 die geologische Aufnahme des Gebiets um Schliersee und Spitzingsee; er nutzte dafür auch Aufschlüsse, die beim Bau der Bahn Schliersee–Bayrischzell entstanden.' + q(*DAC), [], icon='🗺️'),
]))
b.append(H2('eiszeit', '🧊 Die Eiszeit hat die Seen geformt', 'In der Würm-Eiszeit lagen die Täler unter Eis – auch der Spitzingsattel.'))
b.append(P('Nach der Beschreibung der Bayerischen Geologischen Landesuntersuchung von 1935 floss in der Würm-Eiszeit ein Arm des Brandenberger Eises über den Spitzingsattel.' + q(*LFU35)
           + ' Beim Abschmelzen entstanden in einer Phase, als die Eisgrenze bei etwa 1.000 m lag, der Ur-Tegernsee und der Ur-Schliersee.' + q(*BNH)))
geologie = (b, q)

# ---------------- LIMNOLOGIE ----------------
q2 = Q()
SV = ('Bayer. Schlösserverwaltung – Spitzingsee', 'https://schloesser.bayern.de/englisch/lakes/objects/spitzing.htm')
WEN = ('Wikipedia – Spitzingsee', 'https://en.wikipedia.org/wiki/Spitzingsee')
WVS = ('Wikivoyage – Spitzingsee', 'https://de.wikivoyage.org/wiki/Spitzingsee')
LAU79 = ('Laufener Seminarbeiträge 3/1979 – Seensanierung in Bayern (PDF)', 'https://www.zobodat.at/pdf/Laufener-Spez-u-Seminarbeitr_3_1979_0044-0068.pdf')
LAU97 = ('Laufener Seminarbeiträge 3/1997 – Wasserwirtschaft und Gewässerökologie (PDF)', 'https://www.zobodat.at/pdf/Laufener-Spez-u-Seminarbeitr_3_1997_0011-0015.pdf')
MUC = ('muenchen.de – Tegernsee', 'https://www.muenchen.de/int/en/culture-leisure/sport-fitness/tegernsee.html')
b = []
b.append(H2('seen', '💧 Drei Seen, drei Charaktere', 'Höhe, Fläche und Tiefe im direkten Vergleich stehen auf der Region-Seite.'))
b.append(P('Der <a href="/content/regional/#vergleich">Seen-Vergleich</a> zeigt Spitzingsee, Schliersee und Tegernsee nebeneinander – mit Quellen für jede Zahl. Hier geht es darum, wie die Seen funktionieren.'))
b.append(GRID([
 CARD('spitzingsee', 'Spitzingsee', '1.084 m · 28 ha',
      'Mit 28 Hektar ist er laut Schlösserverwaltung Bayerns größter Bergsee.' + q2(*SV) + ' Er hat mit 7,51 km² ein vergleichsweise großes Einzugsgebiet; Zuflüsse sind Lochgraben und Firstgraben, der Abfluss ist die Rote Valepp.' + q2(*WEN),
      [('Winter', 'Wegen der Höhenlage friert der See sehr schnell zu und überschneit dann' + q2(*WVS)),
       ('Wasserscheide', 'Der Abfluss geht nach Süden zum Inn, nicht zur Mangfall – siehe <a href="/content/regional/#vergleich">Region</a>')], icon='🏔️'),
 CARD('tegernsee', 'Tegernsee', 'Vorbild der Seensanierung',
      'Zu Beginn des 20. Jahrhunderts noch nährstoffarm, war der Tegernsee bis Mitte der 1950er durch Abwasser eutroph geworden. Dagegen entstand die weltweit erste Ringkanalisation, 1965 mit einer Sammelkläranlage für 60.000 Einwohnerwerte vollendet; die Sanierung kostete rund 40 Mio. DM.' + q2(*LAU79),
      [('Schliersee', 'Nicht lange nach dem Tegernsee folgte auch der Schliersee mit einer Ringkanalisation' + q2(*LAU97)),
       ('Entstehung', 'Vor rund 18.000 Jahren füllte sich ein Gletscherbecken mit Wasser; heute ist der See 6,5 km lang und 1,5 km breit' + q2(*MUC))], icon='🌊'),
]))
b.append(BOX('<strong>Eis ist kein Weg:</strong> Dass der Spitzingsee früh zufriert, heißt nicht, dass das Eis trägt. Zuflüsse und Abfluss halten Stellen offen oder dünn – Eis nur betreten, wenn die Gemeinde es ausdrücklich freigibt.', '#fef2f2', '#b91c1c'))
limno = (b, q2)

# ---------------- MOORE ----------------
q3 = Q()
LTM = ('Bayerischer Landtag – Drucksache 18/4536: Moore und Moorrenaturierung in Oberbayern (PDF)', 'https://www1.bayern.landtag.de/www/ElanTextAblage_WP18/Drucksachen/Schriftliche%20Anfragen/18_0004536.pdf')
BNM = ('Bund Naturschutz – Pressemitteilung Moorrenaturierung im Alpenraum (PDF)', 'https://bund-naturschutz.de/fileadmin/_migrated/news_uploads/PM_FA_39_08_Moore_Alpenvorland_ccalps.pdf')
LRA = ('Landratsamt Bad Tölz – NSG Ellbach- und Kirchseemoor: Hochmoor-Renaturierung (PDF)', 'https://lra-toelz.de/export/download.php?id=3926')
WAT = ('Regierung von Oberbayern – FFH-Gebiet Wattersdorfer Moor (PDF)', 'https://www.regierung.oberbayern.bayern.de/mam/dokumente/bereich5/sg51/natura2000/mpl-entwuerfe/8137_301_n_wattersdorf_rt.pdf')
b = []
b.append(H2('moore', '🌿 Moore im Landkreis Miesbach', 'Klein, aber wichtig – fürs Klima und für Spezialisten unter Pflanzen und Tieren.'))
b.append(P('Laut Moorbodenkarte des LfU gibt es im Landkreis Miesbach 33 Hochmoore mit zusammen 238 Hektar. Entwässerte Moore verursachen rund 6 Prozent der klimarelevanten Emissionen Bayerns.' + q3(*LTM)))
b.append(GRID([
 CARD('renaturierung', 'Wiedervernässung', 'so funktioniert Renaturierung',
      'Der erste Schritt einer Hochmoor-Renaturierung ist die Wiedervernässung mit Regenwasser: Alle Entwässerungsgräben werden verschlossen.' + q3(*LRA),
      [('Klima', 'Naturnahe Moore speichern je nach Ausgangslage bis zu 5.000 kg Kohlenstoff pro Hektar und Jahr' + q3(*BNM)),
       ('Vor Ort', 'Der BN Miesbach arbeitet u. a. in den Mariensteiner Mooren' + q3(*BNM))], icon='💧'),
 CARD('wattersdorf', 'Wattersdorfer Moor', 'FFH-Gebiet · Landkreis Miesbach',
      'Die Wälder im FFH-Gebiet nehmen im voralpinen Hügelland des Landkreises wegen ihrer Ausprägung und naturnahen Abfolge eine besondere Stellung ein.' + q3(*WAT), [], icon='🌲'),
]))
b.append(BOX('Moore sind trittempfindlich: auf Wegen und Stegen bleiben, Hunde anleinen. Welche Pflanzen in feuchten Lagen am Spitzing wachsen, steht in der <a href="/content/botanik/">Pflanzenwelt</a>.'))
moore = (b, q3)

# ---------------- FORST ----------------
q4 = Q()
BWP = ('Bergwaldprojekt – Dossier Schliersee (PDF)', 'https://bergwaldprojekt.de/sites/default/files/bwp_schliersee_dossier.pdf')
N2K = ('BaySF – Natura-2000-Gebiete im Forstbetrieb Schliersee (Stand 01.12.2025, PDF)', 'https://www.baysf.de/index.php/system/files/doc/natura-2000-schliersee.pdf')
SCH = ('BaySF – Schaufütterung Spitzingsee (PDF)', 'https://www.baysf.de/system/files/doc/schaufuetterung-spitzingsee.pdf')
BWR = ('LWF aktuell 1/2019 – Die Bergwaldrichtlinie der BaySF (PDF)', 'https://lfl.bayern.de/mam/cms04/waldbau-bergwald/dateien/a120_bergwaldrichtlinie_baysf.pdf')
JVS = ('Jahrbuch Verein zum Schutz der Bergwelt 72 (2007): Staatswald im Hochgebirge (PDF)', 'https://www.zobodat.at/pdf/Jb-Verein-Schutz-Bergwelt_72_2007_0133-0140.pdf')
LSG = ('Landkreis Miesbach – Verordnung LSG „Spitzingsee und Umgebung“ (Entwurf, PDF)', 'https://www.landkreis-miesbach.de/media/custom/2823_6641_1.PDF?1763630337')
b = []
b.append(H2('bergwald', '🌲 Bergwald ist Schutzwald', 'Am Spitzing geht es im Wald weniger um Holz als um Schutz vor Lawinen, Steinschlag und Erosion.'))
b.append(P('Über zwei Drittel der von den Bayerischen Staatsforsten im Hochgebirge bewirtschafteten Waldfläche sind gesetzlicher Schutzwald; seine wichtigste Funktion ist der Schutz von Menschen, Siedlungen und Infrastruktur.' + q4(*BWR)
           + ' Der Hochgebirgswald liefert nur gut 7 % des geplanten Holzeinschlags der BaySF.' + q4(*JVS)))
b.append(GRID([
 CARD('forstbetrieb', 'Forstbetrieb Schliersee', 'Bayerische Staatsforsten',
      'Der Forstbetrieb reicht vom Voralpenland bis in die Kalkalpen und ist vor allem mit der Sanierung der Schutzwälder betraut.' + q4(*BWP),
      [('Natura 2000', 'Er ist an 10 FFH-Gebieten und einem Vogelschutzgebiet mit rund 14.680 ha beteiligt – etwa 43 % seiner Fläche' + q4(*N2K)),
       ('Bergwaldprojekt', 'Freiwillige arbeiten seit 2006 im Forstbetrieb, bauen Steige und pflegen den Wald' + q4(*BWP))], icon='🌲'),
 CARD('schaufuetterung', 'Schaufütterung Spitzingsee', 'Rotwild im Winter',
      'Die Staatsforsten bieten im Winter eine Rotwild-Schaufütterung am Spitzingsee an: vom 7. Januar bis zur Faschingswoche donnerstags bis sonntags ab 15 Uhr, in der Faschingswoche täglich.' + q4(*SCH),
      [('Hinweis', 'Termine können sich ändern – vorher beim Forstbetrieb Schliersee nachfragen')], icon='🦌'),
 CARD('lsg', 'Landschaftsschutzgebiet', '„Spitzingsee und Umgebung“',
      'Der Landkreis Miesbach hat eine neue Verordnung für das rund 3.234 ha große Landschaftsschutzgebiet ausgelegt; prägend sind Spitzingsee, Rote Valepp und die umliegenden Berge mit zahlreichen Almen.' + q4(*LSG), [], icon='📜'),
]))
b.append(P('Welche Baumarten den Bergmischwald bilden, steht in der <a href="/content/botanik/#bergwald">Pflanzenwelt</a>; welche Tiere darin leben, in der <a href="/content/fauna/">Tierwelt</a>.'))
forst = (b, q4)

for pfad, titel, h1, intro, hero, nav, (body, qq), desc, crumb in [
    ('content/geologie/index.html', 'Geologie rund um Spitzingsee und Schliersee', '🪨 Geologie', 'Molasse, Flysch und Kalkalpen auf engstem Raum, die Kössener Mergel am Spitzing und wie die Eiszeit die Seen geformt hat – mit Fachquellen.',
     FIG('ausblick-von-der-obere-firstalm-auf-den-brecherspitz.jpg', 'Blick von der Oberen Firstalm auf den Brecherspitz', 'Blick von der Oberen Firstalm zum Brecherspitz.'),
     [('zonen', '🪨 Zonen'), ('eiszeit', '🧊 Eiszeit'), ('quellen', '📚 Quellen')], geologie,
     'Geologie mit Quellen: Faltenmolasse, Flysch (Kalkgraben-Schichten) und Nördliche Kalkalpen, Kössener Mergel und Hangbewegungen am Spitzingsee, Würm-Eiszeit.', 'Geologie'),
    ('content/limnologie/index.html', 'Seen: Spitzingsee, Schliersee, Tegernsee', '💧 Seen', 'Wie die Seen gespeist werden, warum der Spitzingsee früh zufriert und wie der Tegernsee mit der ersten Ringkanalisation der Welt gerettet wurde.',
     FIG('spitzingsee-perfekt.jpg', 'Spitzingsee', 'Der Spitzingsee auf 1.084 m.'),
     [('seen', '💧 Seen'), ('quellen', '📚 Quellen')], limno,
     'Seen mit Quellen: Spitzingsee (28 ha, Einzugsgebiet, Abfluss Rote Valepp), Tegernsee und Schliersee mit Ringkanalisation.', 'Seen'),
    ('content/moore/index.html', 'Moore im Landkreis Miesbach', '🌿 Moore', '33 Hochmoore im Landkreis, ihre Bedeutung fürs Klima und wie Renaturierung funktioniert – mit amtlichen Zahlen.',
     '', [('moore', '🌿 Moore'), ('quellen', '📚 Quellen')], moore,
     'Moore mit Quellen: 33 Hochmoore mit 238 ha im Landkreis Miesbach, Klimawirkung, Wiedervernässung, Wattersdorfer Moor.', 'Moore'),
    ('content/forstwirtschaft/index.html', 'Bergwald und Forstwirtschaft am Spitzingsee', '🌲 Bergwald & Forst', 'Warum der Wald hier vor allem Schutzwald ist, was der Forstbetrieb Schliersee macht und wo man im Winter Rotwild beobachten kann.',
     '', [('bergwald', '🌲 Bergwald'), ('quellen', '📚 Quellen')], forst,
     'Bergwald mit Quellen: Schutzwald, Forstbetrieb Schliersee, Natura 2000, Rotwild-Schaufütterung Spitzingsee, Landschaftsschutzgebiet.', 'Bergwald & Forst'),
]:
    body.append(qq.liste())
    seite(pfad, titel, h1, intro, hero, nav, ''.join(body), desc, crumb, WEITER)
