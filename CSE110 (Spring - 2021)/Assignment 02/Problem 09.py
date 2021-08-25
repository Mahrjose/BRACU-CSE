user_input = int(input())
new_counter = 0

counter = 0

while counter <= user_input:
    if counter % 7 == 0:
        new_counter += counter
    if counter == user_input:
        print(new_counter)
        break
    counter += 1
