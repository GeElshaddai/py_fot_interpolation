import sys

import numpy as np
import pandas as pd

CSV_PATH = "fot_main.csv"

df = pd.read_csv(CSV_PATH, skipinitialspace=True)
df.columns = df.columns.str.strip()
df = df.sort_values("sounding_m").reset_index(drop=True)
df["percent"] = df["percent"] / 100

s_min, s_max = df["sounding_m"].min(), df["sounding_m"].max()


def parse(token: str) -> float:
    return float(token.strip().replace(",", "."))


def main() -> None:
    args = sys.argv[1:]
    if not args:
        args = input(f"Sounding result in m ({s_min} - {s_max}): ").split()

    try:
        values = [parse(a) for a in args]
    except ValueError:
        sys.exit("Error: Sounding result must be a number, e.g. 0.34")

    bad = [v for v in values if not (s_min <= v <= s_max)]
    if bad:
        sys.exit(f"Error: {bad} is outside the table range {s_min} - {s_max}")

    readings = pd.DataFrame({"sounding_m": values})
    for col in ("percent", "capacity_cm", "capacity_t"):
        readings[col] = np.interp(readings["sounding_m"], df["sounding_m"], df[col])

    print(readings.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
