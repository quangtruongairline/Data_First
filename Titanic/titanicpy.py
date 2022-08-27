
from cgi import test
import pandas as pd
import numpy as np

train_df= pd.read_csv("D:/codepython_DS/Titanic/titanic/train.csv")
test_df= pd.read_csv("D:/codepython_DS/Titanic/titanic/test.csv")

train_df.set_index(train_df.PassengerId, inplace=True)

train_df.drop('PassengerId', axis=1, inplace=True)
train_df["Survived"]= train_df["Survived"].astype("category")

chuyen_feature=["Pclass","Sex","SibSp","Parch","Embarked"]

for x in chuyen_feature:
    train_df[x]=train_df[x].astype("category")

for x in chuyen_feature:
    test_df[x]=test_df[x].astype("category")

print(test_df.info())
print(train_df)
#khai pha du lieu
# Exploratory data analysis 
