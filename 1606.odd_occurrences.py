command = input().split()
dictionary = {}

for element in command:
    if element.lower() not in dictionary.keys():
        dictionary[element.lower()] = 1
    else:
        dictionary[element.lower()] += 1

for key in dictionary.keys():
    if dictionary[key] % 2 != 0:
        print(key, end = " ")

