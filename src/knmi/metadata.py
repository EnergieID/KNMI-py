from collections import namedtuple

Station = namedtuple("Station", ["number", "longitude", "latitude", "altitude", "name"])

stations = {
    209: Station(
        number=209, longitude=4.518, latitude=52.465, altitude=0.0, name="IJMOND"
    ),
    210: Station(
        number=210, longitude=4.43, latitude=52.171, altitude=-0.2, name="VALKENBURG"
    ),
    215: Station(
        number=215, longitude=4.437, latitude=52.141, altitude=-1.1, name="VOORSCHOTEN"
    ),
    225: Station(
        number=225, longitude=4.555, latitude=52.463, altitude=4.4, name="IJMUIDEN"
    ),
    235: Station(
        number=235, longitude=4.781, latitude=52.928, altitude=1.2, name="DE KOOY"
    ),
    240: Station(
        number=240, longitude=4.79, latitude=52.318, altitude=-3.3, name="SCHIPHOL"
    ),
    242: Station(
        number=242, longitude=4.921, latitude=53.241, altitude=10.8, name="VLIELAND"
    ),
    248: Station(
        number=248, longitude=5.174, latitude=52.634, altitude=0.8, name="WIJDENES"
    ),
    249: Station(
        number=249, longitude=4.979, latitude=52.644, altitude=-2.4, name="BERKHOUT"
    ),
    251: Station(
        number=251,
        longitude=5.346,
        latitude=53.392,
        altitude=0.7,
        name="HOORN (TERSCHELLING)",
    ),
    257: Station(
        number=257, longitude=4.603, latitude=52.506, altitude=8.5, name="WIJK AAN ZEE"
    ),
    258: Station(
        number=258, longitude=5.401, latitude=52.649, altitude=7.3, name="HOUTRIBDIJK"
    ),
    260: Station(
        number=260, longitude=5.18, latitude=52.1, altitude=1.9, name="DE BILT"
    ),
    265: Station(
        number=265, longitude=5.274, latitude=52.13, altitude=13.9, name="SOESTERBERG"
    ),
    267: Station(
        number=267, longitude=5.384, latitude=52.898, altitude=-1.3, name="STAVOREN"
    ),
    269: Station(
        number=269, longitude=5.52, latitude=52.458, altitude=-3.7, name="LELYSTAD"
    ),
    270: Station(
        number=270, longitude=5.752, latitude=53.224, altitude=1.2, name="LEEUWARDEN"
    ),
    273: Station(
        number=273, longitude=5.888, latitude=52.703, altitude=-3.3, name="MARKNESSE"
    ),
    275: Station(
        number=275, longitude=5.873, latitude=52.056, altitude=48.2, name="DEELEN"
    ),
    277: Station(
        number=277, longitude=6.2, latitude=53.413, altitude=2.9, name="LAUWERSOOG"
    ),
    278: Station(
        number=278, longitude=6.259, latitude=52.435, altitude=3.6, name="HEINO"
    ),
    279: Station(
        number=279, longitude=6.574, latitude=52.75, altitude=15.8, name="HOOGEVEEN"
    ),
    280: Station(
        number=280, longitude=6.585, latitude=53.125, altitude=5.2, name="EELDE"
    ),
    283: Station(
        number=283, longitude=6.657, latitude=52.069, altitude=29.1, name="HUPSEL"
    ),
    285: Station(
        number=285, longitude=6.399, latitude=53.575, altitude=0.0, name="HUIBERTGAT"
    ),
    286: Station(
        number=286, longitude=7.15, latitude=53.196, altitude=-0.2, name="NIEUW BEERTA"
    ),
    290: Station(
        number=290, longitude=6.891, latitude=52.274, altitude=34.8, name="TWENTHE"
    ),
    308: Station(
        number=308, longitude=3.379, latitude=51.381, altitude=0.0, name="CADZAND"
    ),
    310: Station(
        number=310, longitude=3.596, latitude=51.442, altitude=8.0, name="VLISSINGEN"
    ),
    311: Station(
        number=311, longitude=3.672, latitude=51.379, altitude=0.0, name="HOOFDPLAAT"
    ),
    312: Station(
        number=312, longitude=3.622, latitude=51.768, altitude=0.0, name="OOSTERSCHELDE"
    ),
    313: Station(
        number=313,
        longitude=3.242,
        latitude=51.505,
        altitude=0.0,
        name="VLAKTE V.D. RAAN",
    ),
    315: Station(
        number=315, longitude=3.998, latitude=51.447, altitude=0.0, name="HANSWEERT"
    ),
    316: Station(
        number=316, longitude=3.694, latitude=51.657, altitude=0.0, name="SCHAAR"
    ),
    319: Station(
        number=319, longitude=3.861, latitude=51.226, altitude=1.7, name="WESTDORPE"
    ),
    323: Station(
        number=323,
        longitude=3.884,
        latitude=51.527,
        altitude=1.4,
        name="WILHELMINADORP",
    ),
    324: Station(
        number=324, longitude=4.006, latitude=51.596, altitude=0.0, name="STAVENISSE"
    ),
    330: Station(
        number=330,
        longitude=4.122,
        latitude=51.992,
        altitude=11.9,
        name="HOEK VAN HOLLAND",
    ),
    331: Station(
        number=331, longitude=4.193, latitude=51.48, altitude=0.0, name="THOLEN"
    ),
    340: Station(
        number=340, longitude=4.342, latitude=51.449, altitude=19.2, name="WOENSDRECHT"
    ),
    343: Station(
        number=343,
        longitude=4.313,
        latitude=51.893,
        altitude=3.5,
        name="R'DAM-GEULHAVEN",
    ),
    344: Station(
        number=344, longitude=4.447, latitude=51.962, altitude=-4.3, name="ROTTERDAM"
    ),
    348: Station(
        number=348, longitude=4.926, latitude=51.97, altitude=-0.7, name="CABAUW"
    ),
    350: Station(
        number=350, longitude=4.936, latitude=51.566, altitude=14.9, name="GILZE-RIJEN"
    ),
    356: Station(
        number=356, longitude=5.146, latitude=51.859, altitude=0.7, name="HERWIJNEN"
    ),
    370: Station(
        number=370, longitude=5.377, latitude=51.451, altitude=22.6, name="EINDHOVEN"
    ),
    375: Station(
        number=375, longitude=5.707, latitude=51.659, altitude=22.0, name="VOLKEL"
    ),
    377: Station(
        number=377, longitude=5.763, latitude=51.198, altitude=30.0, name="ELL"
    ),
    380: Station(
        number=380, longitude=5.762, latitude=50.906, altitude=114.3, name="MAASTRICHT"
    ),
    391: Station(
        number=391, longitude=6.197, latitude=51.498, altitude=19.5, name="ARCEN"
    ),
}

