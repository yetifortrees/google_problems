####
#This code recursively removes an inserted word
#from a chunk of text to find the original text
####
def answer(chunk, word):
    allWords = [chunk]
    foundNew = True
    while foundNew == True:
        foundNew = False
        new = []
        for i in allWords:
            allIndex = findIndices(i, word)
            if len(allIndex) > 0:
                foundNew = True
                #possibilities = []
                for j in allIndex:
                    #print(chunk[:j] + chunk[j+len(word):])
                    new.append(i[:j] + i[j+len(word):])
            else:
                new.append(i)
            #list(set(possibilities))
            #new = new + possibilities
            #print(new)
        allWords = list(set(new))
    allWords.sort()
    print(allWords[0])
def findIndices(chunk, word):
    indices = []
    for i in range(0, len(chunk) - len(word) + 1):
        if chunk[i:i+len(word)] == word:
            indices.append(i)
    return indices
    
answer("goodgooogoogfogoood", "goo")
answer("lolol", "lol")
answer("aabb", "ab")
answer("lololololo", "lol")