num = int(input())
num_list = []
filtered = []

for i in range(num):
    current_num = int(input())
    num_list.append(current_num)

command = input()

if command == 'even':
    for number in num_list:
        if number % 2 == 0:
            filtered.append(number)
elif command == 'odd':
    for number in num_list:
        if number % 2 != 0:
            filtered.append(number)
elif command == 'negative':
    for number in num_list:
        if number < 0:
            filtered.append(number)
elif command == 'positive':
    for number in num_list:
        if number >= 0:
            filtered.append(number)
print(filtered)
