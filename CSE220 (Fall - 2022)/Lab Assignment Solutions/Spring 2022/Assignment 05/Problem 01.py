# Problem -01

# 1(a)
def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)


print("\nNo. 1(a)-->")
n = int(input("To find n!, Please input n -> "))
print(f"{n}! is = ", end="")
print(factorial(n))

# 1(b)
def fibonacci(num):
    if num == 0:
        return 0

    if num == 1 or num == 2:
        return 1

    if num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)


print("\nNo. 1(b)-->")
n = int(input("Input n to find nth fibonacci number -> "))
print(f"{n}th fibonacci number is -> ", end="")
print(fibonacci(n))

# 1(c)
def printArray(arr, index=0):
    if index == len(arr):
        return

    print(arr[index])
    printArray(arr, index + 1)


print("\nNo. 1(c)-->")
printArray([1, 2, 3, 4, 5])

# 1(d)
def powerN(base, n):
    if n == 0:
        return 1

    return base * powerN(base, n - 1)


print("\nNo. 1(d)-->")
print(powerN(3, 1))
print(powerN(3, 2))
print(powerN(3, 3))
