
# Viikon työtunnit
work_hours = int(input("Syötä viikon työtunnit:\n"))

# Tuntipalkka
hourly_rate = float(input("Syötä tuntipalkka:\n"))

# Lasketaan perusansiot
salary = (work_hours * hourly_rate)

# Ylityölisä ja pyöristetään
if work_hours > 40:
    overtime_pay = ((work_hours - 40) * hourly_rate) * 0.5
    salary = round(salary + overtime_pay, 2)
    
print(f"Viikon ansiosi ovat {salary}€")

