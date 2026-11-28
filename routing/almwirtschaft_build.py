#!/usr/bin/env python3
"""Almwirtschaft (content/almwirtschaft/index.html) – Zahlen, Almsommer, Natur, Förderung, Verhalten. Nur belegte Angaben."""
import sys; sys.path.insert(0, 'routing')
from kern import Q, CARD, seite, H2, P, BOX, GRID, FIG, UL, TAB

q = Q('Stand: 28. November 2026. Zahlen zur Almwirtschaft schwanken von Jahr zu Jahr; wir nennen jeweils das Bezugsjahr der Quelle.')
AELF = ('AELF Holzkirchen – Statistik Landwirtschaft Landkreis Miesbach 2024 (PDF)', 'https://oekomodellregionen.bayern/file/58445051-5382-4a3b-b9cc-d6fff8da8afa.pdf/statistik-aelf-holzkirchen-landwirtschaft-landkreis-miesbach-2024')
BN = ('Bund Naturschutz – Almwirtschaft und Naturschutz (2024, PDF)', 'https://bund-naturschutz.de/fileadmin/Bilder_und_Dokumente/Themen/Alpen/Almwirtschaft/BN-Informiert-Almwirtschaft-und-Naturschutz_2024-10-18.pdf')
STM = ('bayern.de – Pressemitteilung Almsommer (StMELF)', 'https://www.bayern.de/pdf/printpdf.php?id=34444')
STM2 = ('bayern.de – Pressemitteilung Almabtrieb (StMELF)', 'https://www.bayern.de/pdf/printpdf.php?id=34424')
HIN = ('Hinterstoisser: Almwirtschaft in Oberbayern – ANLiegen Natur 31/1 (2007, PDF)', 'https://www.zobodat.at/pdf/AnliegenNatur_31_1_2007_0052-0056.pdf')
AGR = ('Bayerischer Agrarbericht 2020 – Alm- und Alpwirtschaft (PDF)', 'https://agrarbericht2020.bayern.de/landwirtschaft-laendliche-entwicklung/pdf/alm-und-alpwirtschaft.pdf')
LT = ('Bayerischer Landtag – Drucksache 18/7435 (Weideflächen, KULAP B52)', 'https://www1.bayern.landtag.de/www/ElanTextAblage_WP18/Drucksachen/Schriftliche%20Anfragen/18_0007435.pdf')
LFU = ('LfU Bayern – FFH-Lebensraumtypen Grasland (PDF)', 'https://www.lfu.bayern.de/natur/natura_2000/ffh/natuerliche_lebensraeume/doc/lrt_6xxx_natuerliches_naturnahes_grasland.pdf')
DAVS = ('DAV – Schwendaktionen der Bergsteigerdörfer', 'https://www.alpenverein.de/verband/presse/pressemeldungen/anpacken-fuer-den-naturschutz-schwendaktionen-der-bergsteigerdoerfer')
ANL = ('ANL – Das Almprojekt in Oberbayern (2013, PDF)', 'https://www.anl.bayern.de/publikationen/anliegen/doc/an35209lang_et_al_2013_almprojekt.pdf')
BML = ('BMLUK Österreich – 10 Regeln für den sicheren Umgang mit Weidevieh', 'https://www.bmluk.gv.at/service/presse/landwirtschaft/2025/10-regeln-fuer-sicheren-umgang-mit-weidevieh-auf-almen-beachten.html')
BGL = ('Berchtesgadener Land Tourismus – Richtiges Verhalten auf der Alm', 'https://www.berchtesgaden.de/tradition-brauchtum/almsommer/verhalten-auf-der-alm')
BGL2 = ('Berchtesgadener Land Tourismus – Herdenarten auf der Alm', 'https://www.berchtesgaden.de/region/brauchtum-kultur/almsommer/verhalten-auf-der-alm')

b = []
b.append(H2('zahlen', '📊 Almwirtschaft in Zahlen', 'In Oberbayern heißen sie Almen, im Allgäu Alpen.'))
b.append(TAB(['', 'Wert', 'Quelle'], [
    ('Almen im Landkreis Miesbach', '156 Almen, 3.750 ha Lichtweide (2024)', q(*AELF)),
    ('Almen und Alpen in Bayern', 'ca. 1.470, davon ca. 770 Almen in Oberbayern und ca. 700 Alpen im Allgäu', q(*BN)),
    ('Gesömmerte Tiere in Bayern (2020)', 'ca. 53.000 Rinder (davon 3.900 Kühe), 4.800 Schafe und Ziegen, 800 Pferde auf rund 37.000 ha Lichtweide', q(*BN)),
    ('Almsommer', 'rund 100 Tage auf den Almen und Alpen', q(*STM2)),
]))
b.append(P('Die Mehrzahl der Tiere auf den Almen ist Jungvieh, nicht Milchkühe – das zeigen die Zahlen deutlich (3.900 Kühe von 53.000 Rindern).' + q(*BN)
           + ' Laut Staatsregierung wurde in den vergangenen vierzig Jahren keine der rund 1.400 bayerischen Almen und Alpen aufgegeben.' + q(*STM)))

