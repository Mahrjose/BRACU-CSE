list_1 = [int(count) for count in input("List_One = ")[1:-1].split(",")]
list_2 = [int(count) for count in input("List_Two = ")[1:-1].split(",")]

list_1.pop()
print(list_1 + list_2)
