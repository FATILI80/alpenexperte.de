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

## Quellenabgleich Touren ab Oberer Firstalm und Transalp (Stand 2026-11-25)
Regeln: Nur Fakten übernehmen, Quelle angeben, keine Texte kopieren.

| Angabe | Status | Quelle (Abruf 2026-11-25) |
|---|---|---|
| Obere Firstalm 1.375 m | BELEGT | bergwelten.com/h/obere-firstalm; hoehenrausch.de/huetten/obere-firstalm |
| Spitzingsattel → Obere Firstalm: 40–45 min, ca. 246–250 Hm | BELEGT | hoehenrausch.de/huetten/obere-firstalm (Aufstieg 45 min, 250 Hm); bergwelten.com/t/w/38247 (1:00 h, 2,6 km) |
| Brecherspitz 1.683 m | BELEGT | hoehenrausch.de/berge/brecherspitz (Höhe), bergtour-online.de (Gehzeit Spitzingsattel → Gipfel ca. 2:00 h) |
| Brecherspitz ab Oberer Firstalm: 308 Hm (1.683 − 1.375) | BELEGT (aus den Höhen abgeleitet) | Höhen oben |
| Brecherspitz ab Oberer Firstalm: 2,2 km, 1:15 Std. | OFFEN | Länge nicht gefunden. Gehzeit nur abgeleitet |
| Bodenschneid 1.668 m | KORREKTUR | hoehenrausch.de nennt 1.669 m. Auf der Seite auf 1.669 m ändern |
| Roßkopf 1.580 m | BELEGT | hoehenrausch.de/huetten/obere-firstalm (Verweis Roßkopf 1580 m) |
| Rotwand 1.884 m, Hochmiesing 1.883 m, Taubenstein 1.692 m, Stümpfling 1.506 m, Jägerkamp 1.746 m, Tanzeck 1.703 m, Aiplspitz 1.759 m, Rotwandhaus 1.737 m | OFFEN | Nicht in den geprüften Quellen gefunden |
| Untere Firstalm 1.318 m | BELEGT | hoehenrausch.de/berge/brecherspitz (1.318 m) |
| Brecherspitz 8,5 km, 560 Hm (Kurvenlift) | BELEGT | hoehenrausch.de/berge/brecherspitz |
| Obere Firstalm – Spitzingsattel Rundtour: 2:30 h, 300 Hm | BELEGT | bergtour-online.de (leicht, 300 hm, 2:30 h) |
| Donauwörth–Altino 717 km (Via Claudia Augusta) | WIDERSPRUCH | biketrailspfannenstiel.ch nennt ca. 740 km für Donauwörth–Ostiglia. Strecke muss gleich sein |
| Brenner–Bozen 96 km (53 + 43 km) | OFFEN | Nicht gefunden. Quellen nennen keine Teilkilometer |
| Verona–Florenz 686 km, Ciclovia del Sole | OFFEN | Nicht gefunden |
| Gardasee-Radroute ab Brenner, wenig Höhenmeter | BELEGT | bergwelten.com/t/m/51562 (Dolce-Vita-Tour Brenner–Riva) |
| Thiersee-Runde 34,7 km / 520 Hm | OFFEN | Nicht gefunden |

## Ergebnis
- Mehrere Höhen und Zeiten sind belegt. Die Liste ist nicht vollständig.
- Ein Widerspruch (Via Claudia Augusta, 717 vs. 740 km) und eine Korrektur (Bodenschneid 1.669 m) sind festgehalten.
- Viele Gipfelhöhen und die Transalp-Kilometer sind offen. Sie kommen erst auf den Stand, wenn eine Quelle sie bestätigt oder der BRouter-Lauf vorliegt.

## Gipfel-Nachprüfung (Stand 2026-11-25)
| Gipfel | Status | Quelle |
|---|---|---|
| Rotwand 1.884 m | BELEGT | muenchen.de (Höhe 1884 m); hoehenrausch.de/berge/rotwand |
| Rotwandhaus 1.737 m | BELEGT | hoehenrausch.de/berge/rotwand |
| Hochmiesing 1.883 m | BELEGT | hoehenrausch.de/berge/hochmiesing |
| Taubenstein 1.692 m | BELEGT, Abweichung | hoehenrausch.de nennt 1.692 m und 1.693 m; summitpost nennt 1.692 m |
| Stümpfling 1.506 m | BELEGT | Wikipedia (Stümpfling) |
| Jägerkamp 1.746 m, Tanzeck 1.703 m | BELEGT | hoehenrausch.de/wandern/deutschland/schliersee (Liste mit Höhen) |
| Aiplspitz 1.759 m | BELEGT | hoehenrausch.de/wandern/deutschland/bayrischzell |
| Roßkopf 1.580 m | BELEGT | komoot.com/smarttour/41981736 |
Markierungen "Angabe prüfen" bei diesen Gipfeln entfernt.
