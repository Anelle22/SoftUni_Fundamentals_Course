first_string = str(input())
second_string = str(input())

for character_index in range (len(first_string)):
    if first_string[character_index] == second_string[character_index]:
        continue
    print(second_string[:character_index + 1] + first_string[character_index + 1:])







