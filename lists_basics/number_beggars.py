money_as_string = input().split(", ")
count_of_beggars = int(input())
money_as_digits = []
total_sum = []
start_index = 0

for element in money_as_string:
    money_as_digits.append(int(element))

while start_index < count_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(money_as_digits), count_of_beggars):
        sum_for_current_beggar += money_as_digits[current_index]
    total_sum.append(sum_for_current_beggar)
    start_index += 1

print(total_sum)
