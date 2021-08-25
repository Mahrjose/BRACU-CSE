def show_palindrome(num):
    for count in range(1, num):
        print(count, end="")
    for rev_count in range(num, 0, -1):
        print(rev_count, end="")
    print("")


# Function Call
show_palindrome(5)
show_palindrome(3)
