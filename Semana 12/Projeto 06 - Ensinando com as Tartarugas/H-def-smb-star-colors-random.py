from turtle import *
from random import *
def main():
    def moveToRandomLocation():
        penup()
        setpos( randint(-400, 400) , randint(-400, 400))
        pendown()
        
    def drawStar(starSize, starColor):
        
        color(starColor)
        pendown()
        begin_fill()
        for side in range(5):
            left(144)
            forward(starSize)
        end_fill()
        penup()
        
    bgcolor('MidnightBlue')
    
    for star in range(30):
        moveToRandomLocation()
        drawStar( randint(5, 25), "White")
    
    hideturtle()
    done()

if __name__ == '__main__':
        main()