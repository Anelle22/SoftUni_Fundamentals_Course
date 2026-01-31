def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for i in range (1, some_number):
        if some_number % i == 0:
            divisors_sum += i

    if divisors_sum == some_number:
        return "We have a perfect number!"

    return "It's not so perfect."

number = int(input())
print(is_perfect(number))
