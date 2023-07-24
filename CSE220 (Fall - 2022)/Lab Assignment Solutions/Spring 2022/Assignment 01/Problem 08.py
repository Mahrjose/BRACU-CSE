# Problem -08


def repetition(arr) -> bool:

    repeated_values = []
    # Create a dictionary for counting item repetition
    dictionary = {item: arr.count(item) for item in arr}

    # if item repetition value is more than 1,
    # item has been repeated so add to a list for more experiment
    for repeated_count in dictionary.values():
        if repeated_count > 1:
            repeated_values.append(repeated_count)

    # if 2 or more value are the same, length of set would be
    # smaller than the main list meaing there're same repeated value
    # for 2 or more items
    if len(repeated_values) == len(set(repeated_values)):
        return False
    else:
        return True


def main():
    source = [4, 5, 6, 6, 4, 3, 6, 4]
    print(repetition(source))

    source = [3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6]
    print(repetition(source))


if __name__ == "__main__":
    main()
