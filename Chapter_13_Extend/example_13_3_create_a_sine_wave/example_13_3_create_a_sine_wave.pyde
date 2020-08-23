add_library('sound') 

sine = None
freq = 400.0

def setup():
    global sine
    size(440, 440)
    # Create and start the sine oscillator 
    sine = SinOsc(this)
    sine.play()

def draw():
    background(176, 204, 176)
    # Map the mouseX value from 20Hz to 440Hz for frequency 
    hertz = map(mouseX, 0, width, 20.0, 440.0) 
    sine.freq(hertz)
    # Draw a wave to visualize the frequency of the sound 
    stroke(26, 76, 102)
    for x in range(width):
        angle = map(x, 0, width, 0, TWO_PI * hertz) 
        sinValue = sin(angle) * 120
        line(x, 0, x, height/2 + sinValue)
        
        saveFrame("frames/SaveExample-####.png")
