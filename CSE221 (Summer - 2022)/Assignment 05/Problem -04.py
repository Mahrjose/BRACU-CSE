# Problem -04


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def main():

    from math import sqrt

    fileInput = [line.replace("\n", "") for line in readLines("task4_input.txt")]
    fileOutput = []
    squre_num_count = 0

    for line in fileInput:
        if line == "0 0":
            break

        a, b = tuple(map(int, line.split(" ")))

        for number in range(a, b + 1):
            squre_root = sqrt(number)

            if squre_root - int(squre_root) == 0.0:
                squre_num_count += 1

        fileOutput.append(squre_num_count)
        squre_num_count = 0

    fileOutput = [str(i) for i in fileOutput]
    writeLines("task4_output.txt", fileOutput)


if __name__ == "__main__":
    main()
