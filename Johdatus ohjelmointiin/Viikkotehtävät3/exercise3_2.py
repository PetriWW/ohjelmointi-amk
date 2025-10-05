
# Kysytään päivän lämpötila
temp = int(input("Syötä päivän lämpötila:\n"))


# Raja-arvot lämpötiloille
if temp <= 10:
    print("Kylmää")

elif temp <= 15:
    print("Koleaa")

elif temp <= 20:
    print("Normaali lämpötila")

elif temp <= 25:
    print("Lämmintä")

else:
    print("Hellettä")