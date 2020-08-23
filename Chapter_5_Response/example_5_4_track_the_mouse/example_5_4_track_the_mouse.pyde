def setup():
      size(480, 120)
      fill(0, 102)
      noStroke()
def draw():
      ellipse(mouseX, mouseY, 9, 9)
      
      saveFrame("frames/SaveExample-####.png")
