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
        #for idRanges in freshIDs:
            
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
#print(f'The total number of accessable rolls is {totalAccessable}')