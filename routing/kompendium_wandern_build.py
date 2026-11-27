#!/usr/bin/env python3
"""Baut die fünf Wander-Kompendium-Artikel neu (Header, lesbares Layout, Quellen).

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
<title>{nr}. {titel} | Wander-Kompendium | Alpen-Experte</title>
<meta name="description" content="{lead}">
<link rel="canonical" href="https://www.alpenexperte.de/content/wandern/{slug}.html">
<link rel="stylesheet" href="/css/style.css?v=20261127a">
{CSS}
</head><body>
{HEADER}
<main class="ka" id="main"><article>
<span class="badge">🔬 Faktor-10 Wander-Kompendium · Teil {nr} von 5</span>
<h1>{titel}</h1>
<p class="lead">{lead}</p>
{body}
<h2>Quellen</h2>
<ul class="quellen">{ql}</ul>
<p style="font-size:.85rem;color:#64748b;">Rechenbeispiele sind eigene Rechnungen mit den genannten Annahmen und keine Messwerte. Stand der Quellen: November 2026.</p>
<div class="anzeige"><span style="background:#6c757d;color:#fff;padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:700;">Anzeige / Affiliate</span>
<h3 style="margin:12px 0 6px;color:#1f2933;">🛒 {ad_titel}</h3><p>{ad_text}</p>
<a href="{ad_url}" target="_blank" rel="sponsored noopener nofollow" style="background:#ff9900;color:#111;font-weight:700;padding:8px 18px;border-radius:6px;text-decoration:none;display:inline-block;">Bei Amazon ansehen &rarr;</a></div>
<p style="margin-top:28px;text-align:center;"><a href="/content/wandern/index.html" style="font-weight:700;color:#14532d;">← Zurück zur Wander-Übersicht</a></p>
</article></main>
<footer class="site-footer" role="contentinfo"><div class="container" style="text-align:center;padding:var(--space-lg);"><p>&copy; 2025-2026 Alpen-Experte. Alle Rechte vorbehalten.</p></div></footer>
<script src="/js/main.js?v=20260612b" defer></script>
</body></html>
"""
    (ROOT / f"content/wandern/{slug}.html").write_text(html, encoding="utf-8")


AMZ = "https://www.amazon.de/s?k={}&linkCode=ll2&tag=bb8ozi-21&ref_=as_li_ss_tl"

