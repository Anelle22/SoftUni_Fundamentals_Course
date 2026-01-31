n = int(input())
lst = []
new_list = []

for i in range(n):
    number = int(input())
    lst.append(number)

command = str(input())

if command == "even":
    for i in range (len(lst)):
        if lst[i] % 2 == 0:
            new_list.append(lst[i])
elif command == "odd":
    for i in range (len(lst)):
        if lst[i] % 2 != 0:
            new_list.append(lst[i])
elif command == "negative":
    for i in range (len(lst)):
        if lst[i] < 0:
            new_list.append(lst[i])
elif command == "positive":
    for i in range (len(lst)):
        if lst[i] >= 0:
            new_list.append(lst[i])

print(new_list)