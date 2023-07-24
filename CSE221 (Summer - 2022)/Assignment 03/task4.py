# Problem -04
# Warning! - May have error.


def readLines(file_path: str) -> list:

    with open(file_path, "r") as file:
        lines: list = file.readlines()
        return lines


def writeLines(file_path: str, lines: list) -> None:

    with open(file_path, "w") as file:
        file.writelines(" ".join(lines))


class AdjNode:
    def __init__(self, value) -> None:
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, total) -> None:
        self.length = total
        self.graph = [None] * self.length

    def add_edge(self, source, destination):

        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

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


def BFS(visited: list, graph: list, node: AdjNode, endPoint: AdjNode):
    import queue

    q = queue.Queue()

    path_len = 0

    visited[node] = node
    q.put(node)

    while not q.empty():
        m = q.get()

        if m == endPoint:
            break

        node = graph[m]
        path_len += 1
        while node is not None:

            if visited[node.vertex] == None:
                visited[node.vertex] = node.vertex
                q.put(node.vertex)

            node = node.next

    return path_len


def main():

    output_list = []
    input_list = [lines.replace("\n", "") for lines in readLines("Input4.txt")]
    input_list = [lines for lines in input_list if lines != ""]

    line = 1
    for _ in range(int(input_list[0])):
        temp = list(map(int, input_list[line].split(" ")))
        vertices, edges = temp[0], temp[1]

        graph = Graph(vertices + 1)

        line += 1

        for _ in range(edges):
            index = line

            vertex = list(map(int, input_list[index].split(" ")))
            graph.add_edge(vertex[0], vertex[1])

            line += 1

        output_list.append(graph)

    visited_graph_1 = [None] * (output_list[0].length + 1)
    path_1 = BFS(visited_graph_1, output_list[0].graph, 1, 3)

    visited_graph_2 = [None] * (output_list[1].length + 1)
    path_2 = BFS(visited_graph_2, output_list[1].graph, 1, 4)

    result = []
    result.append(str(path_1))
    result.append(str(path_2))

    writeLines("Output4.txt", result)


if __name__ == "__main__":
    main()
