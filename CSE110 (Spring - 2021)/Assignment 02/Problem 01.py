# a) 24, 18, 12, 6, 0, -6

# initialize loop counter
counter = 24

# loop structure
while counter >= -6:

    # inside loop body
    if counter == -6:
        print(counter, end="")
    else:
        print(counter, end=", ")

    counter = counter - 6  # updating loop counter
    # inside loop body

# outside loop body

# b)-10, -5, 0, 5, 10, 15, 20

counter = -10

while counter <= 20:

    if counter == 20:
        print(counter, end="")
    else:
        print(counter, end=", ")

    counter = counter + 5


# c)18, 27, 36, 45, 54, 63

counter = 18

while counter <= 63:

    if counter == 63:
        print(counter, end="")
    else:
        print(counter, end=", ")

    counter = counter + 9

# d)18,-27, 36,-45,54,-63

counter = 18

while counter <= 63:

    if counter == 63:
        print(counter * (-1), end="")
    elif counter == 27 or counter == 45:
        print(counter * (-1), end=", ")
    else:
        print(counter, end=", ")

    counter = counter + 9
