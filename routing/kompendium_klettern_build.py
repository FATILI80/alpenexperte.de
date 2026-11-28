#!/usr/bin/env python3
"""Baut die fünf Kletter-Kompendium-Artikel neu (Header, lesbares Layout, Quellen).

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
<title>{nr}. {titel} | Kletter-Kompendium | Alpen-Experte</title>
<meta name="description" content="{lead}">
<link rel="canonical" href="https://www.alpenexperte.de/content/klettern/{slug}.html">
<link rel="stylesheet" href="/css/style.css?v=20261127a">
{CSS}
</head><body>
{HEADER}
<main class="ka" id="main"><article>
<span class="badge">🔬 Faktor-10 Kletter-Kompendium · Teil {nr} von 5</span>
<h1>{titel}</h1>
<p class="lead">{lead}</p>
{body}
<h2>Quellen</h2>
<ul class="quellen">{ql}</ul>
<p style="font-size:.85rem;color:#64748b;">Rechenbeispiele sind eigene Rechnungen mit den genannten Annahmen und keine Messwerte. Stand der Quellen: November 2026.</p>
<div class="anzeige"><span style="background:#6c757d;color:#fff;padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:700;">Anzeige / Affiliate</span>
<h3 style="margin:12px 0 6px;color:#1f2933;">🛒 {ad_titel}</h3><p>{ad_text}</p>
<a href="{ad_url}" target="_blank" rel="sponsored noopener nofollow" style="background:#ff9900;color:#111;font-weight:700;padding:8px 18px;border-radius:6px;text-decoration:none;display:inline-block;">Bei Amazon ansehen &rarr;</a></div>
<p style="margin-top:28px;text-align:center;"><a href="/content/klettern/index.html" style="font-weight:700;color:#14532d;">← Zurück zur Klettern-Übersicht</a></p>
</article></main>
<footer class="site-footer" role="contentinfo"><div class="container" style="text-align:center;padding:var(--space-lg);"><p>&copy; 2025-2026 Alpen-Experte. Alle Rechte vorbehalten.</p></div></footer>
<script src="/js/main.js?v=20260612b" defer></script>
</body></html>
"""
    (ROOT / f"content/klettern/{slug}.html").write_text(html, encoding="utf-8")


AMZ = "https://www.amazon.de/s?k={}&linkCode=ll2&tag=bb8ozi-21&ref_=as_li_ss_tl"

# ---------------------------------------------------------------- 1
seite("angstmanagement", 1, "Sturzangst: Was Studien über Angst am Fels zeigen",
"Warum wir höher über dem Boden langsamer, zögerlicher und kürzer greifen – und wie man mit Sturztraining dagegen ansteuert.",
"""
<h2>Gleiche Route, andere Höhe</h2>
<p>Die Bewegungswissenschaftler um Rob Pijpers, Raôul Oudejans und Frank Bakker (VU Amsterdam) haben ein simples, aber wirkungsvolles Experiment gebaut: zwei identische Quergänge an einer Kletterwand, einer knapp über dem Boden, einer hoch oben. Die Route war gleich schwer – nur die Angst war es nicht.</p>
<ul>
<li>Im hohen Quergang brauchten Anfänger länger, machten mehr suchende Bewegungen, hielten die Griffe länger fest und bewegten sich langsamer (Pijpers et al. 2005).</li>
<li>Angst verkleinerte sowohl die geschätzte als auch die tatsächlich erreichte maximale Reichhöhe (Pijpers et al. 2006). Man traut sich also nicht nur weniger zu – man kann im Moment auch weniger.</li>
<li>Auch der Blick verändert sich: Unter Angst stiegen Kletter- und Bewegungszeiten, begleitet von veränderten Blickmustern (Nieuwenhuys et al. 2008).</li>
</ul>
<p>Die gute Nachricht: Wer mit Angst trainiert, klettert unter Druck besser. Das zeigten Oudejans und Pijpers 2009 bei erfahrenen Sportlern.</p>
<div class="merke"><strong>Merke:</strong> Sturzangst ist keine Charakterschwäche, sondern ein messbarer Effekt. Er lässt sich abbauen, wenn man ihn gezielt und in kleinen Schritten trainiert.</div>

<h2>Richtig stürzen – die DAV-Sicherheitsforschung</h2>
<p>In der Kletterhallen-Unfallstatistik von DAV und KLEVER waren in drei Jahren rund 23 Prozent der Seilkletterunfälle mit Rettungseinsatz Anprallverletzungen an der Wand, 55 Prozent Bodenstürze. Der DAV nimmt deshalb eigene Lehreinheiten zum richtigen Stürzen in die Trainerausbildung auf. Korrektes Fallen ersetzt aber kein aufmerksames, dynamisches Sichern.</p>
<h2>Sturztraining in kleinen Schritten</h2>
<ol>
<li>In der Halle, im steilen, freien Gelände, mit erfahrener Sicherungsperson.</li>
<li>Zuerst ins Seil setzen, dann knapp über der Exe loslassen, dann Schritt für Schritt höher.</li>
<li>Haltung: flacher Absprung, Blick zur Wand, Arme und Beine leicht gebeugt als „Puffer“.</li>
<li>Erst wenn das in der Halle sitzt, am Fels üben – und nie über Absätzen oder Bändern.</li>
</ol>
<div class="firstalm"><strong>Am Spitzingsee:</strong> Die Krettenburg oberhalb der Oberen Firstalm ist senkrecht bis überhängend und gut gebohrt – Gelände, in dem Stürze meist frei ins Seil gehen. Plattige Sektoren wie die Wichtelwand eignen sich dafür weniger. <a href="/content/klettern/index.html#krettenburg">Zur Krettenburg</a></div>
""",
[("Pijpers, Oudejans & Bakker 2005 – Anxiety-induced changes in movement behaviour (Quarterly Journal of Experimental Psychology)", "https://informahealthcare.com/doi/abs/10.1080/02724980343000945"),
 ("Pijpers, Oudejans, Bakker & Beek 2006 – The role of anxiety in perceiving and realizing affordances (Ecological Psychology, PDF)", "https://research.vu.nl/ws/files/2180736/191438.pdf"),
 ("Nieuwenhuys, Pijpers, Oudejans & Bakker 2008 – The Influence of Anxiety on Visual Attention in Climbing (PDF)", "https://research.vu.nl/ws/files/2397238/214718.pdf"),
 ("Oudejans & Pijpers 2009 – Training with anxiety (Literaturangabe)", "https://informahealthcare.com/doi/ref/10.1080/10615800903447588"),
 ("DAV – Meisterhaft fallen: richtig stürzen", "https://www.alpenverein.de/artikel/meisterhaft-fallen-richtig-stuerzen_d25bf736-ff71-4152-8203-0a7e44247b09")],
"Kletterhelm", "Auch am gut gebohrten Fels schützt der Helm bei Anprall und Steinschlag.", AMZ.format("Kletterhelm"))

# ---------------------------------------------------------------- 2
seite("neuromuskulaere-rekrutierung", 2, "Fingerkraft: Wie das Nervensystem die Muskeln zuschaltet",
"Vom Größenprinzip der motorischen Einheiten bis zu Studien mit dem Fingerboard: was Fingerkraft ausmacht und was Training nachweislich bringt.",
"""
<h2>Das Größenprinzip</h2>
<p>Ein Muskel besteht aus vielen motorischen Einheiten – je ein Nerv und alle Fasern, die er ansteuert. Elwood Henneman beschrieb ab 1957 das <em>Größenprinzip</em>: Je mehr Kraft gebraucht wird, desto mehr Einheiten werden zugeschaltet, und zwar in fester Reihenfolge von klein nach groß. So muss das Nervensystem die Reihenfolge nicht jedes Mal neu „berechnen“.</p>
<p>Für das Klettern heißt das: An großen Griffen arbeiten vor allem kleine, ausdauernde Einheiten. An kleinen Leisten müssen auch die großen, kräftigen Einheiten mit – und genau die ermüden schneller.</p>

<h2>Wie wichtig ist Fingerkraft?</h2>
<p>Maximale Fingerkraft und die Dauer, die man an einer Leiste hängen kann, erklärten in Studien bis zu 52 bzw. 70 Prozent der Unterschiede im Kletterkönnen (Baláš et al. 2012; Laffaye et al. 2016, zitiert nach Hermans et al. 2022). Ab etwa 45 bis 75 Prozent der maximalen Griffkraft wird zudem die Durchblutung des Unterarms abgedrückt – ab da läuft die Uhr bis zum „Pump“ (zitiert nach Devise et al. 2022).</p>
<div class="rechnung"><strong>Rechenbeispiel:</strong> Wer an einer Leiste maximal 600 N Fingerkraft aufbringt, drückt sich laut dieser Spanne schon ab 270 bis 450 N die Durchblutung ab. Je höher die Maximalkraft, desto größer der Abstand zwischen der Kraft, die eine Route verlangt, und dieser Schwelle. Eigene Rechnung, keine Messung.</div>

<h2>Was Fingerboard-Training nachweislich bringt</h2>
<ul>
<li><strong>Hermans et al. 2022:</strong> 35 Kletternde, 10 Wochen, zwei Einheiten à 48 Minuten pro Woche zusätzlich zum normalen Klettern – die maximale Fingerkraft stieg deutlich stärker als in der Kontrollgruppe.</li>
<li><strong>Devise et al. 2022:</strong> 54 erfahrene Kletternde, vier Wochen mit verschiedenen Intensitäten – Maximalkraft und Ausdauer nahmen zu, je nach Intensität unterschiedlich.</li>
<li><strong>López-Rivera & González-Badillo 2019:</strong> 26 fortgeschrittene Sportkletternde (Niveau um 7c+/8a), acht Wochen maximale oder intermittierende Hangs – alle Gruppen verbesserten die Haltedauer, ohne klaren Sieger.</li>
</ul>
<div class="merke"><strong>Merke:</strong> Fingerboard-Training ist für Fortgeschrittene wirksam, für Einsteiger aber riskant für Ringbänder und Sehnen. Wer neu anfängt, gewinnt am meisten durch viel abwechslungsreiches Klettern.</div>
""",
[("Hermans et al. 2022 – 10 Weeks Hangboard Training (Frontiers in Sports and Active Living)", "https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2022.888158/full"),
 ("Devise et al. 2022 – Effects of Different Hangboard Training Intensities (PMC)", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9039162/"),
 ("López-Rivera & González-Badillo 2019 – Three Hangboard Programs on Grip Endurance (PMC)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6458579/"),
 ("Henneman's size principle (Übersicht)", "https://en.wikipedia.org/wiki/Henneman%27s_size_principle"),
 ("Neuroscience (NCBI Bookshelf) – The size principle", "https://www.ncbi.nlm.nih.gov/books/NBK11021/")],
"Fingerboard", "Für Fortgeschrittene: Trainingsbrett mit verschiedenen Leistentiefen.", AMZ.format("Fingerboard+Klettern"))

# ---------------------------------------------------------------- 3
seite("uiaa-skala", 3, "UIAA-Skala und Normen: Von Welzenbach bis Fangstoß",
"Wie die Schwierigkeitsskala entstand, warum sie seit 1978 nach oben offen ist – und was die Zahlen auf Seil und Klettersteigset bedeuten.",
"""
<h2>Eine Skala aus München</h2>
<p>1923 hat der Münchner Bergsteiger Willo Welzenbach eine ältere Skala umgedreht und gestaucht – daraus wurden die Grade I bis VI. 1967 machte die UIAA sie offiziell zur „UIAA-Skala“. Der VI. Grad galt lange als „Grenze des Menschenmöglichen“; Reinhold Messner stellte das 1973 in seinem Buch <em>Der siebte Grad</em> infrage. 1978 nahm die UIAA den VII. Grad auf, 1985 wurde die Skala offiziell nach oben offen.</p>
<table><tr><th>UIAA</th><th>Französisch (ungefähr)</th></tr>
<tr><td>VI+</td><td>6a</td></tr><tr><td>VIII</td><td>7a+</td></tr><tr><td>XI</td><td>9a</td></tr></table>
<p>Die Umrechnungen gelten nur ungefähr – das betont die UIAA selbst.</p>
<div class="firstalm"><strong>Zum Einordnen:</strong> Der Taubenstein-Südgrat ist III, der Ruchenköpfe-Westgrat IV, die Krettenburg reicht vom 5. bis zum 10-. Grad. <a href="/content/klettern/index.html">Alle Ziele</a></div>

<h2>Kletterseile: EN 892</h2>
<p>Beim Normsturz fällt ein 80-kg-Gewicht 4,8 m tief, das Seilende ist fest – die ganze Energie muss das Seil schlucken. Solche Belastungen kommen in der Praxis so gut wie nie vor.</p>
<table><tr><th>Seiltyp</th><th>Prüfgewicht</th><th>Fangstoß max.</th><th>Normstürze min.</th></tr>
<tr><td>Einfachseil</td><td>80 kg</td><td>12 kN</td><td>5</td></tr>
<tr><td>Halbseil (Einzelstrang)</td><td>55 kg</td><td>8 kN</td><td>5</td></tr>
<tr><td>Zwillingsseil (Doppelstrang)</td><td>80 kg</td><td>12 kN</td><td>12</td></tr></table>
<div class="rechnung"><strong>Rechenbeispiel Sturzfaktor:</strong> Sturzfaktor = Fallhöhe geteilt durch ausgegebenes Seil. Wer 2 m über der letzten Exe stürzt und 10 m Seil ausgegeben hat, fällt mindestens 4 m: Faktor 4 / 10 = 0,4. Kurz über dem Boden mit wenig Seil ist der Faktor höher – dort wirken die größten Kräfte. Eigene Rechnung, ohne Seildehnung und Schlappseil.</div>

<h2>Klettersteigsets: EN 958</h2>
<p>Seit 2017 werden Klettersteigsets mit 40 und 120 kg Sturzmasse geprüft statt nur mit 80 kg. Der Bandfalldämpfer darf bis 220 cm lang sein und erst ab 1,3 kN aufreißen. Die Karabiner müssen längs 26 kN, quer 7 kN und offen 8 kN halten. Inzwischen gilt die Fassung EN 958:2024.</p>
<div class="merke"><strong>Merke:</strong> Sets nach alter Norm sind laut DAV nicht „unsicher“ – besonders leichte und schwere Personen sollten aber eines nach neuer Norm nutzen.</div>
""",
[("UIAA – Grades for rock climbing", "https://www.theuiaa.org/mountaineering/uiaa-grades-for-rock-climbing/"),
 ("UIAA – The scales of difficulty in climbing (PDF)", "https://www.theuiaa.org/documents/sport/THE-SCALES-OF-DIFFICULTY-IN-CLIMBING_p1b.pdf"),
 ("Grade (climbing) – Geschichte der Skalen", "https://en.wikipedia.org/wiki/Grade_(climbing)"),
 ("DAV – Der siebte Grad und by fair means", "https://www.alpenverein.de/artikel/der-siebte-grad-und-by-fair-means-1970er-bis-1980er-jahre_a7f886f0-ca83-4bd0-97e2-bf747a648299"),
 ("DAV Panorama 4/2021 – Wie funktioniert das? Bergseile (PDF)", "https://services.alpenverein.de/chameleon/public/acfb9707-6801-dea8-e3e2-1a26c6d994e1/Panorama-4-2021-Wie-funktioniert-das-Bergseile_32322.pdf"),
 ("Petzl – Worauf bezieht sich der Fangstoß eines Seils?", "https://www.petzl.com/DE/de/Sport/Worauf-bezieht-sich-der-Fangsto%C3%9F-eines-Seils-"),
 ("DAV – Klettersteigsets: Wie funktioniert das?", "https://www.alpenverein.de/artikel/klettersteigsets-wie-funktioniert-das_68908889-5acd-49e7-aeef-cf311455bff6"),
 ("DIN – EN 958:2017, ersetzt durch EN 958:2024", "https://6sku3uaup9f9.din.de/en/standard/din-en-958/261288707")],
"Einfachseil nach EN 892", "Dynamisches Kletterseil für Halle und Klettergarten.", AMZ.format("Einfachseil+Kletterseil+EN+892"))

# ---------------------------------------------------------------- 4
seite("erstbegehung", 4, "Erstbegehung: Wie Kletterrouten entstehen – und wer sie bezahlt",
"Vom roten Punkt im Frankenjura bis zur neuen Route an den Ruchenköpfen 2025: wie Routen erschlossen werden und warum Erschließer auf Spenden hoffen.",
"""
<h2>Der rote Punkt</h2>
<p>Im Frühjahr 1975 malte Kurt Albert im Frankenjura einen roten Punkt an den Einstieg des Adolf-Rott-Gedächtniswegs (VI+). Der Punkt hieß: Diese Route ist frei geklettert – ohne sich an Haken festzuhalten oder hochzuziehen. Aus dem Zeichen wurde der „Rotpunkt“, bis heute der Maßstab für eine saubere Begehung im Sportklettern.</p>

<h2>Klassiker und Neues am Spitzingsee</h2>
<ul>
<li><strong>Ruchenköpfe:</strong> Die Routennamen erzählen Klettergeschichte – die Neue Südwand heißt nach ihrem Erstbegeher Göttner, an der Südwand gibt es einen Dülferriss (V-). Gleichzeitig entstehen weiter neue Linien: Tom Schlager eröffnete 2025 an der Westwand „Im Westen viel Neues“ (7/7+).</li>
<li><strong>Taubenstein:</strong> Nach einer ruhigen Zeit begann die IG Klettern München &amp; Südbayern, die klassischen Routen zu sanieren und neue zu erschließen.</li>
<li><strong>Löchelwand:</strong> ein noch junges Gebiet mit teils losem Fels. Im Sektor „Tage“ steht eine Spendenbox für die weitere Erschließung.</li>
</ul>
<div class="merke"><strong>Warum Spenden?</strong> Bohrhaken, Umlenker und Kleber kosten Geld, das Einrichten viele Arbeitstage. Wer eine Spendenbox sieht, unterstützt damit genau die Routen, an denen er gerade klettert.</div>

<h2>Rücksicht gehört zur Erschließung</h2>
<p>Viele Felsen sind auch Lebensraum. Am Leonhardstein ist der Sektor Westpfeiler vom 1. März bis 31. Juli gesperrt. In anderen Gebieten bitten die Einheimischen, Routen mit brütenden Vögeln bis Ende Juni zu meiden und Felsen nicht übertrieben zu „putzen“.</p>
<div class="firstalm"><strong>Krettenburg:</strong> Das Gebiet über der Oberen Firstalm ist in den letzten Jahren stark gewachsen – Panico zählt 120 Routen, theCrag 124. <a href="/content/klettern/index.html#krettenburg">Zur Krettenburg</a></div>
""",
[("LACRUX – 50 Jahre Rotpunkt", "https://www.lacrux.com/?p=52769"),
 ("planetmountain – Remembering Kurt Albert, father of the redpoint", "https://www.planetmountain.com/en/news/climbing/remembering-kurt-albert-german-climbing-legend-father-of-redpoint.html"),
 ("Panico Topo des Monats 6/2026 – Ruchenköpfe, Mittlere Westwand (PDF)", "https://www.panico.de/media/wysiwyg/PDF/TopoDMonats/Topo%20des%20Monats-06-2026.pdf"),
 ("bergsteigen.com – Ruchenköpfe Neue Südwand (Göttner)", "https://www.bergsteigen.com/touren/klettern/ruchenkoepfe-neue-suedwand-goettner/"),
 ("summitpost – Taubenstein (IG Klettern)", "https://summitpost.org/taubenstein/463663"),
 ("theCrag – Löchelwand", "https://www.thecrag.com/de/klettern/germany/area/6731659860"),
 ("theCrag – Leonhardstein, Sperrung Westpfeiler", "https://www.thecrag.com/de/klettern/germany/area/2567648919"),
 ("theCrag – Spitzsteinwand, Verhaltenshinweise zu Brutzeiten", "https://www.thecrag.com/de/klettern/germany/area/2783598492"),
 ("Panico Topo des Monats 11/2024 – Krettenburg (PDF)", "https://www.panico.de/media/wysiwyg/Topo_des_Monats/Topo_des_Monats-11_2024.pdf")],
"Kletterführer Bayerische Alpen", "Topos zu Ruchenköpfen, Taubenstein und Co.", AMZ.format("Kletterf%C3%BChrer+Bayerische+Alpen+Panico"))

# ---------------------------------------------------------------- 5
seite("vertikale-architektur", 5, "Felsästhetik: Warum der Kalk hier so klettert, wie er klettert",
"Ein Korallenriff aus der Trias, Wasser mit Kohlensäure und viele Füße: woraus die Kletterfelsen zwischen Spitzingsee und Tegernsee bestehen.",
"""
<h2>Ein Riff mitten in den Voralpen</h2>
<p>Die markantesten Kletterberge der Gegend gehören zu einem Zug aus ehemaligem Riffkalk: Er zieht sich von Ost nach West und bildet Gipfel wie Leonhardstein, Plankenstein (Blankenstein), die Ruchenköpfe im Rotwandgebiet und den Brünnstein bei Kiefersfelden. Die benachbarte Rotwand selbst besteht laut geologischer Beschreibung aus Plattenkalk, Liasbasiskalk und Oberrätkalk aus der Trias.</p>

<h2>Wasserrillen: Kunst der Kohlensäure</h2>
<p>Regenwasser nimmt Kohlendioxid auf und wird zu schwacher Kohlensäure, die Kalk (Calciumcarbonat) lösen kann. Wo Wasser über nackten Fels läuft, entstehen <em>Karren</em> – Lösungsrinnen im Zentimeter- bis Meterbereich. Bei größerem Abfluss bilden sich Rinnenkarren mit gerundeten Kanten. Genau diese Rillen sind die griffigen „Wasserrillen“, die Kletterer am Kalk so lieben.</p>

<h2>Abgespeckt, locker, kompakt</h2>
<ul>
<li><strong>Abgespeckt:</strong> Viel begangene Normalwege werden glatt – der Buchstein-Normalweg und der Blankenstein-Normalweg gelten als „schon sehr abgespeckt“.</li>
<li><strong>Locker:</strong> Junge Gebiete wie die Löchelwand haben noch losen Fels; Helm ist dort dringend empfohlen.</li>
<li><strong>Kompakt:</strong> Am Taubenstein-Südgrat beschreiben Begeher den Fels als sehr kompakt und noch nicht abgespeckt.</li>
</ul>
<div class="merke"><strong>Merke:</strong> Kalk wird bei Nässe glatt, und abgespeckte Stellen besonders. Nach Regen lieber ein, zwei trockene Tage abwarten – das empfehlen Begeher auch für die grasigen Platten am Leonhardstein.</div>
<div class="firstalm"><strong>Hausfels:</strong> Die Krettenburg ist südseitig ausgerichtet – sie trocknet schnell und ist oft bis in den Herbst kletterbar. <a href="/content/klettern/index.html#krettenburg">Zur Krettenburg</a></div>
""",
[("summitpost – Buchstein: Riffkalk von Leonhardstein bis Brünnstein", "https://Summitpost.Org/buchstein/1074211"),
 ("Rotwand (Bayern) – Gestein", "https://wikiwand.com/de/articles/Rotwand_(Bayern)"),
 ("Spektrum Lexikon der Geowissenschaften – Karren", "https://www.spektrum.de/lexikon/geowissenschaften/karren/8093"),
 ("via-ferrata.de – Blankenstein Normalweg (abgespeckt)", "https://www.via-ferrata.de/gipfeldatenbank/bergtour/blankenstein?tab=reviews"),
 ("tourentipp.com – Ross- und Buchstein (abgespeckte Rinne, PDF)", "https://tourentipp.com/portal/touren/32/pdf/get"),
 ("via-ferrata.de – Taubenstein Südgrat (kompakter Fels)", "https://www.via-ferrata.de/touren/gps/taubenstein-suedgrat?tab=reviews"),
 ("theCrag – Löchelwand (loser Fels)", "https://www.thecrag.com/de/klettern/germany/area/6731659860"),
 ("bergsteigen.com – Hey Leoni, Leonhardstein (Nässe)", "https://www.bergsteigen.com/touren/klettern/hey-leoni-leonhardstein/")],
"Kletterschuhe", "Präzise Schuhe für Reibung auf Kalk und kleine Tritte.", AMZ.format("Kletterschuhe"))

print("fertig")
