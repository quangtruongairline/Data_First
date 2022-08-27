from cProfile import label
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

dt=pd.read_csv("california_cities.csv")

#lean data
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

#luu kinh do va vi do 

lat,long= dt["latd"], dt["longd"]
population, area= dt["population_total"], dt["area_total_km2"]

# Dung plot API
plt.figure(figsize=(9,9))
plt.style.use("seaborn");
plt.scatter(long, lat, c=population, cmap='turbo', s=area);
plt.title("CALIFORNIA");
plt.axis("equal");
plt.xlabel("Longlatiude");
plt.ylabel("Latitude");
plt.colorbar(label='log$_{10}$(population)');
 
# creat legend for cities's size

note=[50,100,300, 500]

for area in note:
    plt.scatter([],[], s=area, c='k', alpha=0.4 ,label= str(area)+ 'km$^2$')

plt.legend(labelspacing=1,title="Area City California");
plt.show();