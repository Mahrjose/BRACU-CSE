# Problem -01


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def assignmentSelection(arr):
    arr.sort(key=lambda x: x[1])
    selected = []

    selected.append(arr[0])
    for i in range(1, len(arr)):
        if selected[-1][1] <= arr[i][0]:
            selected.append(arr[i])

    return selected


def main():

    inPath = ["task1_input1.txt", "task1_input2.txt"]
    outPath = ["task1_output1.txt", "task1_output2.txt"]

    for name in range(0, 2):

        fileInput = [line.replace("\n", "") for line in readLines(inPath[name])]
        ref_arr = []

        t = int(fileInput[0])
        for line in range(1, t + 1):
            ref_arr.append(tuple(map(int, fileInput[line].split(" "))))

        fileOutput = []
        selected = assignmentSelection(ref_arr)
        fileOutput.append(str(len(selected)))

        for i in selected:
            line = " ".join([str(j) for j in i])
            fileOutput.append(line)

        writeLines(outPath[name], fileOutput)


if __name__ == "__main__":
    main()
