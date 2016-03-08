#####
#an optimized tool for determining the number of ways to arrange
#a line of n unique height objects iwth x visible from the left
#and y visible from the right. This problem is commonly known as
#skyscraper numbers
#
#this tool uses combinatorics to determine the number of possible arrangements
#per the paper Skyscraper Numbers by Tanya Khovanova and Joel Lewis.
#The number can be found by finding some binomial coefficients and by
#calculating the unsigned stirling numbers of the first kind
#####

import math
s = {}
#main solution function
def answer(x, y, n):
    total = 0
    #this represents the main formula
    for i in range(0, n):
        total += choose(n-1, i) * abs(wrapc(i, x - 1)) * abs(wrapc(n - i - 1, y - 1))
    return int(total)
#a recursive function to calculate stirling numbers
def c(n, a):
    if n == 0 and a == 0:
       return 1
    elif a == 0 and n >= 1:
       return 0
    elif a > n:
       return 0
    elif n == a:
        return 1
    return wrapc(n-1, a-1) - (n - 1) * wrapc(n-1, a)
#a decorator function for the main stirling number function
#for optimizing speed
def wrapc(*args):
    if args not in s:
        s[args] = c(*args)
    return s[args]
#a function for calculating n choose k (combinations)
def choose(n, k):
    if k > n:
        return 0
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
    
#runs when the file is called and outputs answers for analysis
line = []
for i in range (1, 25):
    line = []
    for j in range(1, 25):
        line.append(answer(i, j, 30))
    print(line)