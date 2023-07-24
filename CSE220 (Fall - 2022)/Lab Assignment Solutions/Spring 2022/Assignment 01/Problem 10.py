# Problem -02


def intersection(array_1, start_1, size_1, array_2, start_2, size_2):

    intersection_array = []

    # Array 1
    array_1_A = []
    array_1_B = []
    for i in range(1, len(array_1)):
        if array_1[i] == 0 and array_1[i - 1] != 0:
            for j in range(i):
                array_1_B.append(array_1[j])

    for i in range(1, len(array_1)):
        if array_1[i] != 0 and array_1[i - 1] == 0:
            for j in range(i, len(array_1)):
                array_1_A.append(array_1[j])

    # Array 2
    array_2_A = []
    array_2_B = []
    for i in range(1, len(array_2)):
        if array_2[i] == 0 and array_2[i - 1] != 0:
            for j in range(i):
                array_2_B.append(array_2[j])

    for i in range(1, len(array_2)):
        if array_2[i] != 0 and array_2[i - 1] == 0:
            for j in range(i, len(array_2)):
                array_2_A.append(array_2[j])

    # Combine
    new_array_1 = array_1_A + array_1_B
    new_array_2 = array_2_A + array_2_B

    # search for common items
    for i in range(len(new_array_1)):
        new = new_array_1[i]
        for i in range(len(new_array_2)):
            if new == new_array_2[i]:
                if new not in intersection_array:
                    intersection_array.append(new)
                else:
                    continue
            else:
                continue

    print(intersection_array)


def main():
    array_1 = [40, 50, 0, 0, 0, 10, 20, 30]
    array_2 = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]

    intersection(array_1, 5, 5, array_2, 8, 7)


if __name__ == "__main__":
    main()
