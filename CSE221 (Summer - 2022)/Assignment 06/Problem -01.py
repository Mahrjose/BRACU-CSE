# Problem -01


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines(" -> ".join(lines))


def minStep(number, arr, step=0):

    arr.append(str(number))

    if number == 0:
        return step

    maxDigit = max(int(i) for i in str(number))
    number -= maxDigit

    return minStep(number, arr, step + 1)


def main():

    fileOutput = []
    fileInput = [i.replace("\n", "") for i in readLines("task1_input.txt")]

    step = minStep(int(fileInput[0]), fileOutput)
    fileOutput[0] = f"{str(step)} Steps\n" + fileOutput[0]
    writeLines("task1_output.txt", fileOutput)


if __name__ == "__main__":
    main()
