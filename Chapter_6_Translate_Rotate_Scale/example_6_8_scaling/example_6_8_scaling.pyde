def setup():
      size(120, 120)
def draw():
    translate(mouseX, mouseY) 
    scale(mouseX / 60.0) 
    rect(-15, -15, 30, 30)
    
    saveFrame("frames/SaveExample-####.png")
