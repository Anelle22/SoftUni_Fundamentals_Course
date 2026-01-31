
numbers_as_string = input().split()
numbers_as_integer = []
for number in numbers_as_string:
    numbers_as_integer.append(int(number))

min_number = min(numbers_as_integer)
max_number = max(numbers_as_integer)
sum_of_numbers = sum(numbers_as_integer)

print(f"The minimum number is {min_number}")

print(f"The maximum number is {max_number}")

print(f"The sum number is: {sum_of_numbers}")


