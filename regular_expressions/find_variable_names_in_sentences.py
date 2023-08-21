import re

sentences = input()

pattern = r"\b_([a-zA-Z0-9]+)\b"
matched = re.findall(pattern, sentences)

print(",".join(matched))
