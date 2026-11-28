#!/usr/bin/env python3
"""Baut wetter-webcams.html: Live-Wetter (Open-Meteo, CC BY 4.0) für Obere Firstalm, Rotwand und Schliersee,
verifizierte Webcams, Lawinenlage und offizielle Wetterdienste. Kopf/Fuß von restaurants.html."""
import re, html
SRC, F = 'restaurants.html', 'wetter-webcams.html'
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t: f'<h2 id="{i}" style="color:#14532d;margin:34px 0 8px;scroll-margin-top:140px;">{t}</h2>'
P = lambda t: f'<p style="color:#1f2933;line-height:1.6;">{t}</p>'
GRID = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;">'
def box(titel, kopf, text, url, link='Webcam öffnen →', top=False):
    return (f'<div style="background:#fff;border:{"2px solid #c2410c" if top else "1px solid #2e7d32"};border-radius:12px;padding:12px 14px;">'
            f'<div style="font-size:.78rem;color:#1d4ed8;font-weight:700;">{E(kopf)}</div><h3 style="margin:3px 0 6px;color:#14532d;font-size:1rem;">{E(titel)}</h3>'
            f'<p style="margin:0 0 8px;font-size:.88rem;color:#0f2942;line-height:1.45;">{text}</p>'
            f'<a href="{url}" target="_blank" rel="noopener" style="font-weight:700;color:#c2410c;font-size:.88rem;">{link}</a></div>')

PUNKTE = [('firstalm', 'Obere Firstalm', 47.6701, 11.8540, 1375), ('rotwand', 'Rotwand (Gipfelbereich)', 47.6497, 11.9283, 1884), ('schliersee', 'Schliersee (Ort)', 47.7360, 11.8600, 784)]
CAMS = [
 box('Obere Firstalm – Blick zur Brecherspitz', '⭐ 1.375 m · unsere Alm', 'Live-Bild mit Archiv: Rodelbahn, Brecherspitz und das Wetter direkt an der Alm.', 'https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/webcams/wcn59687', top=True),
 box('Obere Firstalm – Terrasse', '⭐ 1.375 m · unsere Alm', 'Blick von der Terrasse über das Skigebiet Richtung Spitzingsee.', 'https://www.skiresort.info/ski-resort/spitzingsee-tegernsee/webcams/wcn59688', top=True),
 box('Untere Firstalm – Nordhanglift', '1.317 m · Skigebiet', 'Blick von der Unteren Firstalm auf den Nordhang-Schlepplift und den Snowpark-Bereich.', 'https://www.snow-online.com/ski-resort/spitzingsee/webcam/spitzingsee--ski-lift-nordhang.htm'),
 box("Jagahütt'n am Stümpfling", '1.486 m · Bergstation Stümpflingbahn', 'An der Bergstation der Stümpflingbahn.', 'https://www.snow-online.com/ski-resort/spitzingsee/webcam/mountain-hut-jagahuettn-.htm'),
 box('Talstation Stümpflingbahn', '1.125 m · Spitzingsee', 'Blick von der Talstation – zeigt, wie viel Schnee unten liegt.', 'https://www.snow-online.com/webcam/base-station-stuempflingbahn.htm'),
 box('Alle Webcams im Skigebiet', 'Roßkopf 1.540 m · Sutten · Ostufer', 'Übersicht mit Roßkopf-Bergstation, Stümpfling- und Suttenabfahrt und dem Ostufer des Spitzingsees.', 'https://www.snow-online.com/webcams/ski-resort/spitzingsee.html', 'Übersicht öffnen →'),
 box('Bergstation Taubensteinbahn', '1.651 m', 'Blick von der Bergstation der Taubensteinbahn.', 'https://tourispo.de/webcam/bergstation-der-taubensteinbahn.htm'),
 box('Obere Maxlraineralm', '1.520 m · am Taubenstein', 'Hochfläche unter dem Taubenstein, Fernblick bis in die Zillertaler Alpen.', 'https://en.addicted-sports.com/webcam/spitzingsee/oberemaxlraineralm'),
 box('Schliersee – Café Milchhäusl', 'Seeufer Schliersee', 'Blick vom Südufer über den Schliersee.', 'https://www.windy.com/webcams/1599573286'),
]
DIENSTE = [
 box('Lawinenlagebericht Bayern', 'Lawinenwarndienst Bayern (LfU)', 'Täglicher Lagebericht im Winter, Region „Bayerische Voralpen Mitte“. Dazu Messdaten von rund 20 automatischen Stationen im 10-Minuten-Takt – eine davon am Spitzingsee (1.100 m). Telefonansage: +49 89 9214-1210.', 'https://www.lawinenwarndienst.bayern.de/', 'Lagebericht öffnen →', top=True),
 box('DAV-Bergwetter', 'Deutscher Alpenverein', 'Bergwetter für die Region „Bayerische Alpen Ost, Österreich Nord“ – mit Gipfelwind, Nullgradgrenze und Gewitterrisiko.', 'https://www.alpenverein.de/bergwetter', 'Bergwetter öffnen →'),
 box('Wetterwarnungen', 'Deutscher Wetterdienst', 'Amtliche Unwetter- und Gewitterwarnungen – auf dwd.de den Landkreis Miesbach wählen.', 'https://www.dwd.de/', 'Warnungen öffnen →'),
 box('Messstationen & Schneehöhen', 'bergfex', 'Aktuelle Temperaturen der Stationen Spitzingsee und Brecherspitze direkt neben der Firstalm-Webcam.', 'https://www.bergfex.com/sommer/schliersee-neuhaus-spitzingsee/webcams/c17608/', 'Stationen öffnen →'),
]

