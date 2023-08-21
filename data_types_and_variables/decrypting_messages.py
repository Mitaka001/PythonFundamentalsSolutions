key = int(input())
number_of_lines = int(input())
decrypted_message = ""
for _ in range(number_of_lines):
    letter = input()
    new_letter = ord(letter) + key
    decrypted_message += chr(new_letter)

print(decrypted_message)
