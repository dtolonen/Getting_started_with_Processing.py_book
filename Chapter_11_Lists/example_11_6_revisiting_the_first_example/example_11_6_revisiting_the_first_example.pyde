x = [-20.0, 20.0]

def setup():
  size(240, 120) 
  noStroke()

def draw():
  background(0) 
  x[0] += 0.5 # Increase the first element 
  x[1] += 0.5 # Increase the second element 
  arc(x[0], 30, 40, 40, 0.52, 5.76) 
  arc(x[1], 90, 40, 40, 0.52, 5.76)
  
  saveFrame("frames/SaveExample-####.png")
