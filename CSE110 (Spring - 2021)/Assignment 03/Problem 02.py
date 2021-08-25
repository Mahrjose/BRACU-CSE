word = input()
len_word = len(word)

if len_word < 4:
    print(word)

elif len_word > 3 and word[-2:] == "er":
    new_word = word.replace("er", "est")
    print(new_word)

elif len_word > 3 and word[-3:] == "est":
    print(word)

elif len_word > 3:
    print("{0}er".format(word))
