import random

# Arvotaan luku 1-10 välillä
r_num = random.randint(1, 10)

# Arvotaan luvut sivuille
a = random.randint(2,10)
b = random.randint(2,10)

# Lasketaan pinta-ala
area = a * b

# Tulostetaan vastaukset
print(f"Arvottu luku: {r_num}")
print(f"Arvottu 1. sivu: {a}")
print(f"Arvottu 2. sivu: {b}")
print(f"Arvotuista sivuista laskettu pinta-ala: {area}")