def setup():
    print "Ready to roll!" 
    d1 = 1 + int(random(20)) 
    print "Rolling...", d1 
    d2 = 1 + int(random(20)) 
    print "Rolling...", d2 
    d3 = 1 + int(random(6)) 
    print "Rolling...", d3 
    print "Finished."
    
    saveFrame("frames/SaveExample-####.png")
