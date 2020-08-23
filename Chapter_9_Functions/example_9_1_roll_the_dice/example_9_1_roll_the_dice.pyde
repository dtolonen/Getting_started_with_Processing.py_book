def setup():
    print "Ready to roll!" 
    rollDice(20) 
    rollDice(20) 
    rollDice(6)
    print "Finished."

def rollDice(numSides):
    d = 1 + int(random(numSides)) 
    print "Rolling...", d
    
    saveFrame("frames/SaveExample-####.png")
