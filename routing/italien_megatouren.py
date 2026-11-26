#!/usr/bin/env python3
"""GG-IT-01 bis GG-IT-04: Zwischenpunkte geocodieren, per BRouter (gravel) routen.

Voraussetzung: BRouter-Server läuft auf localhost:17777, Internet für Nominatim.
Ausgabe: routing/ergebnis_italien.json, Geometrie in content/gravel/geojson/GG-IT-0X_gravel.geojson
Hinweis: Für Bologna, Florenz und Rom reicht die Kachel E10_N45 nicht aus; die Kachel E10_N40
muss in C:\\brouter\\segments4 liegen, sonst schlägt die Berechnung dieser Touren fehl.
"""
import json
import math
import time
import urllib.parse
import urllib.request
from pathlib import Path

import route  # brouter(), haversine_m()

HIER = Path(__file__).resolve().parent
GEO_DIR = HIER.parent / "content" / "gravel" / "geojson"
NOMINATIM = "https://nominatim.openstreetmap.org/search"
UA = "alpenexperte-routing/1.0 (kontakt: Fatih)"

START = {"name": "Obere Firstalm", "lat": 47.6701, "lon": 11.8540}

TOUREN = [
    ("GG-IT-01", "Transalp Venedig", ["Achenpass", "Brenner", "Sterzing", "Brixen", "Bruneck", "Toblach", "Cortina d'Ampezzo", "Belluno", "Venedig Markusplatz"]),
    ("GG-IT-02", "Transalp Gardasee & Verona", ["Brenner", "Bozen", "Trient", "Verona Arena"]),
    ("GG-IT-03", "Via Claudia Augusta bis Ostiglia", ["Telfs", "Landeck", "Reschenpass", "Mals", "Meran", "Bozen", "Mantua", "Ostiglia"]),
    ("GG-IT-04", "Ciclovia del Sole bis Rom", ["Brenner", "Verona Arena", "Bologna", "Florenz Dom", "Rom Kolosseum"]),
]


def geocode(anfrage):
    q = urllib.parse.urlencode({"q": anfrage + ", Italien OR Österreich OR Deutschland", "format": "json", "limit": 1})
    req = urllib.request.Request(f"{NOMINATIM}?{q}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        t = json.loads(r.read().decode("utf-8"))
    time.sleep(1.1)
    if not t:
        raise ValueError(f"kein Treffer: {anfrage}")
    return {"lat": float(t[0]["lat"]), "lon": float(t[0]["lon"]), "treffer": t[0]["display_name"]}


def lonlats(punkte):
    return "|".join(f"{p['lon']},{p['lat']}" for p in punkte)


def brouter_kette(punkte):
    q = urllib.parse.urlencode({"lonlats": lonlats(punkte), "profile": "gravel", "format": "geojson"})
    with urllib.request.urlopen(f"{route.BROUTER}?{q}", timeout=900) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ergebnisse = []
    GEO_DIR.mkdir(parents=True, exist_ok=True)
    for kennung, name, zwischen in TOUREN:
        try:
            punkte = [START]
            for z in zwischen:
                ort = geocode(z)
                ort["name"] = z
                punkte.append(ort)
            geo = brouter_kette(punkte)
            feat = geo["features"][0]
            koords = feat["geometry"]["coordinates"]
            props = feat.get("properties", {})
            summe = sum(route.haversine_m(a[1], a[0], b[1], b[0]) for a, b in zip(koords, koords[1:]))
            eintrag = {
                "kennung": kennung, "name": name,
                "zwischenpunkte": [{"name": p["name"], "treffer": p.get("treffer")} for p in punkte[1:]],
                "laenge_km_brouter": round(float(props.get("track-length", 0)) / 1000, 2),
                "laenge_km_geometrie": round(summe / 1000, 2),
                "hm_aufstieg": round(float(props.get("filtered ascend", 0) or 0)),
            }
            (GEO_DIR / f"{kennung}_gravel.geojson").write_text(json.dumps(geo, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            eintrag = {"kennung": kennung, "name": name, "fehler": str(e)}
        print(json.dumps(eintrag, ensure_ascii=False), flush=True)
        ergebnisse.append(eintrag)
    (HIER / "ergebnis_italien.json").write_text(json.dumps(ergebnisse, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Fertig: routing/ergebnis_italien.json", flush=True)


if __name__ == "__main__":
    main()
