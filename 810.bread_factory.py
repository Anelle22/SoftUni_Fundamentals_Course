initial_energy = 100
initial_coins = 100
working_day_events = input().split("|")
handled_all_events = True

for action in working_day_events:
    event_values = action.split("-")
    event_type, event_value = event_values[0], int(event_values[1])


    if event_type == "rest":
        original_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - original_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_type == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            print("You had to rest!")
            initial_energy += 50

    else:
        if initial_coins >= event_value:
            print(f"You bought {event_type}.")
            initial_coins -= event_value
        else:
            handled_all_events = False
            break

if handled_all_events:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
else:
    print(f"Closed! Cannot afford {event_type}.")