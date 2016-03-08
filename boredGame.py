####
#This program is a brute force solution for how many valid
#games there are with turns t and board size n, where the game board
#is a line of squares, a player starts on the left side, each
#turn a player can move left or right one square, and once on
#the end square the player cannot leave.
####

#the main function to call
def answer(t, n):
    # your code here
    games = 0
    paths = []
    #make an array of length t, where each value is a move
    for i in range(0, t):
        paths.append(0)
    #if we aren't on the last path
    while check(paths):
        #print(paths)
        #check next path and move to the next one
        games += verify(paths, n)
        paths = increment(paths)
    #print(paths)
    #check the last path
    games += verify(paths, n)
    #return the number of valid paths
    return games
#checks if a path on gameboard of length n is valid
def verify(path, n):
    #where on the board we are
    x = 1
    reachedEnd = False
    for i in path:
        #move left
        if i == 0:
            x -= 1
        #move right
        if i == 2:
            x += 1
        #check if at the end of the board
        if x == n:
            reachedEnd = True
        #if we reached the end and left
        if reachedEnd and x != n:
            return 0
        #if we went off the board
        if x < 1:
            return 0
    #if were on the end then we did it!
    if x == n:
        return 1
    return 0
def check(paths):
    toReturn = False
    for i in paths:
        if i != 2:
            toReturn = True
    return toReturn
#increments a path to the next path
def increment(paths):
    paths[0] += 1
    counter = 0
    for i in paths:
        if i == 3:
            paths[counter] = 0
            paths[counter+1] += 1
        counter += 1
    return paths
#testing
line = []
for i in range (1, 12):
    line = []
    for j in range(1,12):
        line.append(answer(i, j))
    print(line)