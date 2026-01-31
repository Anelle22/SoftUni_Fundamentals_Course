def characters_in_between(first: str, second: str) -> list:
    first_as_integer = ord(first)
    second_as_integer = ord(second)
    list_of_characters = []

    for i in range (first_as_integer + 1, second_as_integer):
        list_of_characters.append(chr(i))

    return list_of_characters


first_character = str(input())
second_character = str(input())
symbols = characters_in_between(first_character, second_character)
print(" ".join(symbols))
