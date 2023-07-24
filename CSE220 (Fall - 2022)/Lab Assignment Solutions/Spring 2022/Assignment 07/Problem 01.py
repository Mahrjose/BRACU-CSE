# Problem -01


def maxValue(list):
    val = list[0]
    for i in list:
        if val < abs(i):
            val = abs(i)
    return val


class keyIndex:
    def __init__(self, k):
        self.k = k

        global max_val
        max_val = maxValue(self.k)
        self.temp = [0] * ((max_val * 2) + 1)

        for i in self.k:
            if 0 == self.temp[max_val + i]:
                self.temp[max_val + i] = 1
            else:
                self.temp[max_val + i] = self.temp[max_val + i] + 1

    def search(self, key):
        k = int(key)
        if k + max_val < 0 or k + max_val >= len(self.temp):
            return False
        else:
            if self.temp[k + max_val] != 0:
                return True
            else:
                return False

    def sort(self):
        indx = 0
        for i in range(0, len(self.temp)):
            if len(self.k) <= indx:
                print(self.k)
                break

            if self.temp[i] >= 1:
                for _ in range(0, self.temp[i]):
                    self.k[indx] = i - max_val
                    indx += 1

    def printlist(self):
        print(self.temp)


print("No. 1 -->")
list = [-5, 8, 4, 6, 1, -8, -10]
key_indx = keyIndex(list)
key_indx.printlist()

print("")
try:
    var = int(input("Search for : "))
except ValueError:
    var = 3
    print("User didnot manually enter the search value. Searching for default value 3.")

if key_indx.search(var):
    print(f"{var} is in the list.")
else:
    print(f"{var} is not in the list.")

print()
print("Sorted List -> ", end="")
key_indx.sort()
