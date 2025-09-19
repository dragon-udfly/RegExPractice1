import re 

text= "This text is containing89, is running 34, is walking 45. Not the same thing but the only thing. 23 Can you be running."

english_characters= re.findall("[a-z]", text)
print(f"Number of english characters: {len(english_characters)}")

digits= re.findall("\d", text)
print(f"Number of digits: {len(digits)}")

non_digits= re.findall("\D", text)
print(f"Number of non digital characters: {len(non_digits)}")

non_word_characters= re.findall("\W", text) 
print(f"Number of non-word characters: {len(non_word_characters)}")

letters_and_numbers= re.findall("\w", text) 
print(f"Number of letters and characters: {len(letters_and_numbers)}")

whitespaces= re.findall("\s", text) 
print(f"Number of whitespace characters: {len(whitespaces)}")

non_whitespace_characters= re.findall("\S", text) 
print(f"Number of non word characters: {len(non_whitespace_characters)}")

is_word= re.findall(r'\bis\b', text)
print(f"Number of 'is': {len(is_word)}")

thing_word= re.findall(r'\bthing\b', text) 
print(f"Number of 'thing': {len(thing_word)}")

running_word= re.findall(r'\brunning\b', text) 
print(f"Number of 'running': {len(running_word)}")