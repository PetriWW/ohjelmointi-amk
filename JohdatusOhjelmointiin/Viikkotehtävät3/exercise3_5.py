# Kysytään pistemäärää
points = int(input("Anna pistemäärä:\n"))

# Määrittellään pisterajat ja tulostetaan arvosana
if points < 0 or points > 100:
    print("Pistemäärä ei ole mahdollinen.")
    
elif points <= 50:
    print("Arvosana: 0")
    
elif points <= 60:
    print("Arvosana: 1")

elif points <= 70:
    print("Arvosana: 2")
    
elif points <= 80:
    print("Arvosana: 3")

elif points <= 90:
    print("Arvosana: 4")

else:
    print("Arvosana: 5")