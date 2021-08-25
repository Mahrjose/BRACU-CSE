str_1 = input()
str_2 = input()

if sorted(str_1) == sorted(str_2):
    print("They are anagram")
else:
    print("They are not anagram")
