import requests
from .parsers import parse_day_data, parse_dataframe

__title__ = "knmi-py"
__version__ = "0.1.0"
__author__ = "EnergieID.be"
__license__ = "MIT"


def get_day_data_raw(stations, start=None, end=None, inseason=False, variables=None):
    """
    Get daily weather data from KNMI

    Parameters
    ----------
    stations : list of KNMI station numbers
    start : date (optional, default is begin of current month)
    end : date (optional, default is today)
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
        params.update({"start": start.strftime("%Y%m%d")})
    if end is not None:
        params.update({"end": end.strftime("%Y%m%d")})
    if inseason is True:
        params.update({"inseason": "Y"})
    if variables is None:
        variables = ['ALL']
    params.update({"vars": ":".join(variables)})

    r = requests.post(url=url, data=params)
    if r.status_code != 200:
        raise requests.HTTPError(r.status_code, url, params)

    return parse_day_data(raw=r.text)


def get_day_data_dataframe(stations, start=None, end=None, inseason=False, variables=None):
    """
    Get daily weather data from KNMI as a Pandas DataFrame

    Parameters
    ----------
    stations : list of KNMI station numbers
    start : date (optional, default is begin of current month)
    end : date (optional, default is today)
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