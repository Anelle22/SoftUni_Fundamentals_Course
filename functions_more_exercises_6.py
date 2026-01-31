number_one = int(input())
number_two = int(input())
number_three = int(input())

def multiplication_result(some_number_one, some_number_two, some_number_three) -> str:
    count_of_negative_numbers = 0
    if some_number_one < 0:
        count_of_negative_numbers += 1
    if some_number_two < 0:
        count_of_negative_numbers += 1
    if some_number_three < 0:
        count_of_negative_numbers += 1

    if some_number_one == 0 or some_number_two == 0 or some_number_three == 0:
        result = "zero"
    elif count_of_negative_numbers % 2 == 0 or count_of_negative_numbers == 0:
        result = "positive"
    else:
        result = "negative"

    return result

print(multiplication_result(number_one, number_two, number_three))