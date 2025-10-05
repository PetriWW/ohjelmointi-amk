# Kysytään käyttäjältä ostoksen tiedot
total_sum = int(input("Syötä ostosten kokonaissumma euroina:\n"))
is_student = input("Onko asiakas opiskelija (k/e):\n").lower() == "k"
is_regular = input("Onko asiakas kanta-asiakas (k/e):\n").lower() == "k"

final_price = total_sum

# Kysytään pisteiden määrä jos asiakas
loyalty_points = 0
if is_regular:
    loyalty_points = int(input("Kuinka monta kanta-asiakaspistettä:\n"))

# Kysytään alennuskoodit
discount_code = input("Syötä mahdollinen alennuskoodi:\n").upper()
if discount_code == "FALL25":
    final_price *= 0.9
elif discount_code == "BK2SCHOOL" and is_student:
    final_price *= 0.8

# Sovelletaan pisteet
if is_regular:
    loyalty_discount = (loyalty_points // 1000) * 0.05
    final_price *= (1 - loyalty_discount)

# Lisätään postikulut
if final_price < 99:
    final_price += 7.95

# Tulostetaan hinta
print(f"Tilauksen loppusumma: {final_price} €")