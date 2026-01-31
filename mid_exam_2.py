travel_route_to_Titan = input().split("||")
current_fuel = int(input())
current_ammunition = int(input())

for action in travel_route_to_Titan:
    if action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    instructions = action.split(" ")
    current_command, current_parameter = instructions[0], int(instructions[1])

    if current_command == "Travel":
        light_years = int(current_parameter)
        if current_fuel >= light_years:
            current_fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break

    elif current_command == "Enemy":
        enemy_armour = int(current_parameter)
        if current_ammunition >= enemy_armour:
            current_ammunition -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        else:
            if current_fuel >= 2 * enemy_armour:
                current_fuel -= 2 * enemy_armour
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif current_command == "Repair":
        added_fuel = int(current_parameter)
        current_fuel += added_fuel
        added_ammunition = int(current_parameter) * 2
        current_ammunition += added_ammunition
        print(f"Ammunitions added: {added_ammunition}.")
        print(f"Fuel added: {added_fuel}.")

