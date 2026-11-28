#!/usr/bin/env python3
"""Übersichtsseiten Skitouren und Schneeschuh im Winter-Guide (Bildkarten, verifizierte Eckdaten aus winter_touren_build.py)."""
import re, html, importlib.util, sys
E=lambda t: html.escape(t, quote=False)
spec=importlib.util.spec_from_file_location('wt','routing/winter_touren_build.py')
src=open('routing/winter_touren_build.py',encoding='utf-8').read().split('def esc(t)')[0]   # nur Daten laden, nicht bauen
ns={}; exec(src, ns); T=ns['TOUREN']

def card(img, f, kopf):
    d=T[f]; href='/'+f
    return (f'<a href="{href}" style="display:block;background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;text-decoration:none;color:#0f2942;">'
            f'<img src="/images/{img}" alt="{E(d["name"])}" loading="lazy" style="width:100%;height:150px;object-fit:cover;display:block;">'
            f'<div style="padding:12px 14px;"><div style="font-size:.8rem;color:#1d4ed8;font-weight:700;">{E(kopf)}</div>'
            f'<h3 style="margin:4px 0 6px;color:#14532d;font-size:1.05rem;">{d["icon"]} {E(d["title"])}</h3>'
            f'<p style="margin:0;font-size:.9rem;line-height:1.45;">{E(d["lead"])}</p>'
            '<span style="display:inline-block;margin-top:8px;color:#14532d;font-weight:700;font-size:.88rem;">Tour ansehen →</span></div></a>')
GRID='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;">'
LAW=('<div style="background:#fef2f2;border-left:5px solid #b91c1c;padding:12px 16px;border-radius:10px;margin:0 0 20px;color:#1f2933;">'
     '<strong style="color:#991b1b;">Kein Hang ist „lawinensicher“.</strong> Vor jeder Tour den <a href="https://www.lawinenwarndienst.bayern.de" target="_blank" rel="noopener">Lawinenlagebericht Bayern</a> lesen. LVS, Sonde, Schaufel. Notruf <strong>112</strong>.</div>')

PAGES={
 'content/winter/skitouren/index.html':('Skitouren','🎿 Skitouren am Spitzingsee',
   'Vier Gipfel mit Start am Spitzingsee oder an den Firstalmen – Tourdaten aus den jeweils verlinkten Tourenportalen.',
   [('rotwand-ausblick-im-winter.jpg','content/winter/skitouren/rotwand.html','1.884 m · ca. 800 Hm direkt · Reibn 1.200–1.300 Hm · mittel'),
    ('winter-landschaft.jpg','content/winter/skitouren/taubenstein.html','1.692 m · ca. 600 Hm · leicht'),
    ('AusblickWinterunterfirst.jpg','content/winter/skitouren/brecherspitz.html','Westgipfel ca. 1.630 m · ca. 500 Hm · leicht'),
    ('winter-1.jpeg','content/winter/skitouren/bodenschneid.html','1.669 m · 560–810 Hm · mittel bis steil')],
   '<p style="margin-top:14px;"><a href="/content/skigebiete/">Pistentouren im Skigebiet</a> · <a href="/content/winter/skitouren-anfaenger.html">Skitouren für Einsteiger</a></p>'),
 'content/winter/schneeschuh/index.html':('Schneeschuh','👣 Schneeschuh- &amp; Winterwandern am Spitzingsee',
   'Drei Touren vom flachen Seeufer bis zum Rotwandhaus. Auf gespurten Wegen reichen oft Grödel, Schneeschuhe lohnen sich nach Neuschnee.',
   [('schneeschuh.jpg','content/winter/schneeschuh/spitzingsee-runde.html','ca. 3 km · 20–30 Hm · 1 h · leicht'),
    ('rodelpiste.jpg','content/winter/schneeschuh/firstalm.html','ca. 250 Hm · 45 min · leicht'),
    ('rotwandhaus-winter.jpg','content/winter/schneeschuh/rotwand.html','660–800 Hm · 2:30–2:45 h Aufstieg · mittel')],
   '<p style="margin-top:14px;"><a href="/content/winter/winterwandern-groedel.html">Winterwandern mit Grödeln</a> · <a href="/content/winter/firstalm-rodelbahn.html">Rodelbahn Obere Firstalm</a></p>')}

for f,(crumb,h1,lead,cards,extra) in PAGES.items():
    main=('<main id="main"><article class="container" style="max-width:1000px;margin:0 auto;padding:24px 16px 48px;">'
          f'<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <a href="/content/winter/index.html">Winter-Guide</a> › <span aria-current="page">{crumb}</span></nav>'
          f'<header style="margin-bottom:16px;"><h1 style="color:#14532d;margin:0 0 8px;">{h1}</h1><p style="font-size:1.06rem;color:#1f2933;margin:0;">{E(lead)}</p></header>'
          + LAW + GRID + ''.join(card(*c) for c in cards) + '</div>' + extra +
          '<p style="margin-top:20px;"><a href="/content/winter/index.html">← Zurück zum Winter-Guide</a></p></article></main>')
    s=open(f,encoding='utf-8').read(); a=s.find('<main'); b=s.find('</main>')+7
    head,tail=s[:a],s[b:]
    for pat in [r'<!-- ===== BRB ECHTZEIT-FAHRPLAN.*?</div>\s*',r'<section class="quellen-section".*?</section>\s*',r'<!-- URWAHN-AFFILIATE -->.*?<!-- /URWAHN-AFFILIATE -->\s*']:
        tail=re.sub(pat,'',tail,flags=re.S)
    tail=re.sub(r'(<!-- ===== PARTNER-HUB-BOX \(Allgemein\) ===== -->)+','',tail)
    head=re.sub(r'(<meta name="description"\s+content=")[^"]*(")',lambda m:m.group(1)+html.escape(lead)+m.group(2),head,count=1)
    open(f,'w',encoding='utf-8').write(head+main+tail); print('ok',f)
