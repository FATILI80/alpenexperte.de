#!/usr/bin/env python3
"""Almkultur & Brauchtum (content/almkultur/index.html) – nur belegte Angaben aus der Region Schliersee/Tegernsee/Leitzachtal."""
import sys; sys.path.insert(0, 'routing')
from kern import Q, CARD, seite, H2, P, BOX, GRID, FIG

q = Q('Stand: 28. November 2026. Termine von Brauchtumsfesten können sich ändern – vor dem Besuch beim Veranstalter oder der Gemeinde nachfragen.')
KRE = ('Tegernseer Tal Tourismus – Leonhardi Kreuth', 'https://tegernsee.com/en/leonhardi-kreuth')
DAVK = ('DAV – Bergsteigerdorf Kreuth: Im Herzen des Mangfallgebirges', 'https://alpenverein.de/artikel/im-herzen-des-mangfallgebirges_dab3578e-4673-4baf-874f-76b76c9aa6c5')
AZ = ('Abendzeitung (dpa) – Leonhardi-Wallfahrt Benediktbeuern', 'https://www.abendzeitung-muenchen.de/bayern/mehrere-tausend-bei-leonhardi-wallfahrt-in-benediktbeuern-art-645184')
LIT = ('Literaturportal Bayern – Schillerndes Kreuth (PDF)', 'https://www.literaturportal-bayern.de/images/lpbplaces/2021/TELITO_Schillerndes_Kreuth.pdf')
GAC = ('Google Arts & Culture – Schliersee, Filial- und Wallfahrtskirche St. Leonhard', 'https://artsandculture.google.com/asset/schliersee-catholic-filial-and-pilgrimage-church-st-leonhard/QwFpznDAFWdDNQ')
WV = ('Wikivoyage – Schliersee', 'https://de.wikivoyage.org/wiki/Schliersee')
LECH = ('Lechner am See – Schliersee (Brauchtum)', 'https://lechneramsee.de/en/?p=1169')
MERK = ('Merkur (via Ground News) – Alt-Schlierseer Kirchtag: 40. Überfahrt', 'https://ground.news/article/alt-schlierseer-kirchtag-boat-crossing-with-four-sponsorships-for-the-first-time')
BYZ = ('Bayrischzell – Ortsgeschichte (dasbayrischzell.de)', 'https://www.dasbayrischzell.de/en/region/bayrischzell')
BAY = ('bayern.de – Pressemitteilung zum Trachtenwesen (PDF)', 'https://www.bayern.de/pdf/printpdf.php?id=120189')
OKT = ('oktoberfest.de – Lederhosen: vom Skandal zum Must-have', 'https://www.oktoberfest.de/dirndl-tracht/lederhosen-vom-skandal-beim-gottesdienst-zum-must-have')
TRW = ('Wikipedia – Tracht', 'https://en.wikipedia.org/wiki/Tracht')
IHK = ('IHK München – 170 Schritte vom Schaf bis zur Joppe', 'https://www.ihk-muenchen.de/magazin/unternehmen/unternehmen-in-oberbayern/170-schritte-vom-schaf-bis-zur-joppe.html')
NDB = ('Deutsche Biographie – Kiem, Emanuel (Kiem Pauli)', 'https://www.deutsche-biographie.de/sfz40851.html')
KPW = ('dewiki – Kiem Pauli', 'https://dewiki.de/Lexikon/Paul_Kiem')
WUE = ('Warmuth: Das Unterfränkische Volksliederwettsingen 1932 (Uni Würzburg)', 'https://journals.bibliothek.uni-wuerzburg.de/frl-nf/article/download/8553/8595/8855')
EBES = ('Förderverein Volksmusik Oberbayern – Kiem Pauli in Au bei Aibling', 'https://www.ebes-volksmusik.de/files/3_ovb/806_ja_ja.pdf')
BGL = ('Berchtesgadener Land Tourismus – Almabtrieb', 'https://www.berchtesgaden.de/tradition-brauchtum/almsommer/almabtrieb')
SOB = ('Sonntagsblatt – Almabtrieb und Viehscheid in Allgäu und Oberbayern', 'https://sonntagsblatt.de/artikel/psychologie-ratgeber/almabtrieb-und-viehscheid-allgaeu-und-oberbayern')

