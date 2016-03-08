def answer(t, n):
    # your code here
    games = 0
    paths = []
    for i in range(0, t):
        paths.append(0)
    while check(paths):
        #print(paths)
        games += verify(paths, n)
        paths = increment(paths)
    #print(paths)
    games += verify(paths, n)
    return games
def verify(path, n):
    x = 1
    reachedEnd = False
    for i in path:
        if i == 0:
            x -= 1
        if i == 2:
            x += 1
        if x == n:
            reachedEnd = True
        if reachedEnd and x != n:
            return 0
        if x < 1:
            return 0
    if x == n:
        return 1
    return 0
def check(paths):
    toReturn = False
    for i in paths:
        if i != 2:
            toReturn = True
    return toReturn
def increment(paths):
    paths[0] += 1
    counter = 0
    for i in paths:
        if i == 3:
            paths[counter] = 0
            paths[counter+1] += 1
        counter += 1
    return paths
            
line = []
for i in range (1, 12):
    line = []
    for j in range(1,12):
        line.append(answer(i, j))
    print(line)