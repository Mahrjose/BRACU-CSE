# Problem -02

# 2(a)
def decimalToBinary(num):
    if num == 0:
        return 0

    return decimalToBinary(num // 2) * 10 + (num % 2)


print("\nNo. 2(a)-->")
n = int(input("Input Decimal to find the binary -> "))
print(f"{n} in Binary is -> ", end="")
print(decimalToBinary(n))


# 2(b)
class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, element):
        node = Node(element)
        current = self.head

        if self.head is None:
            self.head = node
            node = self.head

        else:
            while current.next is not None:
                current = current.next

            current.next = node

    def printList(self):

        current = self.head
        while current is not None:
            print(f"({current.element} - {current.next})")
            current = current.next


MyList = LinkedList()
MyList.append(10)
MyList.append(20)
MyList.append(30)
MyList.append(40)


def linkedListAdd(head):
    if head == None:
        return 0

    return head.element + linkedListAdd(head.next)


print("\nNo. 2(b)-->")
print(linkedListAdd(MyList.head))

# 2(c)
def printReverse(head):
    if head == None:
        return

    printReverse(head.next)
    print(head.element)


print("\nNo. 2(c)-->")
printReverse(MyList.head)
