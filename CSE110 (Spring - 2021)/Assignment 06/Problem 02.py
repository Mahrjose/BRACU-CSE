def fibonacci(lim):
    first = 1
    second = 1
    third = 2
    if lim >= 2:
        print("0 1 1", end=" ")
        while third <= lim:
            print(third, end=" ")
            first = second
            second = third
            third = first + second
        print("")
    elif lim == 1:
        print("0 1 1")
    elif lim == 0:
        print("0")
    else:
        print(
            "Wrong Input: Limit cannot be a negative number! Please run the program again."
        )


# Function Call
fibonacci(10)
fibonacci(5)
fibonacci(-5)
