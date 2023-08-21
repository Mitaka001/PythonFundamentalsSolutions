def ascending_ordered_numbers(numbers):
    ascending_order = []
    for digits in numbers:
        ascending_order.append(int(digits))
    sorted_numbers = sorted(ascending_order)
    return sorted_numbers

given_numbers = input().split()
result = ascending_ordered_numbers(given_numbers)
print(result)
