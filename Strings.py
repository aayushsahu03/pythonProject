import time
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
turtle1 = turtle.Turtle('square')
turtle1.color("white")
turtle2 = turtle.Turtle('square')
turtle2.color("white")
turtle2.goto(turtle1.position()[0]-20,turtle1.position()[1])
time.sleep(2)
print(turtle1.position())