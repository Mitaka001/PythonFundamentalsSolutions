input_operator = input()
first_num = int(input())
second_num = int(input())

def solve(input_operator, first_num, second_num):
    if input_operator == 'multiply':
        return first_num * second_num
    if input_operator == 'divide':
        return int(first_num / second_num)
    if input_operator == 'add':
        return first_num + second_num
    if input_operator == 'subtract':
        return first_num - second_num

print(solve(input_operator, first_num, second_num))
