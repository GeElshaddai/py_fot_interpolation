import sys

import numpy as np
import pandas as pd

CSV_PATH = "tank_table.csv"

df = pd.read_csv(CSV_PATH, skipinitialspace=True)
df.columns = df.columns.str.strip()
df = df.sort_values("level").reset_index(drop=True)

sounding_level = df["level"].to_numpy(dtype=float)
l_min = float(sounding_level.min())
l_max = float(sounding_level.max())


def parse(token: str) -> float:
    return float(token.strip().replace(",", "."))


def main() -> None:
    args = sys.argv[1:]
    if not args:
        args = input(f"Sounding level between ({l_min} - {l_max}): ").split()

    try:
        values = [parse(a) for a in args]
    except ValueError:
        sys.exit("Error: Sounding result must be a number, e.g. 0.34")

    bad = [v for v in values if not (l_min <= v <= l_max)]
    if bad:
        sys.exit(f"Error: {bad} is outside the table range {l_min} - {l_max}")

    readings = pd.DataFrame({"level": values})
    for col in ("percent", "volume_cm", "volume_t"):
        readings[col] = np.interp(readings["level"], df["level"], df[col])

    print(readings.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
