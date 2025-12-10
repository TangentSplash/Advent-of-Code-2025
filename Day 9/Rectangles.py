import sys


PATH = "Day 9/inputtest.txt"
input = open(PATH, 'r')
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
    def getArea(self,otherCorner):
        x = (self.x - otherCorner.getX()) + 1
        y = (self.y - otherCorner.getY()) + 1
        return abs(x*y)
    
    def __repr__(self) -> str:
        return f"Point ({self.x}, {self.y})"
    
    def getConnectedPoint(self, points, x):
        potentialPoints = []
        for point in points:
            if (point == self):
                continue
            if (x):
                if(point.getX() == self.x):
                    potentialPoints.append(point)
            else:
                if(point.getY() == self.y):
                    potentialPoints.append(point)
        if (len(potentialPoints) != 1):
            print("ahhhh")
            sys.exit(1)
        else:
            point = potentialPoints[0]
        return point
    
class Line():
    def __init__(self,point1,point2):
        self.strType = "Line"
        self.point1 = point1
        self.point2 = point2
        
        x1 = point1.getX()
        y1 = point1.getY()
        
        x2 = point2.getX()
        y2 = point2.getY()
        
        self.vertical = (x1 == x2)
        self.horizontal = (y1 == y2)
        
        self.xv = x1
        self.yh = y1
        # if (not self.vertical):
        #     self.slope = (y2 - y1)/(x2 - x1)
        #     # Equation of a line in the form ax+by+c=0
        #     self.a = self.slope
        #     self.b = -1
        #     self.c = y1 - (self.slope * x1)
            
    def inRange(self, val, X):
        if (X):
            x1 = self.point1.getX()
            x2 = self.point2.getX()
            xl = min(x1,x2)
            xh = max(x1,x2)
            xp = val
            return (xl <= xp <= xh)
        
        else:
            y1 = self.point1.getY()
            y2 = self.point2.getY()
            yl = min(y1,y2)
            yh = max(y1,y2)     
            yp = val
            return (yl <= yp <= yh)
            
    def __repr__(self) -> str:
        if(self.vertical):
            return f"{self.strType}: Vertical at x = {self.xv}"
        else:
            return f"{self.strType}: Horizontal at y = + {self.yh}"
        
    
class BoundingLine(Line):
    def __init__(self, point1, point2):
        super().__init__(point1, point2)
        self.strType = "BoundingLine"
    
class Rectangle():
    def __init__(self, Rpoint1, Rpoint2):
        self.lines = []
        self.Rpoint1 = Rpoint1
        self.Rpoint2 = Rpoint2
        x1 = Rpoint1.getX()
        y1 = Rpoint1.getY()
        
        x2 = Rpoint2.getX()
        y2 = Rpoint2.getY()
        
        Rpoint3 = Point(x1,y2)
        Rpoint4 = Point(x2,y1)
        
        self.lines.append(Line(Rpoint1,Rpoint3))
        self.lines.append(Line(Rpoint3,Rpoint2))
        self.lines.append(Line(Rpoint2,Rpoint4))
        self.lines.append(Line(Rpoint4,Rpoint1))

    # def __getIntersectionPoint(l1, l2):
    #     if(not (l1.vertical or l2.vertical)):
    #         x = ((l1.b*l2.c)-(l2.b*l1.c)) / ((l1.a*l2.b)-(l2.a*l1.b))
    #         y = ((l1.c*l2.a)-(l2.c*l1.a)) / ((l1.a*l2.b)-(l2.a*l1.b))
    #         return Point(x,y)
    #     elif (l1.vertical and l2.vertical):
    #         x = y = None
    #     elif (l1.vertical):
    #         y = l1.point1.getY()
    #         x = (y + (l2.slope*l2.point1.getX()) - l2.point1.getY()) / l2.slope
    #     else:
    #         y = l2.point1.getY()
    #         x = (y + (l1.slope*l1.point1.getX()) - l1.point1.getY()) / l1.slope
    #     return x,y
    
    def containedIn(self, boundingLines):
        for boundary in boundingLines:
            for line in self.lines:
                if (line.vertical and boundary.horizontal and  boundary.inRange(line.xv,True)):
                    if(line.inRange(boundary.yh, False)):
                        return False # Goes out-of-bounds
                    
                elif (line.horizontal and boundary.vertical and boundary.inRange(line.yh,False)):
                    if(line.inRange(boundary.xv, False)):
                        return False # Goes out-of-bounds
        return True # Remains in-bounds
        
    def getArea(self):
        return self.Rpoint1.getArea(self.Rpoint2)
    
    def __repr__(self) -> str:
        return f"Rectangle ({self.x}, {self.y})"
        
points = []
lines = input.readlines()
numPoints = len(lines)
for line in lines:
    line = line.strip('\n')
    pointsStr = line.split(',')
    x = int(pointsStr[0])
    y = int(pointsStr[1])
    points.append(Point(x,y))
  
maxArea = 0    
for i in range(numPoints):
    for j in range(i+1,numPoints):
        area = points[i].getArea(points[j])
        maxArea = max(area,maxArea)
        
print(f"The largest area after calculating all of the areas is {maxArea}")

def inflate(points):
    horz = False #Point1 to 2 is horizontal line
    first = True
    newPoints = []
    for i in range(numPoints):
        point = points[i]
        lastPoint = points[i-1]
        nextPoint = points[(i+1)%numPoints]
        
        pX = point.getX()
        pY = point.getY()
        
        if (horz):
            lY = lastPoint.getY()
                
            if (lY < pY):
                dy = -1
            else:
                dy = 1
        else:
            lX = lastPoint.getX()
            if (lX < pX):
                dx = 1
            else:
                dx = -1
                
            if (first):
                nY = nextPoint.getY()
                if (nY < pY):
                    dy = 1
                else:
                    dy = -1
            
        first = False
        newPoint = Point(pX+dx,pY+dy)
        newPoints.append(newPoint)
        horz = not horz
    return newPoints
        
point1 = points[0]
x = True
boundaryPoints = [point1]
for i in range(numPoints-1):
    point2 = point1.getConnectedPoint(points,x)
    boundaryPoints.append(point2)
    x = not x
    point1 = point2
    
boundaryPointsInflated = inflate(boundaryPoints)
boundingLines = []

for j in range(numPoints - 1):
   boundingLines.append(BoundingLine(boundaryPointsInflated[j],boundaryPointsInflated[j+1]))
maxAreaPt2 = 0    
for i in range(numPoints):
    for j in range(i+1,numPoints):
        rect = Rectangle(points[i],points[j])
        if(rect.containedIn(boundingLines)):
            area = rect.getArea()
            maxAreaPt2 = max(area,maxAreaPt2) 
        
print(f"The largest contained area after calculating all of the areas is {maxAreaPt2}")

# If a line co-linear & share any point with a boundary line it should be entierly contained within
'''
# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............


  ...000000.
  ........0
  ........0
  ...000000
'''