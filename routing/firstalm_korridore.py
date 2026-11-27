#!/usr/bin/env python3
"""F01–F20 ab Oberer Firstalm: Ziele geocodieren (Nominatim), per BRouter messen.

Voraussetzung: BRouter-Server läuft auf localhost:17777, Internet für Nominatim.
Ausgabe: routing/ergebnis_firstalm.json und eine Tabelle zum Prüfen der Trefferorte.
Die Geocoding-Treffer MÜSSEN gegen den angezeigten Ort geprüft werden.
"""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

import route  # nutzt brouter(), messen() aus route.py

HIER = Path(__file__).resolve().parent
NOMINATIM = "https://nominatim.openstreetmap.org/search"
UA = "alpenexperte-routing/1.0 (kontakt: Fatih)"

KORRIDORE = [
    ("F01", "München Isartor", "Isartor, München"),
    ("F02", "Schliersee Bahnhof", "Bahnhof Schliersee"),
    ("F03", "Fischhausen-Neuhaus Bahnhof", "Bahnhof Fischhausen-Neuhaus"),
    ("F04", "Tegernsee Bahnhof", "Bahnhof Tegernsee"),
    ("F05", "Rottach-Egern", "Rottach-Egern"),
    ("F06", "Kreuth", "Kreuth, Oberbayern"),
    ("F07", "Achenpass", "Achenpass"),
    ("F09", "Elendsattel", "Elendsattel"),
    ("F10", "Vorderthiersee", "Vorderthiersee"),
    ("F11", "Thiersee", "Thiersee"),
    ("F12", "Kufstein Bahnhof", "Bahnhof Kufstein"),
    ("F13", "Walchsee", "Walchsee"),
    ("F14", "Bayrischzell Bahnhof", "Bahnhof Bayrischzell"),
    ("F15", "Sudelfeld", "Sudelfeld"),
    ("F16", "Oberaudorf Bahnhof", "Bahnhof Oberaudorf"),
    ("F17", "Fischbachau", "Fischbachau"),
    ("F18", "Miesbach Bahnhof", "Bahnhof Miesbach"),
    ("F19", "Holzkirchen Bahnhof", "Bahnhof Holzkirchen"),
    ("F20", "Ellmau", "Ellmau, Tirol"),
]


def geocode(anfrage):
    q = urllib.parse.urlencode({"q": anfrage, "format": "json", "limit": 1, "countrycodes": "de,at,it"})
    req = urllib.request.Request(f"{NOMINATIM}?{q}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        treffer = json.loads(r.read().decode("utf-8"))
    time.sleep(1.1)  # Nominatim-Richtlinie: max. 1 Anfrage/Sekunde
    if not treffer:
        return None
    t = treffer[0]
    return {"lat": float(t["lat"]), "lon": float(t["lon"]), "treffer": t["display_name"]}


def main():
    start = json.loads((HIER / "start.json").read_text(encoding="utf-8"))
    ergebnisse = []
    for kennung, name, anfrage in KORRIDORE:
        try:
            ziel = geocode(anfrage)
            if ziel is None:
                eintrag = {"kennung": kennung, "ziel": name, "fehler": "kein Geocoding-Treffer"}
            else:
                eintrag = {"kennung": kennung, "ziel": name, "geocoding": ziel}
                ziel_obj = {"name": name, **ziel}
                for profil in route.PROFILE:
                    geo = route.brouter(start, ziel_obj, profil)
                    eintrag[profil] = route.messen(geo, start, ziel_obj)
                    # Geometrie für die Karte speichern (Leaflet lädt diese Datei)
                    geo_dir = HIER / "geojson"
                    geo_dir.mkdir(exist_ok=True)
                    (geo_dir / f"{kennung}_{profil}.geojson").write_text(
                        json.dumps(geo, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            eintrag = {"kennung": kennung, "ziel": name, "fehler": str(e)}
        print(json.dumps(eintrag, ensure_ascii=False), flush=True)
        ergebnisse.append(eintrag)

    (HIER / "ergebnis_firstalm.json").write_text(json.dumps(ergebnisse, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Fertig: routing/ergebnis_firstalm.json", flush=True)


if __name__ == "__main__":
    main()
