import re

name= "John Smith"
print(f"Name: {name}")

characters= re.findall("[a-z]", name)
for c in range(len(characters)):
    print(characters[c])