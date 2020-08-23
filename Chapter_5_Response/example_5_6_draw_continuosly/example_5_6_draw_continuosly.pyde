def setup():
      size(480, 120)
      strokeWeight(4)
      stroke(0, 102)
def draw():
      line(mouseX, mouseY, pmouseX, pmouseY)
      
      saveFrame("frames/SaveExample-####.png")
