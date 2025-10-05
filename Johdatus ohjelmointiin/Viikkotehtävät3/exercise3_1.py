# Muuttujat jossa kysytään käyttäjältä kahta numeroa
q_input1 = int(input("Anna ensimmäinen luku:\n"))
q_input2 = int(input("Anna toinen luku:\n"))


# Verrataan numeroa ja tulostetaan vastaus
if q_input1 > q_input2:
    print(f"Suurempi luku: {q_input1}")

elif q_input1 < q_input2:
    print(f"Suurempi luku: {q_input2}")
    
elif q_input1 == q_input2:
    print("Numerot ovat yhtä suuria.")

# Olisin voinut käyttää 'else' mutta eikö ole tarkempi käyttää 'elif x == y' kun halutaan olla varmoja että ovat yhtä suuret?