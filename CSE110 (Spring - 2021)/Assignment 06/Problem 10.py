def make_square(tup_range):
    start, end = tup_range
    square = {}
    for count in range(start, end + 1):
        square[count] = count ** 2
    return square


# Function Call
print(make_square((1, 3)))
print(make_square((5, 9)))
