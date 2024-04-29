from turtle import *

lados = int(input('Digite a quantidade de lados: ').strip())
angulo = 360 / lados

shape('turtle')
color('Purple')
speed(4)
pensize(6)

for count in range(lados):
    forward(100)
    right(angulo)
    
done()