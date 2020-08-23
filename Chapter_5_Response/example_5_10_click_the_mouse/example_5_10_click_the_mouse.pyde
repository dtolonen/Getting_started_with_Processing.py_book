def setup():
      size(240, 120)
      strokeWeight(30)
def draw(): 
    background(204) 
    stroke(102)
    line(40, 0, 70, height) 
    if mousePressed == True:
        stroke(0)
        line(0, 70, width, 50)
        
        saveFrame("frames/SaveExample-####.png")
