def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def selectionSort(array: list, size: int, pref_choice: int) -> list:

    arr: list = array.copy()

    for step in range(pref_choice):
        min_idx = step

        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i

        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

    return arr


def main() -> None:
    output_list: list = []
    input_list: list = [item.replace("\n", "") for item in readLines("Input.txt")]

    for i in range(0, len(input_list), 2):
        size, pref_choice = map(int, input_list[i].split(" "))
        unsorted_list: list = [int(item) for item in input_list[i + 1].split(" ")]

        sorted_list: list = selectionSort(unsorted_list, size, pref_choice)
        output_list.append(sorted_list[0:pref_choice])

    output_list = [
        str(item).replace("[", "").replace("]", "").replace(",", "")
        for item in output_list
    ]
    writeLines("Output.txt", output_list)


if __name__ == "__main__":
    main()
