list_1 = [int(count) for count in input("List_One = ")[1:-1].split(",")]
list_2 = [int(count) for count in input("List_Two = ")[1:-1].split(",")]

for item in list_1:
    is_true = item in list_2
    if is_true == True:
        break
print(is_true)
