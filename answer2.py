import math
def answer(x):
    array = numberToThree(x)
    print(array)
    answer = []
    count = 0
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