animals = input().split(", ")
wolf_position = animals.index("wolf")
sheep_count = len(animals) - wolf_position - 1

if sheep_count == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
