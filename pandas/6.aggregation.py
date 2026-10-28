import pandas as pd

# aggregate function : Reduces a set of values into a single summary values || used to summarize and analyze data : ||  often used with the group by function

df = pd.read_csv("pandas/No,Name,Type1,Type2,Height,Weight,L.csv")
 
#whole data frame
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

#Single Column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count()) 

# group =df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].max())
# print(group["Height"].min())