budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
bread_cost = flour_price + eggs_price + milk_price
bread_number = 0
coloured_eggs = 0

while (budget >= bread_cost):
    budget = budget - bread_cost
    bread_number += 1
    coloured_eggs += 3

    if bread_number % 3 == 0:
        coloured_eggs -= bread_number - 2

print(f"You made {bread_number} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
