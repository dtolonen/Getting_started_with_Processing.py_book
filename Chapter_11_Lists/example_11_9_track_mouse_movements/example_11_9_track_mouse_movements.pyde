x = []
y = []

def setup():
  size(240, 120) 
  noStroke()

def draw():
  background(0) 
  x.insert(0, mouseX) 
  y.insert(0, mouseY) 
  for i in range(len(x)):
    fill(i * 4)
    ellipse(x[i], y[i], 40, 40)
    
    saveFrame("frames/SaveExample-####.png")
