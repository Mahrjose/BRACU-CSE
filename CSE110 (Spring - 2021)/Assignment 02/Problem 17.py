quantity = int(input())
max = 0
min = 0
total = 0
count = 0

for i in range(0, quantity):
    num = int(input())
    total += num
    count += 1
    if num > max:
        max = num
    elif num < min:
        min = num

print("Maximum", max)
print("Minimum", min)
print("Average is", total / count)
