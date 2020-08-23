x1 = -10.0
x2 = 10.0
x3 = 35.0
x4 = 18.0
x5 = 30.0

def setup():
  size(240, 120) 
  noStroke()

def draw():
  global x1, x2, x3, x4, x5 
  background(0)
  x1 += 0.5
  x2 += 0.5
  x3 += 0.5
  x4 += 0.5
  x5 += 0.5
  arc(x1, 20, 20, 20, 0.52, 5.76) 
  arc(x2, 40, 20, 20, 0.52, 5.76) 
  arc(x3, 60, 20, 20, 0.52, 5.76) 
  arc(x4, 80, 20, 20, 0.52, 5.76) 
  arc(x5, 100, 20, 20, 0.52, 5.76)
  
  saveFrame("frames/SaveExample-####.png")
