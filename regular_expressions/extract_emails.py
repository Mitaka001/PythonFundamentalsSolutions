import re

single_string = input()

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, single_string)
for mails in matches:
    print(mails[0])
