import json

def getTemp(fileName):
    weather = json.load(open(fileName)) 
    return weather["list"][0]["main"]["temp"]
    
def setup():
    temp = getTemp("cincinnati.json") 
    print temp
    
    saveFrame("frames/SaveExample-####.png")
