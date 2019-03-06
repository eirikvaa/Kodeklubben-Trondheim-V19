import random

"""
Tittel: Repetisjon og introduksjon av temaer
"""

"""
Del 1: Repetisjon
"""

# Sist gang jobbet vi med to ting: variabler og løkker. Vi begynner med en liten repetisjon av begge to før vi
# går litt videre til to ting: lister og noe dere ikke har sett før som heter if-setninger.
#
# Variabler bruker vi som bokser for å lagre forskjellige ting. Dette kan være tall, tekst eller til og med
# lister av ting. Vi kan gjøre mye forskjellig med variabler; plusse de sammen og printe de, som noen eksempler.

variabel = 10
print(variabel)

variabel2 = 20
summen = variabel + variabel2
print(summen)

# Løkker bruker vi når vi ikke har lyst til å gjøre det samme mange ganger. Hvis vi skal printe ut "Jeg heter Eirik"
# ti ganger så er det kjedelig å skrive "print("Jeg heter Eirik")" 10 ganger, da er det enklere å lage en for-løkke
# som går fra 0 til 9 som gjør samme jobben, bare med mye mindre arbeid!

"""
Del 2: Lister
"""

# Vi har sett på lister før. Det er variabler som kan lagre flere enn én ting. De ser litt annerledes ut fordi vi
# bruker firkant-paranteser '[' og ']' for å lage en liste.
# Nedenfor lager vi en liste som heter 'minListe' og som består av tre tall, 1, 2 og 3.
minListe = [1, 2, 3]

# Denne gangen skal vi


"""
Del 3: if-setninger
"""

# Når vi koder kan det være veldig nytt å sjekke om for eksempel en variabel er et spesifikt tall,
# eller om et navn er lik "Andreas". Dette kan gjøres med såkalte 'if-setninger'. 

alder = 10
if alder == 10:
    print("Du er 10 år gammel")

navn = "Andreas"
if navn == "Andreas":
    print("Hei Andreas!")

# Sjekke om du er gammel nok
alder = 13
if alder > 12:
    print("Du er gammel nok")

# Vi kan gjøre dette litt mer komplisert
alder = 11
if alder > 12:
    print("Du er gammel nok")
else:
    print("Du er ikke gammel nok")

"""
Del 4: Funksjoner
"""

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
def printMittTall(talletMitt):
    print(talletMitt)


printMittTall(5)
printMittTall(21)
