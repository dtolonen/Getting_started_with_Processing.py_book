def setup():
    size(720, 480)
    # Create the new file
    output = open("botArmy.tsv", "w") 
    # Write a header line with the column titles 
    output.write("type\tx\ty\n")
    for y in range(0, height+1, 60):
        for x in range(0, width+1, 20):
            robotType = str(int(random(1, 4))) 
            output.write(robotType+"\t"+str(x)+"\t"+str(y)+"\n") 
            ellipse(x, y, 12, 12)
    output.close() # Finish the file
    
    saveFrame("frames/SaveExample-####.png")
