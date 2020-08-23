x=120 
y=60 
radius = 12

def setup():
      size(240, 120)
      ellipseMode(RADIUS)
def draw():
    global radius
    background(204)
    d = dist(mouseX, mouseY, x, y) 
    if d < radius:
        radius += 1
        fill(0)
    else:
        fill(255)
    ellipse(x, y, radius, radius)
      
    saveFrame("frames/SaveExample-####.png")
      
