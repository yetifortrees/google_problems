####
#This is an optimized solution for determining if a DFA has a synchronizing word.
#It uses David Eppstein's method as defined in his paper "Reset sequences for monotonic autonama"
####
import math
from collections import deque
#the main method to call
def answer(subway):
    #check if the first subway is good. If it is return -1
    if checkSubway(subway):
        return -1
    #if its not good check if removing a subway makes it good
    else:
        #loop through each station removing it
        for i in range(0, len(subway)):
            #print(i)
            #if the result is good then return that subway number
            if checkSubway(removeSubway(subway, i)):
                return i
        #there is no one station that when removed makes it good
        return -2
#breadth first search from a start node in the power sub
def BFS(tree, start, solved):
    if start in solved:
        return True
    #have a set of nodes we've seen
    seen = set()
    seen.add(start)
    #make a queue of nodes up next
    toVisit = deque()
    #push the start node into it
    toVisit.append(start)
    #while we have more than 0 nodes to visit
    while len(toVisit) > 0:
        #pop out the top
        current = toVisit.pop()
        #look in our graph at current node
        for node in tree[current]:
            #if its a singleton node or we have previously solved it
            if "," not in node or node in solved:
                #add everything weve seen to solved
                for i in seen:
                    solved.add(i)
                return True
            if node not in seen:
                seen.add(node)
                toVisit.append(node)
    return False
#a method to remove a state from the machine given some rules
#subway - the machine
#toRemove - the station/state to remove
def removeSubway(subway, toRemove):
    newSub = []
    for i in range(0, len(subway)):
        if i != toRemove:
            newSub.append([])
            for j in range(0, len(subway[0])):
                if subway[i][j] == toRemove:
                    if subway[toRemove][j] == toRemove:
                        if i > toRemove:
                            newSub[len(newSub) - 1].append(i - 1)
                        else:
                            newSub[len(newSub) - 1].append(i)
                    elif subway[toRemove][j] > toRemove:
                        newSub[len(newSub) - 1].append(subway[toRemove][j] - 1)
                    else:
                        newSub[len(newSub) - 1].append(subway[toRemove][j])
                elif subway[i][j] > toRemove:
                    newSub[len(newSub) - 1].append(subway[i][j] - 1)
                else:
                    newSub[len(newSub) - 1].append(subway[i][j])
    #for i in newSub:
    #    print(i)
    #print("----")
    return newSub
#This method determines if a subway system has a synchronizing sequence
def checkSubway(subway):
    powerSub = {}
    #for i in range(0, len(subway)):
    #    paths = set()
    #    for j in subway[i]:
    #        paths.add(str(j))
    #    powerSub[str(i)] = paths
    #create a power system of all pairs of stations and their connections
    for i in range(0, len(subway)):
        for j in range(i, len(subway)):
            paths = []
            for k in range(0, len(subway[0])):
                walker = [i, j]
                walker[0] = subway[walker[0]][k]
                walker[1] = subway[walker[1]][k]
                #walker = [subway[walker[i]][k] for i in range(0, len(walker))]
                if walker[0] != walker[1]:
                    if walker[0] > walker[1]:
                        paths.append(str(walker[0]) + "," + str(walker[1]))
                    else:
                        paths.append(str(walker[1]) + "," + str(walker[0]))
                else:
                    paths.append(str(walker[0]))
            if i != j:
                if i > j:
                    powerSub[str(i) + "," + str(j)] = set(paths)
                else:
                    powerSub[str(j) + "," + str(i)] = set(paths)
            else:
                powerSub[str(i)] = set(paths)
    #check if all pairs have a path to come together
    #if they do then there is a synchronizing sequence
    allPairs = True
    #print(powerSub)
    solved = set()
    for key in powerSub:
        if "," in key:
            if not BFS(powerSub, key, solved):
                allPairs = False
    return allPairs
#testing
print(answer([[2, 1], [2, 0], [3, 1], [1, 0]]))
print("----new matrices----")
print(answer([[1, 2], [1, 1], [2, 2]]))
print("----new matrices----")
print(answer([[1, 1], [2, 2], [0, 2]]))
print("----new matrices----")
print(answer([[1, 1], [2, 2], [0, 0]]))
print("----new matrices----")
print(answer([[0, 0], [1, 2], [2, 2]]))
print("----new matrices----")
print(answer([[0, 1], [1, 1], [2, 2]]))
#print("----new matrices----")
#print(answer([[0, 2], [0, 1], [2, 3], [3, 4], [4, 3]]))
#print("----new matrices----")
#print(answer([[1, 1, 2, 3, 4], [2, 2, 3, 4, 5], [3, 3, 4, 6, 7], [4, 4, 10, 11, 10], [5, 5, 4, 8, 9], [6, 9, 10, 8, 6], [7, 7, 11, 0, 4], [8, 8, 9, 6, 3], [9, 9, 10, 10, 10], [10, 10, 11, 11, 11], [11, 11, 10, 5, 7], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0], [20, 20, 1, 2, 3], [11, 11, 0, 0, 0], [11, 11, 0, 0, 0]]))