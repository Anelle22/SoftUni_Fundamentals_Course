successful = True

while True:
    name = input()
    name_length = len(name)
    house = ""
    if name_length < 5:
        house = "Gryffindor"
    elif name_length == 5:
        house = "Slytherin"
    elif name_length == 6:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"

    if name == "Voldemort":
        print("You must not speak of that name!")
        successful = False
        break

    if name == "Welcome!":
        break

    print(f"{name} goes to {house}.")

if successful:
    print("Welcome to Hogwarts.")
