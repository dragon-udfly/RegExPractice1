import re 

text= str(input("Enter text here: "))

print(f"Original Text: {text}")

a_zCharacters= re.findall("[a-z]", text)
print("Alphabetical Characters: {a_zCharacters}")