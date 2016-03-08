####
# this program calculates
# the smallest number of weights of only 
# powers of three that can be used to balance any weight,
# and which side of a balance to put them on.
####
import math
def answer(x):
    #convert the number to base three
    array = numberToThree(x)
    print(array)
    answer = []
    count = 0
    #loop through the base three number
    for i in array:
        if (i == 0):
            answer.append("-")
        elif (i == 1):
            answer.append("R")
        else:
            answer.append("L")
            if (count == len(array)):
                answer.append("R")
                return answer
            else:
                q = 0
                array[count+q] += 1
                while (array[count+q] == 3):
                    array[count+q] = 0
                    q += 1
                    if (count + q == len(array)):
                        array.append(1)
                    else:
                        array[count+q] += 1
                    print(array)
        count = count + 1
    return answer
#this method converts a number, n, to an array
#that represents it as a base three value
def numberToThree(n):
    if n == 0:
       return [0]
    digits = []
    while (n > 0):
       digits.append(int(n % 3))
       n = math.floor(n/3)
    #digits.reverse()
    return digits

print(answer(80))