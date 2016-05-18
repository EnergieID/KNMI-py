import pandas as pd
from io import StringIO
from .metadata import Station

def parse_day_data(raw):
    """
    Parse the raw csv-esque response of KNMI into relevant pieces.

    Parameters
    ----------
    raw : str

    Returns
    -------
    disclaimer, stations, legend, header, data
    """
    # split the raw text in chunks
    chunks = chunk_splitter(raw=raw)

    # parse the disclaimer
    disclaimer = next(chunks)
    disclaimer = "\n".join(line.strip("# ") for line in disclaimer)  # strip away the prefix '# ' and rejoin the lines

    # parse the station list
    stations_raw = next(chunks)
    stations_raw = [line.strip("# ") for line in stations_raw]  # strip away the prefix '# '
    stations = {}
    for station in stations_raw[1:]:  # the first row is a header, so start from the second row
        # split by double spaces, because a single space can exist in a name
        # for each property, strip away spaces and colons
        station_split = [prop.strip().strip(":") for prop in station.split("  ") if prop != ""]
        try:
            num, long, lat, alt, name = station_split
        except ValueError:  # an invalid station was requested
            print("Station {} returned invalid results".format(station_split[0]))
        else:
            stations.update(
                {int(num): Station(number=int(num), longitude=float(long), latitude=float(lat), altitude=float(alt),
                                   name=name)}
            )

    # parse the legend
    legend_raw = next(chunks)
    # strip prefix '# ' and suffix '; '
    legend_raw = [entry.strip("# ").strip("; ") for entry in legend_raw]
    legend = {}
    for entry in legend_raw:
        sp = entry.split("=")
        # the key is the term before the first '='
        key = sp[0].strip()
        # the value is everthing that follows, so we rejoin everything with a '='
        value = "=".join(sp[1:]).strip()
        legend.update({key: value})

    # parse the header
    header = next(chunks)
    header = header[0]  # the header is only one line
    header = header.strip('# ').replace(' ', '')

    # parse the data
    data = next(chunks)
    lines = []
    for line in data:
        lines.append(line.strip('# ').replace(' ', ''))

    # join data and header
    lines.insert(0, header)

    data = "\n".join(lines)

    return disclaimer, stations, legend, data


def parse_dataframe(data):
    df = pd.read_csv(StringIO(data), index_col=1, converters={'YYYYMMDD': pd.Timestamp})
    df.index = pd.DatetimeIndex(df.index)
    df = df.tz_localize('Europe/Amsterdam')

    return df


def chunk_splitter(raw):
    """
    Generator to read a raw file and yield chunks that are separated by 'empty lines': "# "

    Parameters
    ----------
    raw : str

    Yields
    -------
    str
    """
    chunk = []
    for line in raw.splitlines():
        if line == "# ":
            if len(chunk) == 0:
                continue
            else:
                yield chunk
                chunk = []
        else:
            chunk.append(line)
    else:
        yield chunk
