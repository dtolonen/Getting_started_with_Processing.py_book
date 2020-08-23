angle = 0.0

def draw():
    global angle
    sinval = sin(angle)
    print sinval
    gray = map(sinval, -1, 1, 0, 255) 
    background(gray)
    angle += 0.1
    
