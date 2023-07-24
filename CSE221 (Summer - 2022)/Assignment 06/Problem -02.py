# Problem -02


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def LCS(str_1, str_2, len_str_1, len_str_2):

    table = [[0 for i in range(len_str_2 + 1)] for i in range(len_str_1 + 1)]

    for i in range(len_str_1 + 1):
        for j in range(len_str_2 + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif str_1[i - 1] == str_2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    index = table[len_str_1][len_str_2]

    lcs = [""] * (index + 1)
    lcs[index] = ""

    i = len_str_1
    j = len_str_2
    while i > 0 and j > 0:

        if str_1[i - 1] == str_2[j - 1]:
            lcs[index - 1] = str_1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = [i for i in lcs if i != ""]
    lcs_str = "".join(lcs)
    return len(lcs), lcs_str


def main():

    zone = {
        "Y": "Yasnaya",
        "P": "Pochinki",
        "S": "School",
        "R": "Rozhok",
        "F": "Farm",
        "M": "Mylta",
        "H": "Shelter",
        "I": "Prison",
    }

    fileInput = [i.replace("\n", "") for i in readLines("task2_input.txt")]
    zone_num = int(fileInput[0])
    string_1 = fileInput[1]
    string_2 = fileInput[2]

    output = LCS(string_1, string_2, len(string_1), len(string_2))

    places = ""

    for string in output[1]:
        for key in zone.keys():
            if key == string:
                places += " " + zone[key]
                break

    places = places[1:]

    length = output[0]
    correctness = (length * 100) // zone_num
    comment = f"Correctness of prediction: {correctness}%"

    fileOutput = []
    fileOutput.append(places)
    fileOutput.append(comment)

    writeLines("task2_output.txt", fileOutput)


if __name__ == "__main__":
    main()
