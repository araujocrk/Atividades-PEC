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
    
    def drawSquare(squareSize, squareColor):
        color(squareColor)
        pendown()
        begin_fill()
        for side in range(4):
            left(90)
            forward(squareSize)
        end_fill()
        penup()
        
    def drawSquares(numberOfSquares):
        moveToRandomLocation()
        for square in range(numberOfSquares):
            penup()
            left( randint(-100, 180))
            forward(randint(5, 20))
            pendown()
            drawSquare(5, 'Red')
    
    def drawConstellation(numberOfStars):
        moveToRandomLocation()
        for star in range(numberOfStars -1):
            drawStar(randint(7, 15), 'White')
            pendown()
            left(randint(-90, 90))
            forward(randint(30, 70))
        drawStar(randint(7, 15), 'White')
    speed(11)

    def drawDashedLine(lineSize):
        moveToRandomLocation()
        color('Green')
        for line in range(lineSize):
            pendown()
            forward(5)
            penup()
            forward(5)
    bgcolor('MidnightBlue')
    
    for star in range(30):
        moveToRandomLocation()
        drawStar(randint(5, 25), 'White')
        
    for squares in range(3):
        drawSquares(randint(5, 20))
    
    for constellation in range(2):
        drawConstellation(randint(4, 7))
        
    for lines in range(5):
        drawDashedLine(randint(10, 20))
        
    hideturtle()
    done()

if __name__ == '__main__':
        main()