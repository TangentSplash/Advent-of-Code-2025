PATH = "Day 1/input.txt"
from math import floor
import sys

input = open(PATH, 'r')

lines = input.readlines()
#print(lines)

START_NUM = 50

num = START_NUM
zero_stopped = 0
zero_passed = 0

for instr in lines:
    change = int(instr[1:])
    times_round = floor(change / 100)
    change -= (100*times_round)
    if instr[0]=='R':
        num += change
        if (num > 100):
            zero_passed+=1
    elif instr[0]=='L':
        prevNum = num
        num -= change
        if (num < 0 and prevNum != 0):
            zero_passed += 1
    else:
        print(f"Invalid instruction: {instr}")
        sys.exit(1)

    num = num%100
    zero_passed += times_round
    # Part 1
    if (num == 0):
        zero_stopped+=1
 
zero_passed +=zero_stopped       
print(f"The number of zeros stopped was {zero_stopped}")
print(f"The number of zeros passed was {zero_passed}")
print(f"The final number was {num}")
        