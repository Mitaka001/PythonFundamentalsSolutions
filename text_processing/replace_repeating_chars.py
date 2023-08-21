string = input()
new_string = ""
current_character = ""

for character in string:
    if character not in current_character:
        new_string += character
        current_character = character

print(new_string)
