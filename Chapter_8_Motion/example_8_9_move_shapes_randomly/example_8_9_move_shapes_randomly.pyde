speed = 2.5 
diameter = 20 
x=0.0 
y=0.0

def setup(): 
    global x, y 
    size(240, 120) 
    x = width/2
    y = height/2

def draw():
    global x, y
    x += random(-speed, speed)
    y += random(-speed, speed) 
    x = constrain(x, 0, width) # ensure that the ellipse remains within the screen
    y = constrain(y, 0, height)
    ellipse(x, y, diameter, diameter)
    
    # The randomSeed() function can be used to force random() 
    # to produce the same sequence of numbers each time a program is run. 
    
    saveFrame("frames/SaveExample-####.png")
