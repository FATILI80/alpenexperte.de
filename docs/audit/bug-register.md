# Fehlerregister (Bug Register) – alpenexperte.de

**Datum:** 11. November 2026  
**Status:** Audit (Phase 2)

| Bug-ID | Kategorie | Betroffene Datei | Beschreibung | Status | Maßnahme |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BUG-01 | P1 | `.github/workflows/update-webgains-feed.yml` | Webgains-Feed Workflow schlug gelegentlich fehl wegen API-Timeout. | **Behoben** | Try-Except-Block mit robustem Daten-Fallback implementiert. |
| BUG-02 | P1 | `shopping.html` | Shopping-Seite war durch Footer-Fragment überschrieben. | **Behoben** | Vollständig als kuratierte Partner-Shopping-Welt wiederhergestellt. |
| BUG-03 | P2 | `content/huetten/alm-restaurants/index.html` | Falsche Bilder bei Firstalm & Taubensteinhaus sowie Layout-Lücken. | **Behoben** | Auf echtes CSS-Grid und originale Originalbilder umgestellt. |
| BUG-04 | P2 | `content/sternenhimmel/index.html` | Historische Himmelskunde unvollständig; doppelte Verlinkungen. | **Behoben** | Historie eingebettet, alte Seite umgeleitet, Duplikate entfernt. |
| BUG-05 | P2 | `content/praxis/index.html` | Doppelte Bilder bei Kacheln und 404-Bildfehler bei Jahreszeiten. | **Behoben** | Passende Bilder zugeordnet und Syntaxfehler korrigiert. |
