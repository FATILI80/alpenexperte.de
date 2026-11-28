#!/usr/bin/env python3
"""Kultur & Geschichte (content/kultur_geschichte/index.html) – Herrschaft, Kirchen, Bergbau, Bahn, Skigeschichte, Kunst. Nur belegte Angaben."""
import sys; sys.path.insert(0, 'routing')
from kern import Q, CARD, seite, H2, P, BOX, GRID, FIG

q = Q()
BW = ('Burgenwelt – Burg Hohenwaldeck (PDF)', 'https://www.burgenwelt.org/deutschland/hohenwaldeck/burgenwelt-hohenwaldeck-deutschland.pdf')
AHS = ('Ancient History Sites – Burg Hohenwaldeck', 'https://www.ancient-history-sites.com/sites/burg-hohenwaldeck/')
HAB = ('Historischer Atlas von Bayern – Landgericht Aibling und Reichsgrafschaft Hohenwaldeck (1967, PDF)', 'https://www.geschichte-bayerns.de/files/repo/kblg/hab-ai/kblg.hab.ai.17/HAB-AI-17_Andrelang_1967.pdf')
KOM = ('Komoot – Schloss Maxlrain (Geschichte)', 'https://www.komoot.com/ko-kr/highlight/4007895')
WZ = ('Wikipedia – Johann Baptist Zimmermann', 'https://en.wikipedia.org/wiki/Johann_Baptist_Zimmermann')
WS = ('Wikipedia – Schliersee', 'https://wikipedia.com/wiki/Schliersee')
GACS = ('Google Arts & Culture / ZI – Schliersee, St. Sixtus (Caspar Glasl, 1712/1714)', 'https://artsandculture.google.com/asset/schliersee-catholic-parish-church-st-sixtus-caspar-glasl/1gHRBS2ftEfqBw')
ADS = ('ADAC – St.-Sixtus-Kirche Schliersee', 'https://maps.adac.de/poi/st-sixtus-kirche-gemeinde-schliersee')
TBI = ('tourispo – Wallfahrtskapelle Birkenstein', 'https://tourispo.de/sehenswuerdigkeit/wallfahrtskapelle-maria-himmelfahrt.html')
WAR = ('Warburg Institute – Birkenstein, Geschichte der Wallfahrt', 'https://iconographic.warburg.sas.ac.uk/object-wpc-wid-ebbo')
IGW = ('ich-geh-wandern – Birkenstein (Weihe 1786)', 'https://www.ich-geh-wandern.de/breitensteiner-fensterl-runde-ueber-kesselalm-und-schwaigeralm')
RE = ('dewiki – Rottach-Egern', 'https://dewiki.de/Lexikon/Rottach-Egern')
ADL = ('ADAC – St. Laurentius Rottach-Egern', 'https://maps.adac.de/poi/st-laurentius-rottach-egern')
WVF = ('Wikivoyage – Friedhöfe in Deutschland (Egerner Friedhof)', 'https://de.wikivoyage.org/wiki/Friedh%C3%B6fe_in_Deutschland')
LPG = ('Literaturportal Bayern – Emil und Ludwig Ganghofer (PDF)', 'https://www.literaturportal-bayern.de/images/lpbplaces/2021/TELITO_Emil_und_Ludwig_Ganghofer.pdf')
HAU = ('Wikipedia – Hausham', 'https://en.wikipedia.org/wiki/Hausham')
BWH = ('dewiki – Bergwerk Hausham', 'https://dewiki.de/Lexikon/Bergwerk_Hausham')
GEO = ('Geologica Bavarica 73 – Die oberbayerische Pechkohle (1975, PDF)', 'https://www.stmwi.bayern.de/fileadmin/user_upload/stmwi/Energie/Bodensch%C3%A4tze/1975-Die_oberbayerische_Peckkohle_Geologica_Bavarica_Nr_73.pdf')
HKS = ('Wikipedia – Holzkirchen station', 'https://en.wikipedia.org/wiki/Holzkirchen_station')
WMS = ('Waymarking – Bahnhof Schliersee', 'https://www.waymarking.com/waymarks/wm10RKJ_Schliersee_Station_Schliersee_Bavaria_DE')
BYZ = ('Wikipedia – Bayrischzell', 'https://www.wikipedia.org/wiki/Sudelfeld')
WV = ('Wikivoyage – Schliersee', 'https://de.wikivoyage.org/wiki/Schliersee')
OGM = ('Tegernseer Tal Tourismus – Olaf Gulbransson Museum', 'https://www.tegernsee.com/en/a-olaf-gulbransson-museum-tegernsee')
MIB = ('museen-in-bayern.de – Olaf Gulbransson Museum', 'https://museen-in-bayern.de/en/museums/museum-details/olaf-gulbransson-museum-tegernsee')
ADG = ('ADAC – Olaf Gulbransson Museum', 'https://maps.adac.de/poi/olaf-gulbransson-museum-stadt-tegernsee')

