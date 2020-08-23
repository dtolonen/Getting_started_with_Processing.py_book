def setup():
    size(480, 120)

def draw():
    background(176, 204, 226)

    # Left owl
    translate(110, 110) 
    stroke(138, 138, 125) 
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
    
    # Right owl
    translate(70, 0); 
    stroke(138, 138, 125) 
    strokeWeight(70) 
    line(0, -35, 0, -65) # Body
    noStroke()
    fill(255)
    ellipse(-17.5, -65, 35, 35) # Left eye dome
    ellipse(17.5, -65, 35, 35) # Right eye dome, note what happens with -17.5!
    arc(0, -65, 70, 70, 0, PI) # Chin
    fill(51, 51, 30)
    ellipse(-14, -65, 8, 8) # Left eye 
    ellipse(14, -65, 8, 8) # Right eye 
    quad(0, -58, 4, -51, 0, -44, -4, -51) # Beak
    
    saveFrame("frames/SaveExample-####.png")
                                  
                                  
                                  
