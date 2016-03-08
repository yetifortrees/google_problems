####
#This program is an optimized solution for how many valid
#games there are with turns t and board size n, where the game board
#is a line of squares, a player starts on the left side, each
#turn a player can move left or right one square, and once on
#the end square the player cannot leave.
####

#the main function to call
def answer(t, n):
    #initialize a representation of the game board
    board = []
    #at this time the board has no walkers on it
    for i in range(0, n):
        board.append(0)
    #this is the next state
    newBoard = list(board)
    #add a walker to the first board space
    board[0] = 1
    #if the board is one square then there is one solution
    if len(board) < 2:
        return 1
    #loop through time
    for i in range(0, t):
        #loop over the board
        for j in range(0, len(board)):
            #walkers can go right or stay from the first spot
            if j == 0:
                newBoard[0] += board[0]
                newBoard[1] += board[0]
            #walkers can only stay in the last spot
            elif j == len(board) - 1:
                newBoard[j] += board[j]
            #walkers can move left, right, or stay anywhere else
            else:
                newBoard[j-1] += board[j]
                newBoard[j] += board[j]
                newBoard[j+1] += board[j]
            #print(newBoard)
        #the next step is now the current step
        board = list(newBoard)
        #reset the new board for the next step
        for i in range(0, len(newBoard)):
            newBoard[i] = 0
        #print("------------")
    #mod the number of games by 123454321 because Google told me to
    return board[len(board) - 1]%123454321
#testing
line = []
for i in range (1, 12):
    line = []
    for j in range(1,12):
        line.append(answer(i, j))
    print(line)