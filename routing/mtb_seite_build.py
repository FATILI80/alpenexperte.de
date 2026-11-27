#!/usr/bin/env python3
"""Baut content/mtb/index.html neu: MTB-Touren ab Oberer Firstalm (BRouter mtb), Karten, Menü, Ausrüstung."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, "/tmp")
SRC = (ROOT / "content/mtb/index.html").read_text(encoding="utf-8")


def divend(s, start):
    depth = 0
    for m in re.finditer(r"<(/?)div\b[^>]*>", s[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return start + m.end()
    return -1


# --- Bausteine aus der bestehenden Seite übernehmen
head = SRC[:SRC.find("<body")]
head = re.sub(r"<title>.*?</title>", "<title>MTB-Touren ab der Oberen Firstalm | Mangfallgebirge | Alpen-Experte</title>", head, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*"', '<meta name="description" content="31 MTB-Touren ab der Oberen Firstalm (1.375 m) – jede mit BRouter berechnet, mit Karte, Länge und Höhenmetern. Ziele aus belegten Tourenbeschreibungen."', head)
body_open = re.search(r"<body[^>]*>", SRC).group(0)
kl = (ROOT / "content/klettern/index.html").read_text(encoding="utf-8")
a = kl.find('<header class="site-header"'); e = kl.find("</header>", a) + 9
HEADER = kl[a:e].replace(" nav-link--active", "").replace(' aria-current="page"', "")
i = SRC.find("Faktor-10 Wissenschaftliches Kompendium"); a = SRC.rfind("<section", 0, i); e = SRC.find("</section>", i) + 10
KOMPENDIUM = SRC[a:e]
i = SRC.find("Was bedeutet die Singletrail-Skala"); a = SRC.rfind('<div class="silo-card"', 0, i)
STS = SRC[a:divend(SRC, a)]
FAQ = ""
i = SRC.find("Häufige Experten-Fragen")
if i > 0:
    a = SRC.rfind("<section", 0, i); e = SRC.find("</section>", i) + 10
    FAQ = SRC[a:e]

T = {t["kennung"]: t for t in json.loads((ROOT / "routing/mtb_touren.json").read_text(encoding="utf-8"))}
E = {e["kennung"]: e for e in json.loads((ROOT / "routing/ergebnis_mtb.json").read_text(encoding="utf-8"))}
# Ergebnisse verwerfen, die nicht zur aktuellen Wegpunktliste passen (z. B. alter Lauf mit anderem Ziel)
E = {k: e for k, e in E.items() if k in T and len(e.get("treffer", [])) == len(T[k]["wegpunkte"])}

de = lambda x: f"{x:.1f}".replace(".", ",")
tsd = lambda n: f"{n:,}".replace(",", ".")


def karte(k):
    t = T[k]; e = E.get(k, {})
    titel = t["name"]
    verlauf = " → ".join(["Obere Firstalm"] + [w.split("@")[0] for w in t["wegpunkte"]] + ["Obere Firstalm"])
    if "laenge_km_brouter" in e:
        werte = f"{de(e['laenge_km_brouter'])} km · ↑↓ {tsd(e['hm_aufstieg'])} Hm (Runde)"
    else:
        werte = "Werte folgen (BRouter)"
    quelle = t.get("quelle", "")
    return (f'<div class="mtb-karte" style="background:#16242b;border:1px solid #f97316;border-radius:10px;padding:13px;">'
            f'<div style="font-size:0.8rem;color:#fdba74;font-weight:700;">{k} · Start: Obere Firstalm (1.375 m) · {werte}</div>'
            f'<h4 style="margin:4px 0 6px 0;color:#ffffff;font-size:1.02rem;">{titel}</h4>'
            f'<p style="margin:0 0 8px 0;color:#e2e8f0;font-size:0.88rem;line-height:1.45;"><strong style="color:#fdba74;">Verlauf:</strong> {verlauf}</p>'
            f'<details style="background:#0f1a20;padding:7px 9px;border-radius:6px;cursor:pointer;"><summary style="color:#fdba74;font-weight:600;font-size:0.84rem;">🚵 Touren-Details &amp; Karte anzeigen</summary>'
            f'<p style="margin:6px 0 0 0;color:#cbd5e1;font-size:0.84rem;"><strong>Länge &amp; Höhenmeter:</strong> BRouter, Profil mtb, Runde ab und bis Obere Firstalm. '
            f'<strong>Ziel belegt durch:</strong> {quelle}.</p>'
            f'<div class="mini-karte" data-route="{k}" style="height:200px;margin-top:8px;border-radius:8px;"></div></details></div>')


def kat(k):
    e = E.get(k, {}); hm = e.get("hm_aufstieg")
    if hm is None:
        return "alm"
    return "kurz" if hm < 700 else ("alm" if hm <= 1600 else "epic")


gruppen = {"kurz": [], "alm": [], "epic": []}
for k in sorted(T, key=lambda x: int(x[1:])):
    gruppen[kat(k)].append(k)


def bild(f, alt):
    return f'<img src="/images/{f}" alt="{alt}" loading="lazy" style="width:100%;max-height:260px;object-fit:cover;border-radius:12px;margin:8px 0 14px;display:block;">'


GRID = 'style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;"'
sek = ""
for gid, titel, img, alt, text in [
    ("kurz", "🟢 Kurz &amp; knackig (unter 700 Hm)", "huetten-hero.jpg", "Almweg in den Bergen", "Feierabendrunden rund um Spitzing, Valepp und Schliersee."),
    ("alm", "🟡 Almtouren (700–1.600 Hm)", "MTB%20Touren.jpg", "Mountainbikes vor Bergkulisse", "Halbtages- und Tagestouren zu Almen und Hütten zwischen Tegernsee, Kreuth und Tirol."),
    ("epic", "🔴 Epic &amp; Grenztouren (über 1.600 Hm)", "forsthaus-valepp.jpg", "Forsthaus Valepp", "Lange Tage über Valepp, Kreuth und die Tiroler Grenze."),
]:
    karten = "".join(karte(k) for k in gruppen[gid])
    sek += (f'<section id="mtb-{gid}" style="margin:28px 0;">{bild(img, alt)}'
            f'<h2 style="color:#14532d;margin:0 0 6px;">{titel} <span style="font-size:.9rem;color:#64748b;">({len(gruppen[gid])} Touren)</span></h2>'
            f'<p style="color:#334155;margin:0 0 12px;">{text}</p><div {GRID}>{karten}</div></section>')

n = len(T)
nav = ('<div id="mobile-mtb-nav" class="kat-nav" style="background:#0b1318;border:1px solid #f97316;border-radius:10px;padding:10px;margin:14px 0;display:flex;flex-wrap:wrap;gap:8px;">'
       + "".join(f'<a href="#mtb-{g}" style="background:{c};color:#fff !important;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:0.84rem;font-weight:700;">{l} ({len(gruppen[g])})</a>'
                 for g, l, c in [("kurz", "🟢 Kurz &amp; knackig", "#2e7d32"), ("alm", "🟡 Almtouren", "#b45309"), ("epic", "🔴 Epic &amp; Grenze", "#7f1d1d")])
       + '<a href="#sts-info" style="background:#334155;color:#fff !important;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:0.84rem;font-weight:700;">ℹ️ Schwierigkeit &amp; Regeln</a>'
       + '<a href="#ausruestung" style="background:#334155;color:#fff !important;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:0.84rem;font-weight:700;">🎒 Ausrüstung</a></div>')

A = "https://www.amazon.de/s?k={}&linkCode=ll2&tag=bb8ozi-21"
items = [("🪖", "MTB-Helm mit MIPS", "Schutz bei Stürzen auf Schotter und Trail", A.format("MTB+Helm+MIPS")),
         ("🛡️", "Knie-Protektoren", "Für Abfahrten mit losem Untergrund", A.format("MTB+Knieprotektoren")),
         ("👟", "Flat-Pedal-Schuhe", "Griffige Sohle für Flatpedals", A.format("MTB+Flat+Pedal+Schuhe")),
         ("🎒", "Bike-Rucksack mit Trinkblase", "Wasser und Werkzeug für lange Almtage", A.format("MTB+Rucksack+Trinkblase")),
         ("🔧", "Multitool &amp; Pannenset", "Kettennieter, Reifenheber, Pumpe", A.format("Fahrrad+Multitool+Kettennieter")),
         ("🩹", "Erste-Hilfe-Set", "Kompakt für den Rucksack", A.format("Erste+Hilfe+Set+Outdoor"))]
cards = "".join(f'<a href="{u}" target="_blank" rel="sponsored noopener nofollow" style="display:block;background:#ffffff;border:1px solid #d5dde5;border-radius:10px;padding:14px;text-decoration:none;"><span style="font-size:1.4rem;">{i}</span><strong style="display:block;color:#14532d;margin:4px 0 2px;">{t}</strong><span style="display:block;color:#334155;font-size:.86rem;line-height:1.4;">{d}</span><span style="display:inline-block;margin-top:8px;color:#b45309;font-weight:700;font-size:.85rem;">Bei Amazon ansehen →</span></a>' for i, t, d, u in items)
URW = "https://www.awin1.com/cread.php?awinmid=68034&amp;awinaffid=3134996&amp;clickref=Start&amp;ued=https%3A%2F%2Falpenexperte.de"
AUSR = f'''<section id="ausruestung" style="margin:36px 0 10px;padding:24px;border:2px solid #b45309;border-radius:14px;background:#fffbeb;">
<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;"><h2 style="margin:0;color:#14532d;">🎒 Ausrüstung für deine MTB-Touren</h2><span style="background:#6c757d;color:#fff;padding:3px 8px;border-radius:4px;font-size:.75rem;font-weight:700;">Anzeige / Affiliate</span></div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:14px;">{cards}</div>
<h3 style="color:#14532d;margin:22px 0 10px;">🚴 Partner für Rad &amp; E-Bike</h3>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;">
<a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" style="display:block;background:#fff;border:1px solid #d5dde5;border-left:4px solid #2e7d32;border-radius:10px;padding:14px;text-decoration:none;"><strong style="display:block;color:#14532d;">Lucky Bike</strong><span style="color:#334155;font-size:.86rem;">Mountainbikes, E-MTBs und Zubehör online und im Fachmarkt.</span><span style="display:block;margin-top:8px;color:#b45309;font-weight:700;font-size:.85rem;">Zu Lucky Bike →</span></a>
<a href="{URW}" target="_blank" rel="sponsored noopener nofollow" style="display:block;background:#fff;border:1px solid #d5dde5;border-left:4px solid #c2722d;border-radius:10px;padding:14px;text-decoration:none;"><strong style="display:block;color:#14532d;">Urwahn Bikes</strong><span style="color:#334155;font-size:.86rem;">E-Bikes aus Magdeburg mit 3D-gedrucktem Stahlrahmen.</span><span style="display:block;margin-top:8px;color:#b45309;font-weight:700;font-size:.85rem;">Zu Urwahn →</span></a></div>
<p style="color:#64748b;font-size:.8rem;margin:14px 0 0;">Transparenz: Bei Käufen über diese Links erhalten wir eine Provision. Der Preis für dich ändert sich nicht.</p></section>'''

REGELN = '''<div id="sts-info"></div>
<div style="background:#f0fdf4;border-left:4px solid #2d8a56;padding:14px 16px;border-radius:6px;margin:18px 0;color:#1f2933;">
<strong>Wo darf ich in Bayern Mountainbike fahren?</strong> Nach Art. 28 Abs. 1 Bayerisches Naturschutzgesetz darf jeder auf Privatwegen in der freien Natur mit Fahrrädern fahren, soweit sich die Wege dafür eignen; im Wald ist Radfahren nur auf Straßen und geeigneten Wegen zulässig (Art. 30 Abs. 2 BayNatSchG). Wanderer haben Vorrang. Auf Tiroler Seite gelten die freigegebenen Mountainbike-Routen. Quelle: Bayerischer Landtag, Drucksache 18/19388.<br>
<strong>Hinweis zu den Werten:</strong> Länge und Höhenmeter sind BRouter-Berechnungen über OpenStreetMap-Wege (Profil mtb). Die Ziele stammen aus den angegebenen Tourenbeschreibungen; die genaue Linie kann von der beschriebenen Route abweichen. Eine Schwierigkeitsbewertung (STS) geben wir erst an, wenn sie belegt ist.</div>'''

intro = f'''<section style="margin:20px 0;">{bild("MTB%20Touren.jpg", "Zwei Mountainbikes vor einer Bergkulisse")}
<h1 style="color:#14532d;margin:6px 0;">🚵 MTB-Touren ab der Oberen Firstalm</h1>
<p style="color:#334155;font-size:1.05rem;">{n} Touren, alle mit Start und Ziel an der Oberen Firstalm (1.375 m) über dem Spitzingsattel. Jede Tour ist mit BRouter berechnet und hat eine Karte. Die Ziele stammen aus veröffentlichten MTB-Tourenbeschreibungen, die bei jeder Tour genannt sind.</p></section>'''

LOADER = '''<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style id="mini-karte-fix">.mini-karte{position:relative;isolation:isolate;overflow:hidden;}.mini-karte .leaflet-container{width:100%!important;height:100%!important;}</style>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".mini-karte").forEach(function (el) {
    var det = el.closest("details"); var geladen = false;
    function init() {
      if (geladen || typeof L === "undefined") return; geladen = true;
      var id = el.getAttribute("data-route");
      var m = L.map(el, { attributionControl: false });
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 18 }).addTo(m);
      fetch("/content/mtb/geojson/" + id + "_mtb.geojson").then(function (r) { return r.json(); }).then(function (g) {
        var l = L.geoJSON(g, { style: { color: "#f97316", weight: 4 } }).addTo(m);
        m.fitBounds(l.getBounds(), { padding: [10, 10] }); setTimeout(function () { m.invalidateSize(); }, 50);
      }).catch(function () { el.innerHTML = '<div style="padding:8px;color:#e2e8f0;font-size:0.8rem;">Keine Karte: Route noch nicht berechnet.</div>'; });
    }
    if (det) det.addEventListener("toggle", function () { if (det.open) init(); });
  });
});
</script>'''

FOOT = '<footer class="site-footer" role="contentinfo"><div class="container" style="text-align:center;padding:var(--space-lg);"><p>&copy; 2025–2026 Alpen-Experte. Alle Rechte vorbehalten.</p></div></footer>'

html = (head.replace("</head>", "") + LOADER.split("<script")[0] + "</head>\n" + body_open + "\n" + HEADER
        + '\n<main id="main" class="container" style="max-width:1150px;margin:0 auto;padding:0 16px;">'
        + intro + nav + sek + REGELN + STS.replace('id="sts-scale" hidden', '') + AUSR + "</main>\n"
        + KOMPENDIUM + "\n" + FAQ + "\n" + FOOT
        + '\n<script src="/js/main.js?v=20260612b" defer></script>\n' + "<script" + LOADER.split("<script", 1)[1] + "\n</body></html>\n")
(ROOT / "content/mtb/index.html").write_text(html, encoding="utf-8")
print("Touren", n, {g: len(v) for g, v in gruppen.items()}, "ohne Werte:", [k for k in T if "laenge_km_brouter" not in E.get(k, {})])
