import math

def closer_point(some_x1, some_y1, some_x2, some_y2) -> str:
    first_point = math.sqrt(some_x1 ** 2 + some_y1 ** 2)
    second_point = math.sqrt(some_x2 ** 2 + some_y2 ** 2)
    if first_point <= second_point:
        result = f"({math.floor(some_x1)}, {math.floor(some_y1)})"
    else:
        result = f"({math.floor(some_x2)}, {math.floor(some_y2)})"
    return result

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closer_point(x1, y1, x2, y2))