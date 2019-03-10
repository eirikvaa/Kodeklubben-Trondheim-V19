import turtle

wn = turtle.Screen()
blyant = turtle.Turtle()
wn.bgcolor("orange")


def tegnKant():
    blyant.penup()
    blyant.setposition(-100, -100)
    blyant.pendown()
    blyant.pensize(3)
    for side in range(4):
        blyant.forward(200)

        if side == 3:
            break

        blyant.left(90)

    blyant.hideturtle()


tegnKant()

spiller = turtle.Turtle()


def tegnSpiller():
    spiller.color("red")
    spiller.shape("diamond")


fart = 1


def snuTilVenstre():
    spiller.left(30)


def snuTilHoyre():
    spiller.right(30)


def okFart():
    global fart
    fart += 1


def senkFart():
    global fart

    if fart == 0:
        return

    fart -= 1


wn.listen()
wn.onkey(snuTilVenstre, "left")
wn.onkey(snuTilHoyre, "right")
wn.onkey(okFart, "up")
wn.onkey(senkFart, "down")

while True:
    x = spiller.xcor()
    y = spiller.ycor()

    if abs(x) > 95:
        spiller.right(180)
    elif abs(y) > 95:
        spiller.right(180)

    spiller.forward(fart)
