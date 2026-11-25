# Design-Vorlage: Gravelseite (gravel.html)

Stand: 2026-11-25. Werte aus dem Quelltext gemessen (Häufigkeit im Dokument), nicht geschätzt.
Die Gravelseite ist die 1:1-Vorlage. Das Menü wird später festgelegt.

## Farben (gemessen)
| Rolle | Hex | Vorkommen |
|---|---|---|
| Text sekundär | #64748b | 70 |
| Akzent Teal | #128290 | 70 |
| Rahmen hell | #cfd8dc | 44 |
| Hell-Blau | #4fc3f7 | 43 |
| Blau Hub | #0288d1 | 23 |
| Grau Rahmen | #90a4ae | 20 |
| Dunkel Hintergrund | #16242b | 20 |
| Dunkel tief | #0f191f | 20 |
| Warm hell | #f0ece2 | 10 |
| Amber | #ffb74d | 9 |
| Orange CTA | #ef6c00 | 5 |
| Rahmen grau | #e0e0e0 | 5 |

## Form und Raster (gemessen)
- Radien: 6px und 10px (je 30), 16px (9), 12px (9), 8px (3)
- Maximale Breite Inhaltsbereich: 1100px (10 Vorkommen)
- Abschnitte: `section--lounge` mit 36px Innenabstand, 16px Radius, 1px Rahmen

## Schrift (gemessen)
- Überschriften: `var(--font-display)`
- Größen: 0.8rem (110), 0.82rem (75), 0.84rem (43), 0.88rem (31), 1rem (20), 1.15rem (70)
- Kleine Labels und Meta-Angaben: 0.8rem, Textfarbe #64748b

## Bausteine
- Kartenraster: `silo-card` (30 Regeln in css/style.css)
- Kategorie-Abschnitte: `tours-category` mit `tours-heading` und `tours-sub`
- Hub-Box (dunkel, blauer Rahmen #0288d1): `firstalm-gravel-hub`
- Affiliate-Button: `btn-affiliate`; GPX-Button: `btn-gpx`

## Regeln für die Umsetzung
1. Dunkle Karten: Überschriften und Text hell (#f0ece2 oder heller), Links in hellem Blau. Die Klasse `dark-box` ist dafür vorgesehen, aber noch nicht eingeführt.
2. Keine `!important`-Farbregeln, die Inline-Farben überstimmen.
3. Helle Flächen: Text dunkel (#16242b oder #64748b), nie helle Schrift.
4. Jede Änderung wird auf einer Vorschau geprüft, bevor sie auf `main` geht.
5. Inhaltliche Angaben werden nur mit Quelle geändert. Ohne Beleg wird nichts umformuliert.
