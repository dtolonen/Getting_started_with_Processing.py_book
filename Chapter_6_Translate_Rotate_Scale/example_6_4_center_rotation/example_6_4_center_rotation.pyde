def setup():
      size(120, 120)
def draw(): 
    rotate(mouseX / 100.0) 
    rect(-80, -10, 160, 20)
    
    saveFrame("frames/SaveExample-####.png")
