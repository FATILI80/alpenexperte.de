#!/usr/bin/env python3
"""Sternenhimmel (content/sternenhimmel/index.html).
Himmelsdaten (Neumonde, Nachtlängen, Milchstraßen-Zentrum, Mond bei Meteorströmen, Sonnenfinsternis 2027)
werden hier mit PyEphem für die Obere Firstalm (47.6701 N, 11.8540 E, 1.375 m) berechnet – freier Horizont angenommen."""
import sys, math
from datetime import datetime, timedelta, timezone
import ephem
sys.path.insert(0, 'routing')
from kern import Q, CARD, seite, H2, P, BOX, GRID, FIG, UL, AFF, TAB

LAT, LON, HOEHE = '47.6701', '11.8540', 1375
def obs(datum, horizont='0'):
    o = ephem.Observer(); o.lat, o.lon, o.elevation, o.pressure, o.horizon = LAT, LON, HOEHE, 0, horizont; o.date = datum; return o
def lokal(d, nur_zeit=False):
    dt = ephem.Date(d).datetime().replace(tzinfo=timezone.utc)
    def letzter_so(m):
        x = datetime(dt.year, m, 31, 1, tzinfo=timezone.utc)
        while x.weekday() != 6: x -= timedelta(days=1)
        return x
    off = 2 if letzter_so(3) <= dt < letzter_so(10) else 1
    t = dt + timedelta(hours=off)
    return t.strftime('%H:%M') if nur_zeit else t.strftime('%d.%m.%Y, %H:%M') + (' MESZ' if off == 2 else ' MEZ')
WT = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

# --- Neumonde Dez 2026 – Dez 2027
neumonde, d = [], ephem.Date('2026/12/01')
while True:
    d = ephem.next_new_moon(d)
    if d > ephem.Date('2027/12/31'): break
    neumonde.append(lokal(d)); d = ephem.Date(d + 1)

# --- Länge der astronomischen Nacht
sonne = ephem.Sun(); naechte = []
for tag, label in [('2026/12/21', '21. Dezember'), ('2027/03/20', '20. März'), ('2027/06/21', '21. Juni'), ('2027/08/12', '12. August'), ('2027/09/23', '23. September')]:
    o = obs(tag + ' 12:00', '-18')
    a, b = o.next_setting(sonne, use_center=True), o.next_rising(sonne, use_center=True)
    h = (b - a) * 24
    naechte.append((label, f'{lokal(a, True)} – {lokal(b, True)}', f'{int(h)} h {round((h - int(h)) * 60):02d} min'))

# --- Milchstraßen-Zentrum (Sgr A*): höchster Stand während astronomischer Nacht, je Monatsmitte 2027
gz = ephem.FixedBody(); gz._ra, gz._dec, gz._epoch = '17:45:40', '-29:00:28', ephem.J2000
zentrum = []
for m in range(1, 13):
    o = obs(f'2027/{m:02d}/15 12:00', '-18')
    a, b = o.next_setting(sonne, use_center=True), o.next_rising(sonne, use_center=True)
    t, best = a, (-90, None)
    while t < b:
        o.date = t; gz.compute(o)
        if math.degrees(gz.alt) > best[0]: best = (math.degrees(gz.alt), t)
        t = ephem.Date(t + ephem.minute * 10)
    zentrum.append((m, best[0], lokal(best[1], True) if best[0] > 0 else '–'))
MON = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']

# --- Mond bei den großen Meteorströmen
mond = ephem.Moon(); stroeme = []
for name, tag, nacht in [('Geminiden', '2026/12/13 15:00', '13./14. Dez. 2026'), ('Quadrantiden', '2027/01/03 15:00', '3./4. Jan. 2027'),
                         ('Lyriden', '2027/04/22 15:00', '22./23. Apr. 2027'), ('Perseiden', '2027/08/12 15:00', '12./13. Aug. 2027'),
                         ('Geminiden', '2027/12/13 15:00', '13./14. Dez. 2027')]:
    o = obs(tag); unter, auf = o.next_setting(mond), o.next_rising(mond)
    o = obs(ephem.Date(ephem.Date(tag) + 8 * ephem.hour)); mond.compute(o)
    stroeme.append((name, nacht, f'{mond.phase:.0f} %', f'Untergang {lokal(unter, True)}, Aufgang {lokal(auf, True)}'))

