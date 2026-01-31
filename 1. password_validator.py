password = list(input())

while True:
    command= input()
    if command == "Complete":
        break
    command_as_a_list = command.split(" ")
    action = command_as_a_list[0]

    if action == "Make":
        second_action = command_as_a_list[1]
        if second_action == "Upper":
            index = int(command_as_a_list[2])
            password[index] = password[index].upper()
            print("".join(password))
        elif second_action == "Lower":
            index = int(command_as_a_list[2])
            password[index] = password[index].lower()
            print("".join(password))

    elif action == "Insert":
        index = int(command_as_a_list[1])
        if index < len(password):
            character = command_as_a_list[2]
            password.insert(index, character)
            print("".join(password))

    elif action == "Replace":
        character = command_as_a_list[1]
        if character in password:
            value = int(command_as_a_list[2])
            character_asci = ord(character)
            sum_value = character_asci + value
            sum_value_asci_character = chr(sum_value)
            password = [symbol.replace(character, sum_value_asci_character) for symbol in password]
            print("".join(password))

    elif action == "Validation":
        condition_two = True
        condition_three = False
        condition_four = False
        condition_five = False

        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        for symbol in password:
            if symbol != "_" and not symbol.isalnum():
                condition_two = False
            if symbol.isupper():
                condition_three = True
            if symbol.islower():
                condition_four = True
            if symbol.isdigit():
                condition_five = True
        if not condition_two:
            print("Password must consist only of letters, digits and _!")
        if not condition_three:
            print("Password must consist at least one uppercase letter!")
        if not condition_four:
            print("Password must consist at least one lowercase letter!")
        if not condition_five:
            print("Password must consist at least one digit!")




