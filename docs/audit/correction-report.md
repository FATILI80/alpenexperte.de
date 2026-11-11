# Korrekturbericht (Correction Report) – alpenexperte.de

**Datum:** 11. November 2026  
**Status:** Lokal umgesetzt, vollständig getestet (10/10 Bestanden) – **NOCH KEIN PUSH, KEIN DEPLOYMENT**  
**Ausgangsbasis:** Branch `main`, Commit `5960968c9d14caf4b41b2d704323256b827795f7`  

---

## 1. Detailliertes Änderungsprotokoll & Begründung

| Datei | Betroffener Abschnitt | Vorheriges Verhalten | Neues Verhalten & Nachweis |
| :--- | :--- | :--- | :--- |
| `index.html` & `js/routen-karte.js` | Routen-Tabelle & JS-Array | Fiktive Route `R045: Rotwand Nordwand Alpinweg \| T5` aufgeführt. | **Vollständig entfernt.** Die Rotwand-Nordwand ist eine reine Felskletterwand (UIAA IV+), kein T5-Wanderweg (Lebensgefahr beseitigt). |
| `index.html` | Zeile 1079 & Tabelle | Brecherspitz-Gipfelweg mit Schwierigkeit `T2` ausgewiesen. | Korrigiert auf **T3 (anspruchsvoll, Trittsicherheit & Schwindelfreiheit am ausgesetzten Westgrat zwingend)**. Belegt durch DAV-Klassifizierung (rot) und SAC-Skala. |
| `index.html` | Sektor 8 (Z. 1101–1146) | Fingierte Erlebnispakete (*Familien-Wochenende 189 €*, *3-Gipfel 279 €*, *Alm-Wellness 349 €*) mit irreführendem Buchungsvermerk. | **Komplett entfernt und ersetzt** durch sachliche DAV-Stützpunkte (*DAV-Haus Spitzingsee*, *Rotwandhaus*, *Schönfeldhütte*) mit offiziellen Reservierungslinks (`alpenvereinshuetten.de`). |
| `index.html` | Zeilen 708, 1318–1334 | Unbelegte Produkttest-Behauptungen (*„8 Modelle im Härtetest auf der Alm“*, *„frei von Herstellereinfluss“*). | Umformuliert in ehrliche **redaktionelle Kaufberatung** ohne fingierte Testreihen (UWG-Konformität). |
| `index.html` & `js/main.js` | Newsletter-Sektion & Handler | Schein-Formular mit `PLACEHOLDER`-URL und JS-Fake-Erfolgsmeldung. | **Deaktiviert.** Ersetzt durch einen ehrlichen Hinweistext (*„Alm-Praxis Newsletter – Demnächst verfügbar“*), um DSGVO-Täuschung zu verhindern. |
| `index.html` | Routen-Tabelle (T3 / T4+) | R049 und R050 fälschlich unter `Alpin (T4+)` gelistet. | **In den korrekten Abschnitt `🟡 Mittel (T3)` verschoben.** Gesamtzahl auf 49 verifizierte Routen harmonisiert. |
| `index.html` | Hero-Leiste (Wetter) | Irreführender Kasten mit *„LIVE-PULS & STATUS“* und statischen 16°C. | **Umbenannt in `REDAKTIONELLER SAISONHINWEIS`** mit Zeitstempel (*„Stand: 11.11.2026 – Redaktionelle Saison-Einschätzung“*) und Verweis auf Open-Meteo. |
| `shopping.html` & `_generator/affiliates.json` | Shop & Partner | Enthielt themenfremde B2B-Software (KlickTipp, FunnelCockpit) und Esoterik (Binaural Beats). | **Restlos entfernt.** Fokus ausschließlich auf Outdoor, Wandern, Bergsteigen, Gravel- & E-Bikes (Amazon, Lucky Bike, Urwahn, Digistore24-Touren). |

---

## 2. Verwendete Quellen für alpine Einstufungen

* **Rotwand (Normalweg & Kletterwand):** Deutscher Alpenverein (DAV Sektion München-Oberland) – Die Nordwand ist alpinistisch als Felskletterei definiert und kein Wanderweg. Abrufdatum: 11.11.2026.
* **Brecherspitz (Normalweg über Firstalm & Westgrat):** 
  * *DAV-Tourensuche / Alpenverein München & Oberland:* Klassifizierung als roter Bergwanderweg (mittelschwer, schmale, teils drahtseilversicherte Passagen). Trittsicherheit und Schwindelfreiheit zwingend. Abrufdatum: 11.11.2026.
  * *SAC-Wanderskala:* **T3 (anspruchsvolles Bergwandern)** – Ausgesetzte Passagen mit Seilversicherungen, Absturzgefahr bei Nässe. Abrufdatum: 11.11.2026.

---

## 3. Testergebnisse (Enhanced Regression Tests)

Das erweiterte Testskript `tests/test_audit_fixes.py` wurde ausgeführt mit folgendem tatsächlichen Ergebnis:

* `[PASS] Test 1: R045 completely removed`
* `[PASS] Test 2: Brecherspitz correctly rated as T3 with Trittsicherheit & Schwindelfreiheit`
* `[PASS] Test 3: Fake Erlebnispakete removed`
* `[PASS] Test 4: Genuine DAV huts present`
* `[PASS] Test 5: Unverified test claims removed`
* `[PASS] Test 6: Newsletter form deactivated`
* `[PASS] Test 7: Valid update date fallback present`
* `[PASS] Test 8: R049 and R050 excluded from T4+ section`
* `[PASS] Test 8b: R049 and R050 located in T3 section before T4+ section`
* `[PASS] Test 9: Weather banner correctly labeled as editorial seasonal notice`

**Gesamtergebnis:** 10 PASSED, 0 FAILED. Alle Regressionstests bestanden erfolgreich.

---

## 4. Offene Punkte & Risiken
* Keine sicherheitskritischen Mängel mehr offen. Alle 5 Audit-Punkte und die zusätzlichen Entwickler-Anforderungen wurden vollständig umgesetzt und testgetreu verifiziert.

---

## 5. Git-Status & Deployment-Nachweis (Lokal)
* **Git Branch:** `main`
* **Geänderte Dateien:** `index.html`, `js/routen-karte.js`, `js/main.js`, `shopping.html`, `_generator/affiliates.json`, `tests/test_audit_fixes.py`, `docs/audit/correction-report.md`.
* **Deployment-Status:** **Kein Deployment erfolgt.** Alle Änderungen befinden sich ausschließlich lokal im Working Tree zur unabhängigen Prüfung durch den Auditor.
