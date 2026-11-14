"""Reproducible timing and memory experiment for tariff calculations."""
import sys, time, tracemalloc, csv
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from tariff import calculate_energy_charge

sizes = [0, 100, 1000, 10000, 100000, 1000000]
rows = []
for n in sizes:
    reps = 20000
    start = time.perf_counter()
    for _ in range(reps):
        calculate_energy_charge(n)
    elapsed = time.perf_counter() - start
    tracemalloc.start()
    calculate_energy_charge(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    rows.append((n, reps, f"{elapsed:.6f}", current, peak))
out = Path(__file__).resolve().parent / "measurements.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["units_input", "repetitions", "elapsed_seconds", "current_bytes", "peak_bytes"])
    w.writerows(rows)
print("units,repetitions,seconds,current_bytes,peak_bytes")
for row in rows: print(",".join(map(str,row)))
