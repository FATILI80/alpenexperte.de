# 🏔️ STRUKTUR_MAP — Alpen-Experte.de
> System gelockt. Architektur konform. Keine Improvisation.
> Stand: 1. Juni 2026
> Cache-Buster: `v=2025-06-01-1`

---

## 1. HUBS (Regionen)

Nur diese 4 Hubs sind definiert. Keine weiteren ohne explizite Freigabe.

```
/region/
├── index.html               # Hub-Übersicht
├── spitzingsee/
│   └── index.html           # Spitzingsee Hub
├── tegernsee/
│   ├── index.html           # Tegernsee Hub
│   ├── geschichte/
│   │   └── index.html       # Historischer Anker (Kloster)
│   ├── huetten/
│   │   └── index.html       # Hütten-Profil
│   └── klettern/
│       └── index.html       # Kletter-Modul
├── schliersee/
│   └── index.html           # Schliersee Hub
└── valepp/
    └── index.html           # Valepp Hub
```

**Module pro Hub:**
- Echtzeit-Status (Wetter, Schnee, Öffnungszeiten)
- Hütten-Profil
- Historische Anker (Jennerwein, Kloster)
- Kultur-Modul
- Alpenaustausch-Teaser (Sektion 8)

---

## 2. SILOS (Deep Dives)

```
/content/
├── ausruestung/             # Affiliate-Silo
│   ├── index.html
│   └── wanderstoecke/
│       └── index.html
├── fauna/                   # Fauna & Flora Silo
│   ├── index.html
│   └── flora/
│       ├── index.html
│       ├── arnika.html
│       ├── edelweiss.html
│       ├── enzian.html
│       └── hohenstufen.html
└── sicherheit/              # Sicherheit Silo
    ├── index.html
    ├── berg-knigge.html
    ├── erste-hilfe.html
    └── wetterkunde.html
```

---

## 3. CONTENT-MODULE (Themenbereiche)

```
/content/
├── klettern/                # Klettern-Modul (13 Seiten)
│   ├── index.html                             # Hub
│   ├── brecherspitz-klettersteig.html         # Besteht
│   ├── rotwand-klettersteig.html              # Besteht
│   ├── taubenstein-klettersteig.html          # Besteht
│   ├── bodenschneid-klettersteig.html         # Besteht
│   ├── blankenstein.html                      # NEU: Ostgrat UIAA 4+
│   ├── ross-buchstein.html                    # NEU: Südwand UIAA 6-7
│   ├── leonhardstein.html                     # NEU: Plaisir + MTB-Combo
│   ├── bodenschneid-gratkletterei.html        # NEU: Grat UIAA III + Jennerwein
│   ├── taubenstein-suedgrat.html              # NEU: Anfänger-Grat UIAA III
│   ├── anfaenger-routen.html                  # NEU: Einsteiger-Guide
│   ├── sicherheit-ausruestung.html            # NEU: Safety + Gear
│   └── felstechniken-uebersicht.html          # NEU: Knoten, Techniken, Video
│
├── mtb/                     # Mountainbike-Modul (9 Seiten)
│   ├── index.html                             # Hub
│   ├── alte-spitzingstrasse.html              # Besteht
│   ├── drei-seen-runde.html                   # Besteht
│   ├── prinzenweg.html                        # Besteht
│   ├── rotwand.html                           # Besteht
│   ├── spitzingsee-runde.html                 # Besteht
│   ├── muenchen-spitzingsee-mtb.html          # NEU: München→Spitzingsee per Rad
│   ├── schwierigkeits-guide-sts.html          # NEU: STS S0-S6 erklärt
│   └── mtb-saisonkalender.html                # NEU: Monat-für-Monat
│
├── winter/                  # Winter-Modul (18 Seiten)
│   ├── index.html                             # Hub
│   ├── langlauf/
│   │   └── index.html                         # Besteht
│   ├── schneeschuh/
│   │   ├── index.html                         # Besteht
│   │   ├── firstalm.html                      # Besteht
│   │   ├── rotwand.html                       # Besteht
│   │   └── spitzingsee-runde.html             # Besteht
│   ├── skigebiet/
│   │   └── index.html                         # Besteht
│   ├── skitouren/
│   │   ├── index.html                         # Besteht
│   │   ├── bodenschneid.html                  # Besteht
│   │   ├── brecherspitz.html                  # Besteht
│   │   ├── rotwand.html                       # Besteht
│   │   └── taubenstein.html                   # Besteht
│   ├── rotwand-reibn-skitouren.html           # NEU: Klassiker-Runde
│   ├── skitouren-anfaenger.html               # NEU: 3 Anfängerziele
│   ├── rodeln-familie.html                    # NEU: Rodeln mit Kindern
│   ├── lawinenkunde-grundlagen.html           # NEU: LVS, Schneeprofil
│   ├── ausruestung-winter.html                # NEU: Winter-Gear komplett
│   └── winterkalender.html                    # NEU: Monats-Guide
│
├── huetten/                 # Hütten-Modul
│   ├── index.html
│   ├── alm-restaurants/
│   │   └── index.html
│   ├── huetten-karte/
│   │   └── index.html
│   ├── klettern/
│   │   ├── index.html
│   │   └── brecherspitz-klettersteig.html
│   ├── rodelpisten/
│   │   └── index.html
│   └── wanderwege/
│       ├── index.html
│       ├── brecherspitz-gipfelweg.html
│       ├── josefsthaler-wasserfaelle.html
│       ├── obere-firstalm.html
│       └── valepp.html
│
├── praxis/                  # Praxis-Modul
│   ├── index.html
│   ├── saisonaler-kalender.html
│   ├── jahreszeiten/
│   │   └── index.html
│   ├── packlisten/
│   │   └── index.html
│   ├── tourenplanung/
│   │   └── index.html
│   └── oepnv-guide/                           # NEU: ÖPNV-Hub
│       └── index.html
│
├── fitness/                 # Fitness-Modul
│   ├── index.html
│   ├── einsteiger/
│   │   └── index.html
│   ├── fortgeschrittene/
│   │   └── index.html
│   └── huettentour/
│       └── index.html
├── layering/                # Layering-Modul
│   ├── index.html
│   ├── baselayer/
│   │   └── index.html
│   ├── midlayer/
│   │   └── index.html
│   └── outer-shell/
│       └── index.html
├── tech/                    # Tech-Modul
│   ├── index.html
│   ├── apps/
│   │   └── index.html
│   ├── kommunikation/
│   │   └── index.html
│   └── wearables/
│       └── index.html
├── regional/                # Regional-Modul
│   ├── index.html
│   ├── 3-seen-vergleich.html
│   ├── almwirtschaft.html
│   ├── geschichte-jennerwein.html
│   ├── spitzingsee.html
│   └── tegernsee.html
└── fehlkauf-vermeidung/     # Fehlkauf-Modul
    ├── index.html
    ├── anfaengerfehler/
    │   └── index.html
    ├── preis-leistung/
    │   └── index.html
    └── qualitaetsmerkmale/
        └── index.html
```

