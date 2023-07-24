# Problem -01


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))


class AdjNode:
    def __init__(self, value) -> None:
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, total) -> None:
        self.length = total
        self.graph = [None] * self.length

    def add_edge(self, source, destination):

        new_node = AdjNode(destination)
        index = source

        # If No graph connection present in the index
        # add the newNode as a new connection
        if self.graph[index] == None:
            self.graph[index] = new_node
            new_node = self.graph[index]

        else:
            # If Graph Connection Already Present
            # travarse them and add the newNode
            # after the last Node
            node = self.graph[index]
            while node.next is not None:
                node = node.next

            node.next = new_node
            new_node = node.next

    def print_graph(self):

        graph = self.graph

        for i in range(1, self.length):
            if graph[i] is None:
                print(f"Vertex: {i}")
            else:
                print(f"Vertex: {i}", end=" -> ")

            node = graph[i]
            while node is not None:
                if node.next is None:
                    print(node.vertex, end="\n")
                    break

                print(node.vertex, end=" -> ")
                node = node.next


def main():

    input_list = [i.replace("\n", "") for i in readLines("Input1.txt")]

    graph = Graph(int(input_list[0]) + 1)

    for i in range(1, len(input_list)):
        connections = [int(j) for j in input_list[i].split(" ")]
        for j in range(1, len(connections)):
            graph.add_edge(connections[0], connections[j])

    graph.print_graph()


if __name__ == "__main__":
    main()
