# Problem -07

arr = [None] * 1000


def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        if arr[num] == None:
            arr[num] = fibonacci(num - 1) + fibonacci(num - 2)

        return arr[num]


print("\nNo. 7 - Recursive Fibonacci Algorithm with memoization --> ")
n = int(input("Input n to find nth fibonacci number -> "))
print(f"{n}th fibonacci number is -> ", end="")
print(fibonacci(n))
print("\n")
