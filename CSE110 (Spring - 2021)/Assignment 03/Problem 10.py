str_input = input()

for ch in str_input:
    if str_input.index(ch) % 2 != 0 and str_input.index(ch) != 0:
        print(ch.upper(), end="")
