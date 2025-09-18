import re 

def Print(arr):
    for ch in range(0, len(arr), 1):
        print(arr[ch], end= " ")
    print("\n")

text= str(input("Enter text here: "))

print(f"Original Text: {text}")

Print(re.findall("[a-z]", text))