b.append(H2('formen', '🏡 Wem gehören die Almen?', 'Die Besitzverhältnisse unterscheiden sich von Landkreis zu Landkreis.'))
b.append(GRID([
 CARD('eigentum', 'Eigentumsalmen', 'typisch für Miesbach',
      'Eigentumsalmen herrschen vor allem in den Landkreisen Rosenheim, Miesbach und in Teilen von Bad Tölz-Wolfratshausen vor; Berechtigungsalmen findet man im Berchtesgadener Land und in Garmisch-Partenkirchen.' + q(*HIN),
      [('Höhenlage', 'Die oberbayerischen Almen liegen zwischen 600 und 2.000 m' + q(*HIN))], icon='🏡'),
 CARD('firstalm', 'Unsere Nachbarschaft', 'Obere Firstalm, 1.375 m',
      'Am Spitzingsattel liegen Almen dicht beieinander – viele mit Ausschank für Wanderer. Welche Almen bewirtschaftet sind und wann sie offen haben, steht mit Quellen im <a href="/huetten.html">Hüttenführer</a>.', [], icon='🐄'),
]))

b.append(H2('natur', '🌸 Almen und Artenvielfalt', 'Ohne Weidevieh würden viele Bergwiesen zuwachsen – aber zu viel Dünger schadet ebenfalls.'))
b.append(UL([
    'Zwei FFH-Lebensraumtypen sind an Beweidung gebunden: artenreiche montane Borstgrasrasen (LRT 6230) und naturnahe Kalk-Trockenrasen (LRT 6210).' + q(*BN),
    'Borstgrasrasen wachsen nur auf sauren Böden; Halbtrockenrasen sind heute vor allem durch Verbuschung gefährdet, wenn Nutzung oder Pflege ausbleiben.' + q(*LFU),
    'Beim Schwenden werden Bäume und Sträucher von Flächen entfernt, die das Vieh nicht abgefressen hat – je nach Lage 10 bis 20 % der Almfläche.' + q(*DAVS),
    'Düngung gilt als Gefahr für die Artenvielfalt auf Almen.' + q(*BN),
    'Die Regierung von Oberbayern ließ ab 2010 auf sechs Almen, u. a. im Landkreis Miesbach, gemeinsam mit den Bewirtschaftern untersuchen, wie Nutzung und Artenvielfalt zusammenhängen.' + q(*ANL),
]))
b.append(P('Welche Pflanzen auf den Almen rund um den Spitzingsee wachsen, steht in der <a href="/content/botanik/">Pflanzenwelt</a>.'))

b.append(H2('foerderung', '💶 Förderung', 'Ohne Ausgleichszahlungen wäre Almwirtschaft kaum wirtschaftlich.'))
b.append(P('Für Almen und Alpen flossen laut Agrarbericht 2020 u. a. rund 8,3 Mio. € Ausgleichszulage (Almen und Flächen über 1.000 m), rund 3,7 Mio. € aus dem Kulturlandschaftsprogramm (KULAP), rund 1,2 Mio. € Vertragsnaturschutz und rund 12,1 Mio. € EU-Direktzahlungen.' + q(*AGR)
           + ' Eine eigene KULAP-Maßnahme fördert die ständige Behirtung anerkannter Almen und Alpen (B52).' + q(*LT)))

b.append(H2('verhalten', '🚶 Wandern durch die Weide', 'Eine Alm ist kein Streichelzoo – die wichtigsten Regeln.'))
b.append(UL([
    'Kontakt zum Weidevieh vermeiden, Tiere nicht füttern, Abstand halten; ruhig bleiben und die Tiere nicht erschrecken.' + q(*BML),
    'Mutterkühe beschützen ihre Kälber – Begegnungen zwischen Mutterkühen und Hunden vermeiden.' + q(*BML),
    'Hunde kurz anleinen, bei einem Angriff sofort ableinen; Wander- und Radwege nicht verlassen.' + q(*BML),
    'Warnsignale ernst nehmen: Senken des Kopfes, Scharren, Brüllen.' + q(*BGL),
    'Milchkühe sind den Kontakt mit Menschen gewohnt und meist am ruhigsten; Mutterkuhherden verteidigen ihre Kälber impulsiv.' + q(*BGL2),
]))
b.append(BOX('Weidetore immer wieder schließen. Und wer auf einer Alm einkehrt, unterstützt genau die Bewirtschaftung, die diese Landschaft offen hält.'))
b.append(P('Bräuche rund um Almauftrieb und Almabtrieb: <a href="/content/almkultur/#almabtrieb">Almkultur</a>.'))
b.append(q.liste())

seite('content/almwirtschaft/index.html', 'Almwirtschaft im Mangfallgebirge',
      '🐄 Almwirtschaft',
      'Wie viele Almen es gibt, wem sie gehören, warum sie für die Artenvielfalt wichtig sind und wie man sich auf der Weide verhält – mit Zahlen aus amtlichen Quellen.',
      FIG('almvieh-kuehe.jpg', 'Kälber werden auf einem Almweg geführt', 'Jungvieh auf dem Weg zur Weide (Symbolbild).'),
      [('zahlen', '📊 Zahlen'), ('formen', '🏡 Besitz'), ('natur', '🌸 Artenvielfalt'), ('foerderung', '💶 Förderung'), ('verhalten', '🚶 Verhalten'), ('quellen', '📚 Quellen')],
      ''.join(b),
      'Almwirtschaft mit Quellen: 156 Almen im Landkreis Miesbach, rund 1.470 in Bayern, Artenvielfalt und Schwenden, Förderung, 10 Regeln für Wanderer auf der Weide.',
      'Almwirtschaft', 'Weiter: <a href="/content/almkultur/">Almkultur</a> · <a href="/huetten.html">Hüttenführer</a> · <a href="/content/botanik/">Pflanzenwelt</a>')
