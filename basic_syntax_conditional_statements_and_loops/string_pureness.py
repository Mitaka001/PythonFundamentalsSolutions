number = int(input())

for _ in range(number):
    string = input()

    is_pure = True
    for char in string:
        if char in [',', '.', '_']:
            is_pure = False
            break

    if is_pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
