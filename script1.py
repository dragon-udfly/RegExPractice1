import re

name= "John Smith"
print(f"Name: {name}")

characters= re.findall("[a-z]", name)
for c in range(0, len(characters), 1):
    print(characters[c])