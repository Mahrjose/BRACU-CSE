# Problem 01


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def main():
    MyList = LinkedList()
    elem1 = Node(3)
    MyList.head = elem1


if __name__ == "__main__":
    main()
