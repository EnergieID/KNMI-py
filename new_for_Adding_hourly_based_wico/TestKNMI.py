#https://github.com/EnergieID/KNMI-py



import knmi
import metadata

print(metadata.stations)# provides a list of all available stations
print(metadata.variables)# provides a list of all variables and explanations

station_de_bilt=260
station_eelde=280
print("Ophalen dagdata")
disclaimer, stations, legend, df = knmi.get_day_data_dataframe(stations=[station_de_bilt,station_eelde],start="20200501",end="20200601" )
print(stations,legend)
print(df)
print("Ophalen uurdata")
disclaimer, stations, legend, df = knmi.get_hour_data_dataframe(stations=[station_de_bilt,station_eelde],start="2020080101",end="2020080105" )
print(stations,legend)
print(df)
print("Ophalen uurdata alleen temp en zon")
disclaimer, stations, legend, df = knmi.get_hour_data_dataframe(stations=[station_de_bilt,station_eelde],start="2020080101",end="2020080124" ,variables=['TEMP','SUNR'])
print(stations,legend)
print(df)


