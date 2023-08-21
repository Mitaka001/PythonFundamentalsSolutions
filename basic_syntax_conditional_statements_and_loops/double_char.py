while True:
    string = input()
    new_string = ''
    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    for i in string:
        new_string += i * 2
    print(new_string)

