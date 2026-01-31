def calculate_total_price(some_product, some_quantity) -> float:
    if some_product == "coffee":
        product_price = 1.5
    elif some_product == "water":
        product_price = 1.0
    elif some_product == "coke":
        product_price = 1.4
    else:
        product_price = 2.0

    total_price = product_price * some_quantity
    return total_price

product = str(input())
quantity = float(input())

print(f"{calculate_total_price(product, quantity):.2f}")