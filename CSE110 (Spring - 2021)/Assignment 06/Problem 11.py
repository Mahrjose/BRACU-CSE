def rem_duplicate(tup):
    tup_list = list(tup)
    no_duplicate = []
    for item in tup_list:
        if item not in no_duplicate:
            no_duplicate.append(item)
    fresh_tup = tuple(no_duplicate)
    return fresh_tup


# Function Call
print(rem_duplicate((1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 0, 0, 0)))
print(rem_duplicate(("Hi", 1, 2, 3, 3, "Hi", "a", "a", [1, 2])))
