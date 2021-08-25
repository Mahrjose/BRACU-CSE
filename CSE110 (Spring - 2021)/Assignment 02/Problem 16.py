number = int(input())

if number > 1:
    for div in range(2, number):
        if number % div == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")
            break
else:
    (number, "is not a prime number")
