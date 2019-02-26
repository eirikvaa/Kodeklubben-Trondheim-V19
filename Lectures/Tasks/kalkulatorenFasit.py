# Vanskelig oppgave.
# I denne oppgaven skal vi lage en kalkulator som kan pluss, minus gange og dele to tall.

# 1. Start med å lage en variabel som tar inn to tall fra tastaturet. Kall dem tall1 og tall2. 
# Test at det fungerer ved å printe ut tallene på skjermen.
print("A - Pluss")
print("B - Minus")
print("C - Gange")
print("D - Dele")
regneoperasjon = input("Hva vil du gjøre?")
tall1 = int(input("Hva er tall nummer 1?"))
tall2 = int(input("Hva er tall nummer 2?"))



# 2. Lag en funksjon som tar inn to tall, plusser dem sammen og printer ut svaret.
def pluss(a, b):
  print(a + b)

# 3. Lag en funksjon som tar inn to tall, trekker dem fra hverandre og printer ut svaret.
def minus(a, b):
  print(a - b)

# 4. Lag en funksjon som tar inn to tall, ganger dem sammen og printer ut svaret.
def gange(a, b):
  print(a * b)

# 5. Lag en funksjon som tar inn to tall, deler dem på hverandre og printer ut svaret.
def dele(a, b):
  print(a / b)

# Test her at alle funksjonene dine fungerer.
# Om tallene dine var 1 og 2 skal følgende printes ut:
# 3
# -1
# 2
# 0.5


# Ekstraoppgave:
# Hva med å lage en kalkulator hvor man bestemmer hvilken matematisk funksjon man vil at skal skje med de to tallene?
# At man f.eks skriver A for å plusse, B for minus, C for gange og D for dele.

# Endre programmet slik at vi har en tredje variabel kalt "regneoperasjon". Brukeren skal her skrive enten A, B, C eller D.
# Sjekk (if-setning) så hva brukeren har skrevet inn, og kall funksjonen som passer med de to tallene.

if regneoperasjon == "A":
  pluss(tall1, tall2)

if regneoperasjon == "B":
  minus(tall1, tall2)

if regneoperasjon == "C":
  gange(tall1, tall2)

if regneoperasjon == "D":
  dele(tall1, tall2)

