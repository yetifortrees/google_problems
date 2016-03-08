####
#This is a naive function for calculating how much area
#it takes to fill in a discrete signal. It works by filling in between
#peaks repeatedly until there is at most one peak/plateau
#the difficulty in its solution lies in the overcomplicated implementation
#that is ultimately wrong under certain cases
####

#the main function
def answer(heights):
    #start with filled in area of 0
    area = 0
    newArea = -1
    #if there are no peaks there is nothing to fill in
    if len(heights) < 2:
        return 0
    #print(heights)
    #while we are still adding area, keep looping
    while newArea != 0:
        localMax = []
        #for if there is a plateau at the start
        for q in range(1, len(heights)):
            if heights[q] != heights[0]:
                break
        #if we went down then we had a peak/plateau at the start
        if heights[0] > heights[q]:
            localMax.append(q - 1)
        #go through and find all of the peaks in the signal
        for i in range(1, len(heights) - 1):
            if (heights[i] > heights[i - 1] and heights[i] > heights[i+1]):
                localMax.append(i)
            elif heights[i] > heights [i - 1] and heights[i] == heights[i + 1]:
                if plateau(heights, i):
                    localMax.append(i)
        #check for a plateau at the end of the signal
        for q in range(2, len(heights) + 1):
            if heights[len(heights) - q] != heights[len(heights) - 1]:
                break
        if heights[len(heights) - 1] > heights[len(heights) - q]:
            localMax.append(len(heights) - q + 1)
        #add the new area based on the given peaks
        newArea = addArea(heights, localMax)
        #print(localMax)
        #if we didn't add new area
        if newArea == 0:
            return area
        #add the new area
        area += newArea
        #build a new, filled in signal based on what we just did
        newHeights = []
        for i in range(0, localMax[0] + 1):
            newHeights.append(heights[localMax[0]])
        #print(newHeights)
        for i in range(0, len(localMax) - 1):
            littlePeak = min({heights[localMax[i]], heights[localMax[i+1]]})
            if littlePeak == heights[localMax[i]]:
                for j in range(localMax[i], localMax[i+1] - 1):
                    newHeights.append(littlePeak)
                newHeights.append(heights[localMax[i+1]])
            else:
                #newHeights.append(heights[localMax[i]])
                for j in range(localMax[i], localMax[i+1]):
                    newHeights.append(littlePeak)
            #print(  newHeights)
        for i in range(localMax[len(localMax) - 1] + 1, len(heights)):
            newHeights.append(heights[localMax[len(localMax) - 1]])
        heights = newHeights
        #print(heights)
    return area
#this function determines how much area is added by filling in the signal
#based on the set of peaks in the signal
def addArea(heights, localMax):
    area = 0
    #if there is only one peak then there can't be any fill-in
    if len(localMax) < 2:
        return 0
    #loop through the peaks
    for i in range(0, len(localMax) - 1):
        #print(i)
        littlePeak = min({heights[localMax[i]], heights[localMax[i+1]]})
        for j in heights[localMax[i]:localMax[i + 1]+1]:
            if (littlePeak > j):
                area += littlePeak - j
            #print(heights[localMax[i]+1:localMax[i + 1]])
            #print(littlePeak)
    return area
#determine if there are plateaus after i
def plateau(heights, i):
    for q in range(i, len(heights)):
        if heights[i] != heights[q]:
            break
    if heights[i] > heights[q]:
        return True
    else:
        return False
#find the superpeaks (peaks which have no higher peak either before or after them)
def superPeaks(heights, localMax):
    newMax
    for i in localMax:
        after = false
        before = false
        for j in localMax:
            if heights[i] < heights[j]:
                if i < j:
                    after = true
                if i > j:
                    before = true
        if not before or  not after:
            newMax.append(i)
#test cases to check speed and accuracy
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
