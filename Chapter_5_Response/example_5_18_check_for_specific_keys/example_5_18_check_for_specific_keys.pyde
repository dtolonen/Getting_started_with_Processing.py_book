def setup():
      size(120, 120)
def draw():
      background(204)
      if keyPressed:
        if key == 'h'or key == 'H': 
            line(30, 60, 90, 60)
        if key == 'n'or key == 'N': 
            line(30, 20, 90, 100)
      line(30, 20, 30, 100)
      line(90, 20, 90, 100)
      
      saveFrame("frames/SaveExample-####.png")
