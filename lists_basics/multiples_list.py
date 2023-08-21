factor = int(input())
count = int(input())
list_of_numbers = []

for multiplier in range(1, count + 1):
    numbers = multiplier * factor
    list_of_numbers.append(numbers)
print(list_of_numbers)
