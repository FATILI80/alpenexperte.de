#!/usr/bin/env python3
"""Zustiege zu den Klettergebieten ab Oberer Firstalm (BRouter, Profil hiking-mountain).

Nutzt die Funktionen aus wander_firstalm.py. Eingabe: kletter_touren.json.
Ausgabe: routing/ergebnis_klettern.json und content/klettern/geojson/{Kennung}_klettern.geojson.
"strecke": true = nur hin (Rückweg mit Bus), sonst Runde Firstalm -> Ziel -> Firstalm.
Gefundene Orte stehen in der Ausgabe und müssen geprüft werden.
"""
import json
import wander_firstalm as wf

HIER = wf.HIER


def main():
    start = json.loads((HIER / "start.json").read_text(encoding="utf-8"))
    touren = json.loads((HIER / "kletter_touren.json").read_text(encoding="utf-8"))
    geo_dir = HIER.parent / "content" / "klettern" / "geojson"
    geo_dir.mkdir(parents=True, exist_ok=True)
    cache, ergebnisse = {}, []
    for t in touren:
        e = {"kennung": t["kennung"], "name": t["name"], "alt": t["alt"]}
        try:
            orte = [wf.geocode_region(o, cache) for o in t["wegpunkte"]]
            fehlend = [o for o, g in zip(t["wegpunkte"], orte) if g is None]
            if fehlend:
                e["fehler"] = f"Kein Treffer: {', '.join(fehlend)}"
                print(e["kennung"], e["fehler"]); ergebnisse.append(e); continue
            e["treffer"] = [g["treffer"] for g in orte]
            strecke = bool(t.get("strecke"))
            punkte = [start] + orte + ([] if strecke else [start])
            ziel = orte[-1] if strecke else start
            geo = wf.kette_brouter(punkte)
            m = wf.route.messen(geo, start, ziel)
            p = geo["features"][0].get("properties", {})
            m["hm_abstieg"] = round(m["hm_aufstieg"] - float(p.get("plain-ascend", 0) or 0))
            e["strecke"] = strecke
            e.update(m)
            (geo_dir / f"{t['kennung']}_klettern.geojson").write_text(json.dumps(geo, ensure_ascii=False), encoding="utf-8")
            print(f"{t['kennung']}: {m['laenge_km_brouter']} km · ↑{m['hm_aufstieg']} ↓{m['hm_abstieg']} Hm · Treffer: {' | '.join(e['treffer'])}")
        except Exception as ex:
            e["fehler"] = str(ex); print(f"{t['kennung']}: Fehler: {ex}")
        ergebnisse.append(e)
    (HIER / "ergebnis_klettern.json").write_text(json.dumps(ergebnisse, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
