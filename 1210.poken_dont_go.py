distances_to_pokemon = [int(element) for element in input().split()]
sum_of_removed_elements = 0

while True:
    index = int(input())
    if index < 0:
        removed_element = distances_to_pokemon[0]
        distances_to_pokemon[0] = distances_to_pokemon[-1]
    elif index > len(distances_to_pokemon) - 1:
        removed_element = distances_to_pokemon[-1]
        distances_to_pokemon[-1] = distances_to_pokemon[0]
    else:
        removed_element = distances_to_pokemon.pop(index)

    for i in range(0, len(distances_to_pokemon)):
        if distances_to_pokemon[i] <= removed_element:
            distances_to_pokemon[i] += removed_element
        else:
            distances_to_pokemon[i] -= removed_element

    sum_of_removed_elements += removed_element
    if not distances_to_pokemon:
        print(sum_of_removed_elements)
        break

