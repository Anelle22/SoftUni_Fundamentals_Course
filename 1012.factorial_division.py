def calculate_factorial(number: int) -> int:
    factorial = 1
    for i in range (1, number + 1):
        factorial *= i
    return factorial

first_number = int(input())
second_number = int(input())
first_factorial = calculate_factorial(first_number)
second_factorial = calculate_factorial(second_number)
print(f"{first_factorial / second_factorial:.2f}")