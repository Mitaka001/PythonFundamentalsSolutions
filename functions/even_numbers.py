given_numbers = input().split()
numbers_as_digits = []
for number in given_numbers:
    numbers_as_digits.append(int(number))
even_numbers = lambda x: x % 2 == 0
result = list(filter(even_numbers, numbers_as_digits))
print(result)
