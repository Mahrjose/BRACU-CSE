user_input = input()
a_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

for item in a_tuple:
    item[-1] = user_input
print(a_tuple)
