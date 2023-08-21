def even_odd_sum(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for element in number:
        if int(element) % 2 == 0:
            sum_of_even_digits += int(element)
        else:
            sum_of_odd_digits += int(element)
    return sum_of_odd_digits, sum_of_even_digits


given_number = input()
odd_numbers, even_numbers = even_odd_sum(given_number)
print(f'Odd sum = {odd_numbers}, Even sum = {even_numbers}')
