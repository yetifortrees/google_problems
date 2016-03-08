####
#This is an incorrect solution for finding if a synchronizing
#word for a dfa exists. It attempts to use an adjacency matrix
#as a tool for determining if all nodes can reach all other nodes.
#This was written before I knew how to define the problem.
####

import random
def answer(subway):
    printAdjacency(subway)
    # your code here
    lines = len(subway[0])
    walker = [i for i in range(0, len(subway))]
    while walker != [walker[0] for i in range(0, len(walker))]:
        move = random.randrange(0, lines, 1)
        print(move)
        walker = [subway[walker[i]][move] for i in range(0, len(subway))]
        print(walker)
def printAdjacency(subway):
    adjacent = [[0 for i in range(0, len(subway))] for j in range(0, len(subway))]
    for i in range(0, len(subway)):
        for j in range(0, len(subway[i])):
            adjacent[i][subway[i][j]] = 1
    for i in adjacent:
        print(i)
    print("-----")
    for i in range(0, len(subway)):
        adjacent = matmult(adjacent, adjacent)
        for i in adjacent:
            print(i)
        print("-----")
#credit to akavall on stackoverflow
def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]
#answer([[2, 1, 3], [2, 5, 4], [3, 1, 1], [1, 0, 5], [4, 2, 3], [3, 4, 0]])
#print("----")
#printAdjacency([[1, 1], [2, 2], [0, 0]])
#print("----new matrices----")
#printAdjacency([[1, 2], [1, 1], [2, 2]])
print("----new matrices----")
answer([[2, 1], [2, 4], [3, 1], [1, 0], [4, 4]])
print("----new matrices----")
print(answer([[2, 1], [2, 1], [3, 1], [1, 0]]))