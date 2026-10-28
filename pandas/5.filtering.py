 #filtering = Keeping the rows that match a condition
 
import pandas as pd 

df = pd.read_csv("pandas/No,Name,Type1,Type2,Height,Weight,L.csv",index_col="Name")

# tall_pokemon = df[df["Height"] > 2]
# heavy_pokemon=df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == True]
fire_pokemon = df[df["Type1"] == "Fire"]

# print(tall_pokemon)
# print(legendary_pokemon)
# print(fire_pokemon.to_string())
print(fire_pokemon)