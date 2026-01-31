n = int(input())
word = str(input())
my_list = []
new_list = []

for i in range(n):
    data = str(input())
    my_list.append(data)

print(my_list)

for i in range(len(my_list)):
    if word in my_list[i]:
        new_list.append(my_list[i])

print(new_list)
