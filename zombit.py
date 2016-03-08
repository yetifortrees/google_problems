import math
def answer(n):
    pads = 0
    for i in range(0, 100):
        sum = math.pow(100 - i, 2)
        #print(sum)
        while (n >= sum):
            n -= sum
            pads += 1
        if n == 0:
            break
    return(pads)
print(answer(24))
print(answer(160))
print(answer(10000))
print(answer(1))
print(answer(100))
    
    