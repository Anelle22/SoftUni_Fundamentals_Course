def sum_of_even_odd_digits(given_number: str) -> str:
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for i in range(len(given_number)):
        if int(given_number[i]) % 2 == 0:
            sum_of_even_digits += int(given_number[i])
        else:
            sum_of_odd_digits += int(given_number[i])
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = input()
print(sum_of_even_odd_digits(number))