import math

S = int(input("Input: "))

if S < 100:
    L = 3000 - 125 * math.pow(S, 2)
    print("Output:", L)
else:
    L = 12000 / (4 + (math.pow(S, 2) / 14900))
    print("Output:", L)
