# Architektur- und Strukturbericht – alpenexperte.de

**Datum:** 11. November 2026  
**Status:** Audit (Phase 1)

## 1. Verzeichnisstruktur
* `/content/`: Enthält die thematischen Fachsilos:
  * `wandern/`, `klettern/`, `mtb/`, `winter/`, `skigebiete/`, `nordic-walking/`
  * `huetten/`, `praxis/`, `regional/`
  * `fauna/`, `botanik/`, `geologie/`, `meteorologie/`, `moore/`, `forstwirtschaft/`, `almwirtschaft/`, `sternenhimmel/`, `almkultur/`
* `/css/`: Design-System (`style.css`, `homepage-v3.css`).
* `/js/`: Client-Side Logik (`main.js`, Karten-Integrationen).
* `/images/`: Optimierte Bild-Assets mit korrekten Alt-Texten.
* `/data/`: Dynamische Produktdaten (`products.json`).
* `/.github/workflows/`: CI/CD Workflows (`update-webgains-feed.yml` mit robustem Fallback).

## 2. Routing & Vercel
* Vercel verarbeitet statische HTML-Seiten direkt.
* Trailing-Slash- und Clean-URL-Regeln sind in `vercel.json` definiert.
