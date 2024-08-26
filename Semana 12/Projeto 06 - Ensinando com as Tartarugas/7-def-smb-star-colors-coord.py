from turtle import *
def main():
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
    
    penup()
    setpos(200, 200)
    pendown()
    
    drawStar(50, 'White')
    
    hideturtle()
    done()

if __name__ == '__main__':
        main()