# Annetaan kulutus muuttujassa
fuel_ratio = 6.5 / 100

# Kysytään matkan pituus
distance = float(input("Syötä matkan pituus:\n"))

# Lasketaan kulutus ja pyöristetään tulos
fuel_consumption = round(distance * fuel_ratio, 1)

# Tulostetaan vastaus
print(f"Kulutus: {fuel_consumption} l")
