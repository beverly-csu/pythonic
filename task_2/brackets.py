openBrackets = {}
closedBrackets = {}

def colorPrint(string, color, correctFlag, ):
    colors = {'black': '\x1B[30m', 'red': '\x1B[31m', 'green': '\x1B[32m', 'yellow': '\x1B[33m', 'blue': '\x1B[34m', 'magenta': '\x1B[35m', 'cyan': '\x1B[36m'}

def findEndIndex(closedBrackets):
    for index in closedBrackets:
        endIndex = index
    return endIndex

def findStartIndex(openBrackets):
    for index in openBrackets:
        startIndex = index
        break
    return startIndex

string = input()
index = 0
for char in string:
    if char in '({[<':
        tempBracket = {index: char}
        openBrackets.update(tempBracket)
    elif char in ')}]>':
        tempBracket = {index: char}
        closedBrackets.update(tempBracket)
    index += 1

"""
if len(openBrackets) == len(closedBrackets):
    startIndex = findStartIndex(openBrackets)
    endIndex = findEndIndex(closedBrackets)
    endFlag = False
    startFlag = False
    while startIndex < endIndex:
        if openBrackets.get(startIndex) == None:
            startIndex += 1
            startFlag = False
        else:
            startFlag = True
        if closedBrackets[endIndex] == None:
            endIndex -= 1
            endFlag = False
        else:
            endFlag = True
        if (startFlag and endFlag):
            if openBrackets[startIndex] == closedBrackets[endIndex]:
                startIndex += 1
                endIndex -= 1
            else:
                print('False', closedBrackets[endIndex], endIndex)
                break
else:
    exit(0)
"""

print(openBrackets, closedBrackets)