# --- partielle Sonnenfinsternis 2. August 2027
best, t = (9, None), ephem.Date('2027/08/02 08:00')
while t < ephem.Date('2027/08/02 13:00'):
    o = obs(t); sonne.compute(o); mond.compute(o)
    s = ephem.separation(sonne, mond)
    if s < best[0]: best = (s, t, sonne.size / 2, mond.size / 2, math.degrees(sonne.alt))
    t = ephem.Date(t + ephem.minute)
sep, tmax, rs, rm, salt = best; rs, rm = math.radians(rs / 3600), math.radians(rm / 3600)
a1 = math.acos((sep ** 2 + rs ** 2 - rm ** 2) / (2 * sep * rs)); a2 = math.acos((sep ** 2 + rm ** 2 - rs ** 2) / (2 * sep * rm))
flaeche = rs ** 2 * a1 + rm ** 2 * a2 - 0.5 * math.sqrt((-sep + rs + rm) * (sep + rs - rm) * (sep - rs + rm) * (sep + rs + rm))
bedeckung = round(100 * flaeche / (math.pi * rs ** 2))

q = Q('Stand: 28. November 2026. Himmelsdaten mit „berechnet“ sind eigene Berechnungen (PyEphem) für die Obere Firstalm mit freiem Horizont – Berge, Bäume und Wetter können die Sicht einschränken.')
RECHNER = 'eigene Berechnung (PyEphem, Obere Firstalm)'
AZL = ('Abendzeitung – Lichtverschmutzung: Auf der Suche nach der verlorenen Nacht', 'https://www.abendzeitung-muenchen.de/bayern/lichtverschmutzung-auf-der-sucher-nach-der-verlorenen-nacht-art-548521')
LEIT = ('Bayer. Umweltministerium – Leitfaden zur Eindämmung der Lichtverschmutzung (PDF)', 'https://regierung.oberfranken.bayern.de/mam/service/umwelt/natur/biodiversitaet/stmuv_leitfaden_beleuchtung_2020.pdf')
ANL = ('ANL Bayern – Interview mit Manuel Philipp zur Lichtverschmutzung (PDF)', 'https://www.anl.bayern.de/publikationen/anliegen/doc/an46106interview_2024_philipp.pdf')
ASTR = ('Astronomy.com – Dark adaptation', 'https://www.astronomy.com/observing/michaels-miscellany-dark-adaption')
DAEM = ('Sterngucker – Dämmerung: wann es richtig dunkel ist', 'https://www.sterngucker.de/wissen/daemmerung/')
MS = ('Sterngucker – Milchstraße fotografieren', 'https://www.sterngucker.de/astrofotografie/milchstrasse-fotografieren/')
FG = ('Sterngucker – Astronomie-Fernglas', 'https://www.sterngucker.de/astronomie-fernglas/')
SPF = ('Spektrum – Himmelsbeobachtung mit dem Fernglas', 'https://www.spektrum.de/ratgeber/himmelsbeobachtung-mit-dem-fernglas/2237998')
EINST = ('Sterngucker – Sterne fotografieren: Einstellungen', 'https://www.sterngucker.de/astrofotografie/sterne-fotografieren-einstellungen/')
ZR = ('Sterngucker – Zeitraffer-Rechner (500er- und NPF-Regel)', 'https://www.sterngucker.de/tools/zeitraffer-rechner/?seite=2')
GEM = ('EarthSky – Geminid meteor shower 2026', 'https://earthsky.org/astronomy-essentials/everything-you-need-to-know-geminid-meteor-shower/?ftag=YHF4eb9d17')
RMG = ('Royal Museums Greenwich – Geminids 2026', 'https://www.rmg.co.uk/discover/explore/geminid-meteor-shower-when-and-where-see-it-uk')
ZDF = ('ZDFheute – Nächste Sonnenfinsternis am 2. August 2027', 'https://www.zdfheute.de/panorama/sonnenfinsternis-naechstes-jahr-2027-wann-ort-100.html')
MOFI = ('Heidelberg24 (Daten: timeanddate) – Nächste Mondfinsternisse in Deutschland', 'https://www.heidelberg24.de/welt/naechste-mondfinsternis-in-deutschland-termine-und-ein-grosser-haken-zr-94463566.html')
IDA = ('DarkSky International – Winklmoosalm Dark Sky Park', 'https://darksky.org/places/winklmoosalm-dark-sky-park/')
RIW = ('Tourist-Info Reit im Winkl – Sternenpark Winklmoos-Alm', 'https://www.reitimwinkl.de/en/dark-sky-park-winklmoos-alm')
RUND = ('Tourist-Info Reit im Winkl – Sternenpark-Rundweg', 'https://www.reitimwinkl.de/en/sternenpark-rundweg')
VSW = ('muenchen.de – Bayerische Volkssternwarte', 'https://www.muenchen.de/sehenswuerdigkeiten/orte/120489.html')
VSW2 = ('muenchen.de – Himmelsbeobachtung in München', 'https://www.muenchen.de/freizeit/tipps-fuer-sternengucker-muenchen.html')

