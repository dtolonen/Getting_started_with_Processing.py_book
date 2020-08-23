# Copy JitterBug class here!

class JitterBug(object):
    def __init__(self, tempX, tempY, tempDiameter):
        self.x = tempX
        self.y = tempY 
        self.diameter = tempDiameter 
        self.speed = 0.5
    
    def move(self):
        self.x += random(-self.speed, self.speed) 
        self.y += random(-self.speed, self.speed)
    
    def display(self):
        ellipse(self.x, self.y, self.diameter, self.diameter)

    
    
bugs = []

def setup():
    size(240, 120)
    for i in range(33):
        x = random(width)
        y = random(height)
        r=i+2 
        bugs.append(JitterBug(x, y, r))

def draw():
    for b in bugs:
        b.move() 
        b.display()
        
        saveFrame("frames/SaveExample-####.png")
