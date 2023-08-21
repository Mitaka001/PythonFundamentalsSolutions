import re

string = input()

while string:
    pattern = "\d+"
    matched = re.findall(pattern, string)
    if matched:
        print(" ".join(matched), end=" ")
    string = input()
