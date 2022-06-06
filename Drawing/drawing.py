from turtle import *

color('red')
bgcolor('black')
speed(2)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b*2)
    b = b + 1
