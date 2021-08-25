dict = {"A": [1, 2, 3], "b": ["1", "2"], "c": [4, 5, 6, 7]}
count = 0

for key, list_value in dict.items():
    for item in list_value:
        count += 1
print(count)
