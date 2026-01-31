text = input()
final_string= ""

for character in text:
    if not final_string or character != final_string[-1]:
        final_string += character

print(final_string)
