def sort_in_ascending_order(list_of_numbers: list) -> list:
    return sorted(list_of_numbers)

numbers_as_string = input().split()
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))

result = sort_in_ascending_order(numbers_as_integers)
print(result)

