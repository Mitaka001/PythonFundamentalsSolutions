def min_max_and_sum(numbers):
    all_numbers = []
    for digits in numbers:
        all_numbers.append(int(digits))
    min_number = min(all_numbers)
    max_number = max(all_numbers)
    sum_of_all_numbers = sum(all_numbers)
    return min_number, max_number, sum_of_all_numbers

given_numbers = input().split()
min_digits, max_digits, sum_digits = min_max_and_sum(given_numbers)
print(f"The minimum number is {min_digits}")
print(f"The maximum number is {max_digits}")
print(f"The sum number is: {sum_digits}")
