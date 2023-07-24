def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def insertionSort(array: list, size: int) -> list:

    arr: list[int] = array.copy()

    for step in range(1, size):
        key = arr[step]

        for index in range(step - 1, -1, -1):
            # Change to > for Ascending Order Sorting
            if arr[index] < key:
                (arr[index], arr[step]) = (key, arr[index])

            # Update the step value
            step = index

    return arr


def main() -> None:
    output_list: list = []
    sorted_id: list = []
    input_list: list = [item.replace("\n", "") for item in readLines("Input.txt")]

    for i in range(0, len(input_list), 3):
        size = int(input_list[i])

        student_id = [int(item) for item in input_list[i + 1].split(" ")]
        student_marks = [int(item) for item in input_list[i + 2].split(" ")]

        memorization = [[student_marks[i], i] for i in range(len(student_marks))]
        sorted_list = insertionSort(student_marks, size)

        for index in range(len(sorted_list)):
            for nested_list in memorization:
                if sorted_list[index] == nested_list[0]:

                    id_index = nested_list[1]
                    sorted_id.append(student_id[id_index])

                    memorization.remove(nested_list)
                    break

        output_list.append(sorted_id)
        sorted_id = []

    output_list = [
        str(item).replace("[", "").replace("]", "").replace(",", "")
        for item in output_list
    ]
    writeLines("Output.txt", output_list)


if __name__ == "__main__":
    main()
