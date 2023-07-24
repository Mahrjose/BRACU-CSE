# ================================ Searching & Sorting ================================


def findMaxValue(list):
    val = list[0]
    for i in list:
        if val < abs(i):
            val = abs(i)
    return val


class KeyIndex:
    def __init__(self, arr):

        self.maxValue = findMaxValue(arr)

        self.aux = [0] * ((self.maxValue * 2) + 1)

        for i in arr:
            if self.aux[self.maxValue + i] == 0:
                self.aux[self.maxValue + i] = 1
            else:
                self.aux[self.maxValue + i] = self.aux[self.maxValue + i] + 1

    def search(self, key):
        key = int(key)

        if key + self.maxValue < 0 or key + self.maxValue >= len(self.aux):
            return False
        else:
            if self.aux[key + self.maxValue] != 0:
                return True
            else:
                return False

    def sort(self):
        index = 0

        arrSize = 0
        for item in self.aux:
            arrSize += item

        arr = [0] * arrSize

        for i in range(0, len(self.aux)):
            if index >= len(arr):
                print(arr)
                break

            if self.aux[i] >= 1:
                for _ in range(0, self.aux[i]):
                    arr[index] = i - self.maxValue
                    index += 1

        return arr


# ================================ Searching & Sorting Testing ================================
print("================ Searching & Sorting ================\n")

list = [-5, 8, 4, 6, 1, -8, -10]
print(f"Given Array: {list}")

key_indx = KeyIndex(list)
print("")

# Searching
try:
    var = 4
    # var = int(input("Search for : "))
    print(f"Searing for -> {var}")
except ValueError:
    var = 3
    print(
        "User didn't manually entered the search value. Searching for default value 3.\n"
    )

if key_indx.search(var):
    print(f"{var} is in the list.\n")
else:
    print(f"{var} is not in the list.\n")

# Sorting
print("Sorted List -> ", end="")
key_indx.sort()
print()

# ================================ Hashtable ================================

# I've implemented the debug_mode because I was bored :3 . It's Not related to the task.
# I've added / commented the same code at the end without the debug_mode. Also, it's by default
# Turned off. But If you don't like the print statements inside the code Please uncomment the
# Clean code / code without debug mode. Thank you :)


class Hashtable:
    def __init__(self, size=9, debug_mode=False) -> None:
        self.size = size
        self.table = [0] * size

        # Debug Mode Flag for turning on/off some
        # print statements to help debugging
        self.debug_mode = debug_mode
        if debug_mode:
            print(f"\n[DEBUG MODE] Created Hashtable with Size - {self.size}\n")

    def hashKey(self, string):

        vowels = "AEIOUaeiou"
        digits = "0123456789"

        total_consonant = 0
        digit_sum = 0

        for char in string:
            # If char is consonant
            if char not in vowels and char not in digits:
                total_consonant += 1

            elif char.isdigit():
                digit_sum += int(char)

        hash_key = (total_consonant * 24) + digit_sum
        return hash_key

    def insert(self, string):

        hash_key = self.hashKey(string)
        position = hash_key % self.size

        if self.debug_mode:
            print(
                f"[DEBUG MODE] String - {string}\n[DEBUG MODE] HashKey - {hash_key}\n[DEBUG MODE] Position - {position}"
            )

        # Loop start from 1 because we need to add 1
        # with hashkey every iteration
        for index in range(1, self.size):
            if self.table[position] == 0:
                self.table[position] = string

                if self.debug_mode:
                    print(f"[DEBUG MODE] String inserted in Position - {position}")
                    print(f"[DEBUG MODE] Current HashTable -> \n{self.table}\n\n")

                break

            else:
                position = (hash_key + index) % self.size

                if self.debug_mode:
                    print(
                        f"> Current Position is not empty. New Position -> {position}"
                    )

    def print(self):
        print("Printing Hashtable -> \n")

        for string in range(self.size):
            print(self.table[string])


# ================================ Hashtable Testing ================================
print("================ Hashtable & Hashing ================\n")

strings = [
    "ST1E89B8A32",
    "ZJO9V49NDOU",
    "X9ZAR2JD6F7",
    "KD9LNX46TT2",
    "G94F5SMC2DG",
    "5YLHRBO79CT",
    "WN2NY54F22D",
    "YVRFKVUOH6Y",
    "5W8UWJSDCJH",
]

hash_table = Hashtable(debug_mode=False)

for string in strings:
    hash_table.insert(string)

hash_table.print()


# =============================== Hashing Without Debug Mode ============================
#
#
# class Hashtable:
#     def __init__(self, size=9) -> None:
#         self.size = size
#         self.table = [0] * size

#     def hashKey(self, string):

#         vowels = "AEIOUaeiou"
#         digits = "0123456789"

#         total_consonant = 0
#         digit_sum = 0

#         for char in string:
#             # If char is consonant
#             if char not in vowels and char not in digits:
#                 total_consonant += 1

#             elif char.isdigit():
#                 digit_sum += int(char)

#         hash_key = (total_consonant * 24) + digit_sum
#         return hash_key

#     def insert(self, string):

#         hash_key = self.hashKey(string)
#         position = hash_key % self.size

#         # Loop start from 1 because we need to add 1
#         # with hashkey every iteration
#         for index in range(1, self.size):
#             if self.table[position] == 0:
#                 self.table[position] = string
#                 break

#             else:
#                 position = (hash_key + index) % self.size

#     def print(self):
#         print("Printing Hashtable -> \n")

#         for string in range(self.size):
#             print(self.table[string])


# print("================ Hashtable & Hashing ================\n")

# strings = [
#     "ST1E89B8A32",
#     "ZJO9V49NDOU",
#     "X9ZAR2JD6F7",
#     "KD9LNX46TT2",
#     "G94F5SMC2DG",
#     "5YLHRBO79CT",
#     "WN2NY54F22D",
#     "YVRFKVUOH6Y",
#     "5W8UWJSDCJH",
# ]

# hash_table = Hashtable()


# for string in strings:
#     hash_table.insert(string)

# hash_table.print()
