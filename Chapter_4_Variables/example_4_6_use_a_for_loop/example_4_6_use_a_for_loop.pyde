size(480, 120)
strokeWeight(8)
for i in range(20, 400, 60):
    line(i, 40, i + 60, 80)
    
    saveFrame("frames/SaveExample-####.png")
