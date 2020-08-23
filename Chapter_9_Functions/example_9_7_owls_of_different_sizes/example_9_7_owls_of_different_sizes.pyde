def setup():
    size(480, 120)

def draw():
    background(176, 204, 226)
    randomSeed(0)
    for i in range(35, width + 40, 40):
        gray = int(random(0, 102)) 
        scalar = random(0.25, 1.0) 
        owl(i, 110, gray, scalar)


def owl(x, y, g, s):
    pushMatrix()
    translate(x, y)
    scale(s) # Set the scale
    stroke(138-g, 138-g, 125-g) # Set the gray value 
    strokeWeight(70)
    line(0, -35, 0, -65) # Body
    noStroke()
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
