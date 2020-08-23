def setup():
      size(120, 120)
      
def draw(): 
    translate(mouseX, mouseY) 
    scalar = mouseX / 60.0 
    scale(scalar)
    if scalar > 0.0:
        strokeWeight(1.0 / scalar) 
    else:
        strokeWeight(0) 
    rect(-15, -15, 30, 30)
    saveFrame("frames/SaveExample-####.png")
