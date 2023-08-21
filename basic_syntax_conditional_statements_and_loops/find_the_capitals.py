text = input()
list_of_indexes = []

for index, char in enumerate(text):
    if char.isupper():
        list_of_indexes.append(index)

print(list_of_indexes)
