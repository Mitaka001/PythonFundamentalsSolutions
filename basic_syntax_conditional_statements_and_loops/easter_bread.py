budget = float(input())
price_per_kilo_flour = float(input())
number_of_loaves = 0
colored_eggs = 0
money_left = budget

price_for_pack_of_eggs = price_per_kilo_flour * 0.75
price_for_liter_milk = price_per_kilo_flour * 1.25
total_for_one_loaf = price_for_pack_of_eggs + price_per_kilo_flour + price_for_liter_milk / 4

while True:
    if money_left < total_for_one_loaf:
        break

    colored_eggs += 3
    money_left -= total_for_one_loaf
    number_of_loaves += 1

    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2


print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
