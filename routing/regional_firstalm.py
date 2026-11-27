#!/usr/bin/env python3
"""R01–R50: Regionaltouren ab Oberer Firstalm als Rundfahrt rechnen (BRouter, gravel).

Jede Tour: Firstalm -> Wegpunkte (aus den bisherigen Tourentexten) -> Firstalm.
Voraussetzung: BRouter-Server läuft auf localhost:17777, Internet für Nominatim.
Ausgabe: routing/ergebnis_regional.json und content/gravel/geojson/R01_gravel.geojson ...
Gefundene Orte werden in der Tabelle mit ihrem Treffer angezeigt und müssen geprüft werden.
"""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

import route  # BROUTER-URL, messen(), PROFILE

HIER = Path(__file__).resolve().parent
NOMINATIM = "https://nominatim.openstreetmap.org/search"
UA = "alpenexperte-routing/1.0 (kontakt: Fatih)"
PROFIL = "gravel"


def geocode(ort, cache):
    if ort in cache:
        return cache[ort]
    q = urllib.parse.urlencode({"q": f"{ort}, Bayern", "format": "json", "limit": 1,
                                "countrycodes": "de,at"})
    req = urllib.request.Request(f"{NOMINATIM}?{q}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        treffer = json.loads(r.read().decode("utf-8"))
    time.sleep(1.1)  # Nominatim: max. 1 Anfrage/Sekunde
    if not treffer:
        cache[ort] = None
    else:
        t = treffer[0]
        cache[ort] = {"name": ort, "lat": float(t["lat"]), "lon": float(t["lon"]),
                      "treffer": t["display_name"]}
    return cache[ort]


def kette_brouter(punkte):
    lonlats = "|".join(f"{p['lon']},{p['lat']}" for p in punkte)
    q = urllib.parse.urlencode({"lonlats": lonlats, "profile": PROFIL, "format": "geojson"})
    with urllib.request.urlopen(f"{route.BROUTER}?{q}", timeout=300) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    start = json.loads((HIER / "start.json").read_text(encoding="utf-8"))
    touren = json.loads((HIER / "regional_touren.json").read_text(encoding="utf-8"))
    geo_dir = HIER.parent / "content" / "gravel" / "geojson"
    geo_dir.mkdir(parents=True, exist_ok=True)
    cache = {}
    ergebnisse = []
    for t in touren:
        eintrag = {"kennung": t["kennung"], "name": t["name"], "alt": t["alt"]}
        try:
            orte = [geocode(o, cache) for o in t["wegpunkte"]]
            fehlend = [o for o, g in zip(t["wegpunkte"], orte) if g is None]
            if fehlend:
                eintrag["fehler"] = f"kein Geocoding-Treffer: {', '.join(fehlend)}"
            else:
                eintrag["orte"] = [{"name": g["name"], "treffer": g["treffer"]} for g in orte]
                punkte = [start] + orte + [start]
                geo = kette_brouter(punkte)
                eintrag.update(route.messen(geo, start, start))
                (geo_dir / f"{t['kennung']}_gravel.geojson").write_text(
                    json.dumps(geo, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            eintrag["fehler"] = str(e)
        ergebnisse.append(eintrag)
        print(json.dumps(eintrag, ensure_ascii=False))
    (HIER / "ergebnis_regional.json").write_text(
        json.dumps(ergebnisse, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Fertig: routing/ergebnis_regional.json")


if __name__ == "__main__":
    main()
