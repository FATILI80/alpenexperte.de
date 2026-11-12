# Google Search Console – Technische Ausgangsprüfung & Baseline
*Datum: 12. November 2026*
*Domain: alpenexperte.de (Strikt ohne Bindestrich)*

---

## 1. Property- & Host-Konfiguration
- **Protokoll & Host:** `https://www.alpenexperte.de` (und `https://alpenexperte.de`).
- **SSL / HTTPS:** Vollständig aktiviert mit automatischen Weiterleitungen auf HTTPS.
- **Canonical-Konvention:** Jede Seite besitzt einen expliziten `<link rel="canonical" href="https://www.alpenexperte.de/...">` Tag.

## 2. Sitemap & Crawling
- **Sitemap-Pfad:** `https://www.alpenexperte.de/sitemap.xml`
- **URL-Anzahl:** 928 valide, indexierbare URLs (inklusive aller Fachartikel, Routen, Hütten und Service-Seiten).
- **Robots.txt:** Erlaubt Crawling aller redaktionellen Verzeichnisse (`/content/`, `/cluster/`, `/region/`, `/images/`, `/css/`, `/js/`), blockiert Hilfskripte und Archive.

## 3. Priorisierte URL-Liste für manuelle GSC-Inspektion
1. `https://www.alpenexperte.de/` (Startseite)
2. `https://www.alpenexperte.de/content/wandern/index.html` (Wander-Hub)
3. `https://www.alpenexperte.de/huetten.html` (Hüttenführer)
4. `https://www.alpenexperte.de/shopping.html` (Shopping & Partner)
5. `https://www.alpenexperte.de/content/wandern/rotwand.html` (Top-Tour Rotwand)
6. `https://www.alpenexperte.de/content/wandern/brecherspitz.html` (Top-Tour Brecherspitz)
7. `https://www.alpenexperte.de/content/alpinismus_sicherheit/wanderschwierigkeit-t1-t6.html` (Sicherheitsratgeber T1-T6)

## 4. Messmetriken & Auswertung
Ab dem Einrichtungsdatum (12.11.2026) werden wöchentlich folgende KPIs verglichen:
- Gesamte Impressionen & Klicks
- Durchschnittliche CTR und Position
- Indexierungsstatus wichtiger Cluster-Seiten
- Suchanfragen-Cluster (Wandern Spitzingsee, Hütten, Klettersteige Voralpen)
