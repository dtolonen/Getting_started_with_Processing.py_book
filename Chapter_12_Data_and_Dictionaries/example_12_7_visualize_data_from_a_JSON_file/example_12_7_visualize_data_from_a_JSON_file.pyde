import json

films = []

def setup():
    global films
    size(480, 120)
    filmFileHandle = open("films.json") 
    films = json.load(filmFileHandle)


def draw():
    background(0)
    for i in range(len(films)):
        film = films[i]
        ratingGray = map(film["rating"], 6.5, 8.1, 102, 255) 
        pushMatrix()
        translate(i*32 + 32, 105)
        rotate(-QUARTER_PI)
        fill(ratingGray)
        text(film["title"], 0, 0)
        popMatrix()
        
        saveFrame("frames/SaveExample-####.png")
