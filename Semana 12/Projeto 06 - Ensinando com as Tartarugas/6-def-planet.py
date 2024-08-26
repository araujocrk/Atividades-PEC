from turtle import *
def main():
    def drawPlanet(planetSize, planetColor):
        
        speed(11)
        color(planetColor)
        pendown()
        begin_fill()
        for side in range(360):
            forward(2 * 3.14 * planetSize / 360)
            right(1)
        end_fill()
        penup()
        
    bgcolor('MidnightBlue')
    
    drawPlanet(30, 'Red')
    forward(150)
    drawPlanet(50, 'White')
    left(130)
    forward(150)
    right(40)
    drawPlanet(70, 'Green')
    
    hideturtle()
    done()

if __name__ == '__main__':
        main()