given_numbers = input().split(", ")
indexes_of_even_numbers = []

for index, digit in enumerate(given_numbers):
    if int(digit) % 2 == 0:
        indexes_of_even_numbers.append(index)

print(indexes_of_even_numbers)
