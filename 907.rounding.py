def round_number(some_numbers) -> list:
    rounded_list = []
    for number in some_numbers:
        rounded_list.append(round(number))
    return rounded_list

numbers = (float(number) for number in input().split())
print(round_number(numbers))