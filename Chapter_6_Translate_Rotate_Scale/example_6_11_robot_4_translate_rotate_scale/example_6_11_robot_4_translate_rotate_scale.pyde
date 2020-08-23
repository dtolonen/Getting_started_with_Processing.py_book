x = 60 # x coordinate
y = 440 # y coordinate
radius = 45 # Head radius
bodyHeight = 180 # Body height
neckHeight = 40 # Neck height

easing = 0.04 



def setup():
    size(360, 480)
    strokeWeight(2)
    ellipseMode(RADIUS)
  
  
def draw():
    background(0, 153, 204)
  
    translate(mouseX, y) # Move all to (mouseX, y)
    if mousePressed:
      scale(1.0)
    else:
      scale(0.6) # 60% size when mouse is pressed
      
    # Body
    noStroke()
    fill(255, 204, 0)
    ellipse(0, -33, 33, 33)
    fill(0)
    rect(-45, -bodyHeight, 90, bodyHeight-33)
    
    # Neck
    stroke(255)
    neckY = -(bodyHeight + neckHeight + radius) 
    line(12, -bodyHeight, 12, neckY)
    
    # Hair
    pushMatrix() 
    translate(12, neckY) 
    angle = -PI/30.0 
    for i in range(31):
        line(80, 0, 0, 0)
        rotate(angle)
    popMatrix()
    
    # Head
    noStroke()
    fill(0)
    ellipse(12, neckY, radius, radius) 
    fill(255)
    ellipse(24, neckY-6, 14, 14) 
    fill(0)
    ellipse(24, neckY-6, 3, 3)
    
    saveFrame("frames/SaveExample-####.png")
