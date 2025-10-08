try:
    num1 = int(input("Anna ensimmäinen numero: "))
    num2 = int(input("Anna toinen numero: "))
    
    answer = num1 / num2

except ValueError:
    print("Virheellinen muoto.")

except ZeroDivisionError:
    print("Nollalla ei saa jakaa.")

else:
    print(answer)