class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class Doublylist:
    def __init__(self, a):
        self.head = Node(a[0], None, None)
        tail = self.head
        for i in range(1, len(a)):
            new_node = Node(a[i], None, tail)
            tail.next = new_node
            tail = new_node

    def showList(self):
        if self.head.next is None:
            print("Empty list")
        else:
            head = self.head
            while self.head is not None:
                if head.next is None:
                    print(head.data)
                    break
                else:
                    print(head.data, "->", end=" ")
                    head = head.next

    def insert(self, newElement):
        head = self.head
        new_node = Node(newElement, None, None)
        while new_node.next is None:
            if head.data == new_node.data:
                print("key already exists")
                break
            if head.next is None:
                head.next = new_node
                new_node.prev = head
                break
            head = head.next

    def insert_index(self, newElement, index):
        condition = False
        if index == 0:
            new_node = Node(newElement, self.head, None)
            self.head.prev = new_node
            self.head = new_node
        else:
            n = self.head
            counter = 0
            while n is not None:
                n = n.next
                if condition is False:
                    n = self.head
                    while n is not None:
                        counter = counter + 1
                        if n.data == newElement:
                            condition = True
                            print("key already exists")
                        if counter == index:
                            new_node = Node(newElement, n.next, n.prev)
                            n.next.prev = new_node
                            n.prev.next = new_node
                        n = n.next

    def remove(self, index):
        if self.head == None:
            print("list is empty")
        else:

            counter = 0
            head = self.head
            while head is not None:

                if index == counter:
                    head.next.prev = head.prev
                    head.prev.next = head.next
                counter = counter + 1
                head = head.next
            if index > counter:
                print("index out of range")

    def removeKey(self, key):
        head = self.head
        while head is not None:
            if head.data == key:
                head.next.prev = head.prev
                head.prev.next = head.next
            head = head.next

        return key


arr = [1, 2, 3, 4, 5]

mylist = Doublylist(arr)
mylist.showList()
print("Insert 7")
mylist.insert(7)
mylist.showList()
print("Insert 6 at the 5th index")
mylist.insert_index(6, 5)
mylist.showList()
print("Remove 2")
mylist.remove(2)
mylist.showList()
key = mylist.removeKey(3)
print("Removed Key", key)
mylist.showList()
