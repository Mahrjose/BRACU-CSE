# Problem -04

# 4(a)
def numPattern(num):
    if num == 0:
        return

    numPattern(num - 1)
    print(num, end=" ")


def patternPrint(num):
    if num == 0:
        return

    patternPrint(num - 1)
    numPattern(num)
    print()


print("\nNo. 4(a)-->")
num = int(input("Pattern Input: "))
patternPrint(num)


# 4(b)
def spacePattern(num):
    if num == 0:
        return

    spacePattern(num - 1)
    print(" ", end=" ")


def numPattern(num):
    if num == 0:
        return

    numPattern(num - 1)
    print(num, end=" ")


def patternPrint(num, var):
    if num == 0:
        return

    spacePattern(num - 1)
    numPattern(var - num + 1)
    print()
    patternPrint(num - 1, var)


print("\nNo. 4(b)-->")
num = int(input("Reverse Pattern Input: "))
patternPrint(num, num)
