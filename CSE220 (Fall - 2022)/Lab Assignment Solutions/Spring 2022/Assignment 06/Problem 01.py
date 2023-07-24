# Problem -01


def findMin(arr, start, end):
    if start == end:
        return start

    min = findMin(arr, start + 1, end)
    if arr[start] > arr[min]:
        return min

    return start


def rec_selection_sort(arr, start, end):
    if start < end:
        min = findMin(arr, start + 1, end)
        if arr[start] > arr[min]:
            temp = arr[start]
            arr[start] = arr[min]
            arr[min] = temp

        rec_selection_sort(arr, start + 1, end)


print("\nNo. 1 - Sorting with Selection Recursion Sort -> \n")
print("Unsorted -> ", end="")
arr = [100, 3, 5, 1, 55, 88, 6, 4, 7, 88, 2, 1, 0]
print(arr)
rec_selection_sort(arr, 0, len(arr) - 1)
print("Sorted -> ", end="")
print(arr)
print("\n")
