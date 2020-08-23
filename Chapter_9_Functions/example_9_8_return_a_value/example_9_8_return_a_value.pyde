def setup():
    yourWeight = 132.0
    marsWeight = calculateMars(yourWeight) 
    print marsWeight

def calculateMars(w): 
    newWeight = w * 0.38 
    return newWeight

    saveFrame("frames/SaveExample-####.png")
