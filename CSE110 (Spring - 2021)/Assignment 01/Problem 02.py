import math

# taking input from the user, then converting it to float.
# Since radius can be a floating point value

radius = float(input("please enter the radius value:"))


# squares can be made using this 3 ways, as written in hints.
# all 3 ways, generates the same result of area

area = math.pi * radius ** 2
print("Area result is:", area)

area = math.pi * math.pow(radius, 2)
print("Area result is:", area)

area = math.pi * radius * radius
print("Area result is:", area)

# TODO
# calculate circumference

circumference = 2 * math.pi * radius
print("Circumference result is:", circumference)
