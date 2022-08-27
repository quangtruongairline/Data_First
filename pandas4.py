
import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv("data.csv")

#truc quan hoa DataFrame
'''df.plot()
plt.show()
'''
#lo phan tan

'''df.plot(kind="scatter", x="Duration", y="Calories")

plt.show()
'''
    #bieu do cot
df["Duration"].plot(kind="hist")
plt.show()