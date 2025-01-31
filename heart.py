import turtle
import math

m = turtle.Turtle()
m.speed(0)
m.color("red")
turtle.bgcolor("black")

def mmm(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2*math.cos(3*n) - math.cos(4*n)
    return x, y

m.penup()
for i in range(15):
    m.goto(0, 0)
    m.pendown()
    for n in range(0, 100, 2):
        x, y = mmm(n/10)
        m.goto(x*i, y*i)
    m.penup()

m.hideturtle()
turtle.done()
