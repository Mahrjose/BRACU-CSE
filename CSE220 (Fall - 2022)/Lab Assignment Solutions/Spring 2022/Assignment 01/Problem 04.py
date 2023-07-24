# Problem -04


def removeAll(arr, size, element):
    if size <= 0 and size > len(arr):
        print("Invalid Size")
        return

    # If index item is equal to the element to remove
    # replace that index item as 0
    for i in range(size):
        if arr[i] == element:
            arr[i] = 0

    j = 0
    for i in range(size):
        # If index item is not 0 (after converting
        # all target elements to 0)
        # Make the array compact with the non zero items
        if arr[i] != 0:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            j += 1

    print(arr)


def main():
    source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
    removeAll(source, 7, 2)


if __name__ == "__main__":
    main()
