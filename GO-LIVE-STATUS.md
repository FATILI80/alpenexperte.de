# GO-LIVE alpenexperte.de — Status & naechster Schritt

## ERLEDIGT (Stand heute)
- Git-Repo initialisiert (3 Commits), 4.366 Dateien, 2.996 Bilder via Git LFS
- Vercel-Projekt `alpenexperte` angelegt (foezhan1-7250s-projects)
- Produktions-Deploy: READY
- Live-URL: https://alpenexperte-dkwj35knt-foezhan1-7250s-projects.vercel.app
- Alias:    https://alpenexperte.vercel.app
- Domain `alpenexperte.de` dem Vercel-Projekt hinzugefuegt
- Domain-Fix: 13 Dateien von `alpen-experte.de` -> `alpenexperte.de` korrigiert
  (inkl. region/spitzingsee, region/schliersee, region/tegernsee, humanstxt, js/main.js)
- Favicon erstellt: images/favicon.svg
- .vercelignore: Backups, Skripte, Reports vom Deploy ausgeschlossen
- QA: 162/162 Sitemap-URLs erreichbar (Stichprobe 30/30 + Volltest)
- QA: 20 Navigationsziele ohne Fehler
- QA: Backup-Leichen liefern alle 404 (nichts leakt)
- Desktop aufgeraeumt: alpenexperte-BACKUP, 2 ZIPs, 3 Hilfs-TXT geloescht

## OFFEN: DNS-Umstellung (braucht IONOS/United-Domains Login)
Aktuell zeigen alpenexperte.de und www auf 89.31.143.90
(Nameserver: ns.udag.de / ns.udag.net / ns.udag.org = IONOS / United Domains)
Dort laeuft NUR die Platzhalterseite "Domain im Kundenauftrag registriert".

### Option A (empfohlen): Vercel-Nameserver setzen
Im IONOS/United-Domains-Kundenbereich -> Domain alpenexperte.de -> Nameserver:
  ns1.vercel-dns.com
  ns2.vercel-dns.com
Danach: HTTPS, www-Redirect und alle Records automatisch.

### Option B: Einzelne DNS-Records setzen
  A      @     216.198.79.1
  A      @     64.29.17.1
  CNAME  www   cname.vercel-dns.com

### Pruefen nach Umstellung
  vercel domains verify alpenexperte.de
  https://alpenexperte.de im Browser oeffnen

## NACH DNS-Umstellung
1. Google Search Console: Property alpenexperte.de anlegen, sitemap.xml einreichen
2. Plausible: Domain alpenexperte.de verifizieren (script ist schon eingebaut)
3. Optional: HSTS in Vercel aktivieren