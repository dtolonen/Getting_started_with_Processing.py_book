x=80
y=30 
w=80 
h=60

def setup():
      size(240, 120)

def draw():
    background(204); 
    if mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h:
        fill(0)
    else:
        fill(255)
    rect(x, y, w, h)
      
    saveFrame("frames/SaveExample-####.png")
