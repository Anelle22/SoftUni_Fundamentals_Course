budget = int(input())
price = 0
total_cost = 0

while True:
    price = input()
    if price == "End":
        break
    total_cost = total_cost + int(price)
    if total_cost > budget:
        print("You went in overdraft!")
        break


if budget >= total_cost:
    print("You bought everything needed.")

