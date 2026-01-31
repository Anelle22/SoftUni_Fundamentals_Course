numbers = input().split()
sum_of_numbers = 0

for number in numbers:
    sum_of_numbers += int(number)

average_of_numbers = sum_of_numbers / len(numbers)

numbers_as_integers = [int(number) for number in numbers]

numbers_as_integers.sort(reverse=True)
top_five_numbers_over_average = []
number_count = 0

for number in numbers_as_integers:
    if number > average_of_numbers:
        top_five_numbers_over_average.append(str(number))
        number_count += 1
    if number_count >= 5:
        break

if number_count == 0:
    print("No")
else:
    print(" ".join(top_five_numbers_over_average))

