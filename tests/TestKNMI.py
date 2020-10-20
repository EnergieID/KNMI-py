#https://github.com/EnergieID/KNMI-py

from knmi import knmi, metadata

print(metadata.stations)# provides a list of all available stations
print(metadata.variables)# provides a list of all variables and explanations

station_de_bilt=260
station_eelde=280
print("Ophalen dagdata")
df = knmi.get_day_data_dataframe(stations=[station_de_bilt,station_eelde],start="20200501",end="20200601" )
print(df)
print("Ophalen uurdata")
df = knmi.get_hour_data_dataframe(stations=[station_de_bilt,station_eelde],start="2020080101",end="2020080105" )
print(df)
print("Ophalen uurdata alleen temp en zon")
df = knmi.get_hour_data_dataframe(stations=[station_de_bilt,station_eelde],start="2020080101",end="2020080124" ,variables=['TEMP','SUNR'])
print(df)
