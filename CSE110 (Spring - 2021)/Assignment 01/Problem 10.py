user_input = int(input())

if not (user_input % 2 == 0) or not (user_input % 5 == 0):
    print(user_input)
else:
    print("No")
