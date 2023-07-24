# Problem -03


class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None


class LinkedList:
    def __init__(self, array) -> None:
        self.head = None

        for element in array:

            node = Node(element)

            if self.head == None:
                self.head = node
                node = self.head
                continue

            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def push(self, element):

        if isinstance(element, Node):
            node = element
        else:
            node: Node = Node(element)

            if self.head is None:
                self.head = node
                node = self.head
                return

            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def showList(self) -> None:
        current = self.head

        if current is not None:
            while current is not None:
                if current.next is None:
                    print(current.element)

                else:
                    print(current.element, end=" -> ")

                current = current.next
        else:
            print("Empty LinkedList")

    # No. 1
    def onlyEven(self):

        evenLinkedList = LinkedList([])

        current = self.head
        while current is not None:
            if current.element % 2 == 0:
                evenLinkedList.push(current.element)

            current = current.next

        return evenLinkedList.showList()

    def count(self, element):

        counter = 0

        if self.head == None:
            return counter

        current = self.head
        while current is not None:
            if current.element == element:
                counter += 1

            current = current.next

        return counter

    # No. 2
    def isInList(self, element) -> bool:
        if self.count(element) > 0:
            return True
        else:
            return False

    # No. 3
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    # No. 4
    def sort(self):
        pass

    # No. 5
    def sum(self):
        sum = 0

        current = self.head
        while current is not None:
            sum += current.element
            current = current.next

        return sum

    # No. 6
    def rotateLeft(self, times=1):
        pass

    def rotateRight(self, times=1):
        pass


MyList = LinkedList([1, 2, 5, 3, 8])
MyList2 = LinkedList([101, 120, 25, 91, 87, 1])
###############--No. 01--###############
print()
print("*No. 1 -->")
print("OnlyEven LinkedList from ===> ", end="")
MyList.showList()
MyList.onlyEven()
print()
print("OnlyEven LinkedList from ===> ", end="")
MyList2.showList()
MyList2.onlyEven()
print("\n")
print()
###############--No. 02--###############
print("*No. 2 -->")
print("Is 7 in 1 -> 2 -> 5 -> 3 -> 8  ===> ", end="")
print(MyList.isInList(7))
print()
print("Is 87 in 101 -> 120 -> 25 -> 91-> 87 -> 1  ===> ", end="")
print(MyList2.isInList(87))
print("\n")
print()
###############--No. 03--###############
print("*No. 3 -->")
listToRev = LinkedList([1, 2, 5, 3, 8])
print("Reversing 1 -> 2 -> 5 -> 3 -> 8 ===> ", end="")
listToRev.reverse()
listToRev.showList()
print("\n")
print()
###############--No. 04--###############
print("*No. 4 -->")
print("\n")
print()
###############--No. 05--###############
print("*No. 5 -->")
print("Sum of all elements in 1 -> 2 -> 5 -> 3-> 8 ===> ", end="")
print(MyList.sum())
print("\n")
print()
###############--No. 06--###############
print("*No. 6 -->")
listToRotate1 = LinkedList([3, 2, 5, 1, 8])
listToRotate2 = LinkedList([3, 2, 5, 1, 8])
print("Rotating 3 -> 2 -> 5 -> 1-> 8 Left 2 times ===> ", end="")
listToRotate1.rotateLeft(2)
print()
print("Rotating 3 -> 2 -> 5 -> 1-> 8 Left 2 times ===> ", end="")
listToRotate2.rotateRight(2)
print("\n")
print()
