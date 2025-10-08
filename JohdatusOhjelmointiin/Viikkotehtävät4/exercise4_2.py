
# Declare input and its reversed version
text_input = input("Anna jokin teksti:\n")
text_reversed = text_input[::-1]
print(text_reversed)


# Check for palindrome
if text_input == 0:
    print("Antamasi teksti on tyhjä.")
elif text_input == text_reversed:
    print("Palindromi: KYLLÄ")
else:
    print("Palindromi: EI")