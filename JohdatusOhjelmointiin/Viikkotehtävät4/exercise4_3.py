text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)

# Replace fox with duck
text = text.replace("fox", "duck")
print(text)

# Ask user for a word to remove
word = input("Anna poistettava sana:\n")

# Remove the word if it exists
if word in text:
    text = text.replace(word, "")
    print(text)
else:
    print("Sanaa ei löytynyt.")

# Count characters and words
print("Merkkejä:", len(text))
print("Sanoja:", len(text.split()))

# Replace periods with new lines
text = text.replace(".", "\n")
print(text)

# Ask user for a sentence and shorten if necessary
usertext = input("Anna jokin lause:\n")
if len(usertext) > 20:
    usertext = usertext[:20]
    usertext += "..."

print(usertext)