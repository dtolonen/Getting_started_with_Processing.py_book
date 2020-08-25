network = None

def setup():
    global network
    size(480, 120)
    network = loadShape("network.svg")

def draw():
    background(0)
    shape(network, 30, 10)
    shape(network, 180, 10, 280, 280)
    
    saveFrame("frames/SaveExample-####.png")
