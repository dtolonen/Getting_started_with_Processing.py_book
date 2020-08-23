def setup():
      size(120, 120)
def draw(): 
    rotate(mouseX / 100.0) 
    rect(40, 30, 160, 20)
    saveFrame("frames/SaveExample-####.png")
