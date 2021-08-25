list_1 = [int(count) for count in input("List_One = ")[1:-1].split(",")]
list_2 = [int(count) for count in input("List_Two = ")[1:-1].split(",")]

list_1 += list_2
list_3 = []

for item in list_1:
    if item not in list_3:
        list_3.append(item)
print(list_3)
