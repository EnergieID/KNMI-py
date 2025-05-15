import os
import pandas as pd
import pytest
from knmi import knmi
from knmi import stations, variables, __version__


@pytest.fixture(scope="function")
def station_de_bilt():
    return 260


@pytest.fixture(scope="function")
def station_eelde():
    return 280


@pytest.fixture(scope="session")
def testdata_dir():
    return os.path.join(os.path.dirname(__file__), "testdata")


def test_import_and_metadata_access():
    print(stations)
    print(variables)
    print(f"KNMI-py version: {__version__}")

    assert len(stations) > 0
    assert len(variables) > 0
    assert isinstance(__version__, str)


def test_get_day_data_dataframe(station_de_bilt, station_eelde, testdata_dir):
    """Test retrieval of daily data"""
    df_should_fn = os.path.join(testdata_dir, "get_day_data.csv")
    df_should = pd.read_csv(df_should_fn, index_col=0, parse_dates=True)
    df = knmi.get_day_data_dataframe(
        stations=[station_de_bilt, station_eelde],
        start="20200501",
        end="20200502",
    )
    df_should.index = df_should.index.tz_convert("Europe/Amsterdam")
    pd.testing.assert_frame_equal(df, df_should)


def test_get_day_data_dataframe_all_stations_rh(testdata_dir):
    """Test retrieval of daily data"""
    df_should_fn = os.path.join(testdata_dir, "get_day_data_all_stn_rh.csv")
    df_should = pd.read_csv(df_should_fn, index_col=0, parse_dates=True)
    df = knmi.get_day_data_dataframe(
        stations="ALL", start="20200501", end="20200502", variables=["RH"]
    )
    df_should.index = df_should.index.tz_convert("Europe/Amsterdam")
    pd.testing.assert_frame_equal(df, df_should)


def test_get_hour_data_dataframe(station_de_bilt, station_eelde, testdata_dir):
    """Test get hour data for all variables"""
    df_should_fn = os.path.join(testdata_dir, "get_hour_data.csv")
    df_should = pd.read_csv(df_should_fn, index_col=0, parse_dates=True)
    df = knmi.get_hour_data_dataframe(
        stations=[station_de_bilt, station_eelde], start="2020080101", end="2020080105"
    )
    pd.testing.assert_frame_equal(df, df_should)


def test_get_hour_data_dataframe_temp_sun(station_de_bilt, station_eelde, testdata_dir):
    """Test get hour data for two variables"""
    df_should_fn = os.path.join(testdata_dir, "get_hour_data_temp_sun.csv")
    df_should = pd.read_csv(df_should_fn, index_col=0, parse_dates=True)
    df = knmi.get_hour_data_dataframe(
        stations=[station_de_bilt, station_eelde],
        start="2020080101",
        end="2020080124",
        variables=["TEMP", "SUNR"],
    )
    pd.testing.assert_frame_equal(df, df_should)
