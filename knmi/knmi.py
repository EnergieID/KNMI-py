import requests
from .parsers import parse_day_data, parse_dataframe, parse_forecast_data

__title__ = "knmi-py"
__version__ = "0.1.7"
__author__ = "EnergieID.be"
__license__ = "MIT"


def get_day_data_raw(stations, start=None, end=None, inseason=False, variables=None):
    """
    Get daily weather data from KNMI

    Parameters
    ----------
    stations : [int]
        list of KNMI station numbers
    start : datetime.datetime | str
        date (optional, default is begin of current month)
        can be a datetime object, or a string in format "%Y%m%d"
    end : datetime.datetime | str
        date (optional, default is today)
        can be a datetime object, or a string in format "%Y%m%d"
    inseason : bool (optional, default False)
        see http://www.knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script
        for the full explanation
    variables : list of variables to fetch (optional, default is ALL)
        WIND = DDVEC:FG:FHX:FHX:FX wind
        TEMP = TG:TN:TX:T10N temperatuur
        SUNR = SQ:SP:Q Zonneschijnduur en globale straling
        PRCP = DR:RH:EV24 neerslag en potentiële verdamping
        PRES = PG:PGX:PGN druk op zeeniveau
        VICL = VVN:VVX:NG zicht en bewolking
        MSTR = UG:UX:UN luchtvochtigheid

    Returns
    -------
    disclaimer, stations, legend, data
    """

    url = "http://projects.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi"
    params = {
        "stns": ":".join(str(station) for station in stations),
    }
    if start is not None:
        if not isinstance(start, str):
            start = start.strftime("%Y%m%d")
        params.update({"start": start})
    if end is not None:
        if not isinstance(end, str):
            end = end.strftime("%Y%m%d")
        params.update({"end": end})
    if inseason is True:
        params.update({"inseason": "Y"})
    if variables is None:
        variables = ['ALL']
    params.update({"vars": ":".join(variables)})

    r = requests.post(url=url, data=params)
    r.raise_for_status()

    disclaimer, stations, legend, data = parse_day_data(raw=r.text)
    return disclaimer, stations, legend, data


def get_day_data_dataframe(stations, start=None, end=None, inseason=False, variables=None):
    """
    Get daily weather data from KNMI as a Pandas DataFrame

    Parameters
    ----------
    stations : [int]
        list of KNMI station numbers
    start : datetime.datetime | str
        date (optional, default is begin of current month)
        can be a datetime object, or a string in format "%Y%m%d"
    end : datetime.datetime | str
        date (optional, default is today)
        can be a datetime object, or a string in format "%Y%m%d"
    inseason : bool (optional, default False)
        see http://www.knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script
        for the full explanation
    variables : list of variables to fetch (optional, default is ALL)
        WIND = DDVEC:FG:FHX:FHX:FX wind
        TEMP = TG:TN:TX:T10N temperatuur
        SUNR = SQ:SP:Q Zonneschijnduur en globale straling
        PRCP = DR:RH:EV24 neerslag en potentiële verdamping
        PRES = PG:PGX:PGN druk op zeeniveau
        VICL = VVN:VVX:NG zicht en bewolking
        MSTR = UG:UX:UN luchtvochtigheid

    Returns
    -------
    Pandas DataFrame
    """

    disclaimer, stations, legend, data = get_day_data_raw(stations=stations, start=start, end=end, inseason=inseason,
                                                          variables=variables)

    df = parse_dataframe(data=data)
    # df.legend = legend
    # df.stations = stations
    # df.disclaimer = disclaimer

    return df


def get_forecast_dataframe(station=260, conform_values=True, variables=None):
    """
    Get 6 day forecast from KNMI as a Pandas DataFrame

    Parameters
    ----------
    station : int
        default 260 (De Bilt)
        No other stations supported right now
    conform_values : bool
        add variables and transform the values so they align with the historical data from the API
    variables : [str]
        list of variables to return
        default returns all

    Returns
    -------
    Pandas DataFrame
    """
    if station != 260:
        raise NotImplementedError("Only station 260 (De Bilt) is supported for forecasts")

    url = 'http://www.knmi.nl/nederland-nu/weer/verwachtingen'

    r = requests.get(url)
    r.raise_for_status()

    df = parse_forecast_data(raw=r.content)

    if conform_values:
        df['STN'] = station
        df['RH'] = df['neerslag'].map(lambda x: float(x) if x > 0 else -1) * 10
        df['TX'] = df['temp_max'].astype(float) * 10
        df['TN'] = df['temp_min'].astype(float) * 10
        df['FG'] = df['windkracht'].map(beaufort_mapping) * 10
        df['DDVEC'] = df['windrichting'].map(winddir_mapping)
        df['SP'] = df['zonneschijn'].map(lambda x: int(x * 100))

    if variables is not None:
        vars = list(variables)
        if 'STN' in df.columns and 'STN' not in vars:
            vars.append('STN')
        df = df[vars]

    return df


# based on https://cdn.knmi.nl/system/downloads/files/000/000/011/original/beaufortschaal.pdf?1433938079
# maps the beaufort scale to approximate m/s
beaufort_mapping = {
    0: 0.1,  # 0 - 0.2
    1: 0.9,  # 0.3 - 1.5
    2: 2.45,  # 1.6 - 3.3
    3: 4.4,  # 3.4 - 5.4
    4: 6.7,  # 5.5 - 7.9
    5: 9.35,  # 8.0 - 10.7
    6: 12.3,  # 10.8 - 13.8
    7: 15.5,  # 13.9 - 17.1
    8: 18.95,  # 17.2 - 20.7
    9: 22.6,  # 20.8 - 24.4
    10: 26.45,  # 24.5 - 28.4
    11: 30.55,  # 28.5 - 32.6
    12: 34.0,  # > 32.6
}


# maps a wind direction (in Dutch) to an orientation according to the API
# note: North = 360, 0 indicates calm/variable
winddir_mapping = {
    'N': 360,
    'NO': 45,
    'O': 90,
    'ZO': 135,
    'Z': 180,
    'ZW': 225,
    'W': 270,
    'NW': 315
}
