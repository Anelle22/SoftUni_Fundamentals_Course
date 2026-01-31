def calculate_results(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'add': num1 + num2,
        'subtract': num1 - num2
    }.get(operator, 'Invalid operator')

operator = input()
num1 = int(input())
num2 = int(input())

print(calculate_results(operator, num1, num2))