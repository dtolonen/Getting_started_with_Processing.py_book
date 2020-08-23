x = 60.0   # x coordinate
y = 440.0 # y coordinate
radius = 45 # Head radius
bodyHeight = 160 # Body height
neckHeight = 70 # Neck height

easing = 0.02


def setup():
    size(360, 480)
    strokeWeight(2)
    ellipseMode(RADIUS)


def draw():
    global x
    targetX = mouseX
    x += (targetX - x) * easing
    
    if mousePressed: 
        neckHeight = 16 
        bodyHeight = 90
    else:
        neckHeight = 70 
        bodyHeight = 160

    ny = y - bodyHeight - neckHeight - radius 
    
    background(0, 153, 204)
    
    # Neck
    stroke(255)
    line(x+12, y-bodyHeight, x+12, ny)
    
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
    
    # Head
    fill(0)
    ellipse(x+12, ny, radius, radius) 
    fill(255)
    ellipse(x+24, ny-6, 14, 14) 
    fill(0)
    ellipse(x+24, ny-6, 3, 3)
    

    saveFrame("frames/SaveExample-####.png")
