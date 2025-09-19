import re

literal_periods= re.findall("\.", "This . not the. way you think.")
print(f"Literal periods: {literal_periods}")
print(f"Number of literal periods: {len(literal_periods)}")

literal_astrisk= re.findall("\*", "This * astrisk as it is *.")
print(f"Literal astrisks: {literal_astrisk}")
print(f"Number of literal astrisks: {len(literal_astrisk)}")