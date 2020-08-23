size(480, 120)
strokeWeight(2)
for i in range(20, 400, 20):
    line(i, 0, i + i/2, 80)
    
    saveFrame("frames/SaveExample-####.png")
