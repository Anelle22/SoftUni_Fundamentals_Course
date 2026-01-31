class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal_name):
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)

        Zoo.__animals += 1


    def get_info(self, species):
        if species == "mammal":
            return f'Mammals in {self.name}: {", ".join(self.mammals)}\nTotal animals: {Zoo.__animals}'
        elif species == "fish":
            return f'Fishes in {self.name}: {", ".join(self.fishes)}\nTotal animals: {Zoo.__animals}'
        else:
            return f'Birds in {self.name}: {", ".join(self.birds)}\nTotal animals: {Zoo.__animals}'

name_of_zoo = input()
zoo = Zoo(name_of_zoo)
lines_of_animal_info = int(input())

for i in range(lines_of_animal_info):
    animal_info = input().split()
    zoo.add_animal(animal_info[0], animal_info[1])

some_species = input()

print(zoo.get_info(some_species))