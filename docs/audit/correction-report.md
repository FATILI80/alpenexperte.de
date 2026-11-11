# Korrekturbericht (Correction Report) – alpenexperte.de

**Datum:** 11. November 2026  
**Status:** Abgeschlossen & Getestet (Schritt 1 & 2)  
**Ausgangsbasis:** Branch `main`, Commit `5960968c9d14caf4b41b2d704323256b827795f7`  

---

## 1. Änderungsprotokoll (Dateien, Änderungen & Begründung)

| Datei | Betroffener Abschnitt | Vorheriges Verhalten | Neues Verhalten & Begründung |
| :--- | :--- | :--- | :--- |
| `index.html` | Zeile 1290 | Fiktive Route `R045: Rotwand Nordwand Alpinweg \| T5` aufgeführt. | **Vollständig entfernt.** Die Rotwand-Nordwand ist eine reine Kletterwand (UIAA IV+), kein T5-Wanderweg (Lebensgefahr beseitigt). |
| `js/routen-karte.js` | Zeile 52 | Route `R045` im JavaScript-Array für Karten und Filter. | **Eintrag gelöscht**, um Inkonsistenzen zwischen Tabelle und interaktiver Karte zu verhindern. |
| `index.html` | Zeile 1079 & Tabelle | Brecherspitz-Gipfelweg mit Schwierigkeit `T2` ausgewiesen. | Korrigiert auf **T3 (anspruchsvoll, Trittsicherheit & Schwindelfreiheit am Grat zwingend)**. Belegt durch DAV-Klassifizierung (rot). |
| `index.html` | Sektor 8 (Z. 1101–1146) | Fingierte Erlebnispakete (*Familien-Wochenende 189 €*, *3-Gipfel 279 €*, *Alm-Wellness 349 €*) mit irreführendem Buchungsvermerk. | **Komplett entfernt und ersetzt** durch sachliche DAV-Stützpunkte (*DAV-Haus Spitzingsee*, *Rotwandhaus*, *Schönfeldhütte*) mit offiziellen Reservierungslinks (`alpenvereinshuetten.de`). |
| `index.html` | Zeilen 699, 1318 | Unbelegte Produkttest-Behauptungen (*„8 Modelle im Härtetest auf der Alm“*). | Umformuliert in ehrliche **redaktionelle Kaufberatung** ohne fingierte Testreihen (UWG-Konformität). |
| `index.html` & `js/main.js` | Newsletter-Sektion & Handler | Schein-Formular mit `PLACEHOLDER`-URL und JS-Fake-Erfolgsmeldung. | **Deaktiviert.** Ersetzt durch einen ehrlichen Hinweistext (*„Newsletter demnächst verfügbar“*), um DSGVO-Täuschung zu verhindern. |
| `.github/workflows/update-webgains-feed.yml` | Feed-Injestor | Fehler bei API-Abruf wurden stumm abgefangen (Exit 0 / Silent Failure). | **Erweitert um GitHub Step Summary & Warnungen**, damit Feed-Ausfälle transparent und nachvollziehbar dokumentiert werden. |
| `index.html` & `js/main.js` | Wetter & Datum | Statische 16°C im Hero; leeres `Stand: .` ohne JS. | **Hero-Wetter als redaktioneller Status** gekennzeichnet; statisches Fallback-Datum (`11.11.2026`) im HTML hinterlegt. |
| `index.html` | Routen-Tabelle | R049 und R050 fälschlich unter `Alpin (T4+)` gelistet. | **In den korrekten Abschnitt `🟡 Mittelschwer (T3)` verschoben.** Gesamtzahl auf 49 verifizierte Routen angepasst. |
| `_generator/affiliates.json` & `shopping.html` | Shop & Partner | Enthielt themenfremde B2B-Software (KlickTipp, FunnelCockpit) und Esoterik (Binaural Beats). | **Restlos entfernt.** Fokus ausschließlich auf Outdoor, Wandern, Bergsteigen, Gravel- & E-Bikes (Amazon, Lucky Bike, Urwahn, Digistore24-Touren). |

---

## 2. Verwendete Quellen für alpine Einstufungen

* **Rotwand (Normalweg & Kletterwand):** Deutscher Alpenverein (DAV Sektion München-Oberland) – Die Nordwand ist alpinistisch als Felskletterei definiert und kein Wanderweg.
* **Brecherspitz (Normalweg über Firstalm):** DAV-Tourenportal / SAC-Wanderskala – Einstufung als mittelschwerer Bergweg mit ausgesetztem, seilversichertem Westgrat (**T3**).

---

## 3. Testergebnisse (Regression Tests)

Das automatisierte Testskript `tests/test_audit_fixes.py` wurde ausgeführt mit folgendem tatsächlichem Ergebnis:

* `[PASS] Test 1: R045 completely removed from public lists and JS cards`
* `[PASS] Test 2: Brecherspitz correctly rated as T3`
* `[PASS] Test 3: Fake Erlebnispakete removed`
* `[PASS] Test 4: Genuine DAV huts and official booking links present`
* `[PASS] Test 5: Unbelegte Produkttestbehauptungen removed`
* `[PASS] Test 6: Fake newsletter form deactivated and replaced with clean info box`
* `[PASS] Test 7: No broken 'Stand: .' date display`
* `[PASS] Test 8: Shopping page cleaned of non-outdoor software & esoterica`

**Gesamtergebnis:** 8 PASSED, 0 FAILED. Alle Regressionstests bestanden.

---

## 4. Offene Punkte & Risiken
* Keine sicherheitskritischen Mängel mehr offen. R045 wurde entfernt, Brecherspitz korrigiert, fingierte Pakete und Fake-Newsletter eliminiert.

---

## 5. Git-Status & Deployment-Nachweis
* **Git Branch:** `main`
* **Commit:** Bereit zum Commit und Push.
* **Vercel Production Deployment:** Wird nach Freigabe durch den Eigentümer ausgelöst.
