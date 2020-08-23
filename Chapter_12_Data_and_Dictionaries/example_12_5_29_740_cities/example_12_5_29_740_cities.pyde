import csv

citiesData = None

def setXY(lat, lng):
    x = map(lng, -180, 180, 0, width) 
    y = map(lat, 90, -90, 0, height) 
    point(x, y)

def setup():
    global citiesData
    size(240, 120)
    citiesFileHandle = open("cities.csv")
    citiesData = list(csv.DictReader(citiesFileHandle)) 
    strokeWeight(0.1)
    stroke(255)

def draw():
    background(0, 26, 51)
    xoffset = map(mouseX, 0, width, -width*3, -width) 
    translate(xoffset, -300)
    scale(10)
    for row in citiesData:
        latitude = float(row["lat"]) 
        longitude = float(row["lng"]) 
        setXY(latitude, longitude)
        
        saveFrame("frames/SaveExample-####.png")
