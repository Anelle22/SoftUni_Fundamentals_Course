factor = int(input())
count = int(input())

numbers_list = []

n = 1

for i in range(count):
    numbers_list.append(n * factor)
    n += 1

print(numbers_list)