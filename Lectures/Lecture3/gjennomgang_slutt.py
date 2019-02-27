import random
"""
Tittel: Repetisjon og introduksjon av temaer
"""

"""
Del 1: Repetisjon:
"""

# Vi snakket om mange ting sist kveld, både variabler, løkker og funksjoner.
# Vi laget også programmet som tegnet i Turtle.
# Jeg skal repetere variabler sånn at vi husker hva det var og hvordan vi kan bruke det. Deretter skal vi gjøre noen
# oppgaver med variabler før vi hopper videre til løkker og deretter funksjoner.

"""
Del 2: Variabler
"""

# Vi begynte med variabler, bokser som vi kan lagre ting i, for eksempel tall
min_variabel = 5

# Variabler har et navn ("min_variabel") og en verdi (5).
# Vi kan også lage variabler som lagrer tekst.
min_tekst = "Hei, jeg heter Eirik!"

# Hva kan vi gjøre med variabler? Vi kan printe.
print(min_variabel)

# Enkelt fortalt betyr dette at vi får datamaskinen til å snakke tilbake til oss.
# Når vi kjører programmet vårt nå vil vi se tallet 5.
# Vi lærte at vi kan lage flere variabler ...
variabel_2 = 10

# ... og at vi plusse de sammen.
print(min_variabel + variabel_2)

# Da vil vi se at det printes ut tallet 15. Datamaskinen så på de vi skrev, skjønte at det var to tall
# og plusset de sammen. Vi lærte også at en variabel kan være en liste, og den ser slik ut:
min_liste = [5, 10, 15]

# Dette er en liste som inneholder tre tall, 5, 10 og 15. En liste er som en variabel som kan inneholde
# flere enn én ting. Vi kan også printe ut tall på samme måte som en variabel.
print(min_liste)

# Da vil vi se [5, 10, 15] i vinduet nederst. For dere er det ingen grense for hvor mange ting vi kan ha i en liste.

"""
Del 3: Løkker
"""

# Løkker er veldig nyttig i programmering siden det lar oss maskinen selv gjøre ting om å om igjen, uten at vi selv 
# trenger å skrive det mange ganger. Vi skiller mellom forskjellige løkker i programmering, men i dag vil vi fokusere på såkalte 
# 'for-loops'

# Vi kan skrive en for-løkke slik
for i in range(10):
  # Noe vi ønsker at skal repeteres
  pass

# Det nye i kodesnutten over er ordet 'range'. I denne sammenhengen sier det rett og slett at vi skal gjøre noe et visst
# antall ganger. I dette tilfellet vil loopen kjøre 10 ganger, fordi vi har spesifisert 10 inni range (som et parameter)

# Hvis vi ønsker å skrive ut navnet vårt 5 ganger, kan dette både være tidkrevende og kjedelig. Hvis vi derimot bruker en loop
# til å gjøre jobben, ser koden både mer avansert ut og man slipper mye ekstra arbeid

for i in range(5):
  print("Andreas")

# Løkker viser seg også til å være nyttig når vi ønsker å printe ut elementer fra en liste. 
# Sett at vi har en liste med navn
navn = ["Andreas", "Eirik", "Magnus"]

# Vi kan godt printe ut navnene hver for seg slik
print(navn[0])
print(navn[1])
print(navn[2])

# men det er mer effektivt å bruke en for loop til dette

for i in navn:
  print(i)

# Hvis vi ønsker å skrive ut en hilsen før hvert navn, kan vi også gjøre dette

for i in navn:
  print("Hei " + i) 

# Vi kan altså bruke loops til mange forskjellige ting, for eksempel printe ut tallene fra 0 til 4
for i in range(4):
  print(i)

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

# Funksjoner brukes veldig ofte når det er ting man skal gjøre mange ganger, men som er kjedelig å skrive om igjen og om igjen.
# Et eksempel på dette er hvis du skal printe tallene 1, 2, 3, 4 og 5 etter hverandre.
def enTilFem():
  print(1)
  print(2)
  print(3)
  print(4)
  print(5)

# Her trenger jeg kun å skrive 6 linjer én gang, men hver gang jeg vil printe alle tallene trenger jeg kun å kjøre funksjonen med én linje:
enTilFem()

# En funksjon kan også 'ta inn' noe som kalles et 'parameter'. Hver gang man skal kjøre funksjonen kan man da "velge" hva som skal skje, - etter visse regler.
# Denne funksjonen sier at vi skal 'ta inn' et tall, vi vet ikke hva det er, men samme det, vi printer det ut uansett.
def printMittTall(talletMitt):
  print(talletMitt)

printMittTall(5)
printMittTall(21)