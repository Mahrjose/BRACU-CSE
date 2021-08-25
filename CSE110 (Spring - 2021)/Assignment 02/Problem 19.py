M, N = input().split(",")
height = int(M)
length = int(N)

for out_counter in range(1, height + 1):
    for in_counter in range(1, length + 1):
        print(in_counter, end="")
    print()