b = []
# 1 – Warum hier
b.append(H2('dunkel', '🌌 Wie dunkel ist es hier wirklich?', 'Ehrlich gesagt: dunkel genug für die Milchstraße – aber kein Sternenpark.'))
b.append(P('Über München liegt eine massive Lichtglocke; selbst vom Peißenberg aus sieht man sie deutlich, und auch Richtung Alpen ist dort viel künstliches Licht zu erkennen.' + q(*AZL)
           + ' Für den Spitzingsee heißt das: Der Blick nach Süden über die Berge ist der dunkelste, nach Norden Richtung Schliersee, Miesbach und München hellt der Horizont auf. Eine offizielle Messung der Himmelshelligkeit für den Spitzingsee haben wir nicht gefunden – deshalb nennen wir hier auch keine SQM- oder Bortle-Werte.'))
b.append(P('Laut bayerischem Umweltministerium kann inzwischen mehr als die Hälfte der Europäer die Milchstraße nicht mehr sehen; die Himmelshelligkeit nimmt in Europa um 5–6 % pro Jahr zu.' + q(*LEIT)
           + ' Bayern hat zwei Gesetze gegen Lichtverschmutzung, etwa zur Anstrahlung öffentlicher Gebäude.' + q(*ANL)))

b.append(H2('nacht', '🕰️ Wann es richtig dunkel ist', 'Sonnenuntergang reicht nicht: Erst wenn die Sonne 18° unter dem Horizont steht, beginnt die astronomische Nacht.'))
b.append(P('Die astronomische Dämmerung dauert, bis die Sonne 18° unter dem Horizont steht.' + q(*DAEM) + ' Im Hochsommer bleibt dadurch auf unserer Breite nur eine kurze echte Nacht übrig:'))
b.append(TAB(['Datum', 'Astronomische Nacht (Ortszeit)', 'Dauer'], naechte) + '<p style="font-size:.84rem;color:#4b5563;margin-top:-6px;">Eigene Berechnung (PyEphem) für die Obere Firstalm.</p>')
b.append(BOX('<strong>Augen anpassen:</strong> Die ersten etwa 30 Minuten Dunkelanpassung sind entscheidend – die Empfindlichkeit der Augen steigt dabei um das Zehntausendfache. Wer Licht braucht, nimmt schwaches Rotlicht, kurz und gedimmt.' + q(*ASTR)
           + ' Sterngucker rechnet mit 20 bis 30 Minuten; wer am Ende der nautischen Dämmerung beginnt, ist zur astronomischen Nacht bereit.' + q(*DAEM)))

# 2 – Kalender
b.append(H2('kalender', '📅 Himmelskalender Dezember 2026 – Dezember 2027', 'Neumond ist die beste Zeit für Milchstraße und Deep-Sky. Alle Zeiten in Ortszeit.'))
b.append(TAB(['Neumond (berechnet)', '', ''], [neumonde[i:i + 3] + [''] * (3 - len(neumonde[i:i + 3])) for i in range(0, len(neumonde), 3)]))
b.append(P('<strong>Sternschnuppen – und was der Mond dazu sagt</strong>'))
b.append(TAB(['Strom', 'Nacht', 'Mond beleuchtet (gegen Mitternacht)', 'Mond (berechnet)'], stroeme))
b.append(P('Die Geminiden im Dezember 2026 haben gute Bedingungen: Der Mond ist eine zunehmende Sichel und geht früh am Abend unter.' + q(*GEM) + q(*RMG)
           + ' Bei den Perseiden 2027 stört der Mond in der ersten Nachthälfte; nach seinem Untergang bleiben bis zur Morgendämmerung gut zwei dunkle Stunden (berechnet). Die Geminiden 2027 fallen auf Vollmond – ein schlechtes Jahr für sie.'))
