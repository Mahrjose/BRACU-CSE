### Take input of 2 numbers from the user
var_1 = input("Please Enter Your First Number")
var_2 = input("Please Enter Your Second Number")

# Since input() function converts everything to String,
# for performing any kind of mathematical operation you need to convert them to int.
# For this conversion, we need to use int() function


# First, let's clarify whether the inputs are actually Strings or not.
print(type(var_1))
print(type(var_2))


# Convert Strings to integer using the int() function
var_3 = int(var_1)
var_4 = int(var_2)

# ===============================================================
# input taking and conversion can be done in a single sentense
# var_1 = int(input('Please Enter Your First Number'))
# var_2 = int(input('Please Enter Your Second Number'))

# ===============================================================

# Perform Addition
sum = var_3 + var_4

# Perform Multiplication
product = var_3 * var_4

# Perform Substraction
difference = var_3 - var_4

# Print all the calculated results
print("Sum =", sum)
print("Product =", product)
print("Difference =", difference)
