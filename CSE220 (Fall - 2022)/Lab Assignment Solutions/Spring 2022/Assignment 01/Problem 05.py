# Problem -05


def Splitting_array(arr):
    arr_A = [0]
    arr_B = []
    flag = None

    for i in range(len(arr)):
        if i == 0:
            arr_A[i] = arr[i]
            arr_B = arr[i + 1 : (len(arr))]
            if sum(arr_A) == sum(arr_B):
                flag = True
                break
            else:
                arr_A = []
                flag = False
        else:
            arr_A = arr[0 : i + 1]
            arr_B = arr[i + 1 : (len(arr))]
            if sum(arr_A) == sum(arr_B):
                flag = True
                break
            else:
                flag = False
    print(flag)


def main():
    arr = [1, 1, 1, 2, 1]
    Splitting_array(arr)

    arr = [2, 1, 1, 2, 1]
    Splitting_array(arr)

    arr = [10, 3, 1, 2, 10]
    Splitting_array(arr)


if __name__ == "__main__":
    main()
