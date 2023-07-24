from cmath import inf
import heapq

fileInput, fileOutput = (open(f"input2.txt", "r"), open(f"output2.txt", "w"))


def graph(edges):
    paths = {}
    for _ in range(edges):
        start, end, weight = fileInput.readline().split()

        if int(start) in paths:
            paths[int(start)].append((int(end), int(weight)))
        else:
            paths[int(start)] = [(int(end), int(weight))]

        if int(end) not in paths:
            paths[int(end)] = []

    return paths


def dijkstra(graph, src, dest):

    if len(graph) == 0:
        return 1

    pq = []
    dist = {src: 0}
    visited = {src: False}
    pq.append((0, src))

    prev = {}
    heapq.heapify(pq)

    for vertex in graph:
        if vertex != src:
            dist[vertex] = inf
            visited[vertex] = False
            pq.append((dist[vertex], vertex))

            prev[vertex] = None

    heapq.heapify(pq)

    while len(pq) != 0:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue

        visited[u] = True

        for i in graph[u]:
            neighbour, current_weight = i
            total = weight + current_weight

            if total < dist[neighbour]:
                dist[neighbour] = total
                prev[neighbour] = u
                heapq.heappush(pq, (total, neighbour))

    arr = []
    current = dest

    while True:
        arr.insert(0, int(current))
        if current == 1:
            break

        current = prev[int(current)]

    string = " ".join([str(i) for i in arr])
    return string


def main():
    for _ in range(int(fileInput.readline().strip())):
        nodes, edges = fileInput.readline().strip().split()
        g = graph(int(edges))

        fileOutput.write(str(dijkstra(g, 1, nodes)) + "\n")


if __name__ == "__main__":
    main()
