number_of_lines = int(input())
capacity = 255
water = 0

for _ in range(number_of_lines):
    liters_of_water = int(input())

    if capacity - liters_of_water < 0:
        print('Insufficient capacity!')
        continue

    capacity -= liters_of_water
    water += liters_of_water

print(water)
