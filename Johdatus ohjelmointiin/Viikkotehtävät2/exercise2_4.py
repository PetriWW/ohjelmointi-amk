# Asetetaan muuttujat ja kysytään kilometrit
m_distance = float(input("Matka-ajon kilometrit:\n"))
k_distance = float(input("Kaupunkiajon kilometrit:\n"))

# Asetetaan muuttujat joissa eri kulutus ajotyypeille
m_ratio = m_distance / 100 * 5.1
k_ratio = k_distance / 100 * 7.5

# Pyöristetään tulos
round(m_ratio + k_ratio, 2)

# Tulostetaan vastaus
print(f"Kulutus: {m_ratio + k_ratio} l")