b = []
b.append(H2('jahreslauf', '📅 Bräuche im Jahreslauf', 'Was rund um Schliersee und Tegernsee wirklich gefeiert wird – nicht das Allgäuer Viehscheid-Klischee.'))
b.append(GRID([
 CARD('leonhardi-kreuth', 'Leonhardifahrt Kreuth', '6. November · Tegernseer Tal',
      'Die älteste belegte Leonhardifahrt Bayerns: In Kreuth ist sie seit 1442 nachgewiesen und findet jedes Jahr am 6. November statt, dem Festtag des heiligen Leonhard, des Schutzpatrons der Pferde.' + q(*KRE) + q(*AZ),
      [('Ablauf', 'Nach dem Gottesdienst wird die Kirche St. Leonhard dreimal umfahren' + q(*LIT)),
       ('Geschichte', 'Nach dem Krieg fand 1946 die erste Leonhardifahrt wieder statt; der vorletzte Tegernseer Abt Benedikt Schwarz starb am Leonharditag 1787 in Kreuth' + q(*KRE)),
       ('Ort', 'Kreuth ist DAV-Bergsteigerdorf; Lederhose, Dirndl und Joppe gehören zum Ortsbild' + q(*DAVK))], icon='🐎'),
 CARD('leonhardi-fischhausen', 'Leonhardifahrt nach Fischhausen', 'Schliersee · St. Leonhard',
      'Auch am Schliersee gibt es eine Leonhardifahrt: Sie führt von Schliersee zur Wallfahrtskirche St. Leonhard in Fischhausen am Südufer.' + q(*LECH),
      [('Kirche', 'Filial- und Wallfahrtskirche, frühbarock; als Bauzeit werden 1646–1688 bzw. 1651/1668 angegeben' + q(*WV) + q(*GAC)),
       ('Termin', 'Den genauen Termin veröffentlicht die Pfarrei bzw. der Markt Schliersee – eine verlässliche Online-Quelle haben wir nicht gefunden')], icon='⛪'),
 CARD('kirchtag', 'Alt-Schlierseer Kirchtag', 'Anfang August · Schliersee',
      'Die Trachtengruppe „Die Historischen“ fährt mit Plätten und Ruderbooten von Fischhausen nach Schliersee; am 2. August 2026 war es die 40. Überfahrt.' + q(*MERK),
      [('Schliersee-Kalender', 'Kirchtag, Fronleichnamsprozession und Leonhardifahrt gelten als feste Termine im Schlierseer Jahr' + q(*LECH))], icon='🚣'),
 CARD('almabtrieb', 'Almabtrieb', 'September/Oktober',
      'In Oberbayern liegen die Almabtriebe meist zwischen Anfang September und Mitte Oktober.' + q(*SOB) + ' Die Leitkuh trägt den prächtigsten Kopfschmuck; ist auf der Alm oder in der Bauernfamilie ein Unglück passiert, kommen die Tiere ungeschmückt ins Tal.' + q(*BGL),
      [('Hier am Spitzing', 'Feste Almabtriebs-Feste mit Programm wie im Allgäu oder Berchtesgaden sind uns für den Spitzingsee nicht bekannt – die Almen treiben je nach Wetter ab')], icon='🐄'),
]))

b.append(H2('tracht', '👗 Tracht', 'Der Landkreis Miesbach ist die Wiege der Trachtenbewegung.'))
b.append(GRID([
 CARD('trachtenverein', 'Erster Trachtenverein', 'Bayrischzell · 1883',
      '1883 wurde in Bayrischzell der „Verein zur Erhaltung der Volkstracht im Leizachtale“ gegründet – der erste Trachtenverein.' + q(*BAY) + ' Gründer war der Lehrer Josef Vogl, im Gasthof Neuwirt.' + q(*BYZ),
      [('Anlass', 'Vogl und seine Freunde wollten statt Lodenhosen kurze Lederhosen tragen – damals ein Verstoß gegen die Etikette' + q(*OKT))], icon='🎩'),
 CARD('miesbacher-tracht', 'Miesbacher Tracht', 'eine von sechs Gebirgstrachten',
      'In Bayern werden heute sechs Untertypen der alpinen Tracht unterschieden: Miesbacher, Werdenfelser, Inntaler, Chiemgauer, Berchtesgadener und Isarwinkler Tracht.' + q(*TRW),
      [('Joppe', 'Karl Jäger entwickelte 1910 die „Original Miesbacher Joppe“ mit Eichenlaub-Stickerei' + q(*IHK)),
       ('Ältestes Foto', 'Die „Gesellschaft Gemüthlichkeit von 1859“ gilt als älteste bekannte Aufnahme einer Trachtengesellschaft (Foto von 1862)' + q(*OKT))], icon='🧵'),
]))

b.append(H2('musik', '🎻 Volksmusik', 'Dass so viele alte Lieder überlebt haben, verdankt Oberbayern zu einem guten Teil einem Mann aus Kreuth.'))
b.append(GRID([
 CARD('kiem-pauli', 'Kiem Pauli', 'Volksliedsammler · 1882–1960',
      'Emanuel „Kiem Pauli“ Kiem, geboren 1882 in München, gestorben 1960 in Bad Kreuth, sammelte bis dahin nur mündlich weitergegebene bayerische Volksmusik.' + q(*NDB) + q(*KPW),
      [('Sammelfahrten', 'Von seiner Wohnung in Bad Kreuth aus zog er in den 1920er Jahren durchs südliche Oberbayern und schrieb Lieder bei Hunderten Sängerinnen und Sängern auf' + q(*EBES)),
       ('Preissingen', 'Er organisierte ein Preissingen in Rottach-Egern – die Quellen nennen 1929 (Gasthaus Überfahrt) bzw. 1930' + q(*KPW) + q(*WUE))], icon='🎶'),
 CARD('bauerntheater', 'Schlierseer Bauerntheater', 'seit 1892',
      'Eine der ältesten Volksbühnen Bayerns – Gründung und Geschichte stehen mit Quellen auf unserer <a href="/content/regional/#schliersee">Region-Seite</a>.', [], icon='🎭'),
]))

b.append(H2('alm', '🧀 Auf der Alm', 'Almkultur heißt hier vor allem: Brotzeit, Milch und Käse dort, wo das Vieh im Sommer steht.'))
b.append(FIG('alm-wirtschaft.jpg', 'Sennküche mit Kupferkessel über offenem Feuer', 'In der Sennküche wird die Milch im Kupferkessel über dem Feuer verarbeitet (Symbolbild).'))
b.append(P('Welche Almen rund um den Spitzingsee bewirtschaftet sind, was es dort gibt und wann sie offen haben, steht im <a href="/huetten.html">Hüttenführer</a> – jede Alm mit Quelle. Wie die Almwirtschaft selbst funktioniert, behandeln wir in der Kategorie <a href="/content/almwirtschaft/">Almwirtschaft</a>.'))
b.append(BOX('<strong>Von der Oberen Firstalm aus:</strong> Die <a href="/huetten.html#ankelalm">Ankelalm</a> (1.311 m) im Kessel unter dem Brecherspitz ist eine der kleinen Brotzeitalmen, die im Sommer Käse und Milch von der eigenen Alm anbieten.'))
b.append(q.liste())

seite('content/almkultur/index.html', 'Almkultur & Brauchtum am Schliersee und Tegernsee',
      '🎺 Almkultur & Brauchtum',
      'Leonhardifahrten, Kirchtag, Tracht und Volksmusik rund um Schliersee, Tegernsee und Leitzachtal – nur was wir belegen können, mit Quellen.',
      FIG('ankelalm-front.jpg', 'Ankel-Alm mit Namensschild 1311 m', 'Ankel-Alm (1.311 m) unter dem Brecherspitz – eigenes Foto.'),
      [('jahreslauf', '📅 Jahreslauf'), ('tracht', '👗 Tracht'), ('musik', '🎻 Volksmusik'), ('alm', '🧀 Auf der Alm'), ('quellen', '📚 Quellen')],
      ''.join(b),
      'Almkultur & Brauchtum mit Quellen: älteste Leonhardifahrt Bayerns in Kreuth, Leonhardifahrt Fischhausen, Alt-Schlierseer Kirchtag, erster Trachtenverein 1883, Kiem Pauli.',
      'Almkultur', 'Weiter: <a href="/content/regional/">Region</a> · <a href="/huetten.html">Hüttenführer</a> · <a href="/content/almwirtschaft/">Almwirtschaft</a>')
