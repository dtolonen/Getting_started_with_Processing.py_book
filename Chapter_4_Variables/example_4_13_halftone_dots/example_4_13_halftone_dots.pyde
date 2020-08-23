size(480, 120)
background(0)
for y in range(32, height, 8):
    for x in range(12, width, 15):
        ellipse(x + y, y, 16 - y/10.0, 16 - y/10.0)
        saveFrame("frames/SaveExample-####.png")