b = []
b.append(H2('herrschaft', '🏰 Herrschaft Hohenwaldeck', 'Schliersee war über Jahrhunderte keine bayerische Gemeinde, sondern Teil einer eigenen Reichsherrschaft.'))
b.append(GRID([
 CARD('hohenwaldeck', 'Burgruine Hohenwaldeck', 'über Fischhausen · 209 m über dem See',
      'Die Burg ist eine Gründung der Waldecker, deren Stammburg Altenwaldeck bei Irschenberg war; sie liegt 209 m über dem Schliersee.' + q(*BW),
      [('Zugang', 'Wanderweg W6 ab der Minigolfanlage, etwa 45 Minuten; von Fischhausen steil in rund 20 Minuten' + q(*BW)),
       ('Ende', 'Die Herrschaft bestand als eigene Einheit bis 1734 und kam dann an Kurbayern' + q(*AHS))], icon='🏰'),
 CARD('reichsgrafschaft', 'Reichsgrafschaft', 'bis 1734',
      'Die Reichsgrafschaft Hohenwaldeck umfasste mit dem Gericht Miesbach auch das Gebiet um Schliersee; der Historische Atlas von Bayern behandelt sie als eigenen Band.' + q(*HAB),
      [('Maxlrainer', 'Nach dem Tod des letzten Maxlrainers 1734 ging dessen Eigenbesitz an den Reichsgrafen Max von Rheinstein-Tattenbach' + q(*KOM)),
       ('Mehr', 'Klostergründung 779 und Umzug des Stifts nach München 1495: siehe <a href="/content/regional/#schliersee">Region</a>')], icon='📜'),
]))

b.append(H2('kirchen', '⛪ Kirchen & Wallfahrten', 'Barock, Rokoko und eine Loreto-Kapelle – drei Kirchen, die man gesehen haben sollte.'))
b.append(GRID([
 CARD('sixtus', 'St. Sixtus, Schliersee', '1712–1714 · Caspar Glasl',
      'Die Pfarrkirche wurde 1712–1714 von Caspar Glasl neu gebaut.' + q(*GACS) + ' Stuck und Fresken schuf 1714 Johann Baptist Zimmermann.' + q(*WZ),
      [('Ausstattung', 'Gnadenstuhl von Erasmus Grasser, Werke von Jan Polack' + q(*WS)),
       ('Bei Schliersee', 'Gotische Kapelle St. Georg auf dem Weinberg aus dem 14. Jahrhundert mit Barockaltar von 1624' + q(*WS))], icon='⛪'),
 CARD('birkenstein', 'Wallfahrt Birkenstein', 'Fischbachau · 1710',
      'Die Wallfahrtskapelle ist eine Nachbildung des „Heiligen Hauses“ von Nazareth bzw. Loreto und wurde 1710 erbaut; seit 1673 wird hier eine spätmittelalterliche Marienstatue verehrt.' + q(*TBI),
      [('Grundstein', '1710 durch den Propst von Fischbachau' + q(*WAR)),
       ('Weihe', '1786 durch Fürstbischof Ludwig Joseph von Welden' + q(*IGW))], icon='🕯️'),
 CARD('laurentius', 'St. Laurentius, Egern', 'Rottach-Egern · 1466',
      'Die Kirche wurde 1111 erstmals erwähnt, 1466 spätgotisch erweitert und ab 1670 barock ausgestaltet.' + q(*RE),
      [('Friedhof', 'Auf dem Friedhof liegen Ludwig Thoma und Ludwig Ganghofer' + q(*ADL) + ' – mehr unter <a href="#kunst">Kunst & Literatur</a>')], icon='🔔'),
]))
b.append(P('Zu den Leonhardifahrten in Kreuth und Fischhausen siehe <a href="/content/almkultur/#jahreslauf">Almkultur & Brauchtum</a>.'))

b.append(H2('bergbau', '⛏️ Bergbau in Hausham', 'Über hundert Jahre prägte die Pechkohle das Tal zwischen Miesbach und Schliersee.'))
b.append(GRID([
 CARD('hausham', 'Kohlenbergwerk Hausham', '1860–1966',
      'Das Bergwerk wurde 1860 eröffnet, konnte gegen billigeres Öl und Steinkohle nicht bestehen und schloss 1966.' + q(*HAU),
      [('Denkmal', 'Das 1934–1935 errichtete Fördergerüst des Klenze-Schachts (Architekten Schupp und Kremmer) steht noch' + q(*BWH)),
       ('Ende der Pechkohle', 'Die Stilllegungen begannen 1966; die letzte Tonne oberbayerischer Pechkohle wurde am 31.3.1971 in Peißenberg gefördert' + q(*GEO))], icon='⛏️'),
]))

