import datetime as dt
import itertools
import re
from io import StringIO

import pandas as pd
from bs4 import BeautifulSoup

from .metadata import Station


def parse_day_data(raw: str):
    """
    Parse the raw csv-esque response of KNMI into relevant pieces.

    Parameters
    ----------
    raw
        raw csv text

    Returns
    -------
    disclaimer, stations, legend, header, data
    """
    lines = raw.splitlines()

    # Split the header and data
    csv_header = list(
        itertools.takewhile(
            lambda line: line.startswith("#") or line.startswith('"#'), lines
        )
    )
    data_numeric = "\n".join(lines[len(csv_header) :]).replace(" ", "")
    data_header = csv_header.pop(-1).replace("#", "").replace(" ", "")
    data = data_header + "\n" + data_numeric

    disclaimer = "\n".join(line.lstrip('"#').lstrip("# ") for line in lines[0:5])

    # parse the station list and legend
    stations = {}
    legend = {}
    try:
        start_station_line = [
            i for i, line in enumerate(csv_header) if line.startswith("# STN")
        ][0] + 1
        station_id_pattern = re.compile(r"# \d{3}")
    except IndexError:
        print("KNMI csv output format changed")
        pass  # Format changed
    else:
        i = 0
        for i, station_line in enumerate(
            itertools.takewhile(
                lambda line: station_id_pattern.match(line),
                csv_header[start_station_line:],
            )
        ):
            station_split = station_line.lstrip("#").split()
            try:
                num, long, lat, alt, *name_elements = station_split
            except ValueError:  # an invalid station was requested
                print("Station returned invalid results: ", station_split)
            else:
                stations[int(num)] = Station(
                    number=int(num),
                    longitude=float(long),
                    latitude=float(lat),
                    altitude=float(alt),
                    name=" ".join(name_elements),
                )
        end_station_line = i + start_station_line

        # parse the legend
        # the lines from which to retrieve the legend should be the remaining lines
        for legend_line in csv_header[end_station_line + 1 :]:
            key, *values = legend_line.lstrip("# ").split(":")
            legend[key.strip()] = ":".join(
                values
            )  # Need to re-join because ':' is used in URLs and such

    return disclaimer, stations, legend, data


def parse_forecast_data(raw):
    """
    Parse the raw html of KNMI forecast into relevant pieces.

    Parameters
    ----------
    raw : str

    Returns
    -------
    Pandas DataFrame
    """

    soup = BeautifulSoup(raw, "html.parser")
    forecast_list = soup.find("ul", {"class": "weather-map__table is-fullwidth"})

    forecasts = []
    for li in forecast_list.find_all("li"):
        spans = li.find_all("span")
        single_forecast = {
            "datum": dt.datetime.strptime(spans[0].text, "%d-%m-%Y").date(),
            "temp_max": int(re.search(r"(\d+)°", spans[2].text).groups()[0]),
            "temp_min": int(re.search(r"(\d+)°", spans[4].text).groups()[0]),
            "neerslag": int(re.search(r"(\d+)mm", spans[6].text).groups()[0]),
            "neerslagkans": int(spans[8].text.split()[1].replace("%", "")) / 100,
            "zonneschijn": int(spans[10].text.split()[1].replace("%", "")) / 100,
            "windrichting": spans[12].text.split()[1],
            "windkracht": int(spans[12].text.split()[-1]),
        }
        forecasts.append(single_forecast)

    df = pd.DataFrame(forecasts)

    df.datum = pd.DatetimeIndex(df.datum)
    df = df.set_index("datum")
    df.index.name = None
    df = df.tz_localize("Europe/Amsterdam")

    return df


def parse_dataframe(data):
    df = pd.read_csv(StringIO(data), index_col=1, converters={"YYYYMMDD": pd.Timestamp})
    df.index = pd.DatetimeIndex(df.index)
    df = df.tz_localize("Europe/Amsterdam")
    return df


def parse_hourly_dataframe(data) -> pd.DataFrame:
    df = pd.read_csv(StringIO(data), dtype={"YYYYMMDD": str, "HH": str})

    hour_column = (
        (df["HH"].astype(int) - 1).astype(str).str.zfill(2)
    )  # zero padded, and shifted to 0-23
    df["YYYYMMDD_HH"] = pd.to_datetime(df["YYYYMMDD"] + hour_column, format="%Y%m%d%H")
    df.drop(
        ["HH", "YYYYMMDD", "HH.1", "YYYYMMDD.1"], axis=1, inplace=True, errors="ignore"
    )  # remove duplicate columns
    df.set_index("YYYYMMDD_HH", inplace=True)
    return df
