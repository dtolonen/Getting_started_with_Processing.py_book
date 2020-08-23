size(480, 120)
background(0)
fill(255)
stroke(102)
for y in range(20, height-15, 10):
    for x in range(20, width-15, 10): 
        ellipse(x, y, 4, 4)
        # Draw a line to the center of the display 
        line(x, y, 240, 60)
        
        saveFrame("frames/SaveExample-####.png")
