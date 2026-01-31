def sum_numbers(first: int, second: int) -> int:
     return first + second

def subtract (some_result: int, third) -> int:
    return some_result - third

def add_and_subtract(first_integer: int, second_integer: int, third_integer: int) -> int:
    returned_result = sum_numbers(first_integer, second_integer)
    final_result = subtract(returned_result, third_integer)
    return final_result




first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
