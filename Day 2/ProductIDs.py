PATH = "Day 2/input.txt"
from math import floor
import sys

input = open(PATH, 'r')

line = input.readline()
#print(lines)
validIDs = set()
ranges = line.split(',')
for numRange in ranges:
    ends=numRange.split('-')
    #print(ends)
    lowString  = ends[0]
    highString = ends[1]
    if(lowString[0]=='0' or highString[0]=='0'):
        print(f"Unexpected leading zero in input")
        print(f"Low {lowString}, High {highString}")
        sys.exit(1)
        
    low  = int(lowString)
    high = int(highString)
    if (low >= high):
        print(f"Low {low}, High {high}")
        sys.exit(1)      
    
    for i in range(low, high+1):
        length=len(str(i))
        size = 10**((length/2))
        #print(low)
        #print(size)
        firstHalf = floor(i/size)
        #print(firstHalf)
        secondHalf = i-(firstHalf*size)
        #print(secondHalf)
        if(firstHalf == secondHalf):
            validIDs.add(i)

IDSum = 0
# Part 1
for i in validIDs:
    IDSum +=i
print(f"The sum of valid IDs is  {IDSum}")
    # Meaningless equation wrangling
    # x/(s)=f
    # x-(f*s)=sec
    
    # Find all sec==f
    
    # x/s=x-(x/s)*s
    # x/s=x-x

