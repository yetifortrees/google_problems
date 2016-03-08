####
#This program is an INCORRECT solution for how many valid
#games there are with turns t and board size n, where the game board
#is a line of squares, a player starts on the left side, each
#turn a player can move left or right one square, and once on
#the end square the player cannot leave.
#
#It attempts to use the lowest layer of a binary tree as a means for
#tracking all paths through the game simultaneously. It could probably be
#fixed.
####

#the main function to call
def answer(t, n):
    paths = []
    state = [0, 1]
    #print(state)
    while state[0] < t:
        #move left
        if state[1] - 1 > 1 and state[1] != n and (n - state[1] + 1) <= (t - state[0] - 1):
            paths.insert(0, [state[0]+1, state[1]-1])
        if state[1] + 1 <= n and (n - state[1] - 1) <= (t - state[0] - 1):
            paths.insert(0, [state[0]+1, state[1]+1])
        if (n - state[1]) <= (t - state[0] - 1):
            paths.insert(0, [state[0]+1, state[1]])
        if len(paths) == 0:
            return 0
        state = paths.pop()
        #print(state)
    return len(paths) + 1
#print(answer(1, 2))
#print(answer(3, 2))

line = []
for i in range (1, 12):
    line = []
    for j in range(1,12):
        line.append(answer(i, j))
    print(line)
