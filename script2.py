import re

text= "This is a 399 and 89 but-    but ."
print(f"Original text: {text}")
digits= re.findall("\d", text)
print(f"Digits: {digits}")
nondigits= re.findall("\D", text)
print(f"Non Digits: {nondigits}")
newline= re.findall("\n", text)
print(f"New line character: {newline}")
nonword= re.findall("\W", text)
print(f"Nonword characters: {nonword}")
words= re.findall("\w", text)
print(f"Word characters: {words}")
whitespace= re.findall("\s", text) 
print(f"Whitespace characters: {whitespace}")