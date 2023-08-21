product = input()
quantity = int(input())

COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00

def total_price(product, quantity):
    if product == 'coffee':
        return quantity * COFFEE
    elif product == 'coke':
        return quantity * COKE
    elif product == 'water':
        return quantity * WATER
    elif product == 'snacks':
        return quantity * SNACKS
print(f'{total_price(product, quantity):.2f}')
