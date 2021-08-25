sum = 0
number = int(input())

for div in range(1, number + 1):
    if number % div == 0 and number != div:
        sum += div

if sum == number:
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")
