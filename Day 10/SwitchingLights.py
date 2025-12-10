import sys


PATH = "Day 10/input.txt"
input = open(PATH, 'r')
ON = '#'
SEARCH_LIMIT = 10

def switchLights(lights, switchOptions, switchOption, presses, minPresses):
    for switch in switchOption:
        lights[switch] = not(lights[switch])
    presses += 1
    if (presses < minPresses):
        if (lights == target):
            return presses
        else:
            return chooseSwitchOption(lights.copy(), switchOptions, presses, minPresses)
    else:
        return SEARCH_LIMIT
    
def chooseSwitchOption(lights, switchOptions, presses, minPresses):
    for nextSwitchOption in switchOptions:
        newPresses = switchLights(lights.copy(), switchOptions, nextSwitchOption, presses, minPresses)
        minPresses = min(minPresses, newPresses)
    return minPresses 
  
lines = input.readlines()
numLines = len(lines)
totalPresses = 0
maxPresses = 0
i = 0
# Input Parsing
for line in lines:
    line = line.strip('\n')
    line = line.split(']')
    target = line[0].strip('[')
    line = line[1].split(')')
    switchOptions = []
    for switchStr in line[:-1]:
        switchStr = switchStr.replace(" (",'')
        switchOptions.append(list(map(int,switchStr.split(','))))
    joltage = line[-1].strip('{').strip('}')
    
    lights = [False] * len(target)
    target = [x == ON for x in target]
    
    # Find the shortest path
    minPresses = chooseSwitchOption(lights, switchOptions, 0, SEARCH_LIMIT)
    maxPresses = max(minPresses, maxPresses)
    if(minPresses == SEARCH_LIMIT):
        print(f"minPresses is search limit for line {i}, please increase limit and try again")
        sys.exit(1)
    totalPresses += minPresses
    print(f"Running Total: {totalPresses}, line {i}/{numLines}, max presses so far {maxPresses}")
    i += 1
print( "######################################")
print(f"The minimum number of presses is {totalPresses}")
                