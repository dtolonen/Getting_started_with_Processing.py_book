img = None

def setup():
    global img
    size(480, 120)
    img = loadImage("lunar.jpg")

def draw():
    background(0)
    image(img, 0, 0, mouseX * 2, mouseY * 2)
    
    saveFrame("frames/SaveExample-####.png")
