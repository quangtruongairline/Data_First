from dataclasses import field
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

data_df=pd.read_csv("cereal.csv")

fields=['shelf', 'weight', 'cups', 'rating']

cereal_df= data_df.drop(fields, axis=1)

#moi tuong quan corr

cereal_corr= cereal_df.corr();

one_corr= np.ones_like(cereal_corr, dtype=bool)

mask= np.triu(one_corr) 

#print(mask)

adjusted_mask= mask[1:, :-1]

adjusted_corr= cereal_corr.iloc[1:,:-1]

fig, ax= plt.subplots(figsize=(10,8))
sns.heatmap(adjusted_corr, mask=adjusted_mask, annot=True, fmt=".2f", cmap="Blues", vmin=-1, vmax=1, linecolor="white", linewidths=0.6);

plt.show()