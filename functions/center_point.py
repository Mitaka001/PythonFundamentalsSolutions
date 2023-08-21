import math


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2.0) + math.pow(y2 - y1, 2.0))


x_one = math.floor(float(input()))
y_one = math.floor(float(input()))
x_two = math.floor(float(input()))
y_two = math.floor(float(input()))

distance_one = distance(x_one, y_one, 0, 0)
distance_two = distance(x_two, y_two, 0, 0)

if distance_one <= distance_two:
    print(f"({x_one}, {y_one})")
else:
    print(f"({x_two}, {y_two})")
