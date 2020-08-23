startX = 20.0 # Initial x coordinate
stopX = 160.0 # Final x coordinate
startY = 30.0 # Initial y coordinate
stopY = 80.0 # Final y coordinate
x = startX # Current x coordinate

y = startY # Current y coordinate
step = 0.005 # Size of each step (0.0 to 1.0) 
pct = 0.0 # Percentage traveled (0.0 to 1.0)

def setup():
  size(240, 120)
  

def draw(): 
    global x, y, pct 
    background(0) 
    if pct < 1.0:
        x = startX + ((stopX-startX) * pct) 
        y = startY + ((stopY-startY) * pct) 
        pct += step
    ellipse(x, y, 20, 20)
    
    saveFrame("frames/SaveExample-####.png")
