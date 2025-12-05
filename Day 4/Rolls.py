PATH = "Day 4/input.txt"
from math import floor
import sys

ROLLS = '@'

input = open(PATH, 'r')

lines = input.readlines()
accessable = 0


height = len(lines)
width = len(lines[0].strip('\n'))
for y in range(height):
    lines[y]=list(lines[y].strip('\n'))
    
for y in range(height):
    for x in range(width):
        searchArea = [['-' for i in range(3)] for j in range(3)]
        if (lines[y][x] == ROLLS):
            for j in range(-1,2):
                q = y + j
                if (q >= 0 and q < height):
                    for i in range(-1,2):
                        p = x + i
                        if (p >= 0 and p < width and not (i == 0 and j == 0)):
                            searchArea[j+1][i+1] = lines[q][p]
            if( sum(line.count(ROLLS) for line in searchArea) < 4 ):
                accessable += 1
                #print(f"{x},{y}")

print(f'The number of accessable rolls is {accessable}')