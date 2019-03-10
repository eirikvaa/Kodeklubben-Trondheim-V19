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

"""
Del 3: Turtle + gjennomgåtte konsepter
"""

# I filen 'turtle_spill.py' så ligger det et spill der man kan styre turtle i et lite rom.
# Der bruker vi mange ting vi har lært frem til nå.
