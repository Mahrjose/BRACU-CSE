# Using a pre-made list
# tup_list = [(2, 3), (4, 5), (6, 7), (2, 8)]
tup_list = [(11, 22), (33, 55), (55, 77), (11, 44)]
print(tup_list)
new_list = []

for a_tuple in tup_list:
    new_list.append(a_tuple[0] * a_tuple[1])

print(new_list)

# Taking input from the user
tup_list = [
    int(item)
    for item in input()[2:-2]
    .replace(")", "")
    .replace("(", "")
    .replace(" ", "")
    .split(",")
]
new_list = []

for item in tup_list[0::2]:
    next_index = tup_list.index(item) + 1
    new_item = item * tup_list[next_index]
    new_list.append(new_item)

print(new_list)
