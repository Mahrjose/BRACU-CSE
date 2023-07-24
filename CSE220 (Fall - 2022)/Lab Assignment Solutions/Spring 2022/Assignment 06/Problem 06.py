# Problem -06


def rec_binary_search(array, left, right, value):
    if left <= right:

        mid_value = int((left + right) // 2)

        if array[mid_value] == value:
            return mid_value

        elif array[mid_value] < value:
            return rec_binary_search(array, mid_value + 1, right, value)

        else:
            return rec_binary_search(array, left, mid_value - 1, value)

    else:
        return -1


print("\nNo. 6 - Recursive Binary Search ->\n")
array = [1, 2, 3, 4, 5, 6, 7, 20, 30, 55, 200]
print(f"Array - {array}")
value = int(input("Item to Search? -> "))
result = rec_binary_search(array, 0, len(array) - 1, value)
if result != -1:
    print(
        f"\nThe searched element : {value}, is present in the array at index {result}."
    )
else:
    print("\nElement is not present in array.")

print("\n")
