from turtle import *

shape('turtle')
color('Purple')
pensize(6) 
speed(2)
for count in range(8):
    left(45)
    forward(35)
    right(90)
    forward(35)

penup()
forward(23)
right(90)
forward(2)
left(90)
pendown()

speed(11)
for count in range(180):
    forward(2)
    right(2)
done()