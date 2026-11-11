# Initiales Bestandsaudit – alpenexperte.de

**Datum:** 11. November 2026  
**Status:** Audit & Bestandsaufnahme (Phase 0 & 1)  
**Domain:** alpenexperte.de (zwingend ohne Bindestrich)  

---

## 1. Executive Summary
alpenexperte.de ist ein spezialisiertes, von Einheimischen betriebenes Alpenportal mit Schwerpunkt auf den Bayerischen Voralpen (Mangfallgebirge, Spitzingsee, Schliersee, Tegernseer Tal). Das Projekt zeichnet sich durch praxisnahe Tourenberichte, Hütten-Guides, wissenschaftlich fundierte Naturartikel (Fauna, Flora, Geologie, Meteorologie, Moore) sowie kuratierte Shopping- und Affiliate-Integrationen aus.

## 2. Tatsächlicher Tech-Stack
* **Frontend:** Semantisches HTML5, CSS3 mit modernen Custom Properties (Design-Tokens in `css/style.css` und `css/homepage-v3.css`), Vanilla JavaScript (`js/main.js`, Leaflet.js für interaktive Karten).
* **Backend / Hosting:** Statische HTML-Seiten mit Python-basierten Build-/Generator-Skripten (z.B. für Sitemaps, Feeds und Strukturdaten).
* **Hosting / Deployment:** Vercel (CI/CD via GitHub Repository `FATILI80/alpenexperte.de.git`).
* **Monetarisierung / Affiliate:** Webgains-Produktfeed (automatisiert per GitHub Actions), Amazon PartnerNet (`bb8ozi-21`), Lucky Bike (`?ref=bb8ozi`), Urwahn Bikes (Awin) und Digistore24 (`Bb8ozi`).

## 3. Sicherheits- und Backup-Status
* **Git Repository:** Aktiver Branch `main`, working tree clean.
* **Backup:** Ein vollständiges Backup aller 530 Repository-Elemente wurde soeben unter `_backups/full_backup_20261111_143756` erstellt.
* **Secrets:** Keine Secrets, API-Schlüssel oder sensiblen Daten im Repository.
