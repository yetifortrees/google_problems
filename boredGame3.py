def answer(t, n):
    board = []
    for i in range(0, n):
        board.append(0)
    newBoard = list(board)
    board[0] = 1
    if len(board) < 2:
        return 1
    for i in range(0, t):
        for j in range(0, len(board)):
            if j == 0:
                newBoard[0] += board[0]
                newBoard[1] += board[0]
            elif j == len(board) - 1:
                newBoard[j] += board[j]
            else:
                newBoard[j-1] += board[j]
                newBoard[j] += board[j]
                newBoard[j+1] += board[j]
            #print(newBoard)
        board = list(newBoard)
        for i in range(0, len(newBoard)):
            newBoard[i] = 0
        #print("------------")
    return board[len(board) - 1]%123454321

line = []
for i in range (1, 12):
    line = []
    for j in range(1,12):
        line.append(answer(i, j))
    print(line)