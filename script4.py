import re 

text= "This text is containing89, is running34, is walking 45. Not the same thing but the only thing. 23 Can you be running."

english_characters= re.findall("[a-z]", text)
print(f"Number of english characters: {len(english_characters)}")

digits= re.findall("\d", text)
print(f"Number of digits: {len(digits)}")

