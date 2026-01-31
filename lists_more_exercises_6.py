numbers = [int(number) for number in input().split()]

while True:
    command = input()
    if command == "end":
        break
    command_as_list = command.split()

    if command_as_list[0] == "exchange":
        split_index = int(command_as_list[1])
        if split_index < 0 or split_index >= len(numbers):
            print("Invalid index")
        else:
            numbers = numbers[split_index + 1:] + numbers[:split_index + 1]

    elif command_as_list[0] == "max":
        even_or_odd = command_as_list[1]
        filtered_list = []
        if even_or_odd == "even":
            filtered_list = [number for number in numbers if number % 2 == 0]
        else:
            filtered_list = [number for number in numbers if number % 2 != 0]

        if len(filtered_list) == 0:
            print("No matches")
        else:
            max_value = max(filtered_list)
            max_index = len(numbers) - 1 - numbers[::-1].index(max_value)
            print(max_index)


    elif command_as_list[0] == "min":
        even_or_odd = command_as_list[1]
        filtered_list = []
        if even_or_odd == "even":
            filtered_list = [number for number in numbers if number % 2 == 0]
        else:
            filtered_list = [number for number in numbers if number % 2 != 0]

        if len(filtered_list) == 0:
            print("No matches")
        else:
            min_value = min(filtered_list)
            min_index = len(numbers) - 1 - numbers[::-1].index(min_value)
            print(min_index)

    elif command_as_list[0] == "first":
        count = int(command_as_list[1])
        if count > len(numbers):
            print("Invalid count")
        else:
            i = 0
            even_or_odd = command_as_list[2]
            returned_list = []

            for number in numbers:
                if i == count:
                    break
                if even_or_odd == "even" and number % 2 == 0:
                    returned_list.append(number)
                    i = i + 1
                elif even_or_odd == "odd" and number % 2 != 0:
                    returned_list.append(number)
                    i = i + 1

            print(returned_list)

    elif command_as_list[0] == "last":
        count = int(command_as_list[1])
        if count > len(numbers):
            print("Invalid count")
        else:
            n = 0
            even_or_odd = command_as_list[2]
            returned_list = []
            for i in range(len(numbers) - 1, -1, -1):
                if n == count:
                    break
                if even_or_odd == "even" and numbers[i] % 2 == 0:
                    returned_list.append(numbers[i])
                    n = n + 1
                elif even_or_odd == "odd" and numbers[i] % 2 != 0:
                    returned_list.append(numbers[i])
                    n = n + 1
            print(returned_list[::-1])

print(numbers)