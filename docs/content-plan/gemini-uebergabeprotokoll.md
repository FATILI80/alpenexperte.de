# 🤝 Übergabe- & Status-Protokoll für Gemini (Alpenexperte.de)
*Kopiere diesen Text in dein neues Chatfenster, um Gemini exakt auf den aktuellen Entwicklungsstand zu bringen.*

---

## 1. Projekt-Identität
- **Projekt:** `alpenexperte.de` (Domain zwingend ohne Bindestrich: `alpenexperte.de`)
- **Ziel:** Hochwertige, wissenschaftlich und sportmedizinisch fundierte, regionale Wissensplattform für die Bayerischen Voralpen (Mangfallgebirge, Spitzingsee, Schliersee, Tegernsee).
- **Tech Stack:** Statisches HTML5 / CSS3 / Vanilla JavaScript, gehostet auf Vercel, optimiert für Performance, Barrierefreiheit (WCAG) und SEO.

## 2. Aktueller technischer & inhaltlicher Stand (Letzter Commit: `6ab1dcb`)
- **50-Themen-Masterplan vollständig abgeschlossen:** Alle 50 Themen (Batches 1 bis 5, IDs A01 bis E50) wurden quellenbasiert (DAV, SAC, DWD, BRB) recherchiert, als dedizierte Fachartikel angelegt und in die Hub-Seiten sowie die `sitemap.xml` (900+ URLs) integriert.
- **Sicherheits- & Qualitäts-Audits (100% grün):**
  - Fiktive Routen entfernt; Brecherspitz korrekt als T3 (ausgesetzter Grat, Trittsicherheit & Schwindelfreiheit) eingestuft.
  - Authentische DAV-Hütteninformationen (`alpenvereinshuetten.de`).
  - Keine unbelegten Praxistests oder Marketing-Versprechen; stattdessen wissenschaftliche Faktor-10 Deep-Dives (Biometrie, HRV, Topografie, Kletter-Normen).
- **Transparente Monetarisierung (Affiliates):**
  - Amazon Outdoor (`tag=bb8ozi-21`) mit kategoriespezifischer Ausrüstung in jedem Fachartikel (Klettersteigsets, Wanderschuhe, Gravel-Reifen, MIPS-Helme, Walkingstöcke).
  - Lucky Bike (`?ref=bb8ozi`) und Urwahn E-Bikes (Awin) als dezente Infrastruktur- und Mobilitäts-Partner.
- **Automatisierte Testsuite (73/73 PASSED):**
  - `tests/test_50_themen.py` (53 Tests für Vollständigkeit und Masterplan)
  - `tests/test_audit_fixes.py` (10 Regressionstests für Sicherheit und Routenvalidierung)
  - `tests/test_master_qa.py` (Master QA für Sitemap und Ordnerintegrität)

## 3. Verbindliche Entwicklungsregeln (.clinerules)
1. **Zerstöre nichts:** Bestehende CSS-Grids und Layouts bleiben unangetastet.
2. **Keine Halluzinationen:** Nur geprüfte Fakten (DAV, SAC, DWD).
3. **Domain = alpenexperte.de** (nie mit Bindestrich).
4. **Partner-Tracking:** Tokens (`tag=bb8ozi-21`, `ref=bb8ozi`, Awin) bleiben in URLs aktiv, ohne Tracking-IDs im sichtbaren Fließtext zu spreizen.

## 4. Auftrag für Gemini
Du bist ab sofort der leitende Technical Lead, SEO-Stratege und QA-Manager für **alpenexperte.de**. Nutze diesen Status als Fundament für alle weiteren Fragen, Erweiterungen, Analysen oder Content-Optimierungen!
