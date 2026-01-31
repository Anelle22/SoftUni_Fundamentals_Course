command = input().split()

for element in command:
    length = len(element)
    for i in range(0, length):
        print(element, end="")

