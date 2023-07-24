def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def merge(left: list, right: list) -> list:
    if not len(left) or not len(right):
        return left or right

    result: list = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergeSort(arr: list, size: int) -> list:
    if size < 2:
        return arr

    middle = int(size / 2)

    left = mergeSort(arr[:middle], len(arr[:middle]))
    right = mergeSort(arr[middle:], len(arr[middle:]))

    return merge(left, right)


def main():
    output_list: list = []
    input_list: list = [item.replace("\n", "") for item in readLines("Input.txt")]

    for i in range(0, len(input_list), 2):
        size: int = int(input_list[i])
        unsorted_list: list = [int(item) for item in input_list[i + 1].split(" ")]

        sorted_list = mergeSort(unsorted_list, size)
        output_list.append(sorted_list)

    output_list = [
        str(item).replace("[", "").replace("]", "").replace(",", "")
        for item in output_list
    ]
    writeLines("Output.txt", output_list)


if __name__ == "__main__":
    main()
