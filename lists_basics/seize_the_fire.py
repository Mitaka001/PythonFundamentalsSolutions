fires_with_their_cells = input().split("#")
water = int(input())
total_fire = 0
effort = 0
extinguished_cells = []

for data in fires_with_their_cells:
    type_of_fire, value_of_cell = data.split(" = ")
    value_of_cell = int(value_of_cell)

    if type_of_fire == "High":
        if 81 <= value_of_cell <= 125:
            if water >= value_of_cell:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                extinguished_cells.append(value_of_cell)

    elif type_of_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            if water >= value_of_cell:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                extinguished_cells.append(value_of_cell)

    elif type_of_fire == "Low":
        if 1 <= value_of_cell <= 50:
            if water >= value_of_cell:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                extinguished_cells.append(value_of_cell)

    if water <= 0:
        break

print("Cells:")
for cell in extinguished_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
