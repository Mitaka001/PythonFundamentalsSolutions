while True:
    command = input()
    reversed_text = ""

    if command == "end":
        break

    for char in reversed(command):
        reversed_text += char

    print(command + " = " + reversed_text)
