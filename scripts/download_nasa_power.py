#!/usr/bin/env python3
"""Download daily NASA POWER point data for the Beni Mellal pilot and save a tidy CSV."""
from __future__ import annotations
import argparse
import csv
import json
import urllib.parse
import urllib.request
from datetime import datetime

API = "https://power.larc.nasa.gov/api/temporal/daily/point"

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="20150101", help="YYYYMMDD")
    p.add_argument("--end", default="20251231", help="YYYYMMDD")
    p.add_argument("--latitude", type=float, default=32.3373)
    p.add_argument("--longitude", type=float, default=-6.3498)
    p.add_argument("--output", default="nasasets/raw/nasa_power/nasa_power_beni_mellal_daily.csv")
    args = p.parse_args()
    datetime.strptime(args.start, "%Y%m%d")
    datetime.strptime(args.end, "%Y%m%d")
    params = {
        "parameters": "T2M,PRECTOTCORR,RH2M,ALLSKY_SFC_SW_DWN",
        "community": "AG",
        "longitude": args.longitude,
        "latitude": args.latitude,
        "start": args.start,
        "end": args.end,
        "format": "JSON",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "FIELD-SHIFT/1.0 data-acquisition"})
    with urllib.request.urlopen(req, timeout=120) as response:
        payload = json.load(response)
    properties = payload["properties"]
    parameter_data = properties["parameter"]
    dates = sorted(set().union(*(values.keys() for values in parameter_data.values())))
    import os
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "date", "latitude", "longitude",
            "air_temperature_2m_C", "precipitation_corrected_mm_day",
            "relative_humidity_2m_percent", "all_sky_surface_shortwave_radiation_MJ_m2_day"
        ])
        for day in dates:
            writer.writerow([
                f"{day[:4]}-{day[4:6]}-{day[6:8]}",
                args.latitude, args.longitude,
                parameter_data.get("T2M", {}).get(day),
                parameter_data.get("PRECTOTCORR", {}).get(day),
                parameter_data.get("RH2M", {}).get(day),
                parameter_data.get("ALLSKY_SFC_SW_DWN", {}).get(day),
            ])
    print(f"Wrote {len(dates)} daily rows to {args.output}")

if __name__ == "__main__":
    main()
