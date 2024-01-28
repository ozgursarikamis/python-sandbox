from difflib import fuzz

name = "Kurtis Pykes"
full_name = "Kurtis K D Pykes"

print(f"Similarity between {name} and {full_name} is {fuzz.ratio(name, full_name)}")