import pandas as pd

df = pd.read_csv("03.01 - Pokemon.csv")
print(df)

# Filtering = Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 5]
print(tall_pokemon)
print()

heavy_pokemon = df[df["Weight"] >= 300]
print(heavy_pokemon)
print()

legendary_pokemon = df[df["Legendary"] == 1] # or == True
print(legendary_pokemon)
print()

water_pokemon = df[df["Type1"] == "Water"]
print(water_pokemon)
print()

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)
print()

legendary_fire_pokemon = df[(df["Legendary"] == True) & (df["Type1"] == "Fire") | (df["Type2"] == "Fire")]
print(legendary_fire_pokemon)
print()