def setup():
    size(240, 120)
def draw():
    background(204)
    line(20, 20, 220, 100)
    if keyPressed:
        line(220, 20, 20, 100)
    
    saveFrame("frames/SaveExample-####.png")
