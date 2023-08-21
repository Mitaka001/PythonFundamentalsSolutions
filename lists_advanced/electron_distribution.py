number_of_electrons = int(input())
list_of_electrons = []
shell = 0

while number_of_electrons > 1:
    shell += 1
    shell_max = 2 * (shell**2)
    if number_of_electrons < shell_max:
        shell_max = number_of_electrons
        number_of_electrons = 0
    else:
        number_of_electrons -= shell_max
    list_of_electrons.append(shell_max)
print(list_of_electrons)
