def round_numbers(numbers):
    rounded_list = [round(float(num)) for num in numbers.split()]
    return rounded_list

input_numbers = input()
rounded_result = round_numbers(input_numbers)
print(rounded_result)
