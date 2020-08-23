radius = 40.0 
x = -radius 
speed = 0.5

def setup():
  size(240, 120)
  ellipseMode(RADIUS)
  
def draw():
    global x 
    background(0)
    x += speed # Increase the value of x
    if x > width+radius: # if the shape is off screen,
        x = -radius # move to the left edge
    arc(x, 60, radius, radius, 0.52, 5.76)
    
    saveFrame("frames/SaveExample-####.png")
