def operation(some_command, some_input):
    if some_command == "int":
        result = int(some_input) * 2
    elif some_command == "real":
        result = f"{(float(some_input) * 1.5):.2f}"
    else:
        result = f"${some_input}$"
    return result

command = str(input())
number = input()

print(operation(command, number))