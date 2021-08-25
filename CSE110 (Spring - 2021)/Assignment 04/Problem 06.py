my_list = [
    int(element)
    for element in input("Please input 5 numbers separated by comma(,): ").split(",")
]
num_large = my_list[0]

for num in my_list:
    if num >= num_large:
        num_large = num
print("My list: ", my_list)
print(
    "Largest number in the list is {} which was found at index {}".format(
        num_large, my_list.index(num_large)
    )
)
