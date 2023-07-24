# Problem -03


def remove(arr, size, index):

    if index < 0 or index > size:
        print("Invalid Index")
        return

    for i in range(size):
        if i >= index and i <= size - 1:
            arr[i] = arr[i + 1]

    arr[size - 1] = 0

    print(arr)


def main():
    source = [10, 20, 30, 40, 50, 0, 0]
    remove(source, 5, 2)


if __name__ == "__main__":
    main()
