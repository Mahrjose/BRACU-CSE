class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p


class DoublyList:
    def __init__(self, arr):
        #  Design the constructor based on data type of a. If 'a' is built in python list then
        #  Creates a linked list using the values from the given array.

        # Creating a DummyHead
        self.dummyHead = Node(None, None, None)
        # Creting DummyHeaded Doubly circular LinkedList
        self.dummyHead.prev = self.dummyHead.next = self.dummyHead

        if type(arr) == Node:

            self.dummyHead.next = arr
            arr.prev = self.dummyHead

            self.dummyHead.prev = arr
            arr.next = self.dummyHead

        else:

            elem = arr[0]
            tail = Node(elem, None, None)

            self.dummyHead.next = tail
            tail.prev = self.dummyHead

            self.dummyHead.prev = tail
            tail.next = self.dummyHead

            head = self.dummyHead

            for i in range(1, len(arr)):

                newNode = Node(arr[i], None, None)

                # add newNode & tail
                # then make the newNode a newTail
                newNode.prev = tail
                tail.next = newNode
                tail = newNode

                # make the LinkedList circular
                head.prev = tail
                tail.next = head

    # Counts the number of Nodes in the list
    def countNode(self):

        counter = 0

        head = self.dummyHead
        current = head.next

        while current != head:
            current = current.next
            counter += 1

        return counter

    # prints the elements in the list
    def forwardprint(self):

        head = self.dummyHead
        tail = head.next

        while tail != head:

            if tail.next == head:
                print(tail.element)

            else:
                print(tail.element, end=", ")

            tail = tail.next

    # prints the elements in the list backward
    def backwardprint(self):

        head = self.dummyHead
        tail = head.prev

        while tail != head:
            if tail.prev == head:
                print(tail.element)

            else:
                print(tail.element, end=", ")

            tail = tail.prev

    # returns the reference of the at the given index. For invalid index return None.
    def nodeAt(self, idx):

        counter = 0
        nodeCount = self.countNode()

        head = self.dummyHead
        tail = head.next

        # Index Validation
        if idx >= nodeCount or idx < 0:
            return None

        # We don't need loop to determine these
        if idx == nodeCount:
            return head.prev

        elif idx == 0:
            return tail

        else:
            while tail != head:
                if counter == idx:
                    return tail

                tail = tail.next
                counter += 1

    # returns the index of the containing the given element.
    # if the element does not exist in the List, return -1.
    def indexOf(self, elem):

        head = self.dummyHead
        tail = head.next
        index = 0

        while tail != head:

            if tail.element == elem:
                return index

            tail = tail.next
            index += 1

        return -1

    # inserts containing the given element at the given index Check validity of index.
    def insert(self, elem, idx):

        head = self.dummyHead
        tail = head.next
        counter = 0

        # Index Validation
        if idx >= self.countNode() + 1 or idx < 0:
            return None

        newNode = Node(elem, None, None)

        while tail != head:

            if counter == idx:

                pred = tail.prev

                newNode.next = tail
                newNode.prev = pred

                pred.next = newNode
                tail.prev = newNode

            tail = tail.next
            counter += 1

    # removes at the given index. returns element of the removed node.
    # Check validity of index. return None if index is invalid.
    def remove(self, idx):

        head = self.dummyHead
        tail = head.next
        counter = 0

        # Index Validation
        if idx >= self.countNode() or idx < 0:
            return None

        while tail != head:
            if counter == idx:

                predNode = tail.prev
                nextNode = tail.next

                predNode.next = nextNode
                nextNode.prev = predNode

                removed = tail.element

                # Garbage Collection
                tail.prev = tail.next = None
                tail.element = None
                # tail = None

                return str(removed)

            tail = tail.next
            counter += 1


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1)  # Creates a linked list using the values from the array

h1.forwardprint()  # This should print: 10,20,30,40.
h1.backwardprint()  # This should print: 40,30,20,10.
print(h1.countNode())  # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(
    myNode.element
)  # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index)  # This should print: 3. In case of element that
# doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2)  # uses the  constructor
h2.forwardprint()  # This should print: 10,20,30,40.

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85, 0)
h2.forwardprint()  # This should print: 85,10,20,30,40.
h2.backwardprint()  # This should print: 40,30,20,10,85.

print()
h2.insert(95, 3)
h2.forwardprint()  # This should print: 85,10,20,95,30,40.
h2.backwardprint()  # This should print: 40,30,95,20,10,80.

print()
h2.insert(75, 6)
h2.forwardprint()  # This should print: 85,10,20,95,30,40,75.
h2.backwardprint()  # This should print: 75,40,30,95,20,10,85.


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3)  # uses the constructor
h3.forwardprint()  # This should print: 10,20,30,40,50,60,70.

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: " + h3.remove(0))  # This should print: Removed element: 10
h3.forwardprint()  # This should print: 20,30,40,50,60,70.
h3.backwardprint()  # This should print: 70,60,50,40,30,20.
print("Removed element: " + h3.remove(3))  # This should print: Removed element: 50
h3.forwardprint()  # This should print: 20,30,40,60,70.
h3.backwardprint()  # This should print: 70,60,40,30,20.
print("Removed element: " + h3.remove(4))  # This should print: Removed element: 70
h3.forwardprint()  # This should print: 20,30,40,60.
h3.backwardprint()  # This should print: 60,40,30,20.
