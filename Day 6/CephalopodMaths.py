from math import prod
import sys


PATH = "Day 6/input.txt"

input = open(PATH, 'r')

lines = input.readlines()

problems=[]
mathsSum = 0
CelphalopodSum = 0
indices = [ 0 ]
line = lines[0]
for i in range(len(line)):
    if line[i] == ' ':
        columnEnd = True
        for j in range(1,len(lines)):
            if lines[j][i] != ' ':
                columnEnd = False
                break
        if (columnEnd):
            indices.append(i)  

for line in lines:
    line = line.strip('\n')
    problems.append([line[a:b] for a,b in zip(indices, indices[1:]+[None])]) 


for i in range(len(problems[0])):
    operator = problems[-1][i]
    operands = []
    numLength = 0
    CelphalopodOperands =[]
    #operands=list(map(int, problems[:-1][i]))
    for j in range(len(problems)-1):
        number = problems[j][i]
        operands.append(int(number))
        numLength = max(numLength, len(number))
    for p in range(numLength-1,-1,-1):
        CelphalopodNum = ''
        for j in range(len(problems)-1):
            number = problems[j][i]
            CelphalopodNum += number[p]
        if(not CelphalopodNum.isspace()):
            CelphalopodOperands.append(int(CelphalopodNum))
                
        
    if (operator.strip(' ') == '+'):
        calculation = sum(operands)
        CelphalopodCal = sum(CelphalopodOperands)
    elif (operator.strip(' ') == '*'):
        calculation = prod(operands)
        CelphalopodCal = prod(CelphalopodOperands)
    else:
        print(f"Unexpected operator {operator}, with operands {operands}")
        sys.exit(1)
    mathsSum += calculation 
    CelphalopodSum += CelphalopodCal   
print(f"The sum of the calculations is {mathsSum}")
print(f"The sum of Celphalopod calculations is {CelphalopodSum}")