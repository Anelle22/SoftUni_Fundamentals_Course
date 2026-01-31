
number = int(input())

i = str(number)

while True:
    number += 1
    i = str(number)
    length = len(i)
    if len(set(i)) == length:
        print(i)
        break