font = None

quote = "That’s one small step for man..."

def setup():
    global font
    size(480, 120)
    font = createFont("SourceCodePro-Regular.ttf", 24) 
    textFont(font)
    
def draw():
    background(102)
    text(quote, 26, 24, 240, 100)
    
    saveFrame("frames/SaveExample-####.png")
