from turtle import *

"""
Tema: Funksjoner
"""


# Oppgave 1
#
# Lag en funksjon som heter tegnSirkel som tegner en sirkel med radius 10.
def tegnSirkel():
    circle(10)


# Oppgave 2
#
# Lag en funksjon som tar inn radius som parameter.
def tegnSirkel2(radius):
    circle(radius)


# Oppgave 3
#
# Lag en funksjon tegnSirkler som tar inn antall sirkler som skal tegnes som et 
# parameter og radius for hver sirkel. 
# Lag en løkke inne i funksjonen som går fra 0 til antall sirkler
# (parameteret) som du skrev i stad. Når en sirkel er tegnet så flytt pennen opp
# (penup) og flytt den litt bort fra den andre sirkelen så du kan se begge.
def tegnSirkler(antall, radius):
    for i in range(antall):
        circle(radius)
        penup()
        forward(10)
        pendown()


# Oppgave 4
#
# Lag en funksjon tegnFormer.
# Lag en løkke inne i funksjon som går fra 0 til 10.
# Inne i løkken, sjekk om variabelen i kan deles på 2.
# Hint: I programmering sjekker vi om et tall kan deles på 2 slik: i % 2 == 0.
# Hvis dette er sant, tegn en sirkel som har radius 10 og sett fargen på
# blyanten til å være blå ('blue').
# Hvis dette ikke er sant, tegn en sirkel som har radius 20 og sett fargen
# på blyanten til å være grønn ('green'). Da bruker man 'pencolor'-funksjonen.
# Husk å flytte turtle litt slik at du ser alle sirklene.
def tegnFormer():
    for i in range(10):
        if i % 2 == 0:
            pencolor('blue')
            circle(10)
        else:
            pencolor('green')
            circle(20)
        penup()
        forward(20)
        pendown()


tegnFormer()
