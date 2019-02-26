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


# Oppgave 1 - middels
#
# Lag en funksjon som heter "siNoe" og som printer teksten "Hei, verden!"
def si_noe():
    print("Hei, verden!")


# Oppgave 2 - vanskelig
#
# Lag først en funksjon som printer ut teksten "Hei, verden!". Lag deretter en løkke som går fra 0 til 10.
# Kall funksjonen i løkken slik at "Hei, verden!" printes 10 ganger.
def min_funksjon():
    print("Hei, verden!")


for i in range(10):
    min_funksjon()

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
