# Taking input from the user
"""
dict_list = [item for item in input()[1:-1].replace("'","").replace(" ","").replace(":",",").split(",")]
key_list = [item for item in dict_list[0::2]]
value_list = [int(item) for item in dict_list[1::2]]

dict = {}
for count in range(len(key_list)):
    dict[key_list[count]] = value_list[count]
"""

# Using a pre-made dictionary
dict = {"sci fi": 5, "mystery": 3, "horror": 14, "young_adult": 2, "adventure": 9}
print(dict)

max_value = 0
for key in dict.keys():
    if dict[key] >= max_value:
        max_value = dict[key]
        max_key = key
print(
    f"The highest selling book genre is '{max_key}' and the number of books sold are {max_value}."
)
