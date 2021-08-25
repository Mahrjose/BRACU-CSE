user_input = int(input())

if user_input % 2 == 0 and user_input % 5 == 0:
    print(user_input)
elif user_input % 2 == 0 or user_input % 5 == 0:
    print("Not multiple of 2 and 5 both")
else:
    print("Not a multiple")
