from turtle import *

# Først må vi "lage" skjermen og sette bakgrunnsfargen.
skjerm = Screen()
skjerm.bgcolor("orange")

# Så skal vi lage en turtle som senere skal tegne veggene rundt.
blyant = Turtle()
blyant.pensize(3)


# Denne funksjonen tegner de fire veggene og så gjemmer "blyanten".
# Hvert hjørne ligger på (-100, -100), (100, -100), (100, 100) og (-100, 100)
def tegnKant():
    blyant.penup()
    blyant.setposition(-100, -100)
    blyant.pendown()

    for side in range(4):
        blyant.forward(200)

        if side == 3:
            break

        blyant.left(90)

    blyant.hideturtle()


# Her tegner vi faktisk kanten. I stad laget vi bare funksjonen som gjør det.
tegnKant()

# Her lager vi spilleren som vi skal styre på skjermen.
spiller = Turtle()
spiller.color("red")
spiller.shape("turtle")

# Dette er farten som spilleren begynner med. Denne kan vi øke og redusere ved å bruke
# PIL OPP- og PIL NED-tastene.
fart = 1


# Denne funksjonen får spileren til å svinge til venstre.
def snuTilVenstre():
    spiller.left(30)


# Denne funksjonen får spileren til å svinge til høyre.
def snuTilHoyre():
    spiller.right(30)


# Denne funksjonen øker farten til spilleren med 1.
def okFart():
    global fart
    fart += 1


# Denne funksjonen sender farten til spilleren med 1.
# Hvis farten blir negativ så rygger spilleren.
def senkFart():
    global fart
    fart -= 1


# Dette gjør at vi kan bruke piltastene våres til å styre spilleren vår.
skjerm.listen()
skjerm.onkey(snuTilVenstre, "left")
skjerm.onkey(snuTilHoyre, "right")
skjerm.onkey(okFart, "up")
skjerm.onkey(senkFart, "down")

# En while-løkke er 'nesten' som en for-løkke. Vi må sjekke om noe er sant før vi kan gå inn
# i løkken. Når vi er ferdige med løkken så går vi opp igjen og sjekker om det igjen er sant.
# Hvis det IKKE er sant, så hopper vi videre i programmet.
while True:
    # Vi må finne posisjonen til spilleren
    x = spiller.xcor()
    y = spiller.ycor()

    # Vi sjekker om spilleren er nesten ved en av de fire veggene.
    # Hvis dette er sant, snu spilleren helt rundt.
    # Først sjekker vi om spilleren er ner den høyre eller venstre veggen
    # Så sjekker vi om spilleren er nær den øverste eller nederste veggen
    if x > 95 or x < -95:
        spiller.right(180)
    elif y > 95 or y < -95:
        spiller.right(180)

    # Flytt spilleren litt fremover og gå opp til toppen av 'while'-løkken.
    spiller.forward(fart)
