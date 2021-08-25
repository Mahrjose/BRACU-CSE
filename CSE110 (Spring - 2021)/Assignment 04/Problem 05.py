user_list = [
    int(element)
    for element in input("Please input numbers separated by comma(,): ").split(",")
]
no_dupli_list = []

for num in user_list:
    if num not in no_dupli_list:
        no_dupli_list.append(num)
print(no_dupli_list)
