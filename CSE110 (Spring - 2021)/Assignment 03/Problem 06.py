str_input = input()
new_str = "{}".format(str_input[0])

if len(str_input) > 1:
    for ch in str_input[1:]:
        if ch != new_str[-1]:
            new_str += ch
    print(new_str)
else:
    print(str_input)
