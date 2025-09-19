import re

literal_periods= re.findall("\.", "This . not the. way you think.")
print(f"Literal periods: {literal_periods}")
print(f"Number of literal periods: {len(literal_periods)}")