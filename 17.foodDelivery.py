chicken = int(input())
fish = int(input())
vegetarian = int(input())

total_price = chicken * 10.35 + fish * 12.40 + vegetarian * 8.15
desert = 0.2 * total_price

print(total_price + desert + 2.5)