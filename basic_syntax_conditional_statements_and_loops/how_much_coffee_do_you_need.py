command = input()
coffee = 0
lowercase = ['coding', 'cat', 'dog', 'movie']
uppercase = ['CODING', 'CAT', 'DOG', 'MOVIE']

while not command == 'END':
    if command in lowercase:
        coffee += 1
    elif command in uppercase:
        coffee += 2

    command = input()

    if command == 'END':
        if coffee > 5:
            print('You need extra sleep')
        else:
            print(coffee)
