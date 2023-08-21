number = input()
max_number = []
for num in number:
    max_number += num
new_number = sorted(max_number, reverse=True)
print(int("".join(new_number)))
