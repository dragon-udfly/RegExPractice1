import re 

text= "This is the begining of the end."

print(re.findall("[a-m]", text))
print(re.findall("[a-x]", text))

print(re.findall("[i-n]", text))