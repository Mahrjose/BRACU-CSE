# Circular arr
# Problem -01


def palindrome(arr, start, size) -> bool:
    new_arr = []

    for _ in range(size):
        if arr[start] != 0:
            new_arr.append(arr[start])
            start += 1
        if start == len(arr):
            start = 0

    arr_half = (len(new_arr) + 1) // 2

    if new_arr[0:arr_half] == new_arr[-1 : -(arr_half + 1) : -1]:
        return True
    else:
        return False


def main():
    source = [20, 10, 0, 0, 0, 10, 20, 30]
    print(palindrome(source, start=5, size=5))

    source = [10, 20, 0, 0, 0, 10, 20, 30]
    print(palindrome(source, start=5, size=5))


if __name__ == "__main__":
    main()
