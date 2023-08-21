divisor = int(input())
boundary = int(input())

for max_number in range(boundary, divisor - 1, -1):
    if max_number % divisor == 0:
        break
print(max_number)
