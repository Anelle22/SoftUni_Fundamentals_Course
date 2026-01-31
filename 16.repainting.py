nylon = int(input())
paint = int(input())
diluter = int(input())
hours = int(input())

total_cost = (nylon + 2) * 1.5 + (paint * 1.1) * 14.5 + diluter * 5 + 0.4
total_labour = total_cost * 0.3 * hours

print(total_cost + total_labour)