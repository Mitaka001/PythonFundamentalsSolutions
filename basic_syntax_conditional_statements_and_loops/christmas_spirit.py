quantity = int(input())
days = int(input())
total_spirit = 0
budget = 0
for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        budget += quantity * 2
        total_spirit += 5

    if current_day % 3 == 0:
        budget += quantity * 5 + quantity * 3
        total_spirit += 13

    if current_day % 5 == 0:
        budget += quantity * 15
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        budget += 23


if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