b.append(GRID([
 CARD('sofi-2027', 'Partielle Sonnenfinsternis', '2. August 2027',
      'In Deutschland ist am 2. August 2027 eine partielle Sonnenfinsternis zu sehen, deutlich geringer als im August 2026; total ist sie in Teilen Spaniens, Nordafrikas und Arabiens.' + q(*ZDF),
      [('Obere Firstalm (berechnet)', f'Maximum gegen {lokal(tmax, True)} Uhr MESZ, rund {bedeckung} % der Sonnenfläche bedeckt, Sonne etwa {salt:.0f}° hoch'),
       ('Wichtig', 'Nie ohne zertifizierte Sonnenfinsternis-Brille oder Sonnenfilter in die Sonne schauen – auch nicht bei teilweiser Bedeckung')], icon='🌘'),
 CARD('mofi-2027', 'Halbschatten-Mondfinsternis', '20. Februar 2027',
      'Die nächste in Deutschland sichtbare Mondfinsternis am 20. Februar 2027 (Maximum 23:14 Uhr) ist nur eine Halbschattenfinsternis – mit bloßem Auge kaum zu bemerken. Die nächste totale folgt erst am 31. Dezember 2028.' + q(*MOFI),
      [], icon='🌕'),
]))

# 3 – Milchstraße
b.append(H2('milchstrasse', '✨ Die Milchstraße über den Bergen', 'Das helle Zentrum der Milchstraße steht bei uns immer tief im Süden.'))
b.append(P('Das Band der Milchstraße ist bei dunklem Himmel das ganze Jahr zu sehen, das helle Zentrum im Sternbild Schütze aber nur im Sommerhalbjahr.' + q(*MS)
           + ' Von der Oberen Firstalm aus steigt das galaktische Zentrum höchstens rund 13° über den Südhorizont – die Berge im Süden müssen also niedrig genug sein (berechnet):'))
b.append(TAB(['Monatsmitte 2027', 'Höchster Stand des Zentrums in der astronomischen Nacht', 'Uhrzeit'],
             [(MON[m - 1], (f'{h:.0f}°' if h > 0 else 'unter dem Horizont'), z) for m, h, z in zentrum]))

# 4 – Ausrüstung
b.append(H2('ausruestung', '🔭 Ausrüstung: weniger ist mehr', 'Das erste Instrument sollte ein Fernglas sein, kein Teleskop.'))
b.append(GRID([
 CARD('fernglas', 'Fernglas 10×50', 'der ehrliche Einstieg',
      'Für den Sternenhimmel aus der Hand ist 10×50 die richtige Größe: 5 mm Austrittspupille, knapp 7° Bildfeld, unter einem Kilogramm.' + q(*FG),
      [('Was du siehst', 'Andromedagalaxie als länglicher Fleck, Orionnebel als neblige Aufhellung um drei Sterne' + q(*FG)),
       ('Warum Fernglas', 'aufrechtes Bild, großes Gesichtsfeld, freihändig – ideal zum Aufsuchen am Himmel' + q(*SPF))], img='sternenhimmel-milchstrasse.jpg', alt='Orionnebel (Symbolbild)'),
 CARD('kleidung', 'Warm anziehen', 'auch im Sommer',
      'Wer still steht und nach oben schaut, kühlt am Berg schnell aus. Wie man dafür richtig schichtet, steht in unserem <a href="/content/layering/">Layering-Ratgeber</a>.',
      [('Licht', 'Stirnlampe mit gedimmtem Rotlicht, damit die Dunkelanpassung erhalten bleibt' + q(*ASTR))], icon='🧥'),
]))
b.append(AFF([('Fernglas 10×50', 'fernglas+10x50'), ('Stirnlampe mit Rotlicht', 'stirnlampe+rotlicht'), ('Drehbare Sternkarte', 'drehbare+sternkarte')]))

