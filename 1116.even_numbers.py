numbers = list(map(int, input().split(', ')))

list_of_even_indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(list_of_even_indices)