import turtle
import random

farger = ["pink", "green", "blue", "yellow", "black", "red"]

ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.pencolor("green")
ninja.speed(10)


# Funksjon 1
def forsteStrek():
    ninja.forward(100)
    ninja.right(-30)  # ENDRE TALL HER


# Funksjon 2
def andreStrek():
    ninja.forward(20)
    ninja.left(-75)  # ENDRE TALL HER


# Funksjon 3
def tredjeStrek():
    ninja.forward(50)
    ninja.right(90)  # ENDRE TALL HER


# Funksjon 4
def tilbakestill():
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)


for i in range(180):
    tilfeldig_tall = random.randint(0, len(farger) - 1)
    tilfeldig_farge = farger[tilfeldig_tall]
    ninja.pencolor(tilfeldig_farge)
    forsteStrek()
    andreStrek()
    tredjeStrek()
    tilbakestill()
