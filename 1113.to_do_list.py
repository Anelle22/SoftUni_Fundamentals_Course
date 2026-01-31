sorted_to_do_list = [0] * 10

while True:
    command = str(input())
    if command == "End":
        break
    instructions = command.split("-")
    importance = int(instructions[0]) - 1
    note = instructions[1]
    sorted_to_do_list.pop(importance)
    sorted_to_do_list.insert(importance, note)


result = [element for element in sorted_to_do_list if element != 0]
print(result)