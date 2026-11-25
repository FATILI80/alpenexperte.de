#!/usr/bin/env python3
"""BRouter-Lauf: Strecken von der Oberen Firstalm zu den Zielen.

Voraussetzung: BRouter-Server läuft auf localhost:17777.
Ergebnis: routing/ergebnis.json (Länge, Höhenmeter, Prüfung je Strecke).
"""
import json
import math
import urllib.parse
import urllib.request
from pathlib import Path

HIER = Path(__file__).resolve().parent
BROUTER = "http://localhost:17777/brouter"
MIN_KM = 50.0          # Gravel-Touren: mindestens 50 km
START_TOL_M = 200      # Start darf höchstens 200 m vom Ausgangspunkt liegen
ZIEL_TOL_M = 500       # Ziel darf höchstens 500 m vom Zielpunkt liegen
PROFILE = ["gravel", "trekking"]


def haversine_m(lat1, lon1, lat2, lon2):
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def brouter(start, ziel, profil):
    lonlats = f"{start['lon']},{start['lat']}|{ziel['lon']},{ziel['lat']}"
    q = urllib.parse.urlencode({"lonlats": lonlats, "profile": profil, "format": "geojson"})
    with urllib.request.urlopen(f"{BROUTER}?{q}", timeout=300) as r:
        return json.loads(r.read().decode("utf-8"))


def messen(geo, start, ziel):
    feat = geo["features"][0]
    koords = feat["geometry"]["coordinates"]  # [lon, lat, ele]
    props = feat.get("properties", {})

    summe_m = 0.0
    for a, b in zip(koords, koords[1:]):
        summe_m += haversine_m(a[1], a[0], b[1], b[0])

    start_abw = haversine_m(koords[0][1], koords[0][0], start["lat"], start["lon"])
    ziel_abw = haversine_m(koords[-1][1], koords[-1][0], ziel["lat"], ziel["lon"])

    laenge_brouter_km = float(props.get("track-length", 0) or 0) / 1000
    hm = float(props.get("filtered ascend", 0) or 0)

    return {
        "laenge_km_brouter": round(laenge_brouter_km, 2),
        "laenge_km_geometrie": round(summe_m / 1000, 2),
        "hm_aufstieg": round(hm),
        "start_abweichung_m": round(start_abw),
        "ziel_abweichung_m": round(ziel_abw),
    }


def pruefen(m):
    fehler = []
    if m["laenge_km_brouter"] < MIN_KM:
        fehler.append(f"Länge {m['laenge_km_brouter']} km unter {MIN_KM} km")
    if m["start_abweichung_m"] > START_TOL_M:
        fehler.append(f"Start {m['start_abweichung_m']} m vom Ausgangspunkt")
    if m["ziel_abweichung_m"] > ZIEL_TOL_M:
        fehler.append(f"Ziel {m['ziel_abweichung_m']} m vom Zielpunkt")
    return {"bestanden": not fehler, "fehler": fehler}


def main():
    start = json.loads((HIER / "start.json").read_text(encoding="utf-8"))
    ziele = json.loads((HIER / "ziele.json").read_text(encoding="utf-8"))

    ergebnisse = []
    for ziel in ziele:
        for profil in PROFILE:
            print(f"Routing {ziel['name']} ({profil}) ...", flush=True)
            try:
                geo = brouter(start, ziel, profil)
                m = messen(geo, start, ziel)
                p = pruefen(m)
                eintrag = {"ziel": ziel["name"], "profil": profil, "messung": m, "pruefung": p}
            except Exception as e:  # Netzwerk-/Serverfehler sichtbar machen
                eintrag = {"ziel": ziel["name"], "profil": profil, "fehler": str(e)}
            print(json.dumps(eintrag, ensure_ascii=False), flush=True)
            ergebnisse.append(eintrag)

    (HIER / "ergebnis.json").write_text(
        json.dumps(ergebnisse, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Fertig: routing/ergebnis.json", flush=True)


if __name__ == "__main__":
    main()