b.append(H2('verkehr', '🚂 Bahn & Wege', 'Die Bahn kam wegen der Kohle – und brachte die Sommerfrischler.'))
b.append(GRID([
 CARD('bahn', 'Bahn nach Schliersee', 'seit 1. August 1869',
      'Die Strecke Holzkirchen–Miesbach wurde 1868 bis Hausham und 1869 bis Schliersee verlängert.' + q(*HKS) + ' Der Bahnhof Schliersee ist seit dem 1. August 1869 in Betrieb; der Ausbau bis Hausham hing am Bergwerk.' + q(*WMS),
      [('Bayrischzell', 'Der Abschnitt Schliersee–Bayrischzell ging am 1. Oktober 1911 in Betrieb' + q(*BYZ)),
       ('Spitzkehre', 'Schliersee blieb ein Kopfbahnhof, in dem die Züge Richtung Bayrischzell wenden' + q(*WMS)),
       ('Heute', 'Anreise mit RB 55 und Bussen: <a href="/content/regional/#anreise">Region – Anreise</a>')], icon='🚂'),
 CARD('ski', 'Wiege des Skisports', 'Fischhausen · ab 1891',
      'Der Münchner Buchhändler August Finsterlin kaufte 1891 den Högerhof in Fischhausen; 1902 gab es dort den ersten Skikurs, 1904 das erste Skirennen.' + q(*WV),
      [('Bockerlbahn', 'Die Waldbahn über den Spitzingsattel 1919/20: <a href="/content/regional/#bockerlbahn">Region</a>')], icon='⛷️'),
]))

b.append(H2('kunst', '🎨 Kunst & Literatur', 'Am Tegernsee lebten und liegen einige der bekanntesten bayerischen Künstler.'))
b.append(GRID([
 CARD('gulbransson', 'Olaf Gulbransson', 'Karikaturist · 1873–1958',
      'Der Norweger wurde als Zeichner des Münchner „Simplicissimus“ bekannt; ihm ist seit 1966 das Museum in Tegernsee gewidmet.' + q(*OGM),
      [('Am Tegernsee', '1929 erwarb er den Schererhof' + q(*ADG)),
       ('Museum', 'Pavillon von Sep Ruf (1966), Kurgarten 5, Tegernsee' + q(*MIB))], icon='✏️'),
 CARD('egern', 'Egerner Friedhof', 'Rottach-Egern',
      'Hier ruhen u. a. Ludwig Thoma, Ludwig Ganghofer, Heinrich und Alexander Spoerl, Leo Slezak mit Familie und der Volksliedsammler Kiem Pauli.' + q(*WVF),
      [('Im Kurpark', 'Bronzegruppe von Ganghofer (1855–1920) und Thoma (1867–1921)' + q(*LPG))], icon='📚'),
]))

b.append(H2('personen', '👤 Köpfe der Region', 'Weitere Persönlichkeiten haben wir dort beschrieben, wo sie hingehören:'))
b.append(P('Wildschütz <a href="/content/regional/#jennerwein">Georg Jennerwein</a>, Alpenvereinsgründer <a href="/content/regional/#trautwein">Theodor Trautwein</a> (mit unserem Foto der Gedenktafel), Olympiasieger <a href="/content/regional/#wasmeier">Markus Wasmeier</a>, Volksliedsammler <a href="/content/almkultur/#kiem-pauli">Kiem Pauli</a> und der Gründer des ersten Trachtenvereins <a href="/content/almkultur/#trachtenverein">Josef Vogl</a>.'))
b.append(q.liste())

seite('content/kultur_geschichte/index.html', 'Kultur & Geschichte rund um Schliersee und Tegernsee',
      '🏛️ Kultur & Geschichte',
      'Reichsgrafschaft Hohenwaldeck, Barockkirchen, Bergbau in Hausham, die Bahn von 1869, die Anfänge des Skisports und die Künstler am Tegernsee – mit Quellen.',
      FIG('schliersee-see.jpg', 'Blick über den Schliersee', 'Der Schliersee – hier begann mit der Klostergründung 779 die Geschichte des Ortes.'),
      [('herrschaft', '🏰 Hohenwaldeck'), ('kirchen', '⛪ Kirchen'), ('bergbau', '⛏️ Bergbau'), ('verkehr', '🚂 Bahn & Ski'), ('kunst', '🎨 Kunst'), ('personen', '👤 Köpfe'), ('quellen', '📚 Quellen')],
      ''.join(b),
      'Kultur & Geschichte mit Quellen: Reichsgrafschaft Hohenwaldeck, St. Sixtus mit Zimmermann-Fresken, Birkenstein, Bergwerk Hausham 1860–1966, Bahn 1869, Skigeschichte Fischhausen, Gulbransson, Egerner Friedhof.',
      'Kultur & Geschichte', 'Weiter: <a href="/content/regional/">Region</a> · <a href="/content/almkultur/">Almkultur</a> · <a href="/content/almwirtschaft/">Almwirtschaft</a>')
