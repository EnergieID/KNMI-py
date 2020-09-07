# KNMI-py
Python wrapper to fetch and parse observations from KNMI,
either as csv or Pandas DataFrame

See http://knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script

Note: This library is not affiliated in any way with KNMI, it only uses the KNMI API to request data.

Currently only daily data is implemented.

## Installation
KNMI-py is available via pip.

`python -m pip install knmi-py`

## 2 Functions
- `knmi.get_day_data_raw(stations, start, end, inseason, variables)`
- `knmi.get_day_data_dataframe(stations, start, end, inseason, variables)`

## Metadata
Don't know which station number you need, or what the variables mean?
We got you covered:

- `knmi.stations` provides a list of all available stations
- `knmi.variables` provides a list of all variables and explanations

## Metadata included in DataFrame
All raw data is included as argument to the DataFrame
(however, the data is lost once you start manipulating the frame, so you'll have to copy it)

# Example

```python
import knmi
df = knmi.get_day_data_dataframe(stations=[260])
print(df.disclaimer)
print(df.stations)
print(df.legend)
df = df.rename(columns=df.legend)
print(df)
```

## Disclaimer

The KNMI-py Python library is not affiliated, created or maintained by KNMI. It merely uses the KNMI API to request data.