# 5 – Fotografieren
b.append(H2('foto', '📸 Milchstraße fotografieren', 'Kamera auf Stativ, lichtstarkes Weitwinkel, mondlose Nacht.'))
b.append(UL(['Belichtung 10 bis 20 Sekunden mit lichtstarkem Weitwinkel, in einer mondlosen Nacht fern der Städte' + q(*MS),
             'Weitwinkel 14–24 mm (Vollformat) bzw. 10–16 mm (APS-C), Blende f/2.8 oder offener' + q(*MS),
             'Manueller Modus, offene Blende, ISO 1600 bis 3200' + q(*EINST),
             '500er-Regel: 500 ÷ (Brennweite × Crop-Faktor) = maximale Belichtung in Sekunden – für heutige hochauflösende Sensoren meist zu großzügig; die NPF-Regel ist strenger. Bei 14 mm und f/2.8 sind meist 15 bis 20 Sekunden drin' + q(*ZR)]))

# 6 – Orte
b.append(H2('orte', '📍 Wo man in der Nähe noch mehr sieht', 'Wer den wirklich dunklen Himmel erleben will, fährt in den Chiemgau.'))
b.append(GRID([
 CARD('winklmoos', 'Sternenpark Winklmoos-Alm', 'Reit im Winkl · Chiemgau',
      'Seit 2018 International Dark Sky Park – der erste in den Alpen und der vierte in Deutschland.' + q(*IDA) + q(*RIW),
      [('Führungen', 'im Sommer öffentliche Sternführungen mit dem Physiker Manuel Philipp, Termine bei der Tourist-Info Reit im Winkl' + q(*RIW)),
       ('Rundweg', 'Sternenpark-Rundweg ab Parkplatz Winklmoos-Alm, 1,6 km' + q(*RUND))], img='sternenhimmel-berg.jpg', alt='Sternenhimmel über Bergen (Symbolbild)'),
 CARD('volkssternwarte', 'Bayerische Volkssternwarte', 'München, Rosenheimer Str. 145h',
      'Mit zwei Spiegel- und zwei Linsenteleskopen, Planetarium und regelmäßigen Abendführungen – geöffnet nur zu Führungen und Sonderveranstaltungen.' + q(*VSW) + q(*VSW2),
      [], icon='🏛️'),
]))
b.append(BOX('<strong>Rücksicht in der Nacht:</strong> Im Winter sind Wildtiere wie die Raufußhühner auf Ruhe angewiesen – nachts bitte auf Wegen und freien Flächen bleiben. Mehr dazu auf unserer Seite <a href="/content/fauna/#raufusshuehner">Tierwelt</a>. Und vor jeder Nacht am Berg: <a href="/wetter-webcams.html">Wetter prüfen</a>.', '#eef2ff', '#4338ca'))
b.append(q.liste())

seite('content/sternenhimmel/index.html', 'Sternenhimmel über Spitzingsee und Mangfallgebirge',
      '🌌 Sternenhimmel über dem Spitzingsee',
      'Wie dunkel es hier wirklich ist, wann die Milchstraße steht, welche Nächte 2027 lohnen und was du dafür brauchst – mit Quellen und eigenen Berechnungen für die Obere Firstalm.',
      FIG('sternenhimmel-berg.jpg', 'Milchstraße über Bergsilhouette', 'Milchstraße über einer Bergsilhouette (Symbolbild, nicht am Spitzingsee aufgenommen).'),
      [('dunkel', '🌌 Wie dunkel?'), ('nacht', '🕰️ Nachtlänge'), ('kalender', '📅 Kalender 2027'), ('milchstrasse', '✨ Milchstraße'),
       ('ausruestung', '🔭 Ausrüstung'), ('foto', '📸 Foto'), ('orte', '📍 Orte'), ('quellen', '📚 Quellen')],
      ''.join(b),
      'Sternenhimmel am Spitzingsee: Lichtverschmutzung ehrlich eingeordnet, Neumonde und Meteorströme 2027, Milchstraßen-Zentrum, Sonnenfinsternis 2.8.2027, Fernglas statt Teleskop, Sternenpark Winklmoos.',
      'Sternenhimmel', 'Weiter: <a href="/wetter-webcams.html">Wetter &amp; Webcams</a> · <a href="/content/layering/">Layering</a> · <a href="/content/fauna/">Tierwelt</a>')
