# Prüfprotokoll Runde 1: Startseite und Gravelseite (Stand 2026-11-25)

Status: OFFEN = noch kein Beleg. BELEGT = Quelle geprüft. WIDERSPRUCH = Seite sagt etwas anderes als die Quelle. Entfernen, wenn kein Beleg kommt.

## index.html (Startseite)
| Angabe | Status | Hinweis |
|---|---|---|
| Kaiserschmarrn Untere Firstalm 12,90 € | OFFEN | Widerspruch zu den Preisen am selben Ort: 14,50 € auf der Schönfeldhütte, Preis im Abschnitt geprüft |
| Parkplatz Spitzingsee 6 €/Tag | OFFEN | Gebühr laut Gemeinde oder Betreiber prüfen |
| Bayern-Ticket ab 25 €, BRB-Gruppen 10 € pro Person | WIDERSPRUCH | Vorher (Ski-Datenbasis) als 39 € bzw. 10 € vermerkt, Tarif prüfen |
| Schönfeldhütte Kaiserschmarrn 14,50 € | OFFEN | Preis beim Betreiber prüfen |
| Bernhard-Kirche Sonnenaufgang 06:30 Uhr Sommer | OFFEN | Sinnvoll nur als Tipp, keine Zeit ohne Beleg |
| Balzzeit März–Mai, 3–6 Uhr, nur mit Führung | OFFEN | Schutzstatus und Führungspflicht prüfen |
| Spitzingsattel, Rotwandhaus, ~3,5 Std, ~760 Hm (T2) | OFFEN | Mit BRouter-Lauf oder Quelle prüfen |
| Valepp, ~4–4,5 Std, ~880 Hm (T3) | OFFEN | dito |
| Parkplatz am Wochenende ab 07:30 "restlos überfüllt" | OFFEN | Beobachtung, nicht belegbar, streichen |

## gravel.html (Gravelseite)
| Angabe | Status | Hinweis |
|---|---|---|
| Brenner–Bozen 96 km (53 + 43 km) | OFFEN | Radweg-Angaben beim Land Tirol oder Südtirol prüfen |
| Donauwörth–Altino 717 km | OFFEN | Summe aus Teilstrecken, Quelle nötig |
| Verona–Florenz 686 km | OFFEN | Quelle nötig |
| Thiersee-Runde 34,7 km / 520 Hm | OFFEN | Mit BRouter prüfen |
| Dreibrunnenjoch 4,6 km / 240 Hm, Radverbindung 2026 | OFFEN | Neue Verbindung: Bauzustand bestätigen |
| Reifenbreite 42–45 mm, Einkehr-Angaben | OFFEN | Herstellerwerte und Einkehr-Angaben prüfen |
| Ca. 60 Tourenkarten mit identischen Stufen (z. B. 20 km / 250 hm, 20 km / 140 hm) | OFFEN | Auffällig: sehr ähnliche Werte. Vor Veröffentlichung über BRouter nachrechnen |
| Routen "verifiziert, 48,9 km, +1.308 Hm" | OFFEN | Verifikation nachweisen oder Begriff streichen |

## Nächster Schritt
- Jede OFFEN-Zeile belegen (URL, Datum des Abrufs) oder streichen.
- Gravel-Routen über BRouter nachrechnen (routing/route.py), bevor Werte stehen bleiben.
- Widersprüche zuerst klären.

## Änderungen nach Nutzer-Angaben (2026-11-25)
- Parkplatz Spitzingsattel: 8 € pro Tag (Nutzer-Angabe, Betreiber noch zu belegen). Text geändert auf "meist recht voll" statt "restlos überfüllt". Unbelegte Uhrzeit (07:00) entfernt.
- Bayern-Ticket-Karte und FAQ-Absatz entfernt (Nutzer-Angabe: wird weggelassen).
- Kaiserschmarrn: Preisvergleich entfernt, bis geklärt ist, welcher Preis zu welcher Hütte gehört. Nutzer nannte 15,50 €. Ob das Untere Firstalm oder Schönfeldhütte betrifft, ist offen. "Sieger 2026" entfernt (unbelegt).

## Routen-Tiefenprüfung (Stand 2026-11-25)
- Nicht möglich in der Sandbox: BRouter (brouter.de) und Nominatim sind gesperrt (HTTP 403). Die Nachrechnung braucht den lokalen BRouter-Lauf (routing/route.py) auf deinem Rechner.
- Offline geprüft: 41 Angaben "km · hm" in content/ und gravel.html. Die Werte sind überwiegend unterschiedlich. Die Vermutung "identische Vorlagen" aus Runde 1 wird damit korrigiert: nicht bestätigt.
- 7 Dateien tragen das Wort "verifiziert". Dort fehlt der Nachweis. Diese Seiten bleiben OFFEN, bis der BRouter-Lauf vorliegt.
