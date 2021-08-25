def upper_lower(string):
    upper_counter = 0
    lower_counter = 0
    for char in string:
        if char.isupper():
            upper_counter += 1
        elif char.islower():
            lower_counter += 1
    print(f"No. of Uppercase Characters: {upper_counter}")
    print(f"No. of Lowercase Characters: {lower_counter}")


# upper_lower('The quick Sand Man')
upper_lower("HaRRy PotteR")
