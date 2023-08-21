def smallest_number(some_numbers):
    result = min(some_numbers)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
smallest_number(numbers)
print(smallest_number(numbers))
