pens = int(input())
markers = int(input())
cleaning_liquid = int(input())
discount = int(input())

total_cost = (1 - discount / 100) * (pens * 5.8 + markers * 7.2 + cleaning_liquid * 1.2)

print(total_cost)
