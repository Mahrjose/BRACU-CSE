sum = 0
user_input = int(input())

for count in range(1, user_input + 1):
    if count % 2 != 0:
        count = count ** 2
    else:
        count = (count ** 2) * (-1)
    sum += count
print(sum)
