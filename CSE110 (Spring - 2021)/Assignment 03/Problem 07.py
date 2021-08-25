str_input = input()
index = int(input())

new_str = str_input[: index + 1]
rev_str = new_str[::-1]

print("{0}{1}".format(rev_str, str_input[index + 1 :]))
