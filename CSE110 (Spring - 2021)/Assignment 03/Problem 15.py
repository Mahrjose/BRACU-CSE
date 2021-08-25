# code is not finished
str_input = input()
new_str = "{}".format(str_input[0])
len_large_str = 0

for ch in str_input[1:]:
    if ch == new_str[-1]:
        new_str += ch
    elif ch != new_str[-1]:
        len_str = len(new_str)
        if len_str > len_large_str:
            len_large_str = len_str
            large_str = new_str
        new_str = ""
        new_str += ch
print(large_str)
