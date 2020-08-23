import json

def getTemp(fileName):
    weatherFileHandle = open(fileName)
    weather = json.load(weatherFileHandle)
    list_value = weather["list"] # get value for "list" key 
    item = list_value[0] # get first item from list_value
    main = item["main"] # item is a dictionary; get "main" value 
    temperature = main["temp"] # get value for "temp" key 
    return temperature
    
def setup():
    temp = getTemp("cincinnati.json") 
    print temp
    
    saveFrame("frames/SaveExample-####.png")
