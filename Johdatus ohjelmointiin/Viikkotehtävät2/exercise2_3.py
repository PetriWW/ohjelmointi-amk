
# Asetetaan muuttujat ja kysytään kuukausipalkka sekä veroprosentti
salary = float(input("Anna kuukausipalkkasi: \n"))
tax = float(input("Anna veroprosenttisi: \n"))

# Lasketaan verot ja nettotulot
tax_total = salary * (tax / 100)
salary_total = salary - tax_total

# Tulostetaan vastaus
print(f"Käteenjäävä osuus: {salary_total} € \nVerot: {tax_total} €")
