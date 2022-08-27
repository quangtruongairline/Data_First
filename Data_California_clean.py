import pandas as pd
import numpy as np

dt=pd.read_csv("california_cities.csv")

x=dt["elevation_m"].mean()
dt["elevation_m"].fillna(x,inplace=True)

x=dt["elevation_ft"].mean()
dt["elevation_ft"].fillna(x,inplace=True)

x=dt["area_total_sq_mi"].mean()
dt["area_total_sq_mi"].fillna(x,inplace=True)

x=dt["area_water_sq_mi"].mean()
dt["area_water_sq_mi"].fillna(x,inplace=True)

x=dt["area_total_km2"].mean()
dt["area_total_km2"].fillna(x,inplace=True)

x=dt["area_land_km2"].mean()
dt["area_land_km2"].fillna(x,inplace=True)

x=dt["area_water_km2"].mean()
dt["area_water_km2"].fillna(x,inplace=True)

x=dt["area_water_percent"].mean()
dt["area_water_percent"].fillna(x,inplace=True)


print(dt.info())