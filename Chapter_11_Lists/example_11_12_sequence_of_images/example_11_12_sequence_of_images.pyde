numFrames = 12 # The number of frames 
images = [] # Make the list 
currentFrame = 0

def setup():
    size(240, 120)
    for i in range(numFrames):
        imageName = "frame-" + nf(i, 4) + ".png"
        images.append(loadImage(imageName)) 
    frameRate(24)

def draw():
    global currentFrame 
    image(images[currentFrame], 0, 0) 
    currentFrame += 1 # Next frame 
    if currentFrame >= len(images):
        currentFrame = 0 # Return to first frame
        
        saveFrame("frames/SaveExample-####.png")
