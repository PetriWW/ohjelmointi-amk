# Asetetaan saatavilla olevat kolikot
coins = (50, 20, 10, 5, 2, 1)

# Kysytään käyttäjältä kolikot
input_coin = int(input("Anna 1-100 senttiä: \n"))

# Lasketaan annettavat kolikot
# Olin kysynyt tekoälyltä "mielipidettä" mutta se antoi vain kuraa joka olisi ollut 10+ riviä
for coin in coins:
    total = input_coin // coin
    input_coin = input_coin % coin

    #Tulostetaan vastaus
    print(f"Annetaan: {coin} snt kpl {total}")