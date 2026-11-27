#!/usr/bin/env python3
"""MTB-Touren ab Oberer Firstalm als Rundtour rechnen (BRouter, Profil mtb).

Jede Tour: Firstalm -> Wegpunkte (mtb_touren.json) -> Firstalm.
Voraussetzung: BRouter-Server läuft auf localhost:17777, Internet für Nominatim.
Koordinaten "lat,lon" werden direkt verwendet, Ortsnamen über Nominatim geocodiert.
Ausgabe: routing/ergebnis_mtb.json und content/wandern/geojson/{Kennung}_mtb.geojson
Gefundene Orte stehen in der Ausgabe und müssen geprüft werden.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

import route
import regional_firstalm as rf

HIER = Path(__file__).resolve().parent
PROFIL = "mtb"


# Suche nur im Gebiet Mangfallgebirge/Tegernsee/Spitzing/Bayrischzell (lon 11.55–12.05, lat 47.55–47.78),
# sonst trifft Nominatim gleichnamige Orte in ganz Bayern (z. B. Buchstein bei Bayreuth).
VIEWBOX = "11.45,47.80,12.20,47.48"


def geocode_region(ort, cache):
    if re.match(r"^\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*$", ort):
        return rf.geocode(ort, cache)
    if ort in cache:
        return cache[ort]
    q = urllib.parse.urlencode({"q": ort, "format": "json", "limit": 1, "countrycodes": "de,at",
                                "viewbox": VIEWBOX, "bounded": 1})
    req = urllib.request.Request(f"{rf.NOMINATIM}?{q}", headers={"User-Agent": rf.UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        treffer = json.loads(r.read().decode("utf-8"))
    time.sleep(1.1)
    if not treffer:
        cache[ort] = None
    else:
        t = treffer[0]
        cache[ort] = {"name": ort, "lat": float(t["lat"]), "lon": float(t["lon"]), "treffer": t["display_name"]}
    return cache[ort]


def kette_brouter(punkte):
    lonlats = "|".join(f"{p['lon']},{p['lat']}" for p in punkte)
    q = urllib.parse.urlencode({"lonlats": lonlats, "profile": PROFIL, "format": "geojson"})
    with urllib.request.urlopen(f"{route.BROUTER}?{q}", timeout=300) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    start = json.loads((HIER / "start.json").read_text(encoding="utf-8"))
    touren = json.loads((HIER / "mtb_touren.json").read_text(encoding="utf-8"))
    geo_dir = HIER.parent / "content" / "mtb" / "geojson"
    geo_dir.mkdir(parents=True, exist_ok=True)
    cache = {}
    ergebnisse = []
    for t in touren:
        eintrag = {"kennung": t["kennung"], "name": t["name"], "alt": t["alt"]}
        try:
            orte = [geocode_region(o, cache) for o in t["wegpunkte"]]
            fehlend = [o for o, g in zip(t["wegpunkte"], orte) if g is None]
            if fehlend:
                eintrag["fehler"] = f"Kein Treffer: {', '.join(fehlend)}"
                ergebnisse.append(eintrag)
                print(eintrag["kennung"], eintrag["fehler"])
                continue
            eintrag["treffer"] = [g["treffer"] for g in orte]
            strecke = bool(t.get("strecke"))
            punkte = [start] + orte + ([] if strecke else [start])
            ziel = orte[-1] if strecke else start
            geo = kette_brouter(punkte)
            m = route.messen(geo, start, ziel)
            p = geo["features"][0].get("properties", {})
            netto = float(p.get("plain-ascend", 0) or 0)
            m["hm_abstieg"] = round(m["hm_aufstieg"] - netto)
            eintrag["strecke"] = strecke
            eintrag.update(m)
            (geo_dir / f"{t['kennung']}_mtb.geojson").write_text(
                json.dumps(geo, ensure_ascii=False), encoding="utf-8")
            print(f"{t['kennung']}: {m['laenge_km_brouter']} km · ↑{m['hm_aufstieg']} ↓{m['hm_abstieg']} Hm "
                  f"(Start-Abweichung {m['start_abweichung_m']} m)")
        except Exception as e:
            eintrag["fehler"] = str(e)
            print(f"{t['kennung']}: Fehler: {e}")
        ergebnisse.append(eintrag)
    (HIER / "ergebnis_mtb.json").write_text(
        json.dumps(ergebnisse, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
