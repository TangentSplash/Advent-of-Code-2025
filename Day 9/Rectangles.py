PATH = "Day 9/input.txt"
input = open(PATH, 'r')

points = []
lines = input.readlines()
numPoints = len(lines)
for line in lines:
    line = line.strip('\n')
    points.append(list(map(int, line.split(','))))
  
maxArea = 0    
for i in range(numPoints):
    x_i = points[i][0]
    y_i = points[i][1]
    for j in range(i+1,numPoints):
        x_j = points[j][0]
        y_j = points[j][1]
        
        x = (x_i - x_j) + 1
        y = (y_i - y_j) + 1
        area = abs(x*y)
        maxArea = max(area,maxArea)
        
print(f"The largest area after calculating all of the areas is {maxArea}")