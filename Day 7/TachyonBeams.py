PATH = "Day 7/input.txt"
START = 'S'
SPLITTER = '^'
BEAM = '|'
input = open(PATH, 'r')

manifold = input.readlines()
manifold = [list(line.strip('\n')) for line in manifold]
height = len(manifold)
width = len(manifold[0])

startInd = manifold[0].index(START)

def split(x,y):
    if (manifold[y][x] != BEAM):
        return findNextSplit(x,y)
    return 0

def findNextSplit(x,y):
    splits = 0
    while y < height:
        if (manifold[y][x] == BEAM):
            return 0
        if (manifold[y][x] == SPLITTER):
            splits += 1
            if (0 <= x-1):
                splits += split(x-1,y)
            if (x+1 < width):
                splits += split(x+1,y)
            manifold[y][x] = str(splits)
            return splits
        manifold[y][x] = BEAM
        y += 1
    return splits
 
totalSplits = findNextSplit(startInd,1)   
print(f"The beam will be split {totalSplits} times")