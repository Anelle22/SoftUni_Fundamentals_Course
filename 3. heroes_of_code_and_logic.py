number_of_heros = int(input())
hero_dictionary = {}
i = 1

for i in range(number_of_heros):
    hero = input().split(" ")
    hero_name, hit_points, mana_points = str(hero[0]), int(hero[1]), int(hero[2])
    hero_dictionary[hero_name] = {"HP": hit_points, "MP": mana_points}

while True:
    instructions_as_a_string = input()
    if instructions_as_a_string == "End":
        break
    instructions = instructions_as_a_string.split(" - ")
    command = str(instructions[0])
    hero_name = str(instructions[1])

    if command == "CastSpell":
        mana_points_needed = int(instructions[2])
        spell_name = str(instructions[3])
        if mana_points_needed <= hero_dictionary[hero_name]['MP']:
            hero_dictionary[hero_name]['MP'] -= mana_points_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dictionary[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        given_damage_amount = int(instructions[2])
        attacker = str(instructions[3])
        hero_dictionary[hero_name]['HP'] -= given_damage_amount
        if hero_dictionary[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {given_damage_amount} HP by {attacker} and now has {hero_dictionary[hero_name]['HP']} HP left!")
        else:
            del hero_dictionary[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        amount = int(instructions[2])
        diff = 200 - hero_dictionary[hero_name]['MP']
        hero_dictionary[hero_name]['MP'] += amount
        if hero_dictionary[hero_name]['MP'] > 200:
            amount = diff
            hero_dictionary[hero_name]['MP'] = 200

        print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(instructions[2])
        diff = 100 - hero_dictionary[hero_name]['HP']
        hero_dictionary[hero_name]['HP'] += amount
        if hero_dictionary[hero_name]['HP'] > 100:
            amount = diff
            hero_dictionary[hero_name]['HP'] = 100

        print(f"{hero_name} healed for {amount} HP!")



for key, value in hero_dictionary.items():
    print(key)
    for nested_key, nested_value in value.items():
        print(f"  {nested_key}: {nested_value}")