str_input = input().capitalize()
modded_str = str_input[0]

for index in range(1, len(str_input)):
    if index % 2 != 0:
        str_input[index].lower()
        modded_str += str_input[index]
    elif index % 2 == 0:
        str_input[index].upper()
        modded_str += str_input[index]
print(modded_str)
