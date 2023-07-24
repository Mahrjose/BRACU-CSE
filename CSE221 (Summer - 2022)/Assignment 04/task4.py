from numpy import Inf
import heapq

fileInput, fileOutput = (open(f"input4.txt", "r"), open(f"output4.txt", "w"))


def graph(edges):
    paths = {}
    for _ in range(edges):
        start, end, weight = fileInput.readline().split()

        if start in paths:
            paths[start].append((end, int(weight)))
        else:
            paths[start] = [(end, int(weight))]

        if end not in paths:
            paths[end] = []

    return paths


def dijkstra(graph, src, dest):

    if len(graph) == 0:
        return 0

    pq = []
    dist = {src: 0}
    visited = {src: False}
    pq.append((0, src))

    heapq.heapify(pq)

    for vertex in graph:
        if vertex != src:
            dist[vertex] = Inf
            visited[vertex] = False
            pq.append((dist[vertex], vertex))

    heapq.heapify(pq)

    while len(pq) != 0:
        weight, v = heapq.heappop(pq)
        if visited[v]:
            continue

        visited[v] = True

        for i in graph[v]:
            neighbour, current_weight = i
            total = weight + current_weight

            if total < dist[neighbour]:
                dist[neighbour] = total
                heapq.heappush(pq, (total, neighbour))

    return dist[dest]


def main():
    nodes, edges = fileInput.readline().strip().split()
    g = graph(int(edges))
    fileOutput.write(str(dijkstra(g, "Motijheel", "MOGHBAZAR")) + "\n")


if __name__ == "__main__":
    main()


"""
We should not use bfs for weighted graphs as it'll mark the first path it finds as the shortest path and
if it finds more shorter path later it'll simply ignore them. Becase bfs assumes that all weigths are same 
just like in a unweigted graph. But, dijkstra algorithm can look for better paths and it'll update if it find
more shorter path later.
"""
