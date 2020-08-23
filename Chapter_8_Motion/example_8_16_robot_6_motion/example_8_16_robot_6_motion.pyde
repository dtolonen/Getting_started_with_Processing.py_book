x = 180.0 # x coordinate
y = 400.0 # y coordinate
bodyHeight = 153.0 # Body height
neckHeight = 56.0 # Neck height
radius = 45.0 # Head radius
angle = 0.0 # Angle for motion


def setup():
  size(360, 480)
  ellipseMode(RADIUS)
  background(0, 153, 204)
  
def draw():
    global x, y, angle
    # Change position by a small random amount 
    x += random(-4, 4)
    y += random(-1, 1)
   
    # Change height of neck
    neckHeight = 80 + sin(angle) * 30 
    angle += 0.05
    
    # Adjust the height of the head
    ny = y - bodyHeight - neckHeight - radius
    
    # Neck
    stroke(102)
    line(x+2, y-bodyHeight, x+2, ny)
    line(x+12, y-bodyHeight, x+12, ny)
    line(x+22, y-bodyHeight, x+22, ny)
    
    # Antennae
    line(x+12, ny, x-18, ny-43)
    line(x+12, ny, x+42, ny-99)
    line(x+12, ny, x+78, ny+15)
    
    # Body 
    noStroke()
    fill(255, 204, 0)
    ellipse(x, y-33, 33, 33)
    fill(0)
    rect(x-45, y-bodyHeight, 90, bodyHeight-33) 
    fill(102)
    rect(x-45, y-bodyHeight+17, 90, 6)
    
    # Head
    fill(0)
    ellipse(x+12, ny, radius, radius) 
    fill(255)
    ellipse(x+24, ny-6, 14, 14) 
    fill(0)
    ellipse(x+24, ny-6, 3, 3)
    
    saveFrame("frames/SaveExample-####.png")
    
    
