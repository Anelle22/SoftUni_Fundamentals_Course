def area_of_rectangle(some_width, some_height) -> int:
    area = some_width * some_height
    return area

width = int(input())
height = int(input())

print(area_of_rectangle(width, height))