variables = {
    "FXXH": "Hourly division in which FXX was measured",
    "PXH": "Hourly division in which PX was measured",
    "TG": "Daily mean temperature in (0.1 degrees Celsius)",
    "RHXH": "Hourly division in which RHX was measured",
    "EV24": "Potential evapotranspiration (Makkink) (in 0.1 mm)",
    "UNH": "Hourly division in which UN was measured",
    "UX": "Maximum relative atmospheric humidity (in percents)",
    "TN": "Minimum temperature (in 0.1 degrees Celsius)",
    "FHXH": "Hourly division in which FHX was measured",
    "PG": "Daily mean sea level pressure (in 0.1 hPa) calculated from 24 hourly values",
    "FG": "Daily mean windspeed (in 0.1 m/s)",
    "SQ": "Sunshine duration (in 0.1 hour) calculated from global radiation (-1 for <0.05 hour)",
    "FHNH": "Hourly division in which FHN was measured",
    "T10NH": "6-hourly division in which T10N was measured; 6=0-6 UT, 12=6-12 UT, 18=12-18 UT, 24=18-24 UT",
    "VVN": (
        "Minimum visibility; 0: <100 m, 1:100-200 m, 2:200-300 m,..., 49:4900-5000 m, "
        "50:5-6 km, 56:6-7 km, 57:7-8 km,..., 79:29-30 km, 80:30-35 km, 81:35-40 km,..., "
        "89: >70 km)"
    ),
    "FHVEC": "Vector mean windspeed (in 0.1 m/s)",
    "YYYYMMDD": "Date (YYYY=year MM=month DD=day)",
    "TNH": "Hourly division in which TN was measured",
    "SP": "Percentage of maximum potential sunshine duration",
    "PNH": "Hourly division in which PN was measured",
    "DDVEC": "Vector mean wind direction in degrees (360=north, 90=east, 180=south, 270=west, 0=calm/variable)",
    "DR": "Precipitation duration (in 0.1 hour)",
    "RH": "Daily precipitation amount (in 0.1 mm) (-1 for <0.05 mm)",
    "VVNH": "Hourly division in which VVN was measured",
    "UXH": "Hourly division in which UX was measured",
    "NG": "Mean daily cloud cover (in octants, 9=sky invisible)",
    "PN": "Minimum hourly sea level pressure (in 0.1 hPa)",
    "T10N": "Minimum temperature at 10 cm above surface (in 0.1 degrees Celsius)",
    "UG": "Daily mean relative atmospheric humidity (in percents)",
    "RHX": "Maximum hourly precipitation amount (in 0.1 mm) (-1 for <0.05 mm)",
    "TX": "Maximum temperature (in 0.1 degrees Celsius)",
    "VVX": (
        "Maximum visibility; 0: <100 m, 1:100-200 m, 2:200-300 m,..., 49:4900-5000 m, "
        "50:5-6 km, 56:6-7 km, 57:7-8 km,..., 79:29-30 km, 80:30-35 km, 81:35-40 km,..., "
        "89: >70 km)"
    ),
    "Q": "Global radiation (in J/cm2)",
    "UN": "Minimum relative atmospheric humidity (in percents)",
    "VVXH": "Hourly division in which VVX was measured",
    "TXH": "Hourly division in which TX was measured",
    "PX": "Maximum hourly sea level pressure (in 0.1 hPa)",
    "FXX": "Maximum wind gust (in 0.1 m/s)",
    "FHX": "Maximum hourly mean windspeed (in 0.1 m/s)",
    "FHN": "Minimum hourly mean windspeed (in 0.1 m/s)",
}
