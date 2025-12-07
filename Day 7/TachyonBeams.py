PATH = "Day 7/input.txt"
START = 'S'
SPLITTER = '^'
BEAM = '|'
# EMPTY = '.'
# TIMELINE_BEAM = '!'
input = open(PATH, 'r')

manifold = input.readlines()
manifold = [list(line.strip('\n')) for line in manifold]
height = len(manifold)
width = len(manifold[0])

startInd = manifold[0].index(START)

def split(x,y,countSplits):
    if (manifold[y][x] == BEAM):
        countSplits = False
    splits, timelines = findNextSplit(x,y,countSplits)
    return splits, timelines

def findNextSplit(x,y,countSplits):
    splits = 0
    timelines = 0
    while y < height:
        if (manifold[y][x] == BEAM):
            countSplits = False
        if (manifold[y][x].isnumeric()):
            timelines = int(manifold[y][x])
            return splits,timelines
        if (manifold[y][x] == SPLITTER):
            timelines += 1
            if(countSplits):
                splits += 1
            if (0 <= x-1):
                newSplits,newTimelines = split(x-1,y,countSplits)
                splits += newSplits
                timelines += newTimelines
            if (x+1 < width):
                #timelines += 1 - only 1 new timeline per split
                newSplits,newTimelines = split(x+1,y,countSplits)
                splits += newSplits
                timelines += newTimelines
            manifold[y][x] = str(timelines)
            return splits,timelines
        # if(not countSplits):
        #     if(manifold[y][x] == EMPTY):
        #         manifold[y][x] == TIMELINE_BEAM
        # else:
        manifold[y][x] = BEAM
        y += 1
    return splits, timelines

totalSplits,timelines = findNextSplit(startInd,1,True) 
timelines += 1 # Add the original timeline  
print(f"The beam will be split {totalSplits} times")
print(f"The number of timelines is {timelines}")