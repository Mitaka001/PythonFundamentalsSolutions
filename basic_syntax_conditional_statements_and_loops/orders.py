number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if not 0.01 <= capsule_price <= 100.00 or not 1 <= days <= 31 or not 1 <= needed_capsules_per_day <= 2000:
        continue

    total_for_order = capsule_price * days * needed_capsules_per_day
    print(f'The price for the coffee is: ${total_for_order:.2f}')
    total_price += total_for_order

print(f'Total: ${total_price:.2f}')
