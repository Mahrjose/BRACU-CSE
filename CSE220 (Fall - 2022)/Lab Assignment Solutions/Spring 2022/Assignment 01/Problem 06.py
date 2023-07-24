# Problem -06


def array_series(num) -> list:

    arr = [0] * (num * num)

    i = 1
    while i <= num:
        j = 1
        while j <= i:
            arr[(i * num) - j] = j

            j += 1
        i += 1

    return arr


def main():

    # Uncomment for manual input
    # print(array_series(int(input("Input 'n' = "))))

    print(f"n = 2: {array_series(2)}")
    print(f"n = 3: {array_series(3)}")
    print(f"n = 4: {array_series(4)}")


if __name__ == "__main__":
    main()
