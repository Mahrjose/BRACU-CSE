# Input string Without ("")
# str_input = input().replace(" ","").lower()

# Input string With ("")
str_input = input().replace('"', "").replace(" ", "").lower()
dict = {}

for char in str_input:
    if char in dict:
        dict[char] += 1
        continue
    dict[char] = 1

print(dict)
