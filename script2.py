import re

text= "This is a 399 and 89 but but ."
print(f"Original text: {text}")
digits= re.findall("\d", text)
print(f"Digits: {digits}")