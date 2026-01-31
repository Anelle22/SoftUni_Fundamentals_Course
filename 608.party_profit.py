number_of_companions = int(input())
days = int(input())
coins = 0

for i in range (1, days + 1):
    if i % 10 == 0:
        number_of_companions -= 2
    if i % 15 == 0:
        number_of_companions += 5

    if i % 3 == 0:
        coins -= 3 * number_of_companions
    if i % 5 == 0:
        coins += 20 * number_of_companions
        if i % 3 ==0:
            coins -= 2 * number_of_companions

    coins += 50 - (2 * number_of_companions)

print(f"{number_of_companions} companions received {int(coins / number_of_companions)} coins each.")