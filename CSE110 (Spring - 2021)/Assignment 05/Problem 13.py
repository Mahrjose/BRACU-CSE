a_list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
a_dict = {}

for a_tuple in a_list:
    key, value = a_tuple

    if key in a_dict:
        a_dict[key].append(value)
        continue
    a_dict[key] = [value]

print(a_dict)
