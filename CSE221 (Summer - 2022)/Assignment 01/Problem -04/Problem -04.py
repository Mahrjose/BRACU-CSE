def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def multiplyMatrix(A, B, n):
    C = [[0] * n for _ in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def main():
    C_lst: list = []
    total: list = []
    lines: list = readLines("Input.txt")
    n = int(lines[0].replace("\n", ""))
    start = 1
    end = n
    for _ in range(2):
        for i in lines[start : end + 1]:
            i = i.replace("\n", "")
            i = map(int, (i.split(",")))
            total.append([j for j in i])

        start += end
        end += end

    A: list = total[:n]
    B: list = total[n:]
    C = multiplyMatrix(A, B, n)

    for i in C:
        C_lst.append(str(i).replace("[", "").replace("]", ""))

    writeLines("Output.txt", C_lst)


if __name__ == "__main__":
    main()
