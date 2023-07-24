# Problem -02


class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None


class LinkedList:

    # No. 1(a)
    def __init__(self, arr: list) -> None:
        self.head = None

        for element in arr:
            node = Node(element)

            if self.head == None:
                self.head = node
                node = self.head
                continue

            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def len(self) -> int:

        lenght: int = 0
        current: Node = self.head
        while current is not None:
            lenght += 1
            current = current.next

        return lenght

    # No. 2
    def showList(self) -> None:

        current: Node = self.head

        if current != None:
            while current is not None:
                if current.next == None:
                    print(current.element)
                else:
                    print(current.element, end=" -> ")

                current = current.next
        else:
            print("Empty List")

    # No. 3
    def isEmpty(self) -> bool:
        if self.len() > 0:
            return False
        else:
            return True

    # No. 4
    def clear(self) -> None:

        current: Node = self.head
        while current is not None:
            current.element = None
            current = current.next

        self.head = None

    # No. 5
    def insert(self, newElement) -> None:

        node: Node = Node(newElement)

        current: Node = self.head
        if current is None:
            self.head = node
            node = self.head

        else:
            while current is not None:
                if current.element == newElement:
                    print("Element already Exists")
                    return

                if current.next == None:
                    break
                else:
                    current = current.next

            current.next = node

    # No. 6
    def insert_with_index(self, newElement, index: int) -> None:
        if index >= 0 and index < self.len():

            current: Node = self.head
            while current is not None:
                if current.element == newElement:
                    print("Element already Exists")
                    return

                current = current.next

            node: Node = Node(newElement)

            if index == 0:
                node.next = self.head
                self.head = node

            elif index == self.len() - 1:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node

            else:
                counter = 0
                current = self.head
                while current is not None:
                    if counter == index - 1:
                        next = current.next
                        current.next = node
                        node.next = next

                    counter += 1
                    current = current.next

        else:
            print("Invalid Index")
            return

    # No. 7
    def remove(self, delete_key):

        current = self.head
        prev = self.head
        counter = 0

        while current is not None:
            if current.element == delete_key:
                if current == self.head:
                    self.head = self.head.next
                    return current.element

                else:
                    prev.next = current.next
                    return current.element

            current = current.next

            if counter > 0:
                prev = prev.next

            counter += 1


def main():
    MyList = LinkedList([1, 2, 3, 4])
    ListToClear = LinkedList([1, 2, 3, 4, 5])
    EmptyList = LinkedList([])
    ############--No. 01 & No. 2--###############
    print()
    print("*No. 1(a) & 2 -->")
    print("LinkedList from [1, 2, 3, 4] ====> ", end="")
    MyList.showList()
    print("LinkedList from [] ====> ", end="")
    EmptyList.showList()
    print("\n")
    print()
    ###############--No. 03--###############
    print("*No. 3 -->")
    print(f"Is 1 -> 2 -> 3 -> 4 Empty? ====> {MyList.isEmpty()}")
    MyList.isEmpty()
    print(f"Is [] Empty? ====> {EmptyList.isEmpty()}")
    print("\n")
    print()
    ###############--No. 04--###############
    print("*No. 4 -->")
    print("Clearing 1 -> 2 -> 3 -> 4 -> 5 ====> ", end="")
    ListToClear.clear()
    ListToClear.showList()
    print("\n")
    print()
    ###############--No. 05--###############
    print("*No. 5 -->")
    print("Inserting 5 into 1 -> 2 -> 3 -> 4 ====> ", end="")
    MyList.insert(5)
    MyList.showList()
    print()
    print("Inserting 2 into 1 -> 2 -> 3 -> 4 -> 5 ====> ", end="")
    MyList.insert(5)
    print("\n")
    print()
    ###############--No. 06--###############
    print("*No. 6 -->")
    print("Inserting value 1 in index 1 of 1 -> 2 -> 3 -> 4 -> 5 ====> ", end="")
    MyList.insert_with_index(1, 1)
    print()
    print("Inserting value 6 in index 7 of 1 -> 2 -> 3 -> 4 -> 5 ====> ", end="")
    MyList.insert_with_index(6, 8)
    print()
    print("Inserting value 0 in index 0 of 1 -> 2 -> 3 -> 4 -> 5 ====> ", end="")
    MyList.insert_with_index(0, 0)
    MyList.showList()
    print()
    print("Inserting value 3.5 in index 4 of 0 -> 1 -> 2 -> 3 -> 4 -> 5 ====> ", end="")
    MyList.insert_with_index(3.5, 4)
    MyList.showList()
    print()
    print(
        "Inserting value 6 in index 6 of 0 -> 1 -> 2 -> 3 -> 3.5 -> 4 -> 5 ====> ",
        end="",
    )
    MyList.insert_with_index(6, 6)
    MyList.showList()
    print("\n")
    print()
    ###############--No. 07--################
    print("*No. 7 -->")
    print("Removing 3.5 from 0 -> 1 -> 2 -> 3 -> 3.5 -> 4 -> 5 -> 6 ====> ", end="")
    MyList.remove(3.5)
    MyList.showList()
    print()


if __name__ == "__main__":
    main()
