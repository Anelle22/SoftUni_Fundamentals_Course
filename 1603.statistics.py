product_information = input()
stock_list = {}
total_products = 0
total_quantity = 0

while product_information != "statistics":
    split_product = product_information.split(": ")
    product = split_product[0]
    quantity = int(split_product[1])
    if product in stock_list.keys():
        stock_list[product] += quantity
    else:
        stock_list[product] = quantity
    product_information = input()

print("Products in stock:")
for key in stock_list.keys():
    print(f"- {key}: {stock_list[key]}")
    total_products += 1
    total_quantity += int(stock_list[key])

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
