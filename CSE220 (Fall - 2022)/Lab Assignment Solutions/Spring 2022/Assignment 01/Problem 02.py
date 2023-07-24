# Problem -02


def rotateLeft(arr, k):

    temp = [value for value in arr[:k]]

    for i in range(len(arr)):
        if i < len(arr) - k and k > 0:
            arr[i] = arr[i + k]

        else:
            if k <= 0 or k > len(arr):
                print("Invalid 'k' position")
                return
            else:
                arr[i] = temp[i - (len(arr) - k)]

    print(arr)


def main():
    source = [10, 20, 30, 40, 50, 60]
    rotateLeft(source, 3)


if __name__ == "__main__":
    main()
