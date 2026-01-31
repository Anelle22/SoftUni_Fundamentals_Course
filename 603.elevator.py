from math import ceil

people_number = int(input())
capacity = int(input())

courses = ceil(people_number / capacity)

print(courses)

