# Fuel Oil Tank Interpolation

A Python project for calculating fuel oil tank volumes through interpolation. Given a measured value (such as sounding level), the application interpolates between known tank calibration (table) data points to estimate the corresponding volume.

## Table of Contents

- [About the Project](#about-the-project)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## About the Project

Fuel oil tanks are usually supplied with a calibration table (tank table) that lists volumes only at specific levels. Real measurements rarely fall exactly on those listed values, so the in-between volume has to be estimated.

This project solves that by applying linear interpolation on the tank table data:

1. Load the tank calibration table (level vs. volume).
2. Find the two table entries that surround the measured level.
3. Interpolate to get the estimated volume at the measured level.

The project is written in **Python** and uses **pandas** for handling table data and **numpy** for numerical computation.

## Requirements

- Python 3.8 or newer
- pip (Python package installer)
- Python packages:
  - `pandas`
  - `numpy`

## Installation

Follow these steps to set up the project on your machine.

### 1. Make sure Python and pip are installed

Check your versions:

```bash
python --version
pip --version
```

If either command is not found, install Python from [python.org](https://www.python.org/downloads/) (pip is included).

### 2. Get the project files

Clone the repository or download and extract the project folder:

```bash
git clone https://github.com/GeElshaddai/py_fot_interpolation.git
```

Then, cd into the directiory:

```bash
cd py_fot_interpolation
```

### 3. (Recommended) Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- Windows:
  ```bash
  venv\Scripts\activate
  ```
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install the dependencies

Install the packages in `requirements.txt` directly with pip:

```bash
pip install -r requirements.txt
```

### 5. Verify the installation

```bash
python -c "import pandas, numpy; print('Installation OK')"
```

If you see `Installation OK`, you are ready to go.

## Usage

### 1. Prepare your tank table

Create a CSV file containing your tank calibration data, with one column for the level and one for the volume. CSV file name should exactly be `tank_table.csv`:

> Note: The header row should exactly be `level`, `percent`, `volume_cm`, and `volume_t`.

```csv
level,percent,volume_cm,volume_t
0,0,0.0,0.0
10,20,12.5,12.0
20,40,28.0,27.5
30,60,46.5,46.0
40,80,67.0,66.5
50,100,90.0,89.5
```

`volume_cm` means volume in cubic metre.
While `volume_t` means volume in tonne.

> Note: The level column must be sorted in ascending order, and column names should match what the application expects.

### 2. Run the application

```bash
python fot_interpolation.py
```

> Note: This way will ask you the measured level.

Or you can directly provide the measured level, for example `25`:

```bash
python fot_interpolation.py 25
```

### 3. Enter your measurement

When prompted, provide the measured level. The application then looks up the surrounding table values, interpolates, and prints the estimated volume.

## Example

Using the sample table above, suppose the measured level is `25`:

- Lower point: level `20` → volume `28.0`
- Upper point: level `30` → volume `46.5`

Linear interpolation formula:

```
V = V1 + (L - L1) * (V2 - V1) / (L2 - L1)
```

Calculation:

```
V = 28.0 + (25 - 20) * (46.5 - 28.0) / (30 - 20)
V = 28.0 + 5 * 18.5 / 10
V = 37.25
```

Estimated volume: **37.25**

## Troubleshooting

| Problem                                         | Possible cause                                  | Solution                                                               |
| ----------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'pandas'` | Dependencies not installed                      | Run `pip install pandas numpy`                                         |
| `FileNotFoundError`                             | Tank table file not found                       | Check the file name and path                                           |
| Unexpected or incorrect volume                  | Table not sorted or measured value out of range | Sort the level column ascending and keep inputs within the table range |
| `pip` command not recognized                    | pip not on PATH                                 | Use `python -m pip install pandas numpy`                               |

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
