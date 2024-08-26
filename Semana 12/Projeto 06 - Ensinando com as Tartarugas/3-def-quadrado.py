from turtle import *
def main():
    def drawSquare():
        
        pendown()
        begin_fill()
        for side in range(4):
            left(90)
            forward(50)
        end_fill()
        penup()
        
    color('WhiteSmoke')
    bgcolor('MidnightBlue')
    
    drawSquare()
    forward(100)
    drawSquare()
    left(110)
    forward(150)
    right(20)
    drawSquare()
    
    hideturtle()
    done()

if __name__ == '__main__':
        main()