angle = 0.0 
angleDirection = 1 
speed = 0.005

def setup():
      size(120, 120)

def draw():
    global angle, angleDirection 
    background(204)
    translate(20, 25) # Move to start position 
    rotate(angle)
    strokeWeight(12)
    line(0, 0, 40, 0)
    translate(40, 0)
    rotate(angle * 2.0)
    strokeWeight(6)
    line(0, 0, 30, 0)
    translate(30, 0)
    rotate(angle * 2.5)
    strokeWeight(3)
    line(0, 0, 20, 0)
    angle += speed * angleDirection
    if angle > QUARTER_PI or angle < 0:
        angleDirection = -angleDirection
        
        saveFrame("frames/SaveExample-####.png")
