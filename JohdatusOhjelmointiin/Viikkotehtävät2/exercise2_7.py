import math

# Kysytään käyttäjältä eri muuttujien arvot
a = float(input("Anna arvo a:\n"))
b = float(input("Anna arvo b:\n"))
c = float(input("Anna arvo c:\n"))

# Olin katsonut aiheesta eri sivustoja koska matematiikka ohjelmmoinnissa on haastavaa
# Kysyin myös tekoälyltä apua miten se voisi selittää auki tätä matematiikkaa
# Toivottavasti meni oikein

# lasketaan diskriminantti
d = (b**2) - (4*a*c)

# Ratkaistaan yhtälö ja tulostetaan vastaus
if d > 0:
    r_var1 = (-b + math.sqrt(d)) / (2*a)
    r_var2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Yhtälöllä on kaksi ratkaisua: {r_var1} ja {r_var2}")
elif d == 0:
    r_var3 = -b / (2*a)
    print(f"Yhtälöllä on yksi ratkaisu: {r_var3}")
else:
    print("Yhtälöllä ei ole reaalisia ratkaisuja")

