# Probem -01


def shiftLeft(arr, k):

    for i in range(len(arr)):
        if i < len(arr) - k and k > 0:
            arr[i] = arr[i + k]

        else:
            if k <= 0:
                print("Invalid 'k' Position")
                return

            else:
                arr[i] = 0

    print(arr)


def main():
    source = [10, 20, 30, 40, 50, 60]
    shiftLeft(source, 3)


if __name__ == "__main__":
    main()
