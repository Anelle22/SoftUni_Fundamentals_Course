animals = input()

new = animals.split(', ')

new.reverse()

sheep_count = 0

for i in range (len(new)):
    if new[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break

    if new[i] == "sheep":
        sheep_count += 1

    if new[i] == "wolf":
        print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
        break




