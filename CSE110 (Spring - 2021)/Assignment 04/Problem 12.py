# Multi-Line Code
# user_input = input()
# user_input = user_input[1:-1]
# user_list = [int(item) for item in user_input.split(",")]
# print([ item**2 for item in user_list ])

# One Line Code
print([item ** 2 for item in [int(item) for item in input()[1:-1].split(",")]])
