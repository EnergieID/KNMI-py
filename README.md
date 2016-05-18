# KNMI-py
Python wrapper to fetch and parse observations from KNMI,
either as csv or Pandas DataFrame

See http://knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script

Currently only daily data is implemented.

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
- `df = knmi.get_day_data_dataframe(stations=[260])`
- `print(df.disclaimer)`
- `print(df.stations)`
- `print(df.legend)`
- `df.rename(columns=df.legend)`

