# Problem -03


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def LCS(str_1, str_2, str_3, len_str_1, len_str_2, len_str_3):

    table = [
        [[0 for i in range(len_str_3 + 1)] for j in range(len_str_2 + 1)]
        for k in range(len_str_1 + 1)
    ]

    for i in range(len_str_1 + 1):
        for j in range(len_str_2 + 1):
            for k in range(len_str_3 + 1):
                if i == 0 or j == 0 or k == 0:
                    table[i][j][k] = 0

                elif str_1[i - 1] == str_2[j - 1] and str_1[i - 1] == str_3[k - 1]:
                    table[i][j][k] = table[i - 1][j - 1][k - 1] + 1

                else:
                    table[i][j][k] = max(
                        max(table[i - 1][j][k], table[i][j - 1][k]), table[i][j][k - 1]
                    )

    return table[len_str_1][len_str_2][len_str_3]


def main():

    fileInputList = ["task3_input1.txt", "task3_input2.txt"]
    fileOutputList = ["task3_output1.txt", "task3_output2.txt"]

    for file in range(2):

        fileInput = [i.replace("\n", "") for i in readLines(fileInputList[file])]
        string_1 = fileInput[0]
        string_2 = fileInput[1]
        string_3 = fileInput[2]

        fileOutput = []
        fileOutput.append(
            LCS(
                string_1,
                string_2,
                string_3,
                len(string_1),
                len(string_2),
                len(string_3),
            )
        )
        fileOutput = [str(i) for i in fileOutput]

        writeLines(fileOutputList[file], fileOutput)


if __name__ == "__main__":
    main()
