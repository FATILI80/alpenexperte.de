# Live-Audit & Repository-Bestandsaufnahme – Alpenexperte.de
*Datum: 12. November 2026*
*Status: Growth Sprint 1 (Priorität 0)*

---

## 1. Executive Summary
Ein systematischer Abgleich zwischen lokaler Codebasis, Sitemap, Navigation und den live ausgelieferten Seiten von **alpenexperte.de** hat mehrere historische Inkonsistenzen, ungedeckte Marketing-Aussagen sowie einen schwerwiegenden SEO-Canoncial-Bug aufgedeckt. Der vorliegende Audit dokumentiert diese Befunde lückenlos und legt den Grundstein für die gezielte Behebung in Growth Sprint 1.

---

## 2. Inventar & URL-Prüfung

| URL / Datei | Live-Status | Befund / Risiko | Vorgeschlagener Fix |
| :--- | :--- | :--- | :--- |
| `https://alpenexperte.de/` | HTTP 200 | Startseite nennt parallel **61+**, **50** und **49** Wanderrouten; enthält statische Wetterwerte (16 °C) und unbelegte Behauptungen. | Konsolidierung auf exakt **49 verifizierte Routen**; Entfernung statischer Live-Puls-Werte. |
| `https://alpenexperte.de/content/wandern/index.html` | HTTP 200 | Meta-Descriptions und Header sprechen von **61 Wanderrouten**; unpassendes Amazon Prime Video Banner ("Für Filme & Serien") im Wander-Hub. | Angleichung auf 49 Routen; Entfernung fachfremder Werbung. |
| `https://alpenexperte.de/huetten.html` | HTTP 200 | Titel/Hero nennt **41 Hütten**, listet aber 6 österreichische Grenzhütten mit „bald im Detail“ ohne echte Detailseite. | Korrektur der Zählung auf echte verifizierte Detailhütten oder Ausformulierung der Grenzhütten. |
| `https://alpenexperte.de/shopping.html` | HTTP 200 | **Kritischer Bug:** Canonical-Tag zeigt fälschlicherweise auf `/huetten.html` statt auf `/shopping.html`. | Sofortige Korrektur des Canonical-Tags auf `https://www.alpenexperte.de/shopping.html`. |
| `https://alpenexperte.de/content/ausruestung/wanderstoecke/index.html` | HTTP 200 | Behauptet *„14 Modelle im Praxistest… im Härtetest im Mangfallgebirge“* ohne reale Dokumentation. | Umformulierung in sachliche redaktionelle Kaufberatung & Modellvergleich. |

---

## 3. Routenzahlen-Konsolidierung
- **Geprüfter Datenbestand:** `js/routen-karte.js` enthält exakt **49 Routen** (`R001` bis `R050` abzüglich der gelöschten Gefahrenroute `R045`).
- **Korrektur:** Alle Hubs, Metadaten und Teaser auf der Startseite und dem Wander-Hub werden zwingend auf **49 verifizierte Routen** vereinheitlicht.

---

## 4. SEO & Technische Integrität
- Canonical-Host: `https://alpenexperte.de` (strikt ohne Bindestrich).
- Sitemap: Enthält 928 valide URLs.
- Robots.txt: Korrekt konfiguriert mit Allow für Content-Ordner und korrekter Sitemap-Direktive.
