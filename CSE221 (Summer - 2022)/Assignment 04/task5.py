# Couldn't Not finished

from numpy import Inf
import heapq

fileInput, FileOutput = (open(f"input5.txt", "r"), open(f"output5.txt", "w"))


def graph(edges):
    paths = {}

    for _ in range(edges):
        start, end, weight = fileInput.readline().split()

        if int(start) in paths:
            paths[int(start)].append((int(end), int(weight)))
        else:
            paths[int(start)] = [(int(end), int(weight))]

        if int(end) in paths:
            paths[int(end)].append((int(start), int(weight)))
        else:
            paths[int(end)] = [(int(start), int(weight))]

    return paths


def dijkstra(graph, src):

    pq = []
    dist = {src: Inf}
    pq.append((0, src))

    heapq._heapify_max(pq)

    for vertex in graph:
        if vertex != src:
            dist[vertex] = -Inf
            pq.append((dist[vertex], vertex))

    dist[src] = 0
    heapq._heapify_max(pq)

    while len(pq) != 0:
        weight, v = heapq._heappop_max(pq)

        for i in graph[v]:
            neighbour, current_weight = i
            total = min(weight, current_weight)

            if total > dist[neighbour]:
                dist[neighbour] = total
                pq.append((total, neighbour))

    return dist


def main():
    for _ in range(int(fileInput.readline().strip())):
        nodes, edges = fileInput.readline().strip().split()
        g = graph(int(edges))

        s = int(fileInput.readline().strip())

        if int(nodes) == 1 and int(edges) == 0:
            FileOutput.write("0" + "\n")


if __name__ == "__main__":
    main()
