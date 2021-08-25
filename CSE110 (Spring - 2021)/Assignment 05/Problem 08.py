# Approach(1)

dict_list = [
    item
    for item in input()[1:-1]
    .replace("'", "")
    .replace(" ", "")
    .replace(":", ",")
    .split(",")
]
key_list = [item for item in dict_list[0::2]]
value_list = [int(item) for item in dict_list[1::2]]

# to know the length of key_list or value_list without using len() function since the question forbid me from using it
list_len = 0
for i in key_list:
    list_len += 1

my_dict = {}
for i in range(list_len):
    my_dict[key_list[i]] = value_list[i]

value_sum = 0
for value in my_dict.values():
    value_sum += value

average = value_sum // list_len
print(f"Average is {average}")

# Approach(2)

my_list = {}

len_dict = int(input("Enter the length of the Dictionary: "))
for count in range(len_dict):
    key, value = input("Input a key then a value separated by colon(:)- ").split(":")
    my_list[key] = int(value)
print(my_list)

value_sum = 0
for value in my_list.values():
    value_sum += value

average = value_sum // len_dict
print(f"Average is {average}")
