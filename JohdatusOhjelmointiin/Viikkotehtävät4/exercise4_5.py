# Set special price and check if user is a student
special_price = False
student_check = input("Oletko opiskelija? k/e:\n")

# Set special price if user is a student and not in summer months
if student_check == "k":
    special_price = True

# Check for summer months    
current_month = int(input("Anna kuukauden numero: \n"))
if current_month in (6, 7, 8):
    special_price = False

# Print the result
if special_price == True:
    print("Alennus myönnetty!")
else:
    print("Normaali hinta.")