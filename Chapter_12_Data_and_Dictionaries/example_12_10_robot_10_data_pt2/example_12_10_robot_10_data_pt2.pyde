import csv

def setup():
    size(720, 480)
    background(0, 153, 204)
    bot1 = loadShape("robot1.svg")
    bot2 = loadShape("robot2.svg")
    bot3 = loadShape("robot3.svg")
    shapeMode(CENTER)
    robotsFileHandle = open("botArmy.tsv") 
    robots = csv.DictReader(robotsFileHandle, delimiter="\t") 
    for row in robots:
        bot = int(row["type"]) 
        x = int(row["x"])
        y = int(row["y"]) 
        sc = 0.3
        if bot == 1:
            shape(bot1, x, y, bot1.width*sc, bot1.height*sc)
        elif bot == 2:
            shape(bot2, x, y, bot2.width*sc, bot2.height*sc)
        else:
            shape(bot3, x, y, bot3.width*sc, bot3.height*sc)
            
            saveFrame("frames/SaveExample-####.png")
