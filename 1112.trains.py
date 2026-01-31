number_of_wagons = int(input())
train_list = [0 for num in range(number_of_wagons)]
command = ""

while command != "End":
    command = input()
    command_list = command.split()
    if command_list[0] == "add":
        train_list[number_of_wagons - 1] += int(command_list[1])
    elif command_list[0] == "insert":
        train_list[int(command_list[1])] += int(command_list[2])
    elif command_list[0] == "leave":
        train_list[int(command_list[1])] -= int(command_list[2])

print(train_list)