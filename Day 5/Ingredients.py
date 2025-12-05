import sys


PATH = "Day 5/input.txt"

input = open(PATH, 'r')

lines = input.readlines()

freshIDs = []
available=0
getFreshIDs = True
for line in lines:
    if getFreshIDs:
        if line=="\n":
            getFreshIDs = False
            continue
        line = line.strip('\n')
        IDrange = line.split('-')
        lower = int(IDrange[0])
        higher = int(IDrange[1])
        if lower > higher:
            print(f"Higher {higher} less than lower {lower}")
            sys.exit(1)
        freshIDs.append((lower,higher))
        #[freshIDs.add(x) for x in range(lower,higher+1)]
        #print(line)
    else:
        id = int(line.strip('\n'))
        for freshID in freshIDs:
            if (freshID[0] <= id <= freshID[1]):
                available += 1
                break      

print(f'The number of available fresh ingredients is {available}')

# Part 2
# Optimise Ranges
newLength = 0
length = 1
freshIDs= sorted(freshIDs, key=lambda tup: tup[0])
while newLength != length:
    length = len(freshIDs)
    newLength = length
    i = 0
    while i < newLength:
        idRange = freshIDs[i]
        j = i + 1
        while j < newLength:
            if (i == j):
                j += 1
                continue
            otherRange = freshIDs[j]
            if (otherRange[0] <= idRange[0] <= otherRange[1] and otherRange[0] <= idRange[1] <= otherRange[1]):
                freshIDs.pop(i)
                j = i + 1
                idRange = freshIDs[i]
                newLength -= 1
                continue
            elif (idRange[0] <= otherRange[0] <= idRange[1] and idRange[0] <= otherRange[1] <= idRange[1]):
                freshIDs.pop(j)
                newLength -= 1
                j -= 1
            elif (idRange[0] <= otherRange[0] <= idRange[1]):
                freshIDs[i] = (idRange[0],otherRange[1])
                freshIDs.pop(j)
                newLength -= 1
                j -= 1
            elif (idRange[0] <= otherRange[1] <= idRange[1]):
                freshIDs[i] = (otherRange[0],idRange[1])
                freshIDs.pop(j)
                newLength -= 1
                j -= 1
            j += 1
        i += 1

freshSum = 0
for idRange in freshIDs:
    freshSum += (idRange[1]+1)-idRange[0]

print(f'The sum of fresh IDs is {freshSum}')
# Too Low - 361427314021581
#           358390896254879 - lower :(