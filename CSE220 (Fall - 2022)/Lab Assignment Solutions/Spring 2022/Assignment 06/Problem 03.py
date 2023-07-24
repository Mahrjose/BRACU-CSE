# Problem -03


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, arr):
        self.head = None
        tail = None

        for i in arr:
            new_node = Node(i)
            if self.head == None:
                self.head = new_node
                tail = new_node

            else:
                tail.next = new_node
                tail = new_node

    def showList(self):

        current = self.head

        if current is None:
            print("Empty List")
        else:
            while current is not None:
                if current.next is None:
                    print(current.value)
                    break
                else:
                    print(current.value, end=" -> ")
                    current = current.next

    def bubble_sort(self):
        head = self.head
        tail = None

        if self.head is None:
            return

        else:
            while head != None:
                tail = head.next
                while tail != None:

                    if tail.value < head.value:
                        temp = head.value
                        head.value = tail.value
                        tail.value = temp

                    tail = tail.next

                head = head.next


print("\nNo. 3 - Sorting Singly LinkedList with Bubble Sort -->\n")
array = [4, 7, 45, 9, 33, 2, 8]
linkedlist = LinkedList(array)
print("Unsorted LinkedList ===> ", end="")
linkedlist.showList()
linkedlist.bubble_sort()
print("Sorted LinkedList ===> ", end="")
linkedlist.showList()
print("\n")
