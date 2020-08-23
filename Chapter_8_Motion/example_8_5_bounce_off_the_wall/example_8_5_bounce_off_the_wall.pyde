radius = 40.0 
x = 110.0 
speed = 0.5 
direction = 1

def setup():
    size(240, 120)
    ellipseMode(RADIUS)
    
def draw():
    global x, direction
    background(0)
    x += speed * direction
    if x > width-radius or x < radius:
        direction = -direction # Flip direction 
    if direction == 1:
        arc(x, 60, radius, radius, 0.52, 5.76) # Face right 
    else:
        arc(x, 60, radius, radius, 3.67, 8.9) # Face left
        
    saveFrame("frames/SaveExample-####.png")
