
# Kysytään käyttäjätlä vuosilukua
input_year = int(input("Anna vuosiluku:\n"))

# Tarkistetaan onko vuosiluku jaollinen 4, 400 ja != 100
is_leap_year = (input_year % 400 == 0) or (input_year % 4 == 0) and (input_year % 100 != 0)

if is_leap_year == True:
    print("Karkausvuosi: KYLLÄ")
else:
    print("Karkausvuosi: EI")