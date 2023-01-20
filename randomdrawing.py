import turtle 
import random

turtle.colormode(255)

def randomColor():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    randomColor = (r,g,b)
    return randomColor


directions = [0, 90, 180, 270]
turtle.pensize(4)
turtle.speed("fast")

for _ in range(200):
    turtle.pencolor(randomColor()) 
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

turtle.penup()
turtle.home()
screen = Screen()

screen.exitonclick()