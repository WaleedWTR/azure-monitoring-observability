#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_service_metrics.csv"

def load():
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def calculate(rows):
    total_requests = sum(int(r["requests"]) for r in rows)
    total_errors = sum(int(r["errors"]) for r in rows)
    available_intervals = sum(r["available"].lower() == "true" for r in rows)
    return {
        "availability_pct": round(available_intervals / len(rows) * 100, 2),
        "error_rate_pct": round(total_errors / total_requests * 100, 2),
        "average_latency_ms": round(
            sum(float(r["latency_ms"]) for r in rows) / len(rows), 1
        ),
        "total_requests": total_requests,
    }

if __name__ == "__main__":
    for key, value in calculate(load()).items():
        print(f"{key}: {value}")
