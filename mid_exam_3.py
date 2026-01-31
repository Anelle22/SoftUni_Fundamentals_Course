days_of_adventure = int(input())
number_of_adventurers = int(input())
current_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())
energy_loss = []
quest_finished = True

for i in range (1, days_of_adventure + 1):
    energy_loss.append(float(input()))

total_food_supply = days_of_adventure * number_of_adventurers * food_per_person
total_water_supply = days_of_adventure * number_of_adventurers * water_per_person

for day_number in range (1, days_of_adventure + 1):
    if current_energy <= energy_loss[day_number - 1]:
        quest_finished = False
        print(f"You will run out of energy. You will be left with {total_food_supply:.2f} food and {total_water_supply:.2f} water.")
        break
    else:
        current_energy -= energy_loss[day_number - 1]

    if day_number % 2 == 0:
        current_energy = current_energy * 1.05
        total_water_supply = total_water_supply * 0.7

    if day_number % 3 == 0:
        current_energy = current_energy * 1.1
        total_food_supply -= total_food_supply / number_of_adventurers


if quest_finished:
    print (f"You are ready for the quest. You will be left with {current_energy:.2f} energy!")
