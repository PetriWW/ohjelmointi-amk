import math

# Kysytään käyttäjältä kolmion kateettien pituudet
a = float(input("Anna kolmion ensimmäinen kateetti: \n"))
b = float(input("Anna kolmion toinen kateetti: \n"))

# Kaava hypotenuusan laskemiseen
c = math.sqrt(a**2 + b**2)

# Käytetään pythagoraan lausetta
a**2 + b**2 == c**2

# Pyöristetään tulos
c = round(c, 1)

# Tulostetaan vastaus
print(f"hypotenuusan pituus: {c} m")