my_dictionary = {"c1": "Red", "c2": "Green", "c3": None, "d4": "Blue", "a5": None}
temp_dict = my_dictionary.copy()

for key in temp_dict:
    if my_dictionary[key] == None:
        del my_dictionary[key]
print(my_dictionary)
