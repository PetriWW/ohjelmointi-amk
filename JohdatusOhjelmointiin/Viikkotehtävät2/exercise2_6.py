import math

# En tiedä pitääkö hedelmien arvo jakaa kun niiden määrä muuttuu kuvan alaosassa
# Esimerkiksi kirsikkaparista tulee vain yksi kirsikka, pitääkö se sitten jakaa kahdella?
# En jakanut hedelmien arvoa

# Lasketaan hedelmät kuvan mukaisesti
cherry = 2 + 2 * 2 + 2 - 2 - 2
apple = (math.sqrt(3 + 10 - 4) / 3) + ((5**3 - 5) / 20) + 3
orange = apple - 9
banana = cherry - 10
pear = banana - 8

# Lasketaan vastaus
answer = apple - banana + orange * pear + cherry

# Tulostetaan vastaus
print(answer)