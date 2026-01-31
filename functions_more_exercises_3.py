import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def format_point(x, y):
    return f"({math.floor(x)}, {math.floor(y)})"

def closer_point(x1, y1, x2, y2) -> str:
    origin_x, origin_y = 0, 0
    first_point = distance(x1, y1, origin_x, origin_y)
    second_point = distance(x2, y2, origin_x, origin_y)

    if first_point <= second_point:
        result = f"{format_point(x1, y1)}{format_point(x2, y2)}"
    else:
        result = f"{format_point(x2, y2)}{format_point(x1, y1)}"
    return result


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4) -> str:
    length_of_first_line = distance(x1, y1, x2, y2)
    length_of_second_line = distance(x3, y3, x4, y4)

    if length_of_first_line >= length_of_second_line:
        result = closer_point(x1, y1, x2, y2)
    else:
        result = closer_point(x3, y3, x4, y4)

    return result

point_1_x = float(input())
point_1_y = float(input())
point_2_x = float(input())
point_2_y = float(input())
point_3_x = float(input())
point_3_y = float(input())
point_4_x = float(input())
point_4_y = float(input())

print(longer_line(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y))

