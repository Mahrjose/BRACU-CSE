def char_remover(sentence, position):
    new_sentence = sentence[0]
    removed_part = ""

    for index in range(1, len(sentence)):
        if index % position != 0:
            new_sentence += sentence[index]
        else:
            removed_part += sentence[index]
    new_sentence += removed_part

    return new_sentence


sentence = input()
position = int(input())

# Function call
print(char_remover(sentence, position))
