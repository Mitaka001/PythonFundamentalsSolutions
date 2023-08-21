def character_as_string(char_one, char_two):
    list_characters = []
    for character_as_digital in range(ord(char_one) + 1, ord(char_two)):
        list_characters.append(chr(character_as_digital))
    return list_characters

first_character = input()
second_character = input()
result = character_as_string(first_character, second_character)
print(" ".join(result))
