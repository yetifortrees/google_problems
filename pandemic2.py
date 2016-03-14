import math
seen = set()
maxConf = []
def answer(n):
    global maxConf
    global seen
    sets = {}
    maxes = [0 for i in range(0, n)]
    print(n)
    if n == 2:
        return "2/1"
    string = [0 for i in range(0, n)]
    maxConf = [n - 2 for i in range(0, n)]
    maxConf[0] += 1
    top = 0
    bottom = math.pow(n - 1, n)
    while string != maxConf:
        #print(string)
        adjacency = [[0 for i in range(0, n)] for i in range(0, n)]
        for i in range(0, n):
            if string[i] < i:
                adjacency[i][string[i]] = 1
            else:
                adjacency[i][string[i] + 1] = 1
        for i in range(0, n):
            for j in range(0, n):
                if adjacency[i][j] == 1 or adjacency[j][i] == 1:
                    adjacency[i][j] = 1
                    adjacency[j][i] = 1
        seen = set()
        sizes = []
        for i in range(0, n):
            if i not in seen:
                sizes.append(BFS(adjacency, i))
        #print(sizes)
        maxHere = max(sizes)
        partition = str(sizes)
        top += maxHere
        if partition in sets:
            sets[partition] += 1
        else:
            sets[partition] = 1
        maxes[maxHere - 1] += 1
        string = increment(list(string), n)
    print(maxes)
    print(sets)
    return str(top) + "/" + str(bottom)
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
    
for i in range(2, 10):
    print(answer(i))
    print("----")   