import json

def setup():
    filmFileHandle = open("film.json") 
    film = json.load(filmFileHandle) 
    title = film["title"]
    director = film["director"]
    year = film["year"]
    rating = film["rating"]
    print "Title: ", title
    print "Director: ", director 
    print "Year: ", year
    print "Rating: ", rating
    
    saveFrame("frames/SaveExample-####.png")
