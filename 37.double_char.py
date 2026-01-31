while True:
    string = input()
    if string == "SoftUni":
        continue
    if string == "End":
        break

    new_string = ""

    for i in range (len(string)):
        new_string += string[i] + string[i]

    print(new_string)

