# Tuple given in the code
a_tuple = ("a", "b", "c", "d", "e", "f", "g", "h")
print(a_tuple)

# Taking input from the user
# a_tuple = tuple(int(item) if item.isdigit() else item for item in input()[1:-1].replace("'","").replace(" ","").split(","))

a_list = list(a_tuple)
a_list.reverse()

a_tuple = tuple(a_list)
print(a_tuple)
