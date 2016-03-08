#####
#a brute force tool for determining the number of ways to arrange
#a line of n unique height objects iwth x visible from the left
#and y visible from the right. This problem is commonly known as
#skyscraper numbers
#
#this tool generates all possible line representations and then
#individually verifies their correctness
#####
from itertools import permutations
#the main function to call
def answer(x, y, n):
    #create a line representation
    list = []
    for i in range(1, n+1):
        list.append(i)
    #create all permutations
    perms = set(permutations(list))
    #print(perms)
    count = 0
    #loop through all permutations and verify
    for i in perms:
        if verify(x, y, n, i):
            #print(i)
            count += 1
    #return the number of valid lines
    return(count)
#main line rep verifier
#x - the number of left visible items
#y - the number of right visible items
#n - the number of items in the line
#line - the unique line rep
#returns whether given the params the line rep is valid
def verify(x, y, n, line):
    left = bunniesVisible(n, line, 0)
    right = bunniesVisible(n, line, 1)
    #print(left, ":", right)
    return x == left and y == right
#this method returns the number of items visible from one side
#maxInLine - the tallest object in the line
#line - the line representation
#side - which side the viewer is one
#returns the number of items viewable from the given side
def bunniesVisible(maxInLine, line, side):
    #left
    maximum = 0
    count = 0
    if side == 0:
        for i in range(0, len(line)):
            #the tallest will always be visible
            #but nothing behind it will be
            if line[i] == maxInLine:
                return count + 1
            if line[i] > maximum:
                maximum = line[i]
                count += 1
        #right
    elif side == 1:
        for i in range(1, len(line) + 1):
            #the tallest will always be visible
            #but nothing behind it will be
            if line[len(line) - i] == maxInLine:
                return count + 1
            if line[len(line) - i] > maximum:
                maximum = line[len(line) - i]
                count += 1
#this is run when the file is called
#it outputs an array of answers for analysis
line = []
for i in range (1, 5):
    line = []
    for j in range(1, 5):
        line.append(answer(i, j, 8))
    print(line)
