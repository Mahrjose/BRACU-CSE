# taking input from user
a_tuple = tuple(int(item) for item in input()[1:-1].split(","))
new_tuple = a_tuple[2:-2]
print(new_tuple)

# Without taking input from user
# a_tuple = (-10, 20, 25, 30, 40)
# new_tuple = (a_tuple[2:-2])
# print(a_tuple)
# print(new_tuple)
