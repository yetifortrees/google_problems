import math
s = {}
def answer(x, y, n):
    total = 0
    for i in range(0, n):
        total += choose(n-1, i) * abs(wrapc(i, x - 1)) * abs(wrapc(n - i - 1, y - 1))
    return int(total)
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
def wrapc(*args):
    if args not in s:
        s[args] = c(*args)
    return s[args]
def choose(n, k):
    if k > n:
        return 0
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
line = []
for i in range (1, 25):
    line = []
    for j in range(1, 25):
        line.append(answer(i, j, 30))
    print(line)