b = ['<main id="main"><article class="container" style="max-width:1100px;margin:0 auto;padding:24px 16px 48px;">',
     '<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">Wetter &amp; Webcams</span></nav>',
     '<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">⛅ Wetter, Webcams &amp; Lawinenlage am Spitzingsee</h1>'
     '<p style="font-size:1.08rem;color:#1f2933;margin:0;">Live-Wetter für die Obere Firstalm, die Rotwand und den Schliersee, die Webcams rund um Spitzingsee und Firstalm und die offiziellen Dienste für Bergwetter und Lawinen – alles auf einer Seite.</p></header>',
     '<nav class="kat-nav" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;z-index:50;">'
     + ''.join(f'<a href="#{i}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for i, t in
               [('live', '🌡️ Live-Wetter'), ('webcams', '📹 Webcams'), ('dienste', '⚠️ Lawine & Bergwetter'), ('tipps', '🧭 Wetter lesen'), ('foehn', '🌬️ Föhn')]) + '</nav>',
     H2('live', '🌡️ Live-Wetter') + '<div id="wx" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;">'
     + ''.join(f'<div class="wxk" data-lat="{la}" data-lon="{lo}" data-ele="{el}" style="background:#fff;border:{"2px solid #c2410c" if i == "firstalm" else "1px solid #2e7d32"};border-radius:12px;padding:12px 14px;">'
               f'<div style="font-size:.78rem;color:#1d4ed8;font-weight:700;">{el:,} m'.replace(',', '.') + f'</div><h3 style="margin:3px 0 6px;color:#14532d;font-size:1rem;">{E(n)}</h3><div class="wxb" style="font-size:.9rem;color:#1f2933;">lädt …</div></div>'
               for i, n, la, lo, el in PUNKTE)
     + '</div><p style="font-size:.78rem;color:#4b5563;">Wetterdaten: <a href="https://open-meteo.com/" target="_blank" rel="noopener">Open-Meteo.com</a> (CC BY 4.0), Modellwerte für die angegebene Höhe – keine Messung vor Ort. Für Touren immer zusätzlich Bergwetter und Lawinenlagebericht prüfen.</p>',
     H2('webcams', '📹 Webcams') + P('Die Bilder liegen bei den Betreibern bzw. Portalen – ein Klick öffnet die aktuelle Aufnahme samt Archiv.') + GRID + ''.join(CAMS) + '</div>',
     H2('dienste', '⚠️ Lawinenlage, Bergwetter &amp; Warnungen') + GRID + ''.join(DIENSTE) + '</div>'
     + '<div style="background:#fef2f2;border-left:5px solid #b91c1c;padding:12px 16px;border-radius:10px;margin:16px 0;color:#1f2933;"><strong>Notruf 112</strong> – Bergwacht, Rettungsdienst und Feuerwehr. Wichtig: Standort, was passiert ist, wie viele Verletzte.</div>',
     '<figure style="margin:18px 0 6px;max-width:520px;"><img src="/images/obere-firstalm-schnee-nov-2026.jpg" alt="Neuschnee vor der Oberen Firstalm, 26. November 2026" loading="lazy" style="width:100%;height:auto;border-radius:12px;display:block;"><figcaption style="font-size:.85rem;color:#4b5563;margin-top:6px;">Wintereinbruch an der Oberen Firstalm (1.375 m), 26. November 2026 – eigenes Foto. Auf der Höhe kann es schneien, während es im Tal noch regnet.</figcaption></figure>' +
     H2('tipps', '🧭 Wetter in den Bergen lesen') + '<ul style="line-height:1.7;color:#1f2933;">'
     '<li><strong>Höhe zählt:</strong> Vergleiche die drei Punkte oben – zwischen Schliersee (784 m) und Rotwand (1.884 m) liegen gut 1.100 Höhenmeter.</li>'
     '<li><strong>Webcam vor Wetterkarte:</strong> Das Bild von der Firstalm zeigt Nebel, Schnee und Rodelbahn-Zustand, bevor ein Modell es tut.</li>'
     '<li><strong>Lawinenlagebericht</strong> gilt im Winter für jede Tour abseits gesicherter Pisten – mehr dazu in den <a href="/content/winter/lawinenkunde-grundlagen.html">Lawinen-Grundlagen</a>.</li>'
     '<li>Gewitter und Wetterumschwung: Verhaltensregeln im <a href="/content/sicherheit/#wetter">Sicherheits-Ratgeber</a>.</li></ul>'
     + H2('foehn', '🌬️ Föhn')
     + '<ul style="line-height:1.7;color:#1f2933;">'
     '<li>Föhn ist ein warmer, trockener, oft böiger Fallwind auf der Leeseite hoher Gebirge – bei uns auf der Alpennordseite als Südföhn.<sup><a href="https://www.spektrum.de/lexikon/geowissenschaften/foehn/5103" target="_blank" rel="noopener">[Spektrum]</a></sup></li>'
     '<li>Über dem Alpenhauptkamm ist dann oft die „Föhnmauer“ zu sehen; sinkt die Luft auf der Nordseite ab, lösen sich die Wolken rasch auf.<sup><a href="https://www.wetterdienst.de/Deutschlandwetter/Thema_des_Tages/774/foehnlage" target="_blank" rel="noopener">[wetterdienst.de]</a></sup></li>'
     '<li>In Föhntälern kann er Sturmstärke erreichen, auf den Gipfeln Orkanstärke – am Grat also mit kräftigem Wind rechnen, auch wenn es im Tal mild und sonnig ist.<sup><a href="https://14-tage-wettervorhersage.de/news/thema/191120/" target="_blank" rel="noopener">[DWD-Thema]</a></sup></li>'
     '<li>Im Winter kann Föhn Gleitschneerutsche und Lawinen auslösen.<sup><a href="https://www.wetterdienst.de/Service/Lexikon/Foehn" target="_blank" rel="noopener">[wetterdienst.de]</a></sup></li>'
     '<li>Die Schulbuch-Erklärung „im Süden regnet es sich aus“ stimmt nicht immer: Föhn kann auch ohne Niederschlag auf der Südseite entstehen.<sup><a href="https://www.srf.ch/meteo/meteo-stories/foehn-fuenf-fakten-zum-warmen-fallwind" target="_blank" rel="noopener">[SRF Meteo]</a></sup></li></ul>'
     '<p style="font-size:.82rem;color:#4b5563;">Stand: 28. November 2026.</p></article></main>']

