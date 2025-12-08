from math import sqrt
import sys


PATH = "Day 8/input.txt"
CONNECTIONS = 1000
NUM_CIRCUITS = 3
input = open(PATH, 'r')

lines = input.readlines()

class JunctionBox():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = None
        
    def get_dist(self, otherBox):
        xdist = otherBox.x - self.x
        ydist = otherBox.y - self.y
        zdist = otherBox.z - self.z
        dist = sqrt((xdist**2) + (ydist**2) + (zdist**2))
        return dist
    
    def addToCircuit(self, circuit):
        self.circuit = circuit
        
    def getCircuit(self):
        return self.circuit
    
    def __repr__(self) -> str:
        return f"Box ({self.x}, {self.y}, {self.z})"
    
class Circuit():
    def __init__(self, box1, box2):
        self.boxes = [box1, box2]
    
    def addBox(self, box):
        self.boxes.append(box)
    
    def getNumberOfBoxes(self):
        return len(self.boxes)
    
    def merge(self, otherCircuit):
        self.boxes.extend(otherCircuit.boxes)
        for box in otherCircuit.boxes:
            box.addToCircuit(self)
            
    def __repr__(self) -> str:
        return f"Circuit, len={len(self.boxes)}, ID={hash(self)}"
        
junctionBoxes = []
for line in lines:
    x,y,z = map(int,line.split(',')) 
    junctionBoxes.append(JunctionBox(x,y,z))

distances = {}
for i in range(len(junctionBoxes)):
    boxi = junctionBoxes[i]
    for j in range(i+1,len(junctionBoxes)):
        boxj = junctionBoxes[j]
        dist = boxi.get_dist(boxj)
        if (distances.get(dist) != None):
            print("Incorrect assumption that all distances were unique")
            sys.exit(1)
        distances[dist] = [boxi,boxj]
        
distancesSorted = sorted(distances.items(), key=lambda item: item[0])

circuits = []
def getNextClosestBoxes(i):
    [box1, box2] = distancesSorted[i][1]
    box1Circuit = box1.getCircuit()
    box2Circuit = box2.getCircuit()
    return box1,box2, box1Circuit, box2Circuit

# Make the CONNECTIONS shortest circuits
for i in range(CONNECTIONS):
    box1, box2, box1Circuit, box2Circuit = getNextClosestBoxes(i)
    if (box1Circuit == box2Circuit and box1Circuit != None):
        pass
    elif (box1Circuit == None and box2Circuit == None):
        newCircuit = Circuit(box1,box2)
        box1.addToCircuit(newCircuit)
        box2.addToCircuit(newCircuit)
        circuits.append(newCircuit)
    elif (box2Circuit == None):
        box1Circuit.addBox(box2)
        box2.addToCircuit(box1Circuit)
    elif (box1Circuit == None):
        box2Circuit.addBox(box1)
        box1.addToCircuit(box2Circuit)
    else: # Merge Circuits
        box1Circuit.merge(box2Circuit)
        circuits.remove(box2Circuit)

        
bigestCircuits = sorted(circuits, key=lambda x: x.getNumberOfBoxes(), reverse=True)
length = 1
for i in range(NUM_CIRCUITS):
    circuitLength = bigestCircuits[i].getNumberOfBoxes()
    length *= circuitLength
    
print(f"The length of the {NUM_CIRCUITS} biggest circuits, multiplied together is {length}")

# Incorrect - 8