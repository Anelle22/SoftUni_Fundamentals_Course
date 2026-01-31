order_number = int(input())
total_price = 0


for i in range(order_number):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not (0.01 <= price_per_capsule <= 100) or not (1 <= days <= 31) or not (1 <= capsules_per_day <= 2000):
        continue
    price = price_per_capsule * days * capsules_per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")