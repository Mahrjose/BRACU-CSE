str_1 = input()
str_2 = input()

if len(str_1) < len(str_2):
    for index in range(len(str_1)):
        new_str = "{0}{1}".format(str_1[index], str_2[index])
        print(new_str, end="")
    print(str_2[len(str_1) :])
else:
    for index in range(len(str_2)):
        new_str = "{0}{1}".format(str_1[index], str_2[index])
        print(new_str, end="")
    print(str_1[len(str_2) :])
