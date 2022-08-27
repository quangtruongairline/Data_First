from turtle import pd
import pandas as pd

df=pd.read_csv("dirtydata.csv")
print(df)
#===========================DATA EMPTY==============================================
#xoa o trong
'''
new_df=df.dropna()
new2=df.dropna(inplace=True)
print(new_df)
'''
# xoa thang tren df
'''
df.dropna(inplace=True)
print(df)
'''
# thay the
'''
df.fillna(130, inplace=True)
print(df)
'''
#thay the chi dinh
'''
df["Calories"].fillna(130,inplace=True)
print(df)
'''
# thay the chi dinh bang trung binh
'''
x=df["Calories"].mean()
df["Calories"].fillna(x,inplace=True)
print(df)
'''
#==================================================================================================
#=====================DATA WRONG FOMAT=============================================================

#chuyen thanh ngay thang 

'''df["Date"]=pd.to_datetime(df["Date"])

print(df)
'''
#xoa hang 

'''df.dropna(subset=["Date"], inplace=True)
y=df["Calories"].mean()
df["Calories"].fillna(y,inplace=True)
print(df)
'''

#Lam sach du lieu 
'''for x in df.index:
    if(df.loc[x,"Duration"] >60):
        df.loc[x,"Duration"]=60

print(df)
'''
#xoa mot hang
'''for x in df.index:
    if(df.loc[x,"Duration"]>60):
        df.drop(x,inplace=True)

print(df)
'''

#loai bo cac hang giong nhau

'''df.drop_duplicates(inplace=True)
print(df)
'''

dff=pd.read_csv("data.csv")

print(dff.corr())