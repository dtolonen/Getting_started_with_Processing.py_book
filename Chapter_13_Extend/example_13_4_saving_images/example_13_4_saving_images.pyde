bot = None 
x=0

def setup():
    global bot
    size(720, 480)
    bot = loadShape("robot1.svg") 
    frameRate(30)
    
def draw():
    global x
    background(0, 153, 204)
    translate(x, 0)
    shape(bot, 0, 80) 
    saveFrame("frames/SaveExample-####.tif") 
    x+=12
    if frameCount == 60:
        exit()
        
        saveFrame("frames/SaveExample-####.png")
