number = int(input())
str_number = str(number)
counter = 0

for div in range(1, number + 1):
    if number % div == 0:
        if div == number:
            print(div, end="")
        else:
            print(div, end=",")
        counter += 1
print("\nTotal", counter, "divisors.")
