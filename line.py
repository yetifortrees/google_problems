from itertools import permutations
def answer(x, y, n):
    # your code here
    list = []
    for i in range(1, n+1):
        list.append(i)
    perms = set(permutations(list))
    #print(perms)
    count = 0
    for i in perms:
        if verify(x, y, n, i):
            #print(i)
            count += 1
    return(count)
def verify(x, y, n, line):
    left = bunniesVisible(n, line, 0)
    right = bunniesVisible(n, line, 1)
    #print(left, ":", right)
    return x == left and y == right
def bunniesVisible(maxInLine, line, side):
    #left
    maximum = 0
    count = 0
    if side == 0:
        for i in range(0, len(line)):
            if line[i] == maxInLine:
                return count + 1
            if line[i] > maximum:
                maximum = line[i]
                count += 1
        #right
    elif side == 1:
        for i in range(1, len(line) + 1):
            if line[len(line) - i] == maxInLine:
                return count + 1
            if line[len(line) - i] > maximum:
                maximum = line[len(line) - i]
                count += 1
line = []
for i in range (1, 5):
    line = []
    for j in range(1, 5):
        line.append(answer(i, j, 8))
    print(line)
