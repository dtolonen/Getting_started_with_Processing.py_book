angle = 0.0 
offset = 60.0 
scalar = 30.0 
speed = 0.05

def setup():
    size(120, 120)

def draw():
    global angle
    x = offset + cos(angle) * scalar 
    y = offset + sin(angle) * scalar 
    ellipse( x, y, 40, 40)
    angle += speed
    
    saveFrame("frames/SaveExample-####.png")
