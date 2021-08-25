def show_palindromic_triangle(num):
    for row in range(1, num + 1):
        for space in range(1, (num - row) + 1):
            print(" ", end=" ")
        for nums in range(1, row):
            print(nums, end=" ")
        for nums in range(row, 0, -1):
            print(nums, end=" ")
        print("")


# Function Call
# show_palindromic_triangle(3)
show_palindromic_triangle(5)
