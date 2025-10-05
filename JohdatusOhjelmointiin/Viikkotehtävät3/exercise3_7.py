
# Olin jumissa tässä tehtävässä päivän tai pari kun en osannut kaikkia operaattoreita
# Kysyin tekoälyltä ja googletin esim mitä eroa oli += ja + operaattoreilla
# 

# Kysytään käyttäjältä tiedot
user_input = input("Kirje vai paketti? (k/p)\n")
weight = int(input("Anna paino:\n"))

# Määritellään hinnat
if user_input == "k":
    price = 50
    mid_rate = 4
    high_rate = 7
else:
    price = 200
    mid_rate = 8
    high_rate = 14

# Lasketaan hinta painon mukaan
# Tekoälyltä sain vinkin tuon min() käyttöön
if weight > 200:
    weight_mid = min(weight, 500) - 200
    price += (weight_mid // 100) * mid_rate

if weight > 500:
    weight_high = weight - 500
    price += (weight_high // 100) * high_rate
    
    # Postilaatikkotarkistus vain kirjeille
    if user_input == "kirje":
        size_check = input("Mahtuuko kirje postilaatikkoon? (k/e)\n")
        if size_check == "e":
            price += 200

# Muutetaan euroiksi
euros = price / 100

print(f"Lähetys maksaa: {euros} euroa")