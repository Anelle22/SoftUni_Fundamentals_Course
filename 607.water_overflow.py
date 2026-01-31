number_of_lines = int(input())
capacity = 255


for i in range (number_of_lines):
    water_litres = int(input())

    if capacity < water_litres:
        print("Insufficient capacity!")
        continue
    capacity -= water_litres

print(255 - capacity)