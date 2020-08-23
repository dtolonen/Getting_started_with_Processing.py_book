add_library('pdf')

bot = None

def setup():
    global bot
    size(600, 800, PDF, "Ex-13-5.pdf") 
    bot = loadShape("robot1.svg")
    
def draw():
    background(255)
    for i in range(100):
        rx = random(-bot.width, width) 
        ry = random(-bot.height, height) 
        shape(bot, rx, ry)
    exit()
    
    
