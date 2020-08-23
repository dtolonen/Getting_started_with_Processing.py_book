size(480, 120) 
y=100
d=130
ellipse(75, y, d, d) # Left
ellipse(175, y, d, d) # Middle
ellipse(275, y, d, d) # Right

saveFrame("frames/SaveExample-####.png")
