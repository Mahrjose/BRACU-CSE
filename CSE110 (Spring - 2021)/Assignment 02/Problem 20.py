number = int(input())

for out_counter in range(1, number + 1):
    for in_counter in range(1, out_counter + 1):
        print(in_counter, end="")
    print()
