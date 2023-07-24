# Problem -07


def maxBunch(arr) -> None:

    streak, currnt_streak = 1, 1
    for i in range(len(arr)):
        # if this is the last element, print the result
        if i == len(arr) - 1:
            print(streak)
            return

        elif arr[i] == arr[i + 1]:
            currnt_streak += 1
        else:
            currnt_streak = 1

        # if current streak is higher than previous streaks
        # make this the new current streak
        if currnt_streak >= streak:
            streak = currnt_streak


def main():
    source = [1, 2, 2, 3, 4, 4, 4]
    maxBunch(source)

    source = [1, 1, 2, 2, 1, 1, 1, 1]
    maxBunch(source)


if __name__ == "__main__":
    main()
