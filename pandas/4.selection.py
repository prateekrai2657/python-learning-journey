import pandas as pd

df = pd.read_csv("pandas/No,Name,Type1,Type2,Height,Weight,L.csv",index_col="Name")

#selection by column

# print(df["Name"]) #show first 5 and last 5 five data set 
# # if you want full data you have to use{{.to_string()}}
# print(df[["Name","Height","Weight"]].to_string())


# Selection by row
print(df.loc["Pikachu",["Height","Weight"]]) #show 0 index row
# pokemon = input("Enter the pokemon name : ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")