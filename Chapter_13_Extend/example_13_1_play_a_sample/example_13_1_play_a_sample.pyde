add_library('sound')



blip = None 
radius = 120 
x=0
speed = 1.0 
direction = 1

def setup():
    global blip, x
    size(440, 440) 
    ellipseMode(RADIUS)
    blip = SoundFile(this, "blip.wav") 
    x = width/2 # Start in the center


def draw():
    global x, direction
    background(0)
    x += speed * direction
    if x > width-radius or x < radius:
        direction = -direction # Flip direction
        blip.play()
    if direction == 1:
        arc(x, 220, radius, radius, 0.52, 5.76) # Face right 
    else:
        arc(x, 220, radius, radius, 3.67, 8.9) # Face left
        
        saveFrame("frames/SaveExample-####.png")
