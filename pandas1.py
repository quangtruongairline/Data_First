import pandas as pd
#Series
'''
a=[1,7,5,2,3]
mylist= pd.Series(a,index=["x","y","z","t","k"]);
print(mylist)
'''

#DataFrame
'''
dataset={"Mon": ["Toan", "Ly", "Hoa"], "Diem":[10,10,10]}
df=pd.DataFrame(dataset);
print(df)
    #loc
print(df.loc[0])
'''

#read csv

df=pd.read_csv("data.csv")
print(df.head(10))

    #infor
print(df.info())