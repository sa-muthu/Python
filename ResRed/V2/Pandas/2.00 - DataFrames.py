import pandas as pd

# For creating a DataFrame from a dictionary
# NOTE: The 'D' in DataFrame is Capitalized
data = {
    "Name": ["Romeo Montague", "Harry Potter", "Frodo Baggins"],
    "Age": [17, 17, 50]
}

novel_characters = pd.DataFrame(data)
print(novel_characters)

# 1. To change index
novel_characters_w_index = pd.DataFrame(data, index = ["Character 1", "Character 2", "Character 3"])
print(novel_characters_w_index)

# 2. To access data (columns wise)
print(novel_characters_w_index.loc["Character 2"]) # Using the indexed name
print(novel_characters_w_index.iloc[1]) # Using the index position

# 3. To change value
novel_characters_w_index.loc["Character 2"] = ["Gerold Weasley", 17]
print(novel_characters_w_index)

# 4. To add a new column
novel_characters_w_index["Novel/Play"] = ["Romeo and Juliet", "Harry Potter", "Lord of the Rings"]
print(novel_characters_w_index)

# 5. To add a new row
new_row = pd.DataFrame([{"Name": "Jon Snow", "Age": 23, "Novel/Play": "Game of Thrones"}], index = ["Character 4"])
novel_characters_w_index = pd.concat([novel_characters_w_index, new_row])
print(novel_characters_w_index)

# 6. To add multiple rows
new_rows = pd.DataFrame([{"Name": "Alan Grant", "Age": 40, "Novel/Play": "Jurassic Park"},
                         {"Name": "Odysseus", "Age": 40, "Novel/Play": "The Odyssey"}]
)
novel_characters_w_index = pd.concat([novel_characters_w_index, new_rows])
print(novel_characters_w_index)
                        
# 7. To remove a row
pd.drop("Character 4", axis = 0, inplace = True) # here, axis means row and 1 means column, and inplace means to modify the original dataframe
print(novel_characters_w_index)

# 8. To remove a column
pd.drop("Novel/Play", axis = 1, inplace = True)
print(novel_characters_w_index)

# 9. To remove multiple rows
pd.drop(["Character 1", "Character 2"], axis = 0, inplace = True)
print(novel_characters_w_index)

# 10. To remove multiple columns
pd.drop(["Name", "Age"], axis = 1, inplace = True)
print(novel_characters_w_index)




