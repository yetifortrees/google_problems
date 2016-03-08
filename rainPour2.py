def answer(heights):
    area = 0
    newArea = -1
    if len(heights) < 2:
        return 0
    #print(heights)
    localMax = []
    for q in range(1, len(heights)):
        if heights[q] != heights[0]:
            break
    if heights[0] > heights[q]:
        localMax.append(q - 1)
    for i in range(1, len(heights) - 1):
        if (heights[i] > heights[i - 1] and heights[i] > heights[i+1]):
            localMax.append(i)
        elif heights[i] > heights [i - 1] and heights[i] == heights[i + 1]:
            if plateau(heights, i):
                localMax.append(i)
    for q in range(2, len(heights) + 1):
        if heights[len(heights) - q] != heights[len(heights) - 1]:
            break
    if heights[len(heights) - 1] > heights[len(heights) - q]:
        localMax.append(len(heights) - q + 1)
    localMax = superPeaks(heights, localMax)
    return(addArea(heights, localMax))

def addArea(heights, localMax):
    area = 0
    if len(localMax) < 2:
        return 0
    for i in range(0, len(localMax) - 1):
        #print(i)
        littlePeak = min({heights[localMax[i]], heights[localMax[i+1]]})
        for j in heights[localMax[i]:localMax[i + 1]+1]:
            if (littlePeak > j):
                area += littlePeak - j
            #print(heights[localMax[i]+1:localMax[i + 1]])
            #print(littlePeak)
    return area
def plateau(heights, i):
    for q in range(i, len(heights)):
        if heights[i] != heights[q]:
            break
    if heights[i] > heights[q]:
        return True
    else:
        return False
def superPeaks(heights, localMax):
    newMax = []
    for i in localMax:
        after = False
        before = False
        for j in localMax:
            if heights[i] < heights[j]:
                if i < j:
                    after = True
                if i > j:
                    before = True
        if not before or  not after:
            newMax.append(i)
    return newMax
    
print(answer([1, 4, 2, 5, 1, 2, 3]))
print(answer([1,0,5]))
print(answer([5,0,1]))
print(answer([5]))
print(answer([1, 0, 3, 2, 1]))
print(answer([1, 2, 3, 2, 1]))
print(answer([3, 2, 1]))
print(answer([1, 2, 1]))
print(answer([1, 2, 3]))
print(answer([1, 2000]))
print(answer([2000, 1, 1]))
print(answer([5, 1, 4, 1, 5]))
print(answer([1, 5, 1, 4, 1, 5, 1]))
print(answer([5, 5, 1, 4, 1, 5, 5]))
print(answer([1, 1, 1, 1, 1, 1, 1, 1]))
print(answer([4, 1, 1, 1, 1, 1, 1, 4]))
print(answer([1, 1, 5, 4, 1, 4, 1, 4, 5, 1, 10]))
print(answer([5, 4, 3, 2, 1] + [x for x in range(1, 8900)]))
print(answer([4, 1, 1, 5, 5, 6, 1, 1, 6, 5, 5, 1, 1, 4]))
print(answer([1, 1, 1, 1, 1, 1, 1, 4]))
print(answer([4, 4, 1, 1, 1, 1, 1, 1]))
print(answer([8, 5, 6, 1, 4, 1, 6, 5, 8]))
