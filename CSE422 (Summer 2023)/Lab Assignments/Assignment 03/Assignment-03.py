### CSE422 - Artificial Intelligence
### Assignment 03: Alpha-Beta Pruning
### ----------------------------------
### Name : Mirza Meherab Hosen Rudra
### ID   : 21101048
### Sec  : 10
### ----------------------------------

import random
import math


class TREE:
    def __init__(self):
        self.tree = {}
        self.root = None

    def addNode(self, node, parent, value=None):
        
        # If the tree is empty, then the first node is the root
        if self.tree == {}:
            self.root = node
            self.tree[node] = [parent, value, None, None]

        if parent in self.tree:

            # Update Left or right leaf node
            if self.tree[parent][2] == None:
                self.tree[parent][2] = node
            else:
                self.tree[parent][3] = node

            # Add the node to the tree
            self.tree[node] = [parent, value, None, None]

    def getValue(self, node):
        if node in self.tree:
            return self.tree[node][1]
        else:
            return None

    def getChildren(self, node):
        if node in self.tree:
            return [child for child in self.tree[node][2:] if child is not None]
        else:
            return None

    def getParent(self, node):
        if node in self.tree:
            return self.tree[node][0]

    def getTree(self):
        return self.tree


def minimax(tree, node, alpha, beta, depth, maximizePlayer):

    if depth == 0:
        return tree.getValue(node)
    
    if maximizePlayer:
        alpha = float("-inf")
        for child in tree.getChildren(node):
            childValue = minimax(tree, child, alpha, beta, depth-1, False)
            alpha = max(alpha, childValue)
            if alpha >= beta:
                break

            tree.getTree()[node][1] = alpha
        
        return alpha

    else:
        beta = float("inf")
        for child in tree.getChildren(node):
            childValue = minimax(tree, child, alpha, beta, depth-1, True)
            beta = min(beta, childValue)
            if beta <= alpha:
                break

            tree.getTree()[node][1] = beta
        
        return beta

def initiateTree(nodeValues):

    # Level 0
    tree = TREE()
    tree.addNode("A", None)
    
    # Level 1
    tree.addNode("B", "A")
    tree.addNode("C", "A")
    
    # Level 2
    tree.addNode("D", "B")
    tree.addNode("E", "B")
    tree.addNode("F", "C")
    tree.addNode("G", "C")

    # Level 3
    tree.addNode("H", "D", nodeValues[0])
    tree.addNode("I", "D", nodeValues[1])
    tree.addNode("J", "E", nodeValues[2])
    tree.addNode("K", "E", nodeValues[3])
    tree.addNode("L", "F", nodeValues[4])
    tree.addNode("M", "F", nodeValues[5])
    tree.addNode("N", "G", nodeValues[6])
    tree.addNode("O", "G", nodeValues[7])

    return tree


def main():
    
    # ID = input("Enter Your ID: ")
    # ID = "25485465"   # Question TEST CASE 01
    # ID = "17564039"   # Question TEST CASE 02
    ID = "21181848" # My ID 21101048; Replaced 0 with 8

    # temp = ""
    # for i in ID:
    #     if i == 0:
    #         i = 8
        
    #     temp += i
    
    # ID = temp

    pointsToWin = (int(ID[-1]) * 10) + int(ID[-2])  # Last 2 digits of ID reversed
    totalShuffles = int(ID[3])                      # 4th digit of ID
    minPoint = int(ID[4])                           # 5th value of the ID
    maxPoint = math.ceil(pointsToWin * 1.5)         # Last 2 digits of ID reversed * 1.5

    # nodeValues = [66, 74, 14, 73, 19, 26, 32, 40]     # Question TEST CASE 01
    # nodeValues = [36, 26, 112, 57, 85, 80, 107, 28]   # Question TEST CASE 02
    nodeValues = [random.randrange(minPoint, maxPoint) for _ in range(8)]

    tree = initiateTree(nodeValues)
    result = minimax(tree, node=tree.root, alpha=float("-inf"), beta=float("inf"), depth=3, maximizePlayer=True)

    # Formatting The Output
    print("##-------TEST CASE 00-------##\n")
    print(f"Student ID: {ID}")
    print(f"Min Ponit: {minPoint}  ###  Max Point: {maxPoint}\n")
    print("Generated 8 random points between the minimum ")
    print(f"and maximum point Limits: {nodeValues}")
    print(f"Total points to win: {pointsToWin}")
    print(f"Achieved point by applying alpha-beta pruning = {result}")

    if result is not None and result >= pointsToWin:
        print("The winner is Optimus Prime")
    else:
        print("The winner is Megatron")

    shuffleResult = []
    for _ in range(totalShuffles):
        random.shuffle(nodeValues)
        tree = initiateTree(nodeValues)
        result = minimax(tree, node=tree.root, alpha=float("-inf"), beta=float("inf"), depth=3, maximizePlayer=True)
        shuffleResult.append(result)

    print("\nAfter the shuffle:")
    print(f"List of all points values from each shuffles: \n{shuffleResult}")
    print(f"The maximum value of all shuffles: {max(shuffleResult)}")

    wincount = 0
    for result in shuffleResult:
        if result >= pointsToWin:
            wincount += 1

    print(f"Optimus Prime Won {wincount} times out of {totalShuffles} number of shuffles")



if __name__ == "__main__":
    main()
