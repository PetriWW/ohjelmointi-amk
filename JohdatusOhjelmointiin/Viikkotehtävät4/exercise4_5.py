special_price = False
student_check = input("Oletko opiskelija? k/e:\n")

if student_check == "k":
    special_price = True

current_month = int(input("Anna kuukauden numero: \n"))
if current_month in (6, 7, 8):
    special_price = False

if special_price == True:
    print("Alennus myönnetty!")
else:
    print("Normaali hinta.")