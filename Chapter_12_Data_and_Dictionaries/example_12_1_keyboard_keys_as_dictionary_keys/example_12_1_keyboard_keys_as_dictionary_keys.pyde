sizes = {
  'a': 40, 
  'b': 80,
  'c': 120,
  'd': 160 
}


def setup():
  size(200, 200)
  rectMode(CENTER)
def draw():
  background(0)
  fill(255)
  if keyPressed:
    if key in sizes:
      rect(100, 100, sizes[key], sizes[key]) 
      
      saveFrame("frames/SaveExample-####.png")
