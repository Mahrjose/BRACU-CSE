# Problem 5(a)


def quickSort(array, left, right):
    if left < right:

        pi = quickSort_partition(array, left, right)

        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)


def quickSort_partition(array, left, right):

    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[right]) = (array[right], array[i + 1])

    return i + 1


# Problem 5(b)


def findk(arr, left, right, k):

    # if k is smaller than number of
    # elements in array
    if k > 0 and k <= right - left + 1:

        pi = findk_partition(arr, left, right)

        # if position is same as k
        if pi - left == k - 1:
            return arr[pi]

        # if position is more, see left subarray
        elif pi - left > k - 1:
            return findk(arr, left, pi - 1, k)

        # else see right subarray
        return findk(arr, pi + 1, right, k - pi + left - 1)

    print("Index out of bound")


def findk_partition(array, left, right):

    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[right]) = (array[right], array[i + 1])

    return i + 1


def main():

    from timeit import default_timer as timer

    # Problem 5(a)
    print("Problem 5(a): ")
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Array to be sorted: \n{sorted_array}\n")

    s_start = timer()
    quickSort(sorted_array, 0, len(sorted_array) - 1)
    s_end = timer()

    print(f"Sorted Array using Quick Sort: \n{sorted_array}\n")
    print(f"Time took for sorting (in seconds): \n{s_end - s_start} seconds")
    print("\n")

    unsorted_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Array to be sorted: \n{unsorted_array}\n")

    u_start = timer()
    quickSort(unsorted_array, 0, len(unsorted_array) - 1)
    u_end = timer()

    print(f"Sorted Array using Quick Sort: \n{unsorted_array}\n")
    print(f"Time took for sorting (in seconds): \n{u_end - u_start} seconds")
    print("\n")

    print("Problem 5(b): ")
    array = [1, 3, 4, 5, 9, 10, 10]
    print(f"The Array: {array}")

    print(
        f"kth element in the array where K = 5 ->  {findk(array, 0, len(array) - 1, k=5)}"
    )
    print(
        f"kth element in the array where K = 7 ->  {findk(array, 0, len(array) - 1, k=7)}"
    )
    print(
        f"kth element in the array where K = 2 ->  {findk(array, 0, len(array) - 1, k=2)}"
    )


if __name__ == "__main__":
    main()
