#!/usr/bin/env python3
"""Gemeinsame Bausteine für die Kategorie-Seiten (Kopf/Fuß von restaurants.html, Quellen-Zählung, Karten)."""
import re, html
E = lambda t: html.escape(t, quote=False)
H2 = lambda i, t, sub='': f'<h2 id="{i}" style="color:#14532d;margin:38px 0 6px;scroll-margin-top:140px;">{t}</h2>' + (f'<p style="color:#374151;margin:0 0 12px;line-height:1.6;">{sub}</p>' if sub else '')
P = lambda t: f'<p style="color:#1f2933;line-height:1.65;">{t}</p>'
def BOX(t, farbe='#e8f5e9', rand='#2e7d32'): return f'<div style="background:{farbe};border-left:5px solid {rand};padding:12px 16px;border-radius:10px;margin:14px 0;color:#1f2933;line-height:1.6;">{t}</div>'
def UL(items): return '<ul style="line-height:1.7;color:#1f2933;">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
GRID = lambda cards: '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin:10px 0 6px;">' + ''.join(cards) + '</div>'

class Q:
    def __init__(s, note='Stand: 28. November 2026.'): s.l = []; s.note = note
    def __call__(s, titel, url):
        if (titel, url) not in s.l: s.l.append((titel, url))
        n = s.l.index((titel, url)) + 1
        return f'<sup><a href="#q{n}" style="color:#1d4ed8;text-decoration:none;">[{n}]</a></sup>'
    def liste(s): return (H2('quellen', '📚 Quellen') + '<ol style="line-height:1.7;font-size:.92rem;">'
                          + ''.join(f'<li id="q{i}"><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for i, (t, u) in enumerate(s.l, 1)) + '</ol>'
                          + f'<p style="font-size:.82rem;color:#4b5563;">{s.note}</p>')

def CARD(cid, name, latin, text, rows, img=None, alt='', icon='🐾'):
    top = (f'<img src="/images/{img}" alt="{E(alt or name)}" loading="lazy" style="width:100%;height:170px;object-fit:cover;display:block;">' if img
           else f'<div style="height:70px;display:flex;align-items:center;justify-content:center;font-size:2.2rem;background:#e8f5e9;">{icon}</div>')
    tab = ''.join(f'<tr><th style="text-align:left;padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#14532d;width:34%;vertical-align:top;">{k}</th><td style="padding:6px 9px;border-bottom:1px solid #e5e7eb;color:#1f2933;vertical-align:top;">{v}</td></tr>' for k, v in rows)
    return (f'<article id="{cid}" style="background:#fff;border:1px solid #2e7d32;border-radius:12px;overflow:hidden;scroll-margin-top:140px;">{top}'
            f'<div style="padding:12px 14px;"><h3 style="margin:0 0 2px;color:#14532d;font-size:1.08rem;">{name}</h3>'
            f'<div style="font-style:italic;color:#4b5563;font-size:.85rem;margin-bottom:6px;">{latin}</div>'
            f'<p style="margin:0 0 8px;font-size:.92rem;line-height:1.5;color:#1f2933;">{text}</p>'
            + (f'<details style="background:#f8fafc;padding:7px 9px;border-radius:6px;"><summary style="color:#14532d;font-weight:600;font-size:.86rem;cursor:pointer;">Steckbrief &amp; Quellen</summary>'
            f'<table style="width:100%;border-collapse:collapse;font-size:.88rem;margin-top:6px;">{tab}</table></details>' if rows else '') + '</div></article>')

def seite(pfad, titel, h1, intro, hero, nav, body, desc, crumb, weiter):
    s = open('restaurants.html', encoding='utf-8').read()
    a = s.find('<main'); z = s.find('</main>') + 7
    head, tail = s[:a], s[z:]
    url = 'https://alpenexperte.de/' + pfad
    head = re.sub(r'<title>.*?</title>', f'<title>{E(titel)} | alpenexperte.de</title>', head, count=1, flags=re.S)
    for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'(<meta ' + prop + r'\s+content=")[^"]*(")', lambda m: m.group(1) + html.escape(desc) + m.group(2), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(titel) + m.group(2), head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S)
    absol = lambda t: re.sub(r'((?:href|src)=")(?!https?:|/|#|mailto:|tel:|data:|javascript:)([^"]+)"', r'\1/\2"', t)
    head, tail = absol(head), absol(tail)
    m = ['<main id="main"><article class="container" style="max-width:1040px;margin:0 auto;padding:24px 16px 48px;">',
         f'<nav aria-label="Breadcrumb" style="font-size:.9rem;margin-bottom:12px;"><a href="/">Home</a> › <span aria-current="page">{crumb}</span></nav>',
         f'<header style="margin-bottom:14px;"><h1 style="color:#14532d;margin:0 0 8px;">{h1}</h1><p style="font-size:1.08rem;color:#1f2933;margin:0;line-height:1.6;">{intro}</p></header>', hero,
         '<nav class="kat-nav" style="background:#e8f5e9;border:1px solid #2e7d32;border-radius:10px;padding:10px;margin:12px 0 16px;display:flex;flex-wrap:wrap;gap:8px;">'
         + ''.join(f'<a href="#{i}" style="background:#14532d;color:#fff;padding:6px 10px;border-radius:6px;text-decoration:none;font-size:.84rem;font-weight:700;">{t}</a>' for i, t in nav) + '</nav>',
         body, f'<p style="margin-top:22px;font-size:.92rem;">{weiter}</p>', '</article></main>']
    open(pfad, 'w', encoding='utf-8').write(head + '\n'.join(m) + tail)
    print('ok', pfad, len(head + ''.join(m) + tail))

HERO = lambda img, alt: f'<img src="/images/{img}" alt="{E(alt)}" loading="lazy" style="width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:block;margin:10px 0 14px;">'

FIG = lambda img, alt, cap: f'<figure style="margin:10px 0 14px;"><img src="/images/{img}" alt="{E(alt)}" loading="lazy" style="width:100%;max-height:320px;object-fit:cover;border-radius:12px;display:block;"><figcaption style="font-size:.84rem;color:#4b5563;margin-top:5px;">{cap}</figcaption></figure>'

def AFF(links): return ('<aside style="border:1px solid #e5e7eb;border-radius:10px;padding:12px 16px;font-size:.95rem;color:#1f2933;margin-top:18px;"><span style="font-size:.75rem;text-transform:uppercase;color:#6b7280;">Anzeige</span><br>'
                        + ' · '.join(f'<a href="https://www.amazon.de/s?k={q}&amp;linkCode=ll2&amp;tag=bb8ozi-21" target="_blank" rel="sponsored noopener">{t}</a>' for t, q in links) + ' bei Amazon</aside>')

def TAB(kopf, zeilen):
    th = ''.join(f'<th style="text-align:left;padding:7px 9px;background:#e8f5e9;color:#14532d;border-bottom:2px solid #2e7d32;">{k}</th>' for k in kopf)
    tr = ''.join('<tr>' + ''.join(f'<td style="padding:6px 9px;border-bottom:1px solid #e5e7eb;vertical-align:top;">{c}</td>' for c in z) + '</tr>' for z in zeilen)
    return f'<div style="overflow-x:auto;margin:10px 0 14px;"><table style="width:100%;border-collapse:collapse;font-size:.92rem;color:#1f2933;"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
