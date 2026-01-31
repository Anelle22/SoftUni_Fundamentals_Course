words_and_definitions = input().split(" | ")
dictionary = {}

for element in words_and_definitions:
    word, definition = element.split(": ")
    if word in dictionary.keys():
        dictionary[word].append(definition)
    else:
        dictionary[word] = [definition]


words = input().split(" | ")
command = input()

if command == "Test":
    for word in words:
        if word in dictionary.keys():
            print(f"{word}:")
            for element in dictionary[word]:
                print(f" -{element}")

if  command == "Hand Over":
    for key in dictionary.keys():
        print(f"{key}", end=" ")


