img = None
    
def setup():
    global img
    size(480, 120)
    img = loadImage("lunar.jpg")
    
def draw():
    image(img, 0, 0)
    
    saveFrame("frames/SaveExample-####.png")
