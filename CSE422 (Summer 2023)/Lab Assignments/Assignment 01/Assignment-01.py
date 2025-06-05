### CSE422 - Artificial Intelligence
### Assignment 01: A* Searching Algorithm
### ----------------------------------
### Name : Mirza Meherab Hosen Rudra
### ID   : 21101048
### Sec  : 10
### ----------------------------------

"""
Arad 366 Zerind 75 Timisoara 118 Sibiu 140
Craiova 160 Dobreta 120 RimnicuVilcea 146 Pitesti 138
Eforie 161 Hirsova 86
Fagaras 176 Sibiu 99 Bucharest 211
Giurgiu 77 Bucharest 90
Mehadia 241 Lugoj 70 Dobreta 75
Neamt 234 lasi 87
Sibiu 253 Oradea 151 Arad 140 RimnicuVilcea 80 Fagaras 99
Oradea 380 Zerind 71 Sibiu 151
Pitesti 100 RimnicuVilcea 97 Craiova 138 Bucharest 101
RimnicuVilcea 193 Sibiu 80 Craiova 146 Pitesti 97
Dobreta 242 Mehadia 75 Craiova 120
Hirsova 151 Urziceni 98 Eforie 86
lasi 226 Vaslui 92 Neamt 87
Lugoj 244 Timisoara 111 Mehadia 70
Timisoara 329 Arad 118 Lugoj 111
Urziceni 80 Bucharest 85 Hirsova 98 Vaslui 142
Vaslui 199 Urziceni 142 lasi 92 
Zerind 374 Oradea 71 Arad 75
Bucharest 0 Fagaras 211 Pitesti 101 Giurgiu 90 Urziceni 85
"""

import heapq

class GRAPH:
    def __init__(self):
        self.adjacencyList = {}

    def addEdges(self, firstNode, secondNode, dist=0):
        if firstNode not in self.adjacencyList:
            self.adjacencyList[firstNode] = []
        
        if secondNode not in self.adjacencyList:
            self.adjacencyList[secondNode] = []

        if (firstNode,dist) not in self.adjacencyList[secondNode]:
            self.adjacencyList[secondNode] += [(firstNode, dist)]

        if (secondNode,dist) not in self.adjacencyList[firstNode]:
            self.adjacencyList[firstNode] += [(secondNode, dist)]

    def getNeighbors(self, node):
        # return the neighbors if the node is present in the graph
        return self.adjacencyList[node] if node in self.adjacencyList else "<!Node not Found!>"

    def getGraph(self):
        return self.adjacencyList

def heuristic(node, heuristicList) -> int:
    # Retrives the Heuristic Values from HeuristicList for any node
    for n, hval in heuristicList:
        if n == node:
            return hval
        
    return 0    #Default value

def aStarSearch(graph, start, goal, heuristicList):
    notVisited = [(0, start)]   # Priority queue of nodes to explore
    visited = set()             # Set of visited nodes
    cost = {start: 0}           # Cost from start node to current node
    parent = {}                 # Parent nodes for path reconstruction

    while notVisited:
        _, current = heapq.heappop(notVisited)

        if current == goal:
            # Path found, reconstruct and return it with cost/distance
            path = []
            total_cost = cost[current]
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)

            return list(reversed(path)), total_cost  #Path and Cost

        visited.add(current)

        for neighbor, neighborCost in graph.getNeighbors(current):
            tentative_cost = cost[current] + neighborCost

            if neighbor in visited or tentative_cost >= cost.get(neighbor, float('inf')):
                continue

            if tentative_cost < cost.get(neighbor, float('inf')):
                parent[neighbor] = current
                cost[neighbor] = tentative_cost
                totalCost = tentative_cost + heuristic(neighbor, heuristicList)
                heapq.heappush(notVisited, (totalCost, neighbor))

    return None, 0  #No path found

def getInput(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    nodeInputs = getInput("Lab Assignments/Assignment 01/Input.txt")
    graph = GRAPH()
    heuristicList = []

    for nodeInfo in nodeInputs:

        nodeInfo = nodeInfo.split(' ')
        nodeList = [(nodeInfo[i], int(nodeInfo[i+1].rstrip())) for i in range(0, len(nodeInfo), 2)]

        node = nodeList[0][0]
        hval = nodeList[0][1]
        heuristicList.append((node, hval))
        neighbors = nodeList[1:]

        for neighbor in neighbors:
            dist = neighbor[1]
            graph.addEdges(node, neighbor[0], dist)

    # start = 'Arad'
    # goal = 'Bucharest'
    start = input("Start: ")
    goal = input("Goal: ")

    path, total_cost = aStarSearch(graph, start, goal, heuristicList)

    if path:
        pathString = ' -> '.join(path)
        print(f"Path found: {pathString}")
        print(f"Total Distance: {total_cost} km")
    else:
        print("No Path Found.")
