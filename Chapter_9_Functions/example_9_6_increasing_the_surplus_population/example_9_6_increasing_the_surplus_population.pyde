

    
def setup():
    size(480, 120)

def draw():
    background(176, 204, 226)
    for x in range(35, width + 70, 70):
        owl(x, 110)
    
    
def owl(x, y):
    pushMatrix()
    translate(x, y)
    stroke(138, 138, 125) 
    strokeWeight(70)
    line(0, -35, 0, -65) # Body 
    noStroke() # Note what happens if you comment this out
    fill(255)
    ellipse(-17.5, -65, 35, 35) # Left eye dome
    ellipse(17.5, -65, 35, 35) # Right eye dome
    arc(0, -65, 70, 70, 0, PI) # Chin
    fill(51, 51, 30)
    ellipse(-14, -65, 8, 8) # Left eye
    ellipse(14, -65, 8, 8) # Right eye
    quad(0, -58, 4, -51, 0, -44, -4, -51) # Beak
    popMatrix()
    
    saveFrame("frames/SaveExample-####.png")
