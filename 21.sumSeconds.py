a = int(input())
b = int(input())
c = int(input())

sum = a + b + c

minutes = sum // 60
seconds = sum % 60

print(f'{minutes}:{seconds:02d}')
