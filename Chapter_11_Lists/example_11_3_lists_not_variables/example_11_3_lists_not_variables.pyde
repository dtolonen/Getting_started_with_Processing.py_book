x = []

def setup():
  size(240, 120) 
  noStroke() 
  fill(255, 200) 
  for i in range(3000):
    x.append(random(-1000, 200))

def draw():
  background(0) 
  for i in range(len(x)):
    x[i] += 0.5
    y = i * 0.4
    arc(x[i], y, 12, 12, 0.52, 5.76)
    
    saveFrame("frames/SaveExample-####.png")
