def repeat_text (some_text, number_of_repeats) -> str:
    repeated_text = some_text * number_of_repeats
    return repeated_text

text = str(input())
counter = int(input())

print(repeat_text(text, counter))

