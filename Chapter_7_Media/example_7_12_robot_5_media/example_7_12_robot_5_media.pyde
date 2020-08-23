bot1 = None 
bot2 = None 
bot3 = None 

easing = 0.05 
offset = 0

def setup():
    global bot1, bot2, bot3, landscape 
    size(720, 480)
    bot1 = loadShape("robot1.svg") 
    bot2 = loadShape("robot2.svg") 
    bot3 = loadShape("robot3.svg") 


def draw():
    global offset
    
    # Set the left/right offset and apply easing to make # the transition smooth
    targetOffset = map(mouseY, 0, height, -40, 40) 
    offset += (targetOffset - offset) * easing
  
    # Draw the left robot
    shape(bot1, 85 + offset, 65)
    
    # Draw the right robot smaller and give it a smaller offset
    smallerOffset = offset * 0.7
    shape(bot2, 510 + smallerOffset, 140, 78, 248)
  
    # Draw the smallest robot, give it a smaller offset
    smallerOffset *= -0.5;
    shape(bot3, 410 + smallerOffset, 225, 39, 124)
    
    saveFrame("frames/SaveExample-####.png")
