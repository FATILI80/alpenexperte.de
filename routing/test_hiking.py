#!/usr/bin/env python3
"""Test: Wander-Profil hiking-mountain an einer bekannten Strecke.

Strecke: Obere Firstalm -> Spitzingsee -> Rotwandhaus -> Obere Firstalm
Vergleich: gleiche Strecke mit gravel (Rad) und hiking-mountain (Wandern).
Voraussetzung: BRouter-Server läuft auf localhost:17777, Internet für Nominatim.
"""
import json
import urllib.parse
import urllib.request
from pathlib import Path

import route
import regional_firstalm as rf

HIER = Path(__file__).resolve().parent
PUNKTE = ["Spitzingsee", "Rotwandhaus"]
PROFILE = ["hiking-mountain", "gravel"]


def kette(punkte, profil):
    lonlats = "|".join(f"{p['lon']},{p['lat']}" for p in punkte)
    q = urllib.parse.urlencode({"lonlats": lonlats, "profile": profil, "format": "geojson"})
    with urllib.request.urlopen(f"{route.BROUTER}?{q}", timeout=300) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    start = json.loads((HIER / "start.json").read_text(encoding="utf-8"))
    cache = {}
    orte = []
    for o in PUNKTE:
        g = rf.geocode(o, cache)
        if g is None:
            print(f"Kein Geocoding-Treffer für {o}")
            return
        orte.append(g)
        print(f"{o}: {g['treffer']} ({g['lat']:.5f}, {g['lon']:.5f})")
    punkte = [start] + orte + [start]
    for profil in PROFILE:
        try:
            geo = kette(punkte, profil)
            m = route.messen(geo, start, start)
            print(f"{profil}: {m['laenge_km_brouter']} km · {m['hm_aufstieg']} Hm "
                  f"(Start-Abweichung {m['start_abweichung_m']} m)")
            (HIER.parent / "content" / "gravel" / "geojson" / f"TEST_{profil}.geojson").write_text(
                json.dumps(geo, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            print(f"{profil}: Fehler: {e}")


if __name__ == "__main__":
    main()
