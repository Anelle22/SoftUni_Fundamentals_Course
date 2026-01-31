list_of_integers = input().split()
n = int(input())

numbers = [int(x) for x in list_of_integers]

lowest_number = numbers[0]

for i in range(n):
    lowest_number = min(numbers)
    numbers.remove(lowest_number)

print(", ".join(str(x) for x in numbers))




