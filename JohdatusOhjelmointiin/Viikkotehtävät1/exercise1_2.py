# Annetaan alv muuttujana
alv = 0.255

# Kysytään hinta ilman alv
hinta = float(input("Anna hinta ilman alv:\n"))

# Lasketaan hinta alv kanssa ja pyöristetään tulos
kokonaishinta = round((hinta * alv) + hinta, 2)

# Tulostetaan kokonaishinta
print("Kokonaishinta alv:n kanssa:", kokonaishinta, "€")
