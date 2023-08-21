text = input()
encrypted_version = ""

for character in text:
    encrypted_character = chr(ord(character) + 3)
    encrypted_version += encrypted_character

print(encrypted_version)
