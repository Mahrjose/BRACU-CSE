global total, odd_parity, even_parity, no_parity, is_palindrome, not_palindrome
odd_parity = 0
even_parity = 0
no_parity = 0
is_palindrome = 0
not_palindrome = 0


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


def recorder() -> list:

    global total, odd_parity, even_parity, no_parity, is_palindrome, not_palindrome

    record: list = [
        f"Percentage of odd parity: {(odd_parity/total) * 100}%",
        f"Percentage of even parity: {(even_parity/total) * 100}%",
        f"Percentage of no parity: {(no_parity/total) * 100}%",
        f"Percentage of palindrome: {(is_palindrome/total) * 100}%",
        f"Percentage of non-palindrome: {(not_palindrome/total) * 100}%",
    ]

    return record


def isPalindrome(word: str) -> str:
    global is_palindrome, not_palindrome

    if word == "":
        not_palindrome += 1
        return "not a Palindrome"

    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            not_palindrome += 1
            return "not a Palindrome"

    is_palindrome += 1
    return "a palindrome"


def parityChecker(str_num: str) -> str:
    global no_parity, even_parity, odd_parity

    if "." in str_num:
        parity = f"{str_num} cannot have parity"
        no_parity += 1
        return parity

    elif int(str_num) % 2 == 0:
        parity = f"{str_num} has even parity"
        even_parity += 1
        return parity

    elif int(str_num) % 2 != 0:
        parity = f"{str_num} has odd parity"
        odd_parity += 1
        return parity


def main():
    global total
    lines: list = []
    output: list = []
    # Please checkout the files path.
    # Program may give error if the path is not correct
    # and in that case give the full file path.
    lines = readLines("Input.txt")
    total = len(lines)
    for line in lines:
        line = line.replace("\n", "")
        str_num, word = line.split(" ")

        parity = parityChecker(str_num)
        palindrome = isPalindrome(word)

        output.append(f"{parity} and {word} is {palindrome}")

    record: list = recorder()
    writeLines("Output.txt", output)
    writeLines("Record.txt", record)


if __name__ == "__main__":
    main()
