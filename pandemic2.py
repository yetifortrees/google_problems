####
#This program is a brute force solver for the following problem:
#
#           Imagine a group of n people. Each person can socialize with one other person of their
#           choosing. That person may or may not choose to socialize back with them, and may instead
#           socialize with someone else. This eventually results in groups of individuals who are connected
#           by a network of socialization. Now imagine someone outside this group wants to infect the largest group
#           of people with a virus. If they are always successful in infecting the largest group of socialized individuals,
#           what is the expected average number of people they will infect.
#
#This problem has 3 layers:
#   1. how can the people be socialized/grouped?
#       This problem is answered by finding the possible integer partitions
#       for the number of people overall.
#   2. how can the people be arranged in these groups?
#       This is answered through combinatorics by calculating the number
#       of ways to split n people into some set of partitions.
#   3. how many ways can the socialization edges be arranged in each partition?
#       This is answered through sequence A000435 on the OEIS. The exact reason is unknown to me,
#       but the number is not as easy to find as one might think because a socialization action is
#       akin to an edge in a digraph, but the disease can travel backwards along edges, as in an undirected
#       graph. Thus a graph must be constructed with directed edges with respect to possible configurations, and
#       then converted to an undirected graph.
#
#This program generates all configurations by representation as an array, converting to an adjacency matrix,
#and then evaluating the largest partition in each configuration. Beyond n=8 this is exceptionally slow because
#configurations grow as (n - 1)^n.
####
import math
seen = set()
maxConf = []
#the main function to call
def answer(n):
    #the largest configuration representation
    global maxConf
    #what people we have seen
    global seen
    #what sets of what sizes we have seen
    sets = {}
    #a count of how many time the max size was some number
    maxes = [0 for i in range(0, n)]
    #for accounting
    print(n)
    #we don't care about trivial cases
    if n == 2:
        return "2/1"
    #the current configuration
    string = [0 for i in range(0, n)]
    #the max configuration
    maxConf = [n - 2 for i in range(0, n)]
    #so we can get the max
    maxConf[0] += 1
    #the top of the fraction
    top = 0
    #the max number of configurations
    bottom = math.pow(n - 1, n)
    #while its a valid configuration
    while string != maxConf:
        #print(string)
        #generate the digraph adjacency matrix
        adjacency = [[0 for i in range(0, n)] for i in range(0, n)]
        for i in range(0, n):
            if string[i] < i:
                adjacency[i][string[i]] = 1
            else:
                adjacency[i][string[i] + 1] = 1
        #convert it to an undirected graph adjacency matrix
        #this could be one step
        for i in range(0, n):
            for j in range(0, n):
                if adjacency[i][j] == 1 or adjacency[j][i] == 1:
                    adjacency[i][j] = 1
                    adjacency[j][i] = 1
        #what people we have seen in this config so far
        seen = set()
        #the sizes of the partitions in this config
        sizes = []
        #breadth first search all the people
        for i in range(0, n):
            if i not in seen:
                sizes.append(BFS(adjacency, i))
        #print(sizes)
        maxHere = max(sizes)
        partition = str(sizes)
        #add to the top the biggest partition size
        top += maxHere
        #accounting
        if partition in sets:
            sets[partition] += 1
        else:
            sets[partition] = 1
        maxes[maxHere - 1] += 1
        #move to next config
        string = increment(list(string), n)
    #accounting + return
    print(maxes)
    print(sets)
    return str(top) + "/" + str(bottom)
#breadth first searches an adjacency matrix
#returns the indices of nodes seen
def BFS(adjacency, start):
    global seen
    visited, queue =set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for i in range(0, len(adjacency)):
                if adjacency[vertex][i] == 1:
                    queue.append(i)
    seen = seen.union(visited)
    return len(visited)
#increments the config
def increment(string, maxVal):
    global maxConf
    string[0] += 1
    if string != maxConf and string[0] == maxVal - 1:
        count = 0
        while string[count] == maxVal - 1:
            string[count] = 0
            string[count + 1] += 1
            count += 1 
    return string
#testing
for i in range(2, 10):
    print(answer(i))
    print("----")   