font = None

def setup():
    global font
    size(480, 120)
    font = createFont("SourceCodePro-Regular.ttf", 32) 
    textFont(font)

def draw():
    background(102)
    textSize(32)
    text("That’s one small step for man...", 25, 60) 
    textSize(16)
    text("That’s one small step for man...", 27, 90)
    
    saveFrame("frames/SaveExample-####.png")
