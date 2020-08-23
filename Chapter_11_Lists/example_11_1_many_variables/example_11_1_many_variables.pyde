x1 = -20.0
x2 = 20.0

def setup():
  size(240, 120) 
  noStroke()

def draw():
  global x1, x2 
  background(0)
  x1 += 0.5
  x2 += 0.5
  arc(x1, 30, 40, 40, 0.52, 5.76) 
  arc(x2, 90, 40, 40, 0.52, 5.76)
  
  saveFrame("frames/SaveExample-####.png")
