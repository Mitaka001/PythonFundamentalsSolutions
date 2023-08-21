string = input()
digit = ""
letter = ""
other = ""

for char in string:
    if char.isdigit():
        digit += char
    elif char.isalpha():
        letter += char
    else:
        other += char

print(digit)
print(letter)
print(other)
