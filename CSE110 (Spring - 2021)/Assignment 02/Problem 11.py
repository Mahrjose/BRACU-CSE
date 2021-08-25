number = int(input())
str_number = str(number)

for num in str_number:
    new_num = num.rstrip(",")
    if num == str_number[-1]:
        print(new_num, end="")
    else:
        print(new_num, end=",")
