my_list = [
    int(element)
    for element in input("Please input numbers separated by comma(,): ").split(",")
]
new_list = my_list.copy()
F_large = my_list[0]

for num in my_list:
    if num >= F_large:
        F_large = num

my_list.pop(my_list.index(F_large))
S_large = my_list[0]

for num in my_list:
    if num >= S_large:
        S_large = num

print("My list: ", new_list)
print(
    "Second largest number in the list is {} which was found at index {}".format(
        S_large, new_list.index(S_large)
    )
)
