
# Kysytään käyttäjältä rahamäärää ja hintaa
q_input = int(input("Anna rahaa:\n"))
q_input_price = int(input("Ostosten hinta:\n"))

# Muuttujat rahoille jotka jäävät yli tai ali
remaining = q_input_price - q_input
change = q_input - q_input_price

# Verrataan menevätkö rahat tasan
if q_input == q_input_price:
    print("Kiitos. Tasaraha")

# Verrataan meneekö rahat yli tai ali, ja menettellään sen mukaan
if change > 0:
    print(f"Kiitos. Annetaan takaisin {change} €")

if remaining > 0:
    retry_pay = int(input(f"Rahat eivät riitä, anna lisää rahaa:\n"))

    if retry_pay == remaining:
        print("Kiitos. Tasaraha.")

    elif retry_pay > remaining:
        print(f"Kiitos. Annetaan takaisin {retry_pay - remaining} €")

    else:
        print("Sinulla ei ole tarpeeksi rahaa.")



