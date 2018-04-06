import requests
from .parsers import parse_day_data, parse_dataframe, parse_forecast_data

__title__ = "knmi-py"
__version__ = "0.1.2"
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
        if not isinstance(start, str):
            end = end.strftime("%Y%m%d")
        params.update({"end": end})
    if inseason is True:
        params.update({"inseason": "Y"})
    if variables is None:
        variables = ['ALL']
    params.update({"vars": ":".join(variables)})

    r = requests.post(url=url, data=params)
    r.raise_for_status()

    return parse_day_data(raw=r.text)


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
    df.legend = legend
    df.stations = stations
    df.disclaimer = disclaimer

    return df


def get_forecast_dataframe(station=260):
    """
    Get 6 day forecast from KNMI as a Pandas DataFrame

    Parameters
    ----------
    station : int
        default 260 (De Bilt)
        No other stations supported right now

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
    return df
