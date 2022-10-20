import random
import turtle as t

hack = t.Screen()
hack.bgcolor("black")
t.pencolor("green")
t.hideturtle()
t.penup()


for i in range(1000):
    x = random.randint(0,1)
    t.write(x, move = True, align = "center", font = ("arial", 16, "normal"))

t.done()