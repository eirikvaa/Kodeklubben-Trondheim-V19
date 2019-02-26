from turtle import *
title("Turtle Keys")
showturtle()

def k1():
    forward(45)

def k2():
    left(45)

def k3():
    right(45)

def k4():
    back(45)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()