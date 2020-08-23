x=280 
y=-100 
diameter = 380

def setup():
      size(480, 120)
      fill(102)
def draw():
      background(204)
      ellipse(x, y, diameter, diameter)
      saveFrame("frames/SaveExample-####.png")
