# Problem -03


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def main():

    from collections import deque

    inPath = ["task3_input1.txt", "task3_input2.txt"]
    outPath = ["task3_output1.txt", "task3_output2.txt"]

    for name in range(0, 2):

        stack = deque()
        fileInput = [line.replace("\n", "") for line in readLines(inPath[name])]

        # total_tasks = fileInput[0]
        task_list = list(map(int, fileInput[1].split(" ")))
        string = fileInput[2]

        task_list.sort()

        seq = ""
        jack = 0
        jill = 0
        index = 0
        for char in string:
            if char == "J":
                stack.append(task_list[index])
                seq += str(task_list[index])
                jack += task_list[index]
                index += 1

            elif char == "j":
                var = stack.pop()
                seq += str(var)
                jill += var

        fileOutput = []
        fileOutput.append(seq)
        fileOutput.append(f"Jack will work for {jack} hours")
        fileOutput.append(f"Jill will work for {jill} hours")

        writeLines(outPath[name], fileOutput)


if __name__ == "__main__":
    main()
