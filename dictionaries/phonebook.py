phonebook = {}
while True:
    info = input()
    if "-" not in info:
        break
    name, number = info.split("-")
    phonebook[name] = number
for search in range(int(info)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
        