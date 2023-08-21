def calculation(number):
    for current_num in range(1, number):
        number *= current_num
    return number


first_number = int(input())
second_number = int(input())
first_factorial = calculation(first_number)
second_factorial = calculation(second_number)
result = first_factorial / second_factorial
print(f"{result:.2f}")
