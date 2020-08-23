class JitterBug(object):
    def __init__(self, tempX, tempY, tempDiameter):
        self.x = tempX
        self.y = tempY 
        self.diameter = tempDiameter 
        self.speed = 0.5 # try 2.5, 10.5, 100
        
    def move(self):
        self.x += random(-self.speed, self.speed) 
        self.y += random(-self.speed, self.speed)
    
    def display(self):
        ellipse(self.x, self.y, self.diameter, self.diameter)

bug = JitterBug(240, 60, 20) 

def setup():
    size(480, 120)

def draw(): 
    bug.move() 
    bug.display()
    
    saveFrame("frames/SaveExample-####.png")
