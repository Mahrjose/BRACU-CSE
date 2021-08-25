def basic_calc(operator, num_1, num_2):
    if operator == "+":
        return num_1 + num_2

    elif operator == "-":
        return num_1 - num_2

    elif operator == "/":
        return num_1 / num_2

    elif operator == "*":
        return num_1 * num_2


operator = input()
num_1 = float(input())
num_2 = float(input())

# Function Call
print(basic_calc(operator, num_1, num_2))
