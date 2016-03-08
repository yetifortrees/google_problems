####
#This program calculates how many connected graphs exist
#with a given number of nodes and a given number of edges
####
import math
#for the decorator functions
s = {}
t = {}
#the main function to call
def answer(n,k):
    return graphWrap(n, k)
#a decorator function to increase performance
def graphWrap(*args):
    if args not in t:
        t[args] = graph(*args)
    return t[args]
#the function to calculate
def graph(n, k):
    #calc possible number of edges
    t = chooseWrap(n, 2)
    #calc possible number of graphs as number of edges possible choose how many we have
    ret = chooseWrap(t, k)
    #if we don't have enough to always cover all nodes
    if k < chooseWrap(n - 1, 2) + 1:
        #then for each node look at the number of ways to exclude
        for i in range(1, n):
            ni = chooseWrap(n - 1, i - 1)
            x = chooseWrap(i, 2)
            for j in range(i - 1, min(x, k) + 1):
                #get rid of everything that isn't connected
                ret -= ni * chooseWrap(chooseWrap(n - i, 2), k - j) * answer(i, j) 
    return ret
#a decorator function for the choose/combination function
def chooseWrap(*args):
    if args not in s:
        s[args] = choose(*args)
    return s[args]
#a function to calculate n choose k or n combination k
def choose(n, k):
    if k > n:
        return 0
    return int(math.factorial(n)/(math.factorial(k) * math.factorial(n - k)))
#testing
print(answer(2, 1))
print(answer(4, 3))
print(answer(3, 2))
print(answer(4, 6))
line = []
for i in range (21, 20):
    line = []
    for j in range(i + 1, int((i * (i - 1)) / 2)):
        line.append(answer(i, j))
    print(line)