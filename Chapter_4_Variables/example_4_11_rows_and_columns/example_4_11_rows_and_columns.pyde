size(480, 120)
background(0)
noStroke()
for y in range(0, height+45, 40):
    fill(255, 140)
    ellipse(0, y, 40, 40)
for x in range(0, width+45, 40):
    fill(255, 140)
    ellipse(x, 0, 40, 40)
    
    saveFrame("frames/SaveExample-####.png")
