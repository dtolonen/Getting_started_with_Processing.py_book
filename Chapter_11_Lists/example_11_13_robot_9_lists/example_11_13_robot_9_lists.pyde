class Robot(object):
    
    # Set initial values
    def __init__(self, shape, tempX, tempY): 
        self.botShape = shape
        self.xpos = tempX
        self.ypos = tempY
        self.angle = random(0, TWO_PI) 
        self.yoffset = 0.0


    def update(self):
        self.angle += 0.05
        self.yoffset = sin(self.angle) * 20
    
    
    def display(self):
        shape(self.botShape, self.xpos, self.ypos + self.yoffset)


bots = [] # Create list for Robot objects 
botCount = 20
    


def setup():
    size(720, 480)
    robotShape = loadShape("robot1.svg") # Create each object
    for i in range(botCount):
        # Create a random x coordinate
        x = random(-40, width-40)
        # Assign the y coordinate based on the order 
        y = map(i, 0, botCount, -100, height-200)
        bots.append(Robot(robotShape, x, y))



def draw():
    background(0, 153, 204)
    for b in bots:
        b.update() 
        b.display()
        
        saveFrame("frames/SaveExample-####.png")
