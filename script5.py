import re

literal_periods= re.findall("\.", "This . not the. way you think.")
print(f"Literal periods: {literal_periods}")
print(f"Number of literal periods: {len(literal_periods)}")

literal_astrisk= re.findall("\*", "This * astrisk as it is *.")
print(f"Literal astrisks: {literal_astrisk}")
print(f"Number of literal astrisks: {len(literal_astrisk)}")

literal_plus= re.findall("\+", "23 + 34= 57 and is it + correct +")
print(f"Literal plus: {literal_plus}")
print(f"Number of literal plus: {len(literal_plus)}")

question_mark= re.findall("\+", "Why? what? how? when?")
print(f"Question mark symbols: {question_mark}")
print(f"Number of question mark symbols: {len(question_mark)}")