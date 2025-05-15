# KNMI-py

[![PyPI version](https://badge.fury.io/py/knmi-py.svg)](https://badge.fury.io/py/knmi-py)
<!-- Optional: Add a GitHub Actions build status badge once CI is set up -->
<!-- [![Build Status](https://github.com/EnergieID/KNMI-py/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/EnergieID/KNMI-py/actions/workflows/pypi-publish.yml) -->

Python wrapper to fetch and parse daily and hourly weather observations from KNMI,
either as raw text, CSV-like strings, or Pandas DataFrames.

See the official KNMI documentation for more details on data retrieval via scripts:
[KNMI Kennis- en datacentrum - Data ophalen vanuit een script](http://knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script)

*Note: This library is not affiliated in any way with KNMI; it only utilizes the KNMI API to request data.*

## Installation

KNMI-py is available via pip:

```bash
python -m pip install knmi-py
```

## Key Functions

The library provides functions to retrieve both daily and hourly weather data:

- `knmi.get_day_data_raw(stations, start, end, inseason, variables)`
- `knmi.get_day_data_dataframe(stations, start, end, inseason, variables)`
- `knmi.get_hour_data_raw(stations, start, end, inseason, variables)`
- `knmi.get_hour_data_dataframe(stations, start, end, inseason, variables)`
- `knmi.get_forecast_dataframe(station, conform_values, variables)` (Limited to De Bilt, station 260)

## Metadata

Need to find a station number or understand what the weather variable abbreviations mean?

- `knmi.stations`: A dictionary of all available KNMI weather stations.
- `knmi.variables`: A dictionary providing explanations for weather variable codes.

## Example Usage

```python
import knmi
import pandas as pd

# Get daily data for De Bilt (station 260) for a specific period
daily_df = knmi.get_day_data_dataframe(
    stations=,
    start='2023-01-01',
    end='2023-01-31'
)
print("Daily Data:")
print(daily_df.head())

# Get hourly data for Schiphol (station 240) for a specific day
# Note: start and end for hourly data are strings like "YYYYMMDDHH"
hourly_df = knmi.get_hour_data_dataframe(
    stations=,
    start="2023032801", # March 28, 2023, 01:00
    end="2023032824"    # March 28, 2023, 24:00
)
print("\nHourly Data:")
print(hourly_df.head())
```

## Disclaimer

The KNMI-py Python library is not affiliated with, created by, or maintained by KNMI. It merely uses the publicly available KNMI API to request data.

## Contributing & Development

Contributions are welcome! Please feel free to open an issue or submit a pull request.

This project uses modern Python development tools:
- **Packaging:** `pyproject.toml` (with `hatchling` as the build backend).
- **Dependency Management & Task Running:** `uv` is used for fast dependency management.
- **Linting & Formatting:** `Ruff` (configured via `pyproject.toml` or `ruff.toml`).
- **Pre-commit Hooks:** Used to ensure code quality and consistency before commits.
- **Testing:** `pytest` for running tests.
- **Multi-version Testing:** `tox` (with `tox-uv`) is used to ensure compatibility across multiple Python versions (currently Python 3.9+). Run `tox` to execute tests in all configured environments.

Please ensure pre-commit hooks pass and tests succeed before submitting a pull request.
