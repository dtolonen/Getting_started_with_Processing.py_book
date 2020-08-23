x=0.0 
easing = 0.01

def setup():
    size(220, 120)

def draw():
    global x
    targetX = mouseX
    x += (targetX - x) * easing 
    ellipse(x, 40, 12, 12) 
    print targetX, x
    
    saveFrame("frames/SaveExample-####.png")
