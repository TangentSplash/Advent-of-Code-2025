PATH = "Day 3/input.txt"
from math import floor
import sys

input = open(PATH, 'r')

lines = input.readlines()

def findBoundedMax(start, end, bank):
    maxNum = 0
    pos = start
    maxNum = max(bank[end:start])
    pos = bank[end:start].index(maxNum)+end
    return pos+1, maxNum
        
    
# for line in lines:
#     int_list = list(map(int, line.split()))
    
nums=[list(map(int, [digit for digit in line.strip('\n')])) for line in lines]    
    # for digit in line(len):
    #     digit = int(digit)
#print(nums)

JoltageSumPart1 = 0
JoltageSumTotal = 0
for bank in nums:
    maxNums = bank[-12:]
    length = len(bank)
    end = 0
    for i in range(0,12):
        end, maxNum = findBoundedMax((length-12)+i+1,end,bank)
        maxNums[i] = maxNum
    string = ''.join([str(n) for n in maxNums])
    JoltageSumPart1 += int(string[:2])
    JoltageSumTotal += int(string)
    
# Part 1
print(f"The Joltage sum part 1 is {JoltageSumPart1}")

# Part 2
print(f"The total Joltage sum is {JoltageSumTotal}")