PATH = "Day 2/input.txt"
from math import floor
import sys

input = open(PATH, 'r')

line = input.readline()
#print(lines)
invalidIDs = set()
invalidIDsPT1 = set()
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
        for numRepititions in range (2,length+1):
            invalidID = True
            repLength = length/numRepititions
            if (repLength.is_integer()):
                repLength = int(repLength)
                section=[]
                prevSections=0
                j=0
                for digits in range (length-repLength,-1,-repLength):
                    size = 10**(digits)
                    newSection = floor((i-prevSections)/size)
                    section.append(newSection)
                    prevSections += (newSection*size)
                    if (j>0 and section[j]!=section[j-1]):
                        invalidID = False
                        break
                    j += 1
                if (invalidID):
                    # All sections equal
                    invalidIDs.add(i)
                    if (numRepititions==2):
                        invalidIDsPT1.add(i)
                    break
                    

IDSum = 0
# Part 1
for i in invalidIDsPT1:
    IDSum +=i
print(f"The sum of invalid IDs in first part is  {IDSum}")

# Part 2
IDSumPT2 = 0
for i in invalidIDs:
    IDSumPT2 +=i
print(f"The sum of all invalid IDs is  {IDSumPT2}")
    # Meaningless equation wrangling
    # x/(s)=f
    # x-(f*s)=sec
    
    # Find all sec==f
    
    # x/s=x-(x/s)*s
    # x/s=x-x

