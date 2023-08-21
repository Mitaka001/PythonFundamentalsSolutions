def calculate_new_prices(items, budget):
    max_prices = {
        "Clothes": 50.00,
        "Shoes": 35.00,
        "Accessories": 20.50
    }

    bought_items_prices = []
    total_profit = 0

    for item in items:
        item_type, price = item.split("->")
        price = float(price)

        if item_type in max_prices and price <= max_prices[item_type]:
            if budget >= price:
                budget -= price
                new_price = price * 1.40
                bought_items_prices.append(new_price)
                total_profit += new_price - price

    return bought_items_prices, total_profit


items_input = input().split("|")
budget_input = float(input())

bought_prices, profit = calculate_new_prices(items_input, budget_input)

print(" ".join(f"{price:.2f}" for price in bought_prices))
print(f"Profit: {profit:.2f}")

if budget_input + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
