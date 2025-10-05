import math

# Kysytään käyttäjältä sivujen pituudet
a = float(input("Anna särmiön ensimmäisen sivun pituus: \n"))
b = float(input("Anna särmiön toisen sivun pituus: \n"))
c = float(input("Anna särmiön kolmannen sivun pituus: \n"))

# Kaava tilavuuden laskemiseen
V = a * b * c

# Tulostetaan vastaus
print("Särmiön tilavuus on:", V, "m3")

# Kysytään käyttäjältä pallon säde
input_radius = float(input("Anna pallon säde: \n"))

# Kaava pallon tilavuuden laskemiseen ja pyöristetään desimaalit
volume = round(4/3 * math.pi * input_radius**3, 2)

# Tulostetaan vastaus
print("Pallon tilavuus on:", volume, "m3")