# ---------------------------------------------------------------- 1
seite("ley-lines-kraftorte", 1, "Kraftorte, Ley-Lines und Magnetfeld: Was davon messbar ist",
"Woher die Idee der Ley-Lines stammt, wie stark das Erdmagnetfeld und seine Anomalien wirklich sind – und warum ein Ort trotzdem Kraft geben kann.",
"""
<h2>Die Ley-Lines: Eine Idee aus Herefordshire</h2>
<p>Den Begriff hat der englische Geschäftsmann und Hobby-Archäologe Alfred Watkins geprägt, vor allem mit seinem Buch <em>The Old Straight Track</em> von 1925. Er hielt die Linien für Reste prähistorischer Handelswege. Erst ab den 1960er-Jahren wurden daraus „Energielinien“.</p>
<p>Fachleute waren von Anfang an skeptisch: Der Archäologe O. G. S. Crawford wollte nicht einmal Anzeigen für das Buch in seiner Zeitschrift <em>Antiquity</em> drucken. Das stärkste Gegenargument ist statistisch: Verteilt man genug Punkte zufällig auf einer Fläche, entstehen zwangsläufig gerade Ausrichtungen – rein zufällig.</p>
<div class="rechnung"><strong>Gedankenexperiment:</strong> Zeichne auf einer Wanderkarte des Mangfallgebirges alle Kapellen, Gipfelkreuze, Almen und Wegkreuze ein. Bei mehreren hundert Punkten findest du mit einem Lineal mühelos Linien mit vier oder fünf „Treffern“. Genau das ist der Zufallseffekt, den Statistiker beschreiben.</div>

<h2>Wie stark ist das Erdmagnetfeld – und eine Anomalie?</h2>
<p>In Mitteleuropa ist das Erdmagnetfeld knapp 50.000 Nanotesla (nT) stark. Magnetisierte Gesteine in der oberen Erdkruste erzeugen an der Oberfläche lokale Anomalien von einigen hundert bis tausend nT. Eine Anomalie verändert das Feld also typischerweise um etwa ein bis zwei Prozent.</p>

<h2>Kann der Mensch das spüren?</h2>
<p>Ein Team um Connie Wang und Joseph Kirschvink (Caltech) hat 2019 im Fachjournal <em>eNeuro</em> gezeigt, dass das Gehirn messbar reagiert, wenn ein Magnetfeld in Erdstärke im Labor gedreht wird: Die Alpha-Wellen im EEG wurden schwächer. Das war eine Reaktion auf <em>Richtungsänderungen</em> des ganzen Feldes, keine bewusste Wahrnehmung. Die Autoren betonen selbst, dass die meisten Menschen geomagnetische Reize im Alltag nicht bewusst wahrnehmen.</p>
<div class="merke"><strong>Einordnung:</strong> Die frühere Behauptung auf dieser Seite, magnetische Anomalien im Nanotesla-Bereich markierten „exakt“ alte Kultplätze und wirkten auf das vegetative Nervensystem, ist durch keine Quelle belegt. Wir haben sie gestrichen.</div>

<h2>Warum ein Ort trotzdem Kraft geben kann</h2>
<p>Dass Menschen an Pässen, Gipfeln oder Quellen zur Ruhe kommen, braucht keine Magnetlinie. Weite Aussicht, Stille, Bewegung und Wald wirken messbar auf Stresswerte – mehr dazu in Teil 2 (Herz und Atmung) und Teil 5 (Waldbaden). Kult- und Wallfahrtsorte entstanden zudem oft an auffälligen Landmarken, Wegkreuzungen und Quellen – praktische Gründe, keine unsichtbaren Felder.</p>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Nimm einen Kompass mit auf die Brecherspitze. Wenn die Nadel auf dem Gipfel ruhig nach Norden zeigt, weißt du: Das „Kribbeln“ oben kommt von der Aussicht und den Höhenmetern, nicht vom Magnetfeld.</div>
""",
[("Wikipedia – Ley line (Watkins, Kritik, Zufallsausrichtungen)", "https://en.wikipedia.org/wiki/Ley_line"),
 ("Wikipedia – Alignments of random points", "https://en.wikipedia.org/wiki/Alignments_of_random_points"),
 ("Wikipedia – The Old Straight Track (1925, Crawford)", "https://en.wikipedia.org/wiki/The_Old_Straight_Track"),
 ("Der Standard – Erdmagnetfeld in Mitteleuropa knapp 50.000 nT", "https://www.derstandard.at/story/3000000297738/"),
 ("chemie.de Lexikon – Erdmagnetismus (Krustenanomalien 100–1000 nT)", "https://www.chemie.de/lexikon/Erdmagnetismus.html"),
 ("Wang et al. 2019, eNeuro – Transduction of the Geomagnetic Field (PubMed)", "https://pubmed.ncbi.nlm.nih.gov/31028046/"),
 ("Wang et al. 2019 – Volltext eNeuro", "https://www.eneuro.org/content/6/2/ENEURO.0483-18.2019")],
"Silva Expedition 4 Kompass", "Klassischer Plattenkompass für Karte und Gelände.", AMZ.format("Silva+Expedition+4+Kompass"))

