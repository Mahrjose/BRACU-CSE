# Problem -04


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

    def selection_sort(self):
        head = self.head

        if self.head is None:
            return
        else:
            while head.next != None:
                tail = head
                val = head.value
                next_val = head.next

                while next_val != None:
                    if val > next_val.value:
                        val = next_val.value
                        tail = next_val

                    next_val = next_val.next

                temp = head.value
                head.value = tail.value
                tail.value = temp

                head = head.next


print("\nNo. 4 - Sorting Singly LinkedList with Selection Sort -->\n")
array = [4, 7, 45, 9, 33, 2, 8]
linkedlist = LinkedList(array)
print("Unsorted LinkedList ===> ", end="")
linkedlist.showList()
linkedlist.selection_sort()
print("Sorted LinkedList ===> ", end="")
linkedlist.showList()
print("\n")
