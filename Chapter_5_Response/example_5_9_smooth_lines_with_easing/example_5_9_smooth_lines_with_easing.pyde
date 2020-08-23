x=0.0 
y=0.0 
px=0.0 
py=0.0 
easing = 0.05;
    
def setup():
      size(480, 120)
      stroke(0, 102)

def draw():
    global x, y, px, py 
    targetX = mouseX;
    x += (targetX - x) * easing 
    targetY = mouseY
    y += (targetY - y) * easing 
    weight = dist(x, y, px, py) 
    strokeWeight(weight) 
    line(x, y, px, py)
    py=y
    px=x
    
    saveFrame("frames/SaveExample-####.png")
