"""
Tittel: Repetisjon og introduksjon av temaer
"""

"""
Del 1: Repetisjon
"""

# Sist gang gikk vi gjennom lister og if-setninger. Lister husker vi er variabler som vi kan legge flere ting i,
# for eksempel 10 tall. Det er veldig kjekt å bruke fordi å bruke 10 ulike variabler er kjedelig.
# En liste ser slik ut:
farger = ["Grønn", "Rød", "Hvit"]

# og vi kan printe ut hele listen, eller enkelte ting i listen.
print(farger)
print(farger[0])

# Hvis vi prøver å printe en posisjon som er lenger enn listen, så får vi en feil.
# print(farger[3] Dette er feil!

# If-setninger bruker vi når vi må gjøre et valg: Basert på noe vi sjekker så kan vi enten gjøre én ting
# eller en annen. Hvis vi skal sjekke om et tall er større enn 0 og gjøre to forskjellige ting, så kan vi gjøre sånn:
# Når vi skriver if-setninger så bruker vi kolon på slutten av setningen og da må vi hoppe litt inn på linjen.
tall = 5
if tall > 0:
    print("Tallet er støre enn 0")
else:
    print("Tallet er 0 eller mindre.")

# Vi kan bruke krokodilletegn, men også to likhetstegn ==.
annetTall = 10
if annetTall == 10:
    print("Tallet er 10")

# Her oppe ser vi at vi har ikke tatt med 'else', og det går helt fint. Men vi må ha med 'if'.
# I dag skal vi gå gjennom noe dere har sett før, men som vi skal jobbe litt mer med og som vi får masse bruk for
# senere i dag. Det er funksjoner. Senere i dag skal vi også jobbe masse med Turtle, og faktisk lage et veldig
# enkelt spill!

"""
Del 2: Funksjoner
"""

import random

# I tillegg til variabler og løkker, og masse masse annet, så har vi noe som heter funksjoner.
# Vi har allerede sett på spesielt én funksjon som vi bruker hele tiden. Det er funksjonen "print"
print("Dette er en funksjon!")

# Python har mange innebygde funksjoner fra før, for eksempel "random"-funksjonen.
# Dette er en funksjon som lager et tilfeldig tall mellom 1 og 10.
random.randint(1, 10)


# Vi kan også skrive våre egne funksjoner, og de kan gjøre akkurat hva vi vil.
# For å skrive en funksjon må vi huske på to ting.
# 1. Vi må følge 'malen' for en funksjon: 'def funksjonsnavn():'
# 2. Vi må huske å ha et 'innrykk' der vi skriver hva funksjonen skal gjøre.
def siHei():
    print("Hei!")


# For å 'kjøre/bruke' funksjonen må vi skrive følgende:
siHei()


# Funksjoner brukes veldig ofte når det er ting man skal gjøre mange ganger,
# men som er kjedelig å skrive om igjen og om igjen. Et eksempel på dette er hvis du skal printe
# tallene 1, 2, 3, 4 og 5 etter hverandre.
def enTilFem():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)


# Her trenger jeg kun å skrive 6 linjer én gang, men hver gang jeg vil printe alle tallene
# trenger jeg kun å kjøre funksjonen med én linje:
enTilFem()


# En funksjon kan også 'ta inn' noe som kalles et 'parameter'. Hver gang man skal
# kjøre funksjonen kan man da "velge" hva som skal skje, - etter visse regler.
# Denne funksjonen sier at vi skal 'ta inn' et tall, vi vet ikke hva det er, men samme det, vi printer det ut uansett.
# Tidligere har vi brukt funksjonen print() mange ganger. Og alt man skriver inni () er også parametre.
def printMittTall(talletMitt):
    print(talletMitt)


printMittTall(5)
printMittTall(21)


# Funksjoner kan brukes med hva som helst, for eksempel turtle
# Man kan for eksempel lage en funksjon som heter firkant()
def firkant():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)


"""
Del 3: Turtle + gjennomgåtte konsepter
"""

# I filen 'turtle_spill.py' så ligger det et spill der man kan styre turtle i et lite rom.
# Der bruker vi mange ting vi har lært frem til nå.
