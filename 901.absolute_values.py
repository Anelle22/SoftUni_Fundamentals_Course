numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

def absolute_values(a: float):
    return abs(a)

absolute_numbers = list(map(absolute_values, numbers))
print(absolute_numbers)

