

text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)

text = text.replace("fox", "duck")
print(text)


word = input("Anna poistettava sana:\n")


if word in text:
    text = text.replace(word, "")
    print(text)
else:
    print("Sanaa ei löytynyt.")

print("Merkkejä:", len(text))
print("Sanoja:", len(text.split()))

text = text.replace(".", "\n")
print(text)

usertext = input("Anna jokin lause:\n")
if len(usertext) > 20:
    usertext = usertext[:20]
    usertext += "..."
print(usertext)