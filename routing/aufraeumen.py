#!/usr/bin/env python3
"""Löscht ersetzte Unterseiten, setzt 301-Weiterleitungen, schreibt interne Links um und bereinigt die Sitemap.
Aufruf: python3 routing/aufraeumen.py mapping.json   (JSON: {"content/x/alt.html": "/content/x/#anker", ...})"""
import json, os, re, glob, subprocess, sys

m = json.load(open(sys.argv[1]))
v = json.load(open('vercel.json')); red = v['redirects']
have = {r['source'] for r in red}
neu = {}
for alt, ziel in m.items():
    if os.path.isfile(alt): subprocess.run(['git', 'rm', '-q', '-f', alt], check=True)
    urls = ['/' + alt]
    if alt.endswith('/index.html'): urls = ['/' + alt[:-11] + '(/|/index\\.html)?']; neu['/' + alt[:-11]] = ziel; neu['/' + alt[:-10]] = ziel
    neu['/' + alt] = ziel
    for u in urls:
        if u not in have: red.append({'source': u, 'destination': ziel, 'permanent': True}); have.add(u)
# Ketten: bestehende Redirects, die auf jetzt gelöschte Seiten zeigen, direkt aufs neue Ziel lenken
for r in red:
    d = r['destination'].split('#')[0]
    if d in neu and r['source'] not in m: r['destination'] = neu[d]
json.dump(v, open('vercel.json', 'w'), ensure_ascii=False, indent=2)
n = len(red) + len(v.get('headers', []))
print('Routen gesamt:', n, '(Limit 2048)'); assert n < 2048

geaendert = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf-8', errors='ignore').read(); o = s
    def rep(mm):
        u = mm.group(2)
        if re.match(r'(https?:|mailto:|tel:|data:|javascript:|#|//)', u): return mm.group(0)
        p = u.split('#')[0].split('?')[0]; anc = u[len(u.split('#')[0]):] if '#' in u else ''
        ap = p if p.startswith('/') else '/' + os.path.normpath(os.path.join(os.path.dirname(f), p))
        if ap in neu:
            z = neu[ap]; return mm.group(1) + (z if ('#' in z or not anc) else z + anc) + mm.group(3)
        return mm.group(0)
    s = re.sub(r'((?:href|src)=")([^"]+)(")', rep, s)
    if s != o: open(f, 'w', encoding='utf-8').write(s); geaendert += 1
print('Links umgeschrieben in', geaendert, 'Dateien')

sm = open('sitemap.xml').read(); vor = sm.count('<loc>')
sm = re.sub(r'\s*<url>\s*<loc>https://alpenexperte\.de/([^<]*)</loc>.*?</url>', lambda mm: '' if mm.group(1) in m else mm.group(0), sm, flags=re.S)
open('sitemap.xml', 'w').write(sm); print('Sitemap:', vor, '->', sm.count('<loc>'))
