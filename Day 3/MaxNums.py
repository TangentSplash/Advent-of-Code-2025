PATH = "Day 3/input.txt"
from math import floor
import sys

input = open(PATH, 'r')

lines = input.readlines()


# for line in lines:
#     int_list = list(map(int, line.split()))
    
nums=[list(map(int, [digit for digit in line[:-1]])) for line in lines]    
    # for digit in line(len):
    #     digit = int(digit)
#print(nums)

JoltageSum = 0
for bank in nums:
    # Find the largest 10's digit
    maxNum = 0
    nextLargest = 0
    for i in range(0,len(bank)-1): # Excludes final element as this can't be the 10s digit
        if bank[i]>maxNum:
            maxNum=bank[i]
            nextLargest = bank[i+1]
        elif bank[i+1] > nextLargest:
            nextLargest = bank[i+1]
    JoltageSum += (maxNum*10)+nextLargest
    
# Part 1
print(f"The Joltage sum is {JoltageSum}")