size(480, 120) 
y=60
d=80
ellipse(75, y, d, d) # Left
ellipse(175, y, d, d) # Middle
ellipse(275, y, d, d) # Right

saveFrame("frames/SaveExample-####.png")
