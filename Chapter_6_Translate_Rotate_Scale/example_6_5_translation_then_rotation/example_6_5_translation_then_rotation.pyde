angle = 0.0 

def setup():
    size(120, 120)
    
def draw():
    global angle 
    translate(mouseX, mouseY) 
    rotate(angle)
    rect(-15, -15, 30, 30) 
    angle += 0.1
    
    saveFrame("frames/SaveExample-####.png")
