number_of_snowballs = int(input())

max_weight = 0
max_time = 0
max_value = 0
max_quality = 0

for snowballs in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = (weight / time_needed) ** quality
    if snowball_value > max_value:
        max_weight = weight
        max_time = time_needed
        max_value = snowball_value
        max_quality = quality
print(f'{max_weight} : {max_time} = {int(max_value)} ({max_quality})')
