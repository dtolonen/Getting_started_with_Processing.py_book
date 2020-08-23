# Using the framerate() function to change the framerate at which the program runs. 
# Uncomment different versions of framerate() to see the difference. Interestingly, at 
# 12 fps, it starts higher and eases down to 12 fps.

# Note from the book: Processing tries to run the code at 60 frames each second, 
# but if it takes longer than 1/60th of a sec- ond to run the draw() method, 
# then the frame rate will decrease. The frameRate() function specifies only 
# the maximum frame rate, and the actual frame rate for any program depends 
# on the computer that is running the code.

def setup():
   #frameRate(30) # Thirty frames each second #
    frameRate(12) # Twelve frames each second #
   # frameRate(2) # Two frames each second #
   # frameRate(0.5) # One frame every two seconds

def draw(): 
    print frameRate
