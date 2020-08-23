gray = []

def setup():
    size(240, 120) 
    for i in range(width):
        gray.append(random(0, 255))

def draw():
  for i in range(len(gray)):
    stroke(gray[i]) 
    line(i, 0, i, height)
    
    saveFrame("frames/SaveExample-####.png")
