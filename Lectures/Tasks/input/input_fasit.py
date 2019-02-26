# I dette programmet skal vi hente tekst skrevet på tastaturet inn i programmet.

mitt_navn = input("Hva heter du? ")
print("Hei " + mitt_navn + "!")

min_alder = input("Hvor gammel er du? ")
print("Jeg er " + min_alder + " år!")

if int(min_alder) > 24:
    print("Oj, du er gammel!")
