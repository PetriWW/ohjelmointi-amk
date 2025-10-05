# Kysytään aikaa minuutteina
time = int(input("Anna minuutit:\n"))

# Lasketaan tunnit ja minuutit
hours = time // 60
minutes = time % 60

# Tulostetaan vastaus
if hours == 0:
    print(f"{minutes}min")
else:
    print(f"{hours}h {minutes}min")