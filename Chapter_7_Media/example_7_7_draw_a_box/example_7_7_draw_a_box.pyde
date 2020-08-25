font = None

def setup():
    global font
    size(480, 120)
    font = createFont("SourceCodePro-Regular.ttf", 24)
    textFont(font)

def draw():
    background(102)
    text("That's one small step for man...", 26, 24, 240, 100)
    
    saveFrame("frames/SaveExample-####.png")
