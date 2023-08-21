numbers = [int(s) for s in input().split(", ")]
group = 10
while len(numbers) > 0:
    filtered_list = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {filtered_list}")
    group += 10
    numbers = [number for number in numbers if number not in filtered_list]
