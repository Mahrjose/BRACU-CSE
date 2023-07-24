# Problem -02


def rec_insertion_sort(array, index):
    if index <= 1:
        return

    rec_insertion_sort(array, index - 1)

    i = index - 2
    j = array[index - 1]

    while array[i] > j and i >= 0:
        array[i + 1] = array[i]
        i -= 1

    array[i + 1] = j


print("\nNo. 2 - Sorting with Insertion Recursion Sort --> \n")
print("Unsorted -> ", end="")
array = [6, 7, 8, 9, 4, 3, 20, 0, 0]
print(array)
index = len(array)
rec_insertion_sort(array, index)
print("Sorted -> ", end="")
print(array)
print("\n")
