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
