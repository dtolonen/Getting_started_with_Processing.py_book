def setup():
      size(480, 120)
      stroke(0, 102)
def draw():
    weight = dist(mouseX, mouseY, pmouseX, pmouseY) 
    strokeWeight(weight)
    line(mouseX, mouseY, pmouseX, pmouseY)

    saveFrame("frames/SaveExample-####.png")
