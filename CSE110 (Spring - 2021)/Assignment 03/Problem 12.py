str_input = input()
ch = input()

if ch in str_input:
    print(str_input.replace(ch, ""))
else:
    if len(str_input) > 3:
        print(str_input[1:-1])
    else:
        print(str_input)
