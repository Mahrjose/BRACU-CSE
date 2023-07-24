# Problem -02


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def scheduleIntervals(tasks, people):

    if people == 0 or len(tasks) == 0:
        return 0

    people_dict = {}
    people_list = []
    # Creating a dict & List to keep track of the people doing tasks
    for i in range(1, people + 1):
        people_dict[f"Person {i}"] = []
        people_list.append(f"Person {i}")

    # Sorting the list by the Endtime
    tasks.sort(key=lambda x: x[1])

    pointer = 0
    person = people_list[pointer]
    people_dict["Person 1"].append(tasks[0])
    totalActivity = 1

    # For every (start, endtime) in tasks
    for i in range(1, len(tasks)):
        if people_dict[person][-1][1] <= tasks[i][0]:
            people_dict[person].append(tasks[i])
            totalActivity += 1
            continue

        else:
            for _ in range(len(people_list) - 1):
                pointer += 1
                if pointer >= len(people_list):
                    pointer = pointer % len(people_list)

                person = people_list[pointer]

                if people_dict[person] == []:
                    people_dict[person].append(tasks[i])
                    totalActivity += 1
                    break

                else:
                    if people_dict[person][-1][1] <= tasks[i][0]:
                        people_dict[person].append(tasks[i])
                        totalActivity += 1
                        break

        pointer, person = 0, "Person 1"

    return totalActivity


def main():

    inPath = ["task2_input1.txt", "task2_input2.txt"]
    outPath = ["task2_output1.txt", "task2_output2.txt"]

    for name in range(0, 2):

        fileInput = [line.replace("\n", "") for line in readLines(inPath[name])]
        ref_arr = []

        task, people = tuple(map(int, fileInput[0].split(" ")))
        for line in range(1, task + 1):
            ref_arr.append(tuple(map(int, fileInput[line].split(" "))))

        # print(scheduleIntervals(ref_arr, people))
        fileOutput = [str(scheduleIntervals(ref_arr, people))]
        writeLines(outPath[name], fileOutput)


if __name__ == "__main__":
    main()
