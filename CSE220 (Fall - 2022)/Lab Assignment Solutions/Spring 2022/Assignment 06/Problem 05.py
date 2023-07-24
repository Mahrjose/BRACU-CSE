# Problem -05


class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class Doublylinkedlist:
    def __init__(self, array):
        self.head = Node(array[0], None, None)
        tail = self.head
        for i in range(1, len(array)):
            new_node = Node(array[i], None, tail)
            tail.next = new_node
            tail = new_node

    def showList(self):
        if self.head.next is None:
            print("Empty list")
        else:
            head = self.head
            while self.head is not None:
                if head.next is None:
                    print(head.value)
                    break
                else:
                    print(head.value, end=" <-> ")
                    head = head.next

    def insertion_sort(self):
        head = self.head
        if head == None:
            return
        else:
            while head is not None:
                tail = head.next
                while tail and tail.prev is not None and tail.value < tail.prev.value:
                    temp = tail.value
                    tail.value = tail.prev.value
                    tail.prev.value = temp

                    tail = tail.prev

                head = head.next


print("\nNo. 5 - Sorting Doubly LinkedList with Insertion Sort -->\n")
array = [4, 7, 45, 9, 33, 2, 8]
doublylinkedlist = Doublylinkedlist(array)
print("Unsorted LinkedList ===> ", end="")
doublylinkedlist.showList()
doublylinkedlist.insertion_sort()
print("Sorted LinkedList ===> ", end="")
doublylinkedlist.showList()
print("\n")
