size(480, 120)
x=25
h=20
y=25
rect(x, y, 300, h) # Top
x=x+100
rect(x, y + h, 300, h)  # Middle
x=x-250
rect(x, y + h*2, 300, h)  # Bottom

saveFrame("frames/SaveExample-####.png")
