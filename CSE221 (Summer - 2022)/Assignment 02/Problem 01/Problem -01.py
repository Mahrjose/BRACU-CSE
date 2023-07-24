def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def bubbleSort(array: list, size: int) -> list:
    arr: list = array.copy()

    isSorted = True
    for i in range(size - 1):
        if arr[i] > arr[i + 1]:
            isSorted = False
            break

    if not isSorted:
        for i in range(size - 1):
            for j in range(size - i - 1):
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr


def main() -> None:
    output: list = []
    input = [item.replace("\n", "") for item in readLines("Input.txt")]

    for i in range(0, len(input), 2):
        size: int = int(input[i])
        unsorted_list: list = [int(item) for item in input[i + 1].split(" ")]

        sorted_list: list = bubbleSort(unsorted_list, size)
        output.append(sorted_list)

    output = [
        str(item).replace("[", "").replace("]", "").replace(",", "") for item in output
    ]
    writeLines("Output.txt", output)


if __name__ == "__main__":
    main()
