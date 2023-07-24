# Problem -02


vowels = ["A", "E", "I", "O", "U"]
consonants = [
    "B",
    "C",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


class Hashstring:
    def __init__(self, str):
        self.str = str

    def string_get(self):
        return self.str

    def string_key(self):
        val = 0
        var = 0

        for i in self.str:
            if i in consonants:
                val = val + 1
            if i not in consonants and i not in vowels:
                var += int(i)

        string_key = (val * 24) + var
        return string_key


class Hashtable:
    def __init__(self, size=9):
        self.size = size
        self.list = [0] * size

    def function(self, string_key):
        return string_key % self.size

    def add(self, s):
        val = s.string_key()
        position = self.function(val)
        for i in range(1, self.size):
            if self.list[position] == 0:
                self.list[position] = s.string_get()
                break
            else:
                position = (val + i) % self.size

    def print(self):
        for i in range(self.size):
            print(self.list[i])


hash_table = Hashtable()
list = [
    "ZJO9V49NDOU",
    "X9ZAR2JD6F7",
    "KD9LNX46TT2",
    "G94F5SMC2DG",
    "5YLHRBO79CT",
    "WN2NY54F22D",
    "YVRFKVUOH6Y",
    "ST1E89B8A32",
    "5W8UWJSDCJH",
]

print("No. 2 -->\n")
for i in list:
    s = Hashstring(i)
    hash_table.add(s)

hash_table.print()
