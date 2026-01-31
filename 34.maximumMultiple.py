divisor = int(input())
boundary = int(input())
number = 0

for i in range (boundary + 1):
    if i % divisor == 0:
        number = i

print(number)


