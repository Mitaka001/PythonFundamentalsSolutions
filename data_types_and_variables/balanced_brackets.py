number_of_lines = int(input())
balanced_bracket = 0

for symbols in range(number_of_lines):
    symbol = input()

    if symbol == "(":
        balanced_bracket += 1

        if balanced_bracket > 1:
            print("UNBALANCED")
            exit()

    elif symbol == ")":
        balanced_bracket -= 1

        if balanced_bracket < 0:
            print("UNBALANCED")
            exit()

    elif symbol == "((" or symbols == "))":
        print("UNBALANCED")
        exit()

if balanced_bracket == 0:
    print("BALANCED")
else:
    print("UNBALANCED")

