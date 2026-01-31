population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())
total_wealth = sum(population)

for i in range (0, len(population)):
    index_of_person_with_max_wealth = population.index(max(population))
    if population[i] < minimum_wealth:
        wealth_needed = minimum_wealth - population[i]
        population[i] += wealth_needed
        population[index_of_person_with_max_wealth] -= wealth_needed

distribution_possible = True

for person in population:
    if person < minimum_wealth:
        distribution_possible = False

if distribution_possible:
    print(population)
else:
    print("No equal distribution possible")


