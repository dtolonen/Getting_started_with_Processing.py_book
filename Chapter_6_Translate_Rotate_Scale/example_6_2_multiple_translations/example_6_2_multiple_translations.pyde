def setup():
      size(120, 120)
def draw():
      translate(mouseX, mouseY)
      rect(0, 0, 30, 30)
      translate(35, 10)
      rect(0, 0, 15, 15)
      saveFrame("frames/SaveExample-####.png")
