dictionary = {"a": 6, "b": 7, "c": 9, "d": 8, "e": 11, "f": 12, "g": 13}
new_dict = {}
lower_value, upper_value = input().split(",")
lower_value = int(lower_value)
upper_value = int(upper_value)

for key, value in dictionary.items():
    if value >= lower_value and value < upper_value:
        new_dict[key] = value
print(new_dict)
