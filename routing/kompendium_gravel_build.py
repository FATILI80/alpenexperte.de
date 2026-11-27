#!/usr/bin/env python3
"""Baut die fünf Gravel-Kompendium-Artikel neu (Header, lesbares Layout, Quellen).

Inhalte: belegte Aussagen mit Quelle, eigene Rechnungen als "Rechenbeispiel" markiert.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
kl = (ROOT / "content/klettern/index.html").read_text(encoding="utf-8")
a = kl.find('<header class="site-header"'); e = kl.find("</header>", a) + 9
HEADER = kl[a:e].replace(" nav-link--active", "").replace(' aria-current="page"', "")

CSS = """<style id="kompendium-artikel">
.ka{max-width:860px;margin:32px auto;padding:0 18px;color:#1f2933}
.ka article{background:#fff;border:1px solid #e0d8cc;border-radius:16px;padding:34px}
.ka h1{color:#14532d;font-size:1.9rem;margin:.4em 0 .3em}
.ka h2{color:#14532d;font-size:1.3rem;margin:1.6em 0 .5em}
.ka p,.ka li{color:#1f2933;line-height:1.7;font-size:1rem}
.ka .lead{font-size:1.1rem;color:#334155}
.ka .badge{background:rgba(45,138,86,.12);color:#2d8a56;padding:4px 12px;border-radius:8px;font-weight:700;font-size:.8rem}
.ka .rechnung{background:#f0f9ff;border-left:4px solid #0288d1;padding:14px 16px;border-radius:6px;margin:18px 0}
.ka .merke{background:#f0fdf4;border-left:4px solid #2d8a56;padding:14px 16px;border-radius:6px;margin:18px 0}
.ka .firstalm{background:#fff7ed;border-left:4px solid #ef6c00;padding:14px 16px;border-radius:6px;margin:18px 0}
.ka table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.95rem}
.ka th,.ka td{border:1px solid #d5dde5;padding:7px 9px;text-align:left;color:#1f2933}
.ka th{background:#f4f6f8}
.ka .quellen li{font-size:.9rem}
.ka .quellen a{color:#0369a1}
.ka .anzeige{margin-top:34px;background:#f8f9fa;padding:22px;border-radius:14px;border:1px solid #ced4da}
</style>"""


def seite(slug, nr, titel, lead, body, quellen, ad_titel, ad_text, ad_url):
    ql = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in quellen)
    html = f"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{nr}. {titel} | Gravel-Kompendium | Alpen-Experte</title>
<meta name="description" content="{lead}">
<link rel="canonical" href="https://www.alpenexperte.de/content/gravel/{slug}.html">
<link rel="stylesheet" href="/css/style.css?v=20261127a">
{CSS}
</head><body>
{HEADER}
<main class="ka" id="main"><article>
<span class="badge">🔬 Faktor-10 Gravel-Kompendium · Teil {nr} von 5</span>
<h1>{titel}</h1>
<p class="lead">{lead}</p>
{body}
<h2>Quellen</h2>
<ul class="quellen">{ql}</ul>
<p style="font-size:.85rem;color:#64748b;">Rechenbeispiele sind eigene Rechnungen mit den genannten Annahmen und keine Messwerte. Stand der Quellen: November 2026.</p>
<div class="anzeige"><span style="background:#6c757d;color:#fff;padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:700;">Anzeige / Affiliate</span>
<h3 style="margin:12px 0 6px;color:#1f2933;">🛒 {ad_titel}</h3><p>{ad_text}</p>
<a href="{ad_url}" target="_blank" rel="sponsored noopener nofollow" style="background:#ff9900;color:#111;font-weight:700;padding:8px 18px;border-radius:6px;text-decoration:none;display:inline-block;">Bei Amazon ansehen &rarr;</a></div>
<p style="margin-top:28px;text-align:center;"><a href="/gravel.html" style="font-weight:700;color:#14532d;">← Zurück zur Gravel-Übersicht</a></p>
</article></main>
<footer class="site-footer" role="contentinfo"><div class="container" style="text-align:center;padding:var(--space-lg);"><p>&copy; 2025-2026 Alpen-Experte. Alle Rechte vorbehalten.</p></div></footer>
<script src="/js/main.js?v=20260612b" defer></script>
</body></html>
"""
    (ROOT / f"content/gravel/{slug}.html").write_text(html, encoding="utf-8")


AMZ = "https://www.amazon.de/s?k={}&linkCode=ll2&tag=bb8ozi-21&ref_=as_li_ss_tl"

# ---------------------------------------------------------------- 1
seite("rollwiderstand", 1, "Watt-Fresser Schotter: Die Physik des Rollwiderstands",
"Warum der härteste Reifen auf der Forststraße nicht der schnellste ist – mit Messdaten vom Prüfstand und der Impedanz-Theorie.",
"""
<h2>Die Grundformel: Watt = Crr × Gewicht × Tempo</h2>
<p>Rollwiderstand ist die Energie, die ein Reifen beim Walken verliert: Er wird bei jeder Umdrehung an der Aufstandsfläche eingedrückt, und die Karkasse gibt diese Verformung nicht verlustfrei zurück. Beschrieben wird das mit dem Rollwiderstandsbeiwert <strong>Crr</strong>. Der Prüfstandsbetreiber BicycleRollingResistance.com nennt dazu die Formel <em>Rollwiderstand (W) = Crr × Geschwindigkeit (m/s) × Last (N)</em>.</p>
<div class="rechnung"><strong>Rechenbeispiel:</strong> Fahrer plus Rad und Gepäck 90 kg (≈ 883 N), Tempo 20 km/h (5,56 m/s).<br>
Crr 0,004 → 0,004 × 5,56 × 883 ≈ <strong>20 W</strong><br>
Crr 0,008 → 0,008 × 5,56 × 883 ≈ <strong>39 W</strong><br>
Ein doppelt so hoher Beiwert kostet bei gleichem Tempo also rund 20 W mehr – das ist auf einer Ausfahrt der Unterschied zwischen „läuft“ und „warum ist heute alles bergauf“.</div>

<h2>Was der Prüfstand misst – und was nicht</h2>
<p>Die bekannten Laborwerte entstehen auf einer Stahltrommel: BicycleRollingResistance.com testet bei 29 km/h, 42,5 kg Radlast und einer 77 cm großen Trommel mit Riffelblech-Oberfläche. Auf dieser glatten Fläche gilt: <strong>mehr Druck = weniger Rollwiderstand</strong>, weil sich der Reifen weniger verformt. Beim Continental GP 5000 S TR stieg der Rollwiderstand im Mittel von 9,6 W bei 5,0 bar auf 11,3 W bei 3,5 bar (Aluminium-Hakenfelge).</p>
<p>Außerdem zeigt die gleiche Testreihe: <strong>Bei gleichem Druck rollt der breitere Reifen leichter.</strong> In jeder Druckstufe lag der 32-mm-GP-5000 unter dem 23-mm-Reifen, zum Beispiel 9,0 W gegenüber 10,2 W.</p>

<h2>Schotter ist keine Trommel: Impedanz und Breakpoint</h2>
<p>Auf rauem Untergrund kommt ein zweiter Verlust dazu, den der Hersteller SILCA <strong>Impedanz</strong> nennt: Ein zu harter Reifen schluckt Unebenheiten nicht mehr, das ganze System aus Rad und Fahrer wird angehoben und durchgeschüttelt – Energie, die im Körper verpufft. SILCA beschreibt den Gesamtverlust als Summe aus Karkassenverlust (Trommelwert) und Impedanz. Daraus ergibt sich ein <strong>Breakpoint-Druck</strong>: Unterhalb davon dominieren die Karkassenverluste, darüber die Impedanz. Je rauer der Untergrund und je schmaler der Reifen, desto niedriger liegt dieser Punkt.</p>
<p>Die Asymmetrie ist der eigentliche Knaller: In SILCAs Messungen auf neuem Asphalt kostete ein Druck 10 psi (≈ 0,7 bar) <em>unter</em> dem Breakpoint nur etwa 1 W, 10 psi <em>darüber</em> dagegen etwa 9 W.</p>
<div class="merke"><strong>Merke:</strong> Lieber etwas zu weich als zu hart. Ein konkreter „richtiger“ Druck hängt von Gesamtgewicht, Reifenbreite, Felge und Untergrund ab – deshalb nennen wir hier bewusst keine Pauschalzahl. Rechner wie der von SILCA schätzen den Breakpoint aus diesen Angaben.</div>

<h2>Schlauch, Latex oder Tubeless?</h2>
<p>Ein Butylschlauch reibt bei jeder Verformung an der Karkasse und kostet messbar Leistung – besonders bei niedrigem Druck, also genau dort, wo Gravel gefahren wird:</p>
<table><tr><th>Druck (MTB-Reifen, je Reifen)</th><th>Tubeless</th><th>Latexschlauch</th><th>Butylschlauch</th></tr>
<tr><td>3,8 bar</td><td>15,5 W</td><td>15,6 W</td><td>18,0 W</td></tr>
<tr><td>1,7 bar</td><td>17,4 W</td><td>18,5 W</td><td>22,4 W</td></tr>
<tr><td>1,0 bar</td><td>20,2 W</td><td>22,0 W</td><td>27,9 W</td></tr></table>
<p style="font-size:.9rem;">Quelle: BicycleRollingResistance.com, Vergleichstest 2014.</p>
<p>Wichtig für die Ehrlichkeit: Tubeless „eliminiert“ nicht jede Reibung – ein guter Latex- oder TPU-Schlauch liegt nah dran. Beim GP 5000 S TR lagen Tubeless (20 ml Milch) und Latexschläuche bei 4,1 bar nur 0,3–0,5 W auseinander. Der große Sprung ist der Abschied vom Standard-Butyl.</p>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Die Schotterabfahrt von der Oberen Firstalm Richtung Spitzingsattel ist der perfekte Breakpoint-Test: Wenn das Rad springt und die Hände kribbeln, ist der Druck zu hoch – dann verlierst du laut Impedanz-Theorie nicht nur Komfort, sondern auch Watt.</div>
""",
[("BicycleRollingResistance.com – Grand Prix 5000 S TR: Hooked vs Hookless (Testbedingungen, Druckreihe)", "https://bicyclerollingresistance.com/specials/grand-prix-5000-s-tr-hooked-vs-hookless"),
 ("BicycleRollingResistance.com – Grand Prix 5000: 23, 25, 28 und 32 mm im Vergleich", "https://bicyclerollingresistance.com/specials/grand-prix-5000-comparison"),
 ("BicycleRollingResistance.com – Tubeless vs Latex vs Butyl (MTB)", "https://www.bicyclerollingresistance.com/specials/tubeless-latex-butyl-tubes"),
 ("BicycleRollingResistance.com – GP 5000 S TR Tubeless vs Schläuche", "https://bicyclerollingresistance.com/specials/grand-prix-5000-s-tr-tubeless-vs-tubes"),
 ("BicycleRollingResistance.com – Formel Crr × Geschwindigkeit × Last (Testbericht Durano Plus)", "https://www.bicyclerollingresistance.com/road-bike-reviews/schwalbe-durano-plus-2017"),
 ("SILCA – Part 4B: Rolling Resistance and Impedance", "https://silca.cc/blogs/silca/part-4b-rolling-resistance-and-impedance"),
 ("SILCA – Tire Pressure Calculator Explained (Breakpoint, ±10 psi)", "https://silca.cc/blogs/silca/tire-pressure-calculator-explained?page=4")],
"Schwalbe G-One R & Dichtmilch", "Schnelles Gravel-Profil, tubeless-fähig.", AMZ.format("Schwalbe+G-One+R+Gravelreifen"))

# ---------------------------------------------------------------- 2
seite("rahmenbau-technologien", 2, "Stahl, Alu, Titan, Carbon, 3D-Druck: Die Physik der Rahmen",
"Was Elastizitätsmodul und Dauerfestigkeit wirklich über einen Gravelrahmen aussagen – und was davon Marketing ist.",
"""
<h2>Steifigkeit: Der Elastizitätsmodul</h2>
<p>Wie stark sich ein Rohr unter Last biegt, hängt vom Werkstoff (Elastizitätsmodul) und von der Rohrform (Durchmesser, Wandstärke) ab. Sheldon Brown fasst die Werte der drei Rahmenmetalle so zusammen:</p>
<table><tr><th>Werkstoff</th><th>E-Modul</th><th>Dichte</th></tr>
<tr><td>Stahl</td><td>ca. 30 × 10⁶ psi (≈ 207 GPa)</td><td>490 lb/ft³</td></tr>
<tr><td>Titan</td><td>ca. 15–16,5 × 10⁶ psi (≈ 103–114 GPa)</td><td>280 lb/ft³</td></tr>
<tr><td>Aluminium</td><td>ca. 10–11 × 10⁶ psi (≈ 69–76 GPa)</td><td>168,5 lb/ft³</td></tr></table>
<p>Daraus folgt: Baut man drei Rahmen mit <em>identischen</em> Rohren, wäre der Alurahmen nur etwa ein Drittel so steif wie der Stahlrahmen, der Titanrahmen etwa halb so steif. Genau deshalb haben Alurahmen dicke Rohre: Ein größerer Durchmesser gleicht den niedrigeren Modul aus. Wichtig: Der E-Modul ist für alle Stähle praktisch gleich – „besserer“ Stahl ist fester, aber nicht steifer.</p>
<div class="merke"><strong>Merke:</strong> Das Fahrgefühl macht vor allem die Konstruktion, nicht der Werkstoffname. road.cc bringt es auf den Punkt: Die Fahreigenschaften entstehen durch gutes Rahmendesign, das die Eigenschaften des Materials nutzt.</div>

<h2>Dauerfestigkeit: Wer hält ewig?</h2>
<p>Stahl und Titan haben eine <strong>Dauerfestigkeit</strong>: Unterhalb einer bestimmten Spannung halten sie beliebig viele Lastwechsel aus. Aluminium hat diese Grenze nicht – bei genug Zyklen versagt es auch bei kleinen Spannungen. Deshalb werden Alurahmen mit mehr Reserve ausgelegt. Auch Faserverbund (Carbon) hat laut einer US-Patentschrift zur Rahmenhaltbarkeit keine Dauerfestigkeitsgrenze im klassischen Sinn.</p>
<p>Carbon ist zudem <strong>anisotrop</strong>: Die Steifigkeit hängt von der Faserrichtung ab. Das ist sein großer Vorteil – Ingenieure können einen Rahmen in Tretlagerrichtung steif und vertikal nachgiebiger auslegen.</p>

<h2>3D-gedruckter Stahl: Das Beispiel Urwahn</h2>
<p>Urwahn aus Magdeburg kombiniert CroMo-Stahlrohre mit 3D-gedruckten Stahl-Knotenpunkten, gefertigt im Laser-Pulverbett-Verfahren. Laut BIKE-Magazin wird jedes neue Modell beim Prüfinstitut EFBE nach der Norm 4210 getestet. Der „Softride“-Hinterbau ohne klassisches Sitzrohr soll das Hinterrad elastisch federn lassen, ohne das Tretlager weich zu machen – so beschreibt es der Partner Schmolke Carbon. Mit dem Softride 2.0 hat Urwahn den Rahmen 2024/25 überarbeitet, 2026 kam laut ingenieur.de eine Titanvariante (Softride Ti64) dazu.</p>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Auf 900 Höhenmetern Forststraße merkst du Steifigkeit im Wiegetritt, Nachgiebigkeit dagegen auf der Abfahrt. Kein Werkstoff gewinnt beides automatisch – entscheidend ist, wie der Rahmen konstruiert ist und welche Reifenbreite reinpasst (siehe Teil 1).</div>
""",
[("Sheldon Brown – Frame Materials for the Touring Cyclist (E-Modul, Dichte)", "https://www.sheldonbrown.com/frame-materials.html"),
 ("road.cc – Ultimate guide to frame materials (Dauerfestigkeit)", "https://road.cc/content/feature/ultimate-guide-frame-materials-226920"),
 ("Princeton University – Materials: S-N-Kurven Stahl vs. Aluminium", "https://www.princeton.edu/~maelabs/hpt/materials/mater_30.htm"),
 ("USPTO – Cycle frame fatigue and durability assembly (Patent 9797810)", "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9797810"),
 ("arXiv – FRAMED: Structural Performance Prediction of Bicycle Frames (Isotropie/Anisotropie)", "https://arxiv.org/pdf/2201.10459"),
 ("BIKE-Magazin – Reportage Urwahn: Stahl, frisch aus dem Drucker", "https://www.bike-magazin.de/fahrraeder/city-bikes/urban-bikes/reportage-urwahn-stahl-frisch-aus-dem-drucker/"),
 ("BIKE-Magazin – Softride 2.0: Rahmen ohne Sitzrohr", "https://www.bike-magazin.de/fahrraeder/kaufberatung/softride-2-0-rahmen-ohne-sitzrohr-urwahn-entwickelt-den-stahlrahmen-weiter/"),
 ("3Dnatives – Schmolke Carbon zur Hinterbau-Federung", "https://www.3dnatives.com/de/22742-2-120220201"),
 ("ingenieur.de – Urwahn Softride Ti64 (Februar 2026)", "https://www.ingenieur.de/technik/fachbereiche/produktion/ein-neuer-titan-auf-dem-fahrradmarkt-urwahn-stellt-neues-modell-vor/")],
"Wera Drehmomentschlüssel", "Carbon- und Alu-Klemmungen richtig anziehen.", AMZ.format("Wera+Bicycle+Set+Torque+Drehmomentschluessel"))

# ---------------------------------------------------------------- 3
seite("funk-schaltungen", 3, "Elektronen am Berg: 1×12 und 1×13 im Steilstück",
"Bandbreite, Gangsprünge und was eine 10–46-Kassette an der Firstalm-Rampe wirklich bedeutet.",
"""
<h2>Bandbreite in Prozent</h2>
<p>Die Bandbreite ist das Verhältnis von größtem zu kleinstem Ritzel. SRAMs 13-fach-Gravelkassetten (XPLR XG-1351, -1371, -1391) haben 10–46 Zähne, laut Hersteller <strong>460 %</strong> Bandbreite, mit der Abstufung 10-11-12-13-15-17-19-21-24-28-32-38-46. Die kleinen Ritzel sind in Ein-Zahn-Schritten gestuft – „Rennrad-Abstufung“, wie BikeRadar schreibt.</p>
<p>Campagnolos Ekar-Kassetten (13-fach) gibt es in drei Abstufungen:</p>
<table><tr><th>Ekar</th><th>Ritzel</th><th>Bandbreite*</th></tr>
<tr><td>9–36 (Endurance)</td><td>9-10-11-12-13-14-16-18-20-23-27-31-36</td><td>400 %</td></tr>
<tr><td>9–42 (Gravel Race)</td><td>9-10-11-12-13-14-16-18-21-25-30-36-42</td><td>467 %</td></tr>
<tr><td>10–44 (Gravel Adventure)</td><td>10-11-12-13-14-15-17-19-22-26-32-38-44</td><td>440 %</td></tr></table>
<p style="font-size:.9rem;">*Eigene Rechnung: größtes ÷ kleinstes Ritzel. Händlerangaben zum 10–44 nennen teils 38, teils 39 Zähne am vorletzten Ritzel. Inzwischen bietet Campagnolo mit Ekar GT zusätzlich eine 10–48-Kassette an.</p>

<h2>Was heißt das am Berg?</h2>
<div class="rechnung"><strong>Rechenbeispiel kleinster Gang:</strong> Kettenblatt 40 Zähne, Ritzel 46 → Übersetzung 0,87. Mit einem angenommenen Radumfang von 2,2 m (typisch für 700C mit 40–45 mm Reifen) und 70 Kurbelumdrehungen pro Minute:<br>
0,87 × 2,2 m × 70 × 60 ÷ 1000 ≈ <strong>8,0 km/h</strong>.<br>
Bei 10 % Steigung und 90 kg Systemgewicht braucht allein das Heben etwa 90 × 9,81 × 2,22 m/s × 0,0995 ≈ <strong>195 W</strong> – plus Roll- und Luftwiderstand.</div>
<p>Wer weniger Dauerleistung hat, braucht also ein kleineres Kettenblatt oder ein größeres Ritzel, um die Trittfrequenz zu halten. Genau dafür sind die großen Sprünge am oberen Kassettenende da.</p>

<h2>Warum 1× am Gravelbike?</h2>
<p>Ein Kettenblatt bedeutet keinen Umwerfer, weniger Teile, die verschlammen, und eine einfache Bedienung. Der Preis sind größere Gangsprünge als bei 2×. Der Schritt von 12 auf 13 Ritzel soll genau diese Lücke verkleinern: SRAM betont die engen Sprünge, Campagnolo wirbt damit, die Bandbreite eines 2×-Systems „ohne Verschwendung“ abzudecken.</p>
<p>„Funk“ bedeutet hier: SRAMs AXS-Komponenten schalten elektronisch und kabellos. Laut BikeRadar ist die neue Red XPLR AXS mit bestehenden 12-fach-AXS-Komponenten kompatibel, braucht aber einen Rahmen mit UDH-Schaltauge.</p>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Die letzten Kehren zur Oberen Firstalm sind kein Ort für Heldentum. Wer hier im 46er-Ritzel noch 60 Umdrehungen schafft, darf oben den Kaiserschmarrn mit gutem Gewissen bestellen.</div>
""",
[("SRAM – XG-1371 Kassette (Ritzelabstufung, 10–46)", "https://www.sram.com/en/sram/models/cs-xg-1371-e1"),
 ("SRAM – XG-1351 Kassette (460 % Bandbreite)", "https://www.sram.com/en/sram/models/cs-xg-1351-e1"),
 ("BikeRadar – SRAM Red XPLR AXS mit 13 Gängen", "https://www.bikeradar.com/news/sram-aims-to-set-the-gravel-standard-with-red-axs-xplr"),
 ("bike-components – Campagnolo Ekar 13-fach Kassette (Abstufungen)", "https://www.bike-components.de/en/Campagnolo/Ekar-13-speed-Cassette-p78104"),
 ("Campagnolo – Ekar GT 13-speed Kassette (bis 10–48)", "https://campagnolo.com/ww-it/pignoni-ekar-gt-13-speed/CCSEKAR1X13SGT.html")],
"SRAM eTap AXS Akku & Kettenwachs", "Ersatzakku für lange Tage am Berg.", AMZ.format("SRAM+eTap+AXS+Akku"))

# ---------------------------------------------------------------- 4
seite("geometrien-flare", 4, "Aero vs. Kontrolle: Was Geometriedaten und Flare verraten",
"Stack, Reach, Lenkwinkel und Flare – wie Zahlen aus dem Datenblatt dein Fahrgefühl auf Schotter bestimmen.",
"""
<h2>Stack und Reach: Die Sitzposition in zwei Zahlen</h2>
<p><strong>Stack</strong> ist der senkrechte Abstand von der Tretlagermitte zur Oberkante des Steuerrohrs, <strong>Reach</strong> der waagerechte Abstand zwischen denselben Punkten. Viel Stack und wenig Reach ergeben eine aufrechte Position, wenig Stack und viel Reach eine gestreckte, aerodynamische.</p>
<p>Race-Gravelbikes übernehmen laut BikeTips viel Rennrad-Geometrie: Lenkwinkel um 72–73°, kurze Kettenstreben, wenig Stack, viel Reach. Adventure-Räder haben mehr Stack, kürzeren Reach und einen flacheren Lenkwinkel für mehr Laufruhe.</p>

<h2>Flare: Breiter Halt unten, schmal oben</h2>
<p>Flare ist der Winkel, um den die Unterlenker nach außen gespreizt sind. Laut bike-components verhindert ein ausgeprägter Flare beim aktiven Fahren im Unterlenker, dass die Unterarme an den Oberlenker stoßen. Üblich für Gravel sind etwa 12–25°. Extreme Beispiele aus dem Gear-Index von Bikepacking.com: Crust Shaka Bar mit 14° und 530 mm Breite, andere Modelle mit 29°.</p>
<p>Der Trick: Durch Flare kann der Lenker oben an den Griffen schmal und unten breit sein. ENVEs SES-Aerolenker zum Beispiel misst an den Griffen 35 cm und durch 5 cm Flare unten 40 cm.</p>

<h2>Lenkerbreite und Aerodynamik</h2>
<p>Schmale Lenker verkleinern die Stirnfläche. Cycling Weekly hat das im Windkanal gemessen: Mit einem etwas schmaleren Lenker ließen sich auf den Griffen bei konstant 35 km/h rund <strong>18 W</strong> sparen, etwa 10 %. Mit noch schmaleren Lenkern und aggressiver Haltung waren es über 50 W.</p>
<div class="merke"><strong>Einordnung:</strong> Diese Werte stammen aus Windkanaltests bei 35–45 km/h. Auf einer steilen Schotterauffahrt mit 8 km/h spielt Aerodynamik kaum eine Rolle – dort zählen Kontrolle und Atmung. Flare ist genau der Kompromiss: schmal und aero auf der Geraden, breit und kontrolliert in der Abfahrt.</div>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Auf dem Rollerweg Richtung Spitzingsee lohnt sich die schmale Griffhaltung, in der losen Abfahrt durch die Kehren greifst du in den breiten Unterlenker. Ein Lenker, zwei Charaktere.</div>
""",
[("Canyon – Gravel bike geometry explained (Stack, Reach)", "https://www.canyon.com/en-us/blog-content/gravel-bike-geometry-explained/b24042025.html"),
 ("BikeTips – Gravel Bike Geometry Explained (Lenkwinkel, Race vs. All-Road)", "https://biketips.com/gravel-bike-geometry-explained/"),
 ("bike-components – Gravel handlebar guide: geometry, flare, drop, reach", "https://www.bike-components.de/blog/en/guides/gravel-handlebar-guide-geometry-flare-drop-reach"),
 ("Competitive Cyclist – Handlebar flare explained (12–25°)", "https://www.competitivecyclist.com/bulletin/handlebar-flare-explained"),
 ("Bikepacking.com – Gear Index: Gravel Bars", "https://bikepacking.com/index/gravel-bars/"),
 ("Saddleback – Aero handlebars: ENVE SES (35/40 cm)", "https://saddleback.co.uk/blogs/journal/aero-handlebars-how-much-difference-do-they-make"),
 ("Cycling Weekly – Windkanaltest schmale Lenker (über Everand)", "https://www.everand.com/article/732219317/Can-Narrow-Handlebars-Make-You-Significantly-Faster")],
"Ergon BT Gravel – Lenkerband", "Dämpfendes Lenkerband für lange Schotterabfahrten.", AMZ.format("Ergon+BT+Gravel+Lenkerband"))

# ---------------------------------------------------------------- 5
seite("bikepacking-schwerpunkt", 5, "Dynamik unter Last: Die Physik der Bikepacking-Taschen",
"Wohin das Gewicht gehört, warum die Lenkerrolle leicht bleiben muss und was jedes Kilo am Berg kostet.",
"""
<h2>Jedes Kilo zählt doppelt: Rollen und Heben</h2>
<p>Rollwiderstand und Hubarbeit wachsen beide mit dem Gewicht (siehe Teil 1). Am Berg dominiert das Heben:</p>
<div class="rechnung"><strong>Rechenbeispiel:</strong> 12 kg Gepäck, 10 % Steigung, 8 km/h (2,22 m/s):<br>
Zusatzleistung fürs Heben ≈ 12 × 9,81 × 2,22 × 0,0995 ≈ <strong>26 W</strong>.<br>
Für die Auffahrt zur Oberen Firstalm heißt das: Entweder 26 W mehr treten oder langsamer fahren. Den Rucksack zum Wirt tragen lassen ist leider keine Option.</div>

<h2>Schwerpunkt: tief und mittig gewinnt</h2>
<p>Laut TOUR halten Rahmentaschen das Gewicht mittig zwischen den Rädern, der Schwerpunkt bleibt tief. Eine 2-kg-Rahmentasche beeinflusst das Fahrverhalten weniger als das gleiche Gewicht auf einem hoch montierten Gepäckträger. Werkzeug, Wasser und Ersatzteile gehören deshalb in den Rahmen.</p>
<p>Old Man Mountain, ein Hersteller von Gepäckträgern, beschreibt den Effekt der Höhe: Je höher die Last sitzt, desto länger dauert es, die Schräglage zu ändern – etwa beim Einlenken oder beim Wechsel von links nach rechts.</p>

<h2>Die Lenkerrolle: groß, aber leicht</h2>
<p>Gewicht am Lenker dreht bei jeder Lenkbewegung mit. Das BIKE-Magazin warnt: Eine schwere Lenkertasche wirkt direkt auf jede Lenkbewegung, deshalb gehören dort nur möglichst leichte Dinge hinein. Polygon empfiehlt als Startpunkt eine Verteilung von etwa 40 % vorne und 60 % hinten und für die Lenkertasche nur leichtes, voluminöses Gepäck wie Schlafsack oder Kleidung.</p>
<table><tr><th>Ort</th><th>Was hinein</th><th>Warum</th></tr>
<tr><td>Rahmentasche</td><td>Werkzeug, Wasser, Essen, Ersatzteile</td><td>Tiefer, mittiger Schwerpunkt</td></tr>
<tr><td>Lenkerrolle</td><td>Schlafsack, Daunenjacke</td><td>Groß, aber leicht – Lenkung bleibt neutral</td></tr>
<tr><td>Satteltasche</td><td>Kleidung, Isomatte</td><td>Mittel; schwer beladen pendelt sie</td></tr></table>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Für eine Übernachtungstour ab der Oberen Firstalm: schwere Sachen in den Rahmen, den Schlafsack nach vorne. Wer die Abfahrt Richtung Valepp mit vollgepackter Lenkerrolle fährt, merkt den Unterschied spätestens in der zweiten Kehre.</div>
""",
[("TOUR – Radfahren mit Gepäck: So beeinflusst Ladung das Fahrverhalten", "https://www.tour-magazin.de/en/buying-advice/counsellor/cycling-with-a-load-how-luggage-affects-handling/"),
 ("BIKE-Magazin – Radfahren mit Gepäck: Handling und Trägheit", "https://www.bike-magazin.de/en/equipment/bike-bags/cycling-with-luggage-how-this-affects-handling-and-inertia/"),
 ("Old Man Mountain – A Balancing Act: Bag Placement and Weight Distribution", "https://oldmanmountain.com/a-balancing-act/"),
 ("Polygon – Weight distribution tips for bikepacking (40/60)", "https://www.polygonbikes.com/weight-distribution-tips-for-bikepacking/")],
"Ortlieb Frame-Pack RC – Rahmentasche", "Wasserdichte Rahmentasche für den tiefen Schwerpunkt.", AMZ.format("Ortlieb+Frame+Pack+Rahmentasche"))

print("fertig")