JS = r'''<script>
(function(){var W={0:'☀️ klar',1:'🌤️ überwiegend klar',2:'⛅ teils bewölkt',3:'☁️ bedeckt',45:'🌫️ Nebel',48:'🌫️ Reifnebel',51:'🌦️ leichter Niesel',53:'🌦️ Niesel',55:'🌧️ starker Niesel',61:'🌧️ leichter Regen',63:'🌧️ Regen',65:'🌧️ starker Regen',66:'🧊 gefrierender Regen',67:'🧊 gefrierender Regen',71:'🌨️ leichter Schneefall',73:'🌨️ Schneefall',75:'❄️ starker Schneefall',77:'🌨️ Schneegriesel',80:'🌦️ Schauer',81:'🌧️ Schauer',82:'⛈️ heftige Schauer',85:'🌨️ Schneeschauer',86:'❄️ starke Schneeschauer',95:'⛈️ Gewitter',96:'⛈️ Gewitter mit Hagel',99:'⛈️ Gewitter mit Hagel'};
var T=['So','Mo','Di','Mi','Do','Fr','Sa'];
document.querySelectorAll('.wxk').forEach(function(k){var u='https://api.open-meteo.com/v1/forecast?latitude='+k.dataset.lat+'&longitude='+k.dataset.lon+'&elevation='+k.dataset.ele+'&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,wind_gusts_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,snowfall_sum,precipitation_sum&hourly=freezing_level_height&forecast_days=3&timezone=Europe%2FBerlin';
fetch(u).then(function(r){return r.json()}).then(function(d){var c=d.current,h='<div style="font-size:1.6rem;font-weight:700;color:#14532d;">'+Math.round(c.temperature_2m)+' °C</div><div>'+(W[c.weather_code]||'')+' · gefühlt '+Math.round(c.apparent_temperature)+' °C</div><div>Wind '+Math.round(c.wind_speed_10m)+' km/h, Böen '+Math.round(c.wind_gusts_10m)+' km/h</div>';
var fz=d.hourly&&d.hourly.freezing_level_height?d.hourly.freezing_level_height[new Date().getHours()]:null;if(fz!=null)h+='<div>Nullgradgrenze ca. '+(Math.round(fz/50)*50).toLocaleString('de-DE')+' m</div>';
h+='<table style="width:100%;margin-top:6px;font-size:.84rem;border-collapse:collapse;">';d.daily.time.forEach(function(t,i){var dt=new Date(t);h+='<tr><td style="padding:3px 0;">'+(i==0?'Heute':T[dt.getDay()])+'</td><td>'+(W[d.daily.weather_code[i]]||'').split(' ')[0]+'</td><td>'+Math.round(d.daily.temperature_2m_min[i])+' / '+Math.round(d.daily.temperature_2m_max[i])+' °C</td><td>'+(d.daily.snowfall_sum[i]>0?d.daily.snowfall_sum[i].toFixed(1)+' cm ❄':d.daily.precipitation_sum[i].toFixed(1)+' mm')+'</td></tr>'});
k.querySelector('.wxb').innerHTML=h+'</table>';}).catch(function(){k.querySelector('.wxb').textContent='Wetterdaten gerade nicht erreichbar.';});});})();
</script>
'''
s = open(SRC, encoding='utf-8').read()
a = s.find('<main'); z = s.find('</main>') + 7
head, tail = s[:a], s[z:]
DESC = 'Live-Wetter für Obere Firstalm, Rotwand und Schliersee, Webcams vom Spitzingsee und der Firstalm, Lawinenlagebericht Bayern und DAV-Bergwetter auf einen Blick.'
head = re.sub(r'<title>.*?</title>', '<title>Wetter, Webcams &amp; Lawinenlage Spitzingsee – Obere Firstalm live | alpenexperte.de</title>', head, count=1, flags=re.S)
for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
    head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(DESC) + m.group(2), head)
head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', r'\1https://alpenexperte.de/wetter-webcams.html\2', head)
head = re.sub(r'(<meta property="og:url" content=")[^"]*(")', r'\1https://alpenexperte.de/wetter-webcams.html\2', head)
head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S)
tail = tail.replace('</body>', JS + '</body>', 1)
open(F, 'w', encoding='utf-8').write(head + '\n'.join(b) + tail)
print('ok')
