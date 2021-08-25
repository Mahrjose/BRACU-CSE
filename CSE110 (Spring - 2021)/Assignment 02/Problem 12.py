number = int(input())
str_num = str(number)
counter = 0

while counter != number:
    digit = number % 10
    number = number // 10
    if number != 0:
        print(digit, end=",")
    else:
        print(digit, end="")
