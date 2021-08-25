user_list = [int(count) for count in input()[1:-1].split(",")]

if len(user_list) > 4:
    print(user_list[2:-2])
elif len(user_list) == 4:
    print([])
else:
    print("Not Possible")
