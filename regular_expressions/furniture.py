import re

command = input()
bought_furniture = []
total = 0
pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total += float(price) * int(quantity)

    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total:.2f}")
