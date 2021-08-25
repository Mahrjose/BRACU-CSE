my_list = [
    int(element)
    for element in input("Please input 5 numbers separated by comma(,): ").split(",")
]
num_large = my_list[0]
num_small = my_list[-1]

for num in my_list:
    if num >= num_large:
        num_large = num
    elif num < num_large and num <= num_small:
        num_small = num

print("My list: ", my_list)
print(
    "Smallest number in the list is {} which was found at index {}".format(
        num_small, my_list.index(num_small)
    )
)
print(
    "Largest number in the list is {} which was found at index {}".format(
        num_large, my_list.index(num_large)
    )
)
