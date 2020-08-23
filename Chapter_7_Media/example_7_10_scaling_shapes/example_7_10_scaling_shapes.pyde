network = None

def setup():
    global network
    size(240, 120)
    shapeMode(CENTER)
    network = loadShape("network.svg")

def draw():
    background(0)
    diameter = map(mouseX, 0, width, 10, 800) 
    shape(network, 120, 60, diameter, diameter)
    
    
    saveFrame("frames/SaveExample-####.png")
