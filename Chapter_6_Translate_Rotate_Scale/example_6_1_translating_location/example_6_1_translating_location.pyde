def setup():
      size(120, 120)
def draw():
      translate(mouseX, mouseY)
      rect(0, 0, 30, 30)
      
      saveFrame("frames/SaveExample-####.png")
