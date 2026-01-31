string = input()

new_string = [char for char in string if char.lower() not in ['a', 'e', 'i', 'o', 'u']]

print("".join(new_string))

