x = 0
counter = 0

while counter <= 600:
    if (counter % 7 == 0 or counter % 9 == 0) and not (
        counter % 7 == 0 and counter % 9 == 0
    ):
        x = x + counter
    if counter == 600:
        print(x)
    counter += 1
