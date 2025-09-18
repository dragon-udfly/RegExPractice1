import re 

text= str(input("Enter text here: "))

print(f"Original Text: {text}")

a_zCharacters= re.findall("[a-z]", text)
for ch in range(0, len(a_zCharacters), 1):
    print(a_zCharacters[ch], end=' ')