# ---------------------------------------------------------------- 2
seite("vagustonus-hrv", 2, "Herz, Atem, Nerven: Was Wandern mit der HRV macht",
"Herzfrequenzvariabilität, langsames Atmen und Stresshormone – was Studien zeigen und was Marketing ist.",
"""
<h2>Was ist HRV?</h2>
<p>Die Herzfrequenzvariabilität (HRV) beschreibt die Schwankungen der Zeitabstände zwischen zwei Herzschlägen. Das Herz schlägt nicht wie ein Metronom: Beim Einatmen wird es etwas schneller, beim Ausatmen langsamer. Diese atemabhängige Schwankung heißt respiratorische Sinusarrhythmie und wird über den Vagusnerv gesteuert.</p>

<h2>Der Atemrhythmus als Stellschraube</h2>
<p>Normalerweise atmet der Mensch etwa 9 bis 24 Mal pro Minute. Atmet man deutlich langsamer, wachsen die Herzfrequenz-Schwankungen stark an – laut Lehrer und Gevirtz bei fast allen Menschen, oft schon innerhalb einer Minute. Die sogenannte Resonanzfrequenz liegt bei vielen Menschen bei etwa 6 Atemzügen pro Minute, individuell meist zwischen 4,5 und 6,5.</p>
<div class="rechnung"><strong>Rechenbeispiel Gehrhythmus:</strong> 6 Atemzüge pro Minute sind 10 Sekunden pro Atemzug. Bei einem ruhigen Aufstiegstempo von etwa 100 Schritten pro Minute wären das rund 8 Schritte pro Atemzug, zum Beispiel 4 Schritte ein, 4 Schritte aus. Steil bergauf klappt das nicht mehr – dann braucht der Körper mehr Luft, und das ist richtig so.</div>

<h2>Natur und Stresswerte</h2>
<p>In einer japanischen Versuchsreihe mit 420 Personen in 35 Wäldern zeigten Menschen, die in der Natur saßen, im Vergleich zur Stadt-Kontrollgruppe 12,4 % niedrigere Cortisolwerte, 7,0 % weniger Aktivität des Sympathikus, 1,4 % niedrigeren systolischen Blutdruck und 5,8 % niedrigeren Puls.</p>
<div class="merke"><strong>Einordnung:</strong> Die frühere Behauptung, der Cortisolspiegel sinke „nach exakt 40 bis 45 Minuten drastisch“, haben wir gestrichen – dafür gibt es keinen Beleg. Auch „Goldstandard für Stressresistenz“ war übertrieben: HRV ist ein nützlicher Marker, aber stark abhängig von Alter, Schlaf, Messzeitpunkt und Gerät.</div>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Auf dem flachen Stück zwischen Oberer und Unterer Firstalm lässt sich die langsame Atmung gut ausprobieren. Spätestens am Gegenanstieg übernimmt dein Körper wieder das Kommando.</div>
""",
[("Lehrer & Gevirtz 2014 – Heart rate variability biofeedback: how and why does it work? (Frontiers in Psychology)", "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00756/full"),
 ("Frontiers in Neuroscience 2020 – A Practical Guide to Resonance Frequency Assessment ", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7578229"),
 ("Frontiers in Public Health 2017 – Resonance Frequency Breathing, HRV, Blood Pressure and Mood (PubMed)", "https://pubmed.ncbi.nlm.nih.gov/28890890/"),
 ("Nihon Eiseigaku Zasshi 2011 – Preventive medical effects of nature therapy (PubMed)", "https://pubmed.ncbi.nlm.nih.gov/21996763/")],
"Garmin Fēnix 7 Pro Solar", "GPS-Uhr mit HRV-Messung über Nacht.", AMZ.format("Garmin+Fenix+7+Pro+Solar"))

# ---------------------------------------------------------------- 3
seite("topografie-klimawandel", 3, "Bröckelnde Riesen: Klimawandel in den Alpen in Zahlen",
"Wie stark sich die Alpen erwärmen, was mit Bayerns Gletschern passiert und warum Steinschlag zunimmt.",
"""
<h2>Doppelt so schnell wie global</h2>
<p>Laut Deutschem Alpenverein steigen die Temperaturen in den Alpen mehr als doppelt so schnell wie im globalen Mittel. Das Klimamittel 1991–2020 ist rund 2 °C wärmer als im späten 19. Jahrhundert. Seit den 1980er-Jahren war die Erwärmung mit etwa 0,5 °C pro Jahrzehnt außergewöhnlich stark.</p>
<p>Für Österreich nennt der DAV einen Anstieg von fast 2 °C seit 1880, während es im globalen Mittel im gleichen Zeitraum 0,9 °C waren. Grundlage solcher Reihen ist der HISTALP-Datensatz mit homogenisierten Messreihen für den Alpenraum.</p>

<h2>Gletscher: Bayern wird eisfrei</h2>
<p>Alpenweit haben die Gletscher seit 1850 mehr als die Hälfte ihrer Fläche und ein Drittel ihres Volumens verloren. 1970 bedeckten sie noch rund 2.900 km², heute knapp 2.000 km².</p>
<p>In Bayern hat der Südliche Schneeferner an der Zugspitze im September 2022 seinen Gletscher-Status verloren, so die Bayerische Akademie der Wissenschaften: Das Eis ist zu dünn, um sich noch zu bewegen. Übrig sind Nördlicher Schneeferner und Höllentalferner an der Zugspitze sowie Blaueis und Watzmanngletscher in den Berchtesgadener Alpen. Bayern dürfte im Laufe der 2030er-Jahre gletscherfrei sein.</p>

<h2>Schnee und Steinschlag</h2>
<p>Seit 1950 ist die Schneefallgrenze in den Alpen um mehr als 100 m gestiegen. Tauender Permafrost und schwindendes Eis führen laut DAV zu Steinschlag, Bergstürzen und Überschwemmungen. Manche Anstiege müssen deshalb neu angelegt oder während der Saison umverlegt werden – etwa der Normalweg auf den Großglockner von der Hochalpenstraße aus.</p>
<div class="merke"><strong>Einordnung:</strong> Frühere Angaben auf dieser Seite („Nullgradgrenze in 40 Jahren über 300 m höher“, „DAV-Stützpunkte brauchen metertiefe Mikropfähle“) konnten wir nicht belegen. Sie sind gestrichen und durch belegte Zahlen ersetzt.</div>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Am Spitzing gibt es keinen Gletscher und kaum Permafrost – aber auch hier liegt der Schnee später und kürzer. Wer im Spätherbst auf die Rotwand steigt, sollte trotzdem mit Steinschlag in den Rinnen rechnen.</div>
""",
[("DAV – Die Klimakrise im Alpenraum (doppelt so schnell, +2 °C, 0,5 °C/Jahrzehnt)", "https://www.alpenverein.de/artikel/die-klimakrise-im-alpenraum_f31acb6e-6397-4c12-a81f-41fc2c613861"),
 ("DAV – Gletscher schmelzen, Permafrost taut (Österreich, Gletscherflächen)", "https://www.alpenverein.de/artikel/gletscher-schmelzen-permafrost-taut_3488e2d8-d095-4b44-a8d9-2ed88a5ba36d"),
 ("DAV – Klimawandel verändert die Alpen (Schneefallgrenze)", "https://www.alpenverein.de/artikel/klimawandel-verandert-die-alpen_22fb74e3-1dd9-451b-9490-0323eaed7606"),
 ("DAV – Folgen: Steinschlag, Großglockner-Normalweg", "https://www.alpenverein.de/natur/gletscher-schmelzen-permafrost-taut_aid_37228.html"),
 ("GeoSphere Austria – HISTALP", "https://www.zamg.ac.at/histalp"),
 ("Bayerische Akademie der Wissenschaften – Pressemitteilung Südlicher Schneeferner (2022)", "https://badw.de/fileadmin/user_upload/Files/BADW/pressemitteilungen/2022/09_Schneeferner.pdf"),
 ("ÖKO-TEST/dpa – Bayern in den 2030ern gletscherfrei", "https://www.oekotest.de/freizeit-technik/Rekordschmelze-Deutschland-wohl-in-2030ern-ohne-Gletscher-_16238_1.html")],
"Petzl Sirocco – Steinschlaghelm", "Leichter Helm für Touren mit Steinschlaggefahr.", AMZ.format("Petzl+Sirocco+Helm"))

# ---------------------------------------------------------------- 4
seite("solo-transalp", 4, "Allein über die Alpen: Kopf, Kohlenhydrate und Erschöpfung",
"Was die Sportwissenschaft über Ermüdung auf langen Touren weiß – und wie viel Energie ein langer Bergtag braucht.",
"""
<h2>Ist Erschöpfung nur Kopfsache?</h2>
<p>Der südafrikanische Sportwissenschaftler Tim Noakes hat das „Central Governor“-Modell geprägt: Das Gehirn bremse die Leistung vorausschauend, um den Körper vor Schaden zu schützen. Das Modell ist populär, aber umstritten. Ein Übersichtsartikel im <em>British Journal of Sports Medicine</em> (Weir et al. 2006) hält dagegen, dass viele periphere Faktoren in den Muskeln die Kraft begrenzen. Am besten passe ein Modell, in dem zentrale und periphere Ermüdung je nach Belastung unterschiedlich stark beitragen. Der kanadische Physiologe Roy Shephard fragte 2009 sogar, ob es Zeit sei, den „Central Governor“ in Rente zu schicken.</p>
<div class="merke"><strong>Einordnung:</strong> Die frühere Aussage „Die Central Governor Theory beweist …“ war falsch. Das Modell ist eine Hypothese und kein Beweis. Auch die „200-km-Reportage“ war kein belegter Erfahrungsbericht – wir haben die Seite deshalb zu einem Sachartikel umgebaut.</div>

<h2>Energie: Wie viel Kohlenhydrate pro Stunde?</h2>
<p>Laut Asker Jeukendrup kann der Körper aus einer einzelnen Zuckerquelle (z. B. Glukose) bis etwa 60 g Kohlenhydrate pro Stunde verwerten; das ist die Empfehlung für Belastungen von 2–3 Stunden. Für Ultra-Ausdauer liegt die Empfehlung bei etwa 90 g pro Stunde. Bei 60–90 g pro Stunde sind Mischungen aus Glukose und Fruktose besser, weil sie schneller aufgenommen werden.</p>
<p>Für Belastungen über 60 Minuten nennt das Gatorade Sports Science Institute einen Bereich von 30 bis 90 g pro Stunde.</p>
<div class="rechnung"><strong>Rechenbeispiel Wandertag:</strong> 8 Stunden unterwegs, davon die meiste Zeit in moderatem Tempo. Bei 30 g pro Stunde (unteres Ende) wären das 240 g Kohlenhydrate, bei 60 g pro Stunde 480 g. Ein mittelgroßer Müsliriegel hat etwa 20–30 g. Ob man das obere Ende braucht, hängt vom Tempo ab – die 90-g-Empfehlung gilt für Ultra-Wettkämpfe, nicht für gemütliche Hüttentage.</div>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Die gute Nachricht für alle, die von der Oberen Firstalm aus starten: Der Kaiserschmarrn an der Hütte liefert die Kohlenhydrate gleich mit. Die wissenschaftliche Datenlage dazu, wie viel man davon „braucht“, ist allerdings dünn.</div>
""",
[("Weir et al. 2006 – Is fatigue all in your head? A critical review of the central governor model (BJSM)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2564297"),
 ("Shephard 2009 – Is it Time to Retire the 'Central Governor'?", "https://www.unm.edu/%7Errobergs/478Shephard.pdf"),
 ("Jeukendrup 2014 – A Step Towards Personalized Sports Nutrition (Sports Medicine)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4008807"),
 ("GSSI – Dietary Carbohydrate and the Endurance Athlete (Wallis & Podlogar 2022)", "https://www.gssiweb.org/en/sports-science-exchange/article/dietary-carbohydrate-and-the-endurance-athlete-contemporary-perspectives")],
"Salomon Adv Skin 12", "Leichter Laufrucksack für lange Tage mit Verpflegung griffbereit.", AMZ.format("Salomon+Adv+Skin+12+Rucksack"))

# ---------------------------------------------------------------- 5
seite("shinrin-yoku", 5, "Waldbaden: Was Studien über den Wald und unsere Abwehr sagen",
"Shinrin-Yoku zwischen Hype und Messdaten – Killerzellen, Cortisol und die Grenzen der Studien.",
"""
<h2>Was ist Shinrin-Yoku?</h2>
<p>„Shinrin-Yoku“ heißt auf Japanisch Waldbaden: ein kurzer, gemütlicher Aufenthalt im Wald, ähnlich einer natürlichen Aromatherapie. Die japanische Forstbehörde hat es 1982 erstmals als Teil eines gesunden Lebensstils vorgeschlagen.</p>

<h2>Die Killerzellen-Studien</h2>
<p>Die bekannteste Forschung stammt von Qing Li. 2007 untersuchte er zwölf gesunde Männer zwischen 37 und 55 Jahren aus drei Tokioter Firmen während einer dreitägigen Waldreise mit mehreren zweistündigen Spaziergängen. Danach waren die Aktivität und die Zahl der natürlichen Killerzellen (NK-Zellen) erhöht. Li erklärte das teilweise mit mehr NK-Zellen und mehr Anti-Krebs-Proteinen in den Zellen. Als möglichen Wirkstoff nennt er Phytonzide, also ätherische Öle der Bäume.</p>
<div class="merke"><strong>Einordnung:</strong> Die frühere Angabe „ein Tag im Nadelwald erhöht die NK-Zellen um bis zu 40 Prozent“ stimmt so nicht. Es war eine <em>dreitägige</em> Reise mit nur zwölf Teilnehmern. Aus so kleinen Studien lassen sich keine festen Prozentwerte für alle ableiten.</div>

<h2>Cortisol: Was die Meta-Analyse sagt</h2>
<p>Eine systematische Übersicht von Antonelli und Kollegen (2019) hat 971 Arbeiten gesichtet, 22 davon ausgewertet und 8 in einer Meta-Analyse zusammengefasst. In fast allen Studien waren die Cortisolwerte nach dem Waldaufenthalt niedriger als in Vergleichsgruppen. Die Autoren raten wegen der begrenzten Datenlage aber zu weiterer Forschung.</p>
<p>Eine Meta-Analyse von 2022 mit Stadtbewohnern fand im Mittel niedrigeren Blutdruck und weniger Cortisol nach Waldtherapie, aber mit großen Unterschieden zwischen den Studien – positive Effekte sind also wahrscheinlich, aber nicht garantiert.</p>

<div class="firstalm"><strong>Firstalm-Praxis:</strong> Der Bergwald unterhalb der Oberen Firstalm ist ein gutes Revier für langsames Gehen ohne Gipfelziel: Handy in den Rucksack, Tempo raus, riechen und hören. Die Killerzellen zählt dabei niemand – die Stimmung merkst du selbst.</div>
""",
[("Li 2010 – Effect of forest bathing trips on human immune function (Environ Health Prev Med)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2793341"),
 ("Li et al. 2007 – Forest bathing enhances human natural killer activity (PubMed)", "https://pubmed.ncbi.nlm.nih.gov/17903349/"),
 ("Antonelli et al. 2019 – Forest bathing and cortisol: systematic review and meta-analysis (PubMed)", "https://pubmed.ncbi.nlm.nih.gov/31001682/"),
 ("IJERPH 2022 – Forest Therapy, Blood Pressure and Salivary Cortisol: A Meta-Analysis (PubMed)", "https://pubmed.ncbi.nlm.nih.gov/36612777/")],
"Klean Kanteen TKWide Thermosflasche", "Isolierflasche für Tee auf langsamen Waldrunden.", AMZ.format("Klean+Kanteen+TKWide+Thermoflasche"))

print("fertig")
