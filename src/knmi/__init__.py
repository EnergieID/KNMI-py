from .knmi import (
    get_day_data_dataframe,
    get_day_data_raw,
    get_forecast_dataframe,
    get_hour_data_dataframe,
    get_hour_data_raw,
)
from . import metadata as knmi_own_metadata_module
from importlib import metadata as _stdlib_metadata


stations = knmi_own_metadata_module.stations
variables = knmi_own_metadata_module.variables

try:
    __version__ = _stdlib_metadata.version("knmi-py")
except _stdlib_metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"

__all__ = [
    "__version__",
    "get_day_data_dataframe",
    "get_day_data_raw",
    "get_forecast_dataframe",
    "get_hour_data_dataframe",
    "get_hour_data_raw",
    "stations",
    "variables",
]
