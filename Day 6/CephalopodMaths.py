from math import prod
import sys


PATH = "Day 6/input.txt"

input = open(PATH, 'r')

lines = input.readlines()

problems=[]
mathsSum = 0

for line in lines:
    line = line.strip('\n')
    problems.append(line.split())
   
for i in range(len(problems[0])):
    operator = problems[-1][i]
    operands = []
    #operands=list(map(int, problems[:-1][i]))
    for j in range(len(problems)-1):
        operands.append(int(problems[j][i]))
        
    if (operator == '+'):
        calculation = sum(operands)
    elif (operator == '*'):
        calculation = prod(operands)
    else:
        print(f"Unexpected operator {operator}, wiith operands {operands}")
        sys.exit(1)
    mathsSum += calculation    
print(f"The sum of the calculations is {mathsSum}")