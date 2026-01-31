initial_energy = int(input())
command = input()
won_battles = 0
game_ended = False

while command != "End of battle":


    distance_to_reach_enemy = int(command)
    if initial_energy >= distance_to_reach_enemy:
        won_battles += 1
        initial_energy -= distance_to_reach_enemy
    else:
        game_ended = True
        break
    if won_battles % 3 == 0:
        initial_energy += won_battles
    command = input()


if game_ended:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")

