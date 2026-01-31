n = int(input())
count = 0


for i in range (n):
    symbol = str(input())
    if symbol == "(":
        count += 1
    if symbol == ")":
        count -= 1
    if count == 2 or count <= -1:
        break

if count == 0:
    print("BALANCED")
else:
    print("UNBALANCED")


