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
            
    def inRange(self, point):
        x1 = self.point1.getX()
        y1 = self.point1.getY()
        
        x2 = self.point2.getX()
        y2 = self.point2.getY()
        
        xl = min(x1,x2)
        xh = max(x1,x2)
        yl = min(y1,y2)
        yh = max(y1,y2)
        
        xp = point.getX()
        yp = point.getY()
        
        return ((xl <= xp <= xh) and (yl <= yp <= yh))
            
    def __repr__(self) -> str:
        if(self.vertical):
            return f"{self.strType}: Vertical at x = {self.point1.getX()}"
        else:
            return f"{self.strType}: ({self.a}x) + ({self.b}y) + ({self.c})"
        
    
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
                if (line.vertical and boundary.vertical and line.xv == boundary.xv):
                    ly1 = line.point1.getY()
                    by1 = boundary.point1.getY()
                    by2 = boundary.point2.getY()
                    if (by1 <= ly1 <= by2):
                        ly2 = line.point2.getY()
                        if not (by1 <= ly2 <= by2):
                            return False # Goes out-of-bounds
                elif (line.horizontal and boundary.horizontal and line.yh == boundary.yh):
                    lx1 = line.point1.getX()
                    bx1 = boundary.point1.getX()
                    bx2 = boundary.point2.getX()
                    if (bx1 <= lx1 <= bx2):
                        lx2 = line.point2.getX()
                        if not (bx1 <= lx2 <= bx2):
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


point1 = points[0]
x = True
boundingLines = []
for i in range(numPoints):
    point2 = point1.getConnectedPoint(points,x)
    boundingLines.append(BoundingLine(point1, point2))
    x = not x
    point1 = point2
   
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
'''