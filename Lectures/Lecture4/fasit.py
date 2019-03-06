"""
Tema: Lister
"""

# Oppgave 1 - enkel
#
# Lag en liste som heter 'minListe' og som inneholder tre tall som du kan velge selv.
minListe = [1, 2, 3]

# Oppgave 2 - enkel
#
# Bruk listen du laget i den første oppgaven og print den ut.
print(minListe)

# Oppgave 3 - middels
#
# Lag en liste som heter 'former' og som inneholder tekstene 'trekant', 'firkant' og 'runding'.
# Lag deretter en ny variabel som heter 'rundingVariabel' og som henter ut 'runding' fra listen.
# Print ut 'rundingVariabel'.
# Hint 1: Når vi skal hente ut en ting fra listen så må vi bruke firkantparanteser
# Hint 2: Husk at når vi teller hvilken plass en ting i listen ligger på, må vi telle fra 0.
former = ["trekant", "firkant", "runding"]
rundingVariabel = former[2]
print(rundingVariabel)

# Oppgave 4 - middels
#
# Lag en liste som heter 'tall' og som inneholder tallene 10, 20 og 30.
# Lag tre variabler som heter 'tall0', 'tall1' og 'tall2' der 'tall0' er det første tallet i listen,
# 'tall1' er det andre tallet i listen og 'tall2' er det siste tallet i listen.
# Lag en ny variabel som heter 'summen' og som er summen av 'tall0', 'tall1' og 'tall2'.
# Print ut verdien til 'summen'.
# Hint: Du henter ut tallene på samme måte som du gjorde i oppgave 3.
tall = [10, 20, 30]
tall0 = tall[0]
tall1 = tall[1]
tall2 = tall[2]
summen = tall0 + tall1 + tall2
print(summen)

# Oppgave 5 - vanskelig
#
# Lag en liste som heter 'tall' og som inneholder tallene 2, 4, 6, 8, 10.
# Lag en løkke som går fra 0 til 5.
# Inne i løkken, bruk løkke-variabelen (variabelen som står etter "for") og hent ut
# elementet fra listen.
tall = [2, 4, 6, 8, 10]
for i in range(5):
    print(tall[i])

"""
Tema: if-setninger
"""

# Oppgave 1 - enkel
#
# Lag en variabel som heter 'tall' og at den skal lagre tallet 2.
# Lag en if-setninger som spør om 'tall'-variabelen er større enn 0.
# Hvis dette er sant, print ut teksten "Tallet er større enn 0".
tall = 2
if tall > 0:
    print("Tallet er større enn 0.")

# Oppgave 2 - middels
#
# Lag en variabel som heter 'antall_dyr_jeg_eier' som inneholder antall kjæledyr du eier.
# Lag en if-setning som spør om 'antall_dyr_jeg_eier' er større enn 5.
# Hvis dette er sant, print ut teksten "Wow, du eier mange kjæledyr!"
# Hvis dette ikke er sant, print ut teksten "Du eier færre enn 6 dyr."
antall_dyr_jeg_eier = 1
if antall_dyr_jeg_eier > 5:
    print("Wow, du eier mange dyr!")
else:
    print("Du eier færre enn 6 dyr!")

# Oppgave 3 - middels
#
# Lag en variabel som heter 'mittNavn' og som lagrer navnet ditt som en tekst,
# for eksempel "Eirik".
# Lag en if-setninger som sjekker om variabelen 'mittNavn' er lik teksten "Ola".
# Hvis dette er sant, print ut "Hei, Ola!" innenfor if.
# Hvis dette ikke er sant, print ut "Ops, feil person!" innenfor else.
mittNavn = "Eirik"
if mittNavn == "Ola":
    print("Hei, Ola!")
else:
    print("Ops, feil person!")

# Oppgave 4 - vanskelig
#
# Lag en variabel som heter 'tall1' og som lagrer verdien 10.
# Lag en annen variabel som heter 'tall2' og som lagrer verdien 30.
# Lag en tredje variabel som heter 'summen' og som plusser sammen 'tall1' og 'tall2'.
# Lag en if-setning som sjekker om 'summen' er større enn 50.
# Hvis dette er sant, print ut "Summen er 50"
# Hvis dette er ikke sant, print ut "Summen er ikke 50".
tall1 = 10
tall2 = 30
summen = tall1 + tall2
if summen == 50:
    print("Summen er 50")
else:
    print("Summen er ikke 50")

"""
Tema: Funksjoner
"""


# Oppgave 1 - Enkel
#
# Lag en funksjon som heter "siNoe" som printer teksten "Hei, verden!"
def siNoe():
    print("Hei, verden!")


# Oppgave 2 - Enkel
#
# Lag en funksjon som heter "visTegn" som printer ut et valgritt tegn, - for eksempel: *, +, -, !, .,
def visTegn():
    print("*")


# Oppgave 3 - Middels
#
# Lag en funksjon som heter "hilsen" som gjør følgende:
# 1. Lagrer navnet ditt i en variabel som heter "navn"
# 2. Printer ut "Hei, <navnet ditt>"
def hilsen():
    navn = "Magnus"
    print("Hei" + navn)


# Oppgave 4 - Middels
#
# Lag en funksjon som heter "regnUt" som gjør følgende:
# 1. Lagrer to tall i variabler. Kall de to variablene "tall1" og "tall1". Du bestemmer selv hvilke tall det skal være.
# 2. Print ut tall1 og tall2 plusset sammen.
def regnUt():
    tall1 = 15
    tall2 = 4
    print(tall1 + tall2)


# Oppgave 5 - vanskelig
#
# Lag først en funksjon som printer ut teksten "Hei, verden!". Lag deretter en løkke som går fra 0 til 10.
# Kall funksjonen i løkken slik at "Hei, verden!" printes 10 ganger.
def hallo():
    print("Hei, verden!")


for i in range(10):
    hallo()


# Oppgave 6 - vanskelig
#
# Lag en funksjon som heter "siHei" og som 'tar inn' et navn. Print ut "Hei, <navn>". Ligner dette på en annen oppgave?
def siHei(navn):
    print("Hei," + navn)
