def data_type(first, second):
    if first == "int":
        new_value = int(second) * 2
        return new_value
    elif first == "real":
        new_value = float(second) * 1.5
        return f"{new_value:.2f}"
    elif first == "string":
        return f"${second}$"


first_line = input()
second_line = input()
print(data_type(first_line, second_line))
