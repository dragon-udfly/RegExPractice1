import re 

text= "This text is containing, is running, is walking. Not the same thing but the only thing. Can you be running."

english_characters= re.findall("[a-z]", text)
print(f"Number of english characters: {len(english_characters)}")