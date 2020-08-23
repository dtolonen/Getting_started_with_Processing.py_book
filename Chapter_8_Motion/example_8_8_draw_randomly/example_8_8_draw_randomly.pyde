def setup():
      size(240, 120)
      
def draw():
    background(204)
    for x in range(20, width, 20):
        mx=mouseX/10
        offsetA = random(-mx, mx)
        offsetB = random(-mx, mx)
        line(x + offsetA, 20, x - offsetB, 100)
        
        saveFrame("frames/SaveExample-####.png")
