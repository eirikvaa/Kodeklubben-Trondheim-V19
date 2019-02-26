"""
Tema: Variabler
"""

# Oppgave 1 - enkel
#
# Lag en variabel som heter "minVariabel" og sett den til å være et tall du kan velge selv.
# Print deretter ut verdien.
minVariabel = 3
print(minVariabel)

# Oppgave 2 - enkel
#
# Lag to variabler der den første heter "variabel1" og den andre "variabel2". Sett den første
# til å ha tallet 10 og den andre til å ha tallet 20. Print ut den ene variabelen plusset med
# den andre.
variabel1 = 10
variabel2 = 20
print(variabel1 + variabel2)

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


"""
Tema: Løkker
"""

# Oppgave 1 - enkel
#
# Lag en løkke som skriver ut 'Hei Verden!' tre ganger
#
for i in range(3):
    print("Hei Verden!")

# Oppgave 2 - middels
#
# Lag et program bestående av to løkker som først skriver ut 'Kaffe' tre ganger
# og 'Te' 4 ganger
#
for i in range(3):
    print("Kaffe")

for i in range(3):
    print("Te")

# Oppgave 3 - vanskelig
#
# Lag en løkke som skriver ut tallene fra 0-9
#
for i in range(10):
    print(i)