---

## 4. ALPENAUSTAUSCH (Sektion 8)

```
/alpenaustausch/             # Community-Modul (Sektion 8)
└── index.html               # Hub: Teaser-Karten + Einreich-Formular

# Teaser auf Regional-Hubs:
# - /region/spitzingsee/ → Link zu /alpenaustausch/
# - /region/tegernsee/   → Link zu /alpenaustausch/
# - /region/valepp/      → Link zu /alpenaustausch/

# Datenstruktur pro Eintrag (statisch, HTML):
# [Titel] [Datum] [Schwierigkeit] [Highlight] [Eingereicht von]
# [Ausrüstungs-Check] optional, Affiliate
# Formular: mailto:alpenaustausch@alpen-experte.de (Template)
```

---

## 5. ASSETS (Design-System)

```
/css/
└── style.css                # Einziges CSS-File
    # NEUE Klassen (Marschbefehl 5):
    # .oepnv-anleitung       # ÖPNV-Standard-Block
    # .oepnv-vergleich       # Auto vs. ÖPNV Tabelle
    # .oepnv-affiliate-btn   # Bayern-Ticket Button
    # .alp-austausch-card    # Community-Eintrag Karte
    # .alp-austausch-grid    # Grid-Layout für Karten
    # .alp-austausch-form    # Einreich-Formular
    # .alp-austausch-meta    # Datum, Schwierigkeit
    # .alp-austausch-highlight
    # .alp-austausch-gear-check  # Ausrüstungs-Check

/fonts/
├── Inter-300.ttf
├── Inter-400.ttf
├── Inter-500.ttf
├── Inter-600.ttf
├── Inter-700.ttf
├── Playfair-400.ttf
├── Playfair-500.ttf
├── Playfair-600.ttf
└── Playfair-700.ttf

/images/
├── favicon.svg
├── logo.svg
├── hero-panorama.jpg + .svg
├── hutte-firstalm.jpg + .svg
├── hutte-jagahuettn.svg
├── featured-wanderstoecke.jpg + .svg
├── kaiserschmarrn.jpg + .svg
├── schweinsbraten.jpg + .svg
├── alpenkaese.jpg + .svg
├── rodelpiste.jpg + .svg
├── silo-*.jpg + .svg         # Alle Silo-Bilder

/js/
└── main.js                  # Einziges JS-File
```

---

## 6. LIVE-SEITEN (Root)

```
/ (root)
├── index.html               # Startseite
├── impressum.html           # Impressum
├── datenschutz.html         # Datenschutzerklärung
├── haftungsausschluss.html  # Haftungsausschluss
├── sitemap.xml              # Sitemap (SEO)
└── STRUKTUR_MAP.md          # Diese Datei (Architektur-Gesetz)
```

---

## 7. ARCHIV (Nicht konforme Dateien)

```
/archive/                    # Verschobene Dateien, die nicht in die Struktur passen
```

---

## 8. REGELN (Nicht verhandelbar)

1. **Keine neuen Hubs** ohne explizite Freigabe (nur Spitzingsee, Tegernsee, Schliersee, Valepp)
2. **Keine neuen Silos** ohne explizite Freigabe (nur Ausrüstung, Fauna, Sicherheit)
3. **Affiliate-Links** sind erlaubt in:
   - `/ausruestung/` Modul (Primär)
   - `oepnv-guide/` und ÖPNV-Blöcken auf Routenseiten (ÖPNV-Partner)
   - `alpenaustausch/` (Ausrüstungs-Check)
   - `is_active` Status als Kommentar in jeder Datei
4. **Keine .md-Dateien** im Content-Bereich — nur `.html` für Live-Seiten
5. **Keine Skripte (.ps1, .py)** im Root — gehören ins `/archive/` oder extern
6. **Keine Duplikate** — `content/huetten-karte/` archiviert (Original unter `content/huetten/huetten-karte/`)
7. **Jede Behauptung** muss Quellen-Status haben: "verifiziert" oder "Platzhalter"
8. **Cache-Buster** bei jeder Änderung inkrementieren (`?v=YYYY-MM-DD-N`)
9. **ÖPNV-Standard-Block** (`<section class="oepnv-anleitung">`) auf allen Routen-Seiten verpflichtend
10. **Alpenaustausch** ist Sektion 8 der Navigation, Position zwischen Sternenhimmel (7) und Praktisches (9)
