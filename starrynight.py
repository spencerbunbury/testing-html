import turtle
import random
pen = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor("black")
pen.width(20)

for i in range(20):
    # setting r,g,b colors
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pen.pencolor(r,g,b)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    pen.up()
    pen.goto(x,y)
    pen.down()


    i = 4
    while i >0:
        i = i-1
        pen.forward(20)
        pen.backward(20)
        pen.left(90)


    

