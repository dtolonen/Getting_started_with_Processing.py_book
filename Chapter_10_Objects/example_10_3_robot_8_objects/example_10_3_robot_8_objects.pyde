class Robot(object):
    def __init__(self, tempSvgName, tempX, tempY):
        self.svgName = tempSvgName 
        self.xpos = tempX
        self.ypos = tempY
        self.angle = random(0, TWO_PI)
        self.yoffset = 0

    def loadSvg(self):
        self.botShape = loadShape(self.svgName)

    def update(self):
        self.angle += 0.05
        self.yoffset = sin(self.angle) * 20

    def display(self):
        shape(self.botShape, self.xpos, self.ypos + self.yoffset);

bot1 = Robot("robot1.svg", 90, 80) 
bot2 = Robot("robot2.svg", 440, 30)

def setup(): 
    size(720, 480)
    bot1.loadSvg() 
    bot2.loadSvg()

def draw():
    background(0, 153, 204)
  
    # Update and display first robot
    bot1.update() 
    bot1.display()

    # Update and display second robot
    bot2.update() 
    bot2.display()
    
    saveFrame("frames/SaveExample-####.png")
