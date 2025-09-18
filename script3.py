import re 

def Print(arr):
    for ch in range(0, len(arr), 1):
        print(arr[ch])
    print("\n")

text= str(input("Enter text here: "))

print(f"Original Text: {text}")

a_zCharacters= re.findall("[a-z]", text)