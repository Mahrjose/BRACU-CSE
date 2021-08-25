user_input = input()

for index in user_input:
    ascii_num = ord(index)
    ascii_num += 1

    if ascii_num > 122:
        ascii_num = 97

    ch = chr(ascii_num)
    print(ch, end="")
