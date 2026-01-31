some_string = input()
final_string = ""
sub_string = ""
repetitions = ""

for index in range(len(some_string)):

    if not some_string[index].isdigit():
        sub_string += some_string[index]

    else:
        repetitions += some_string[index]
        if index + 1 < len(some_string):
            if some_string[index + 1].isdigit():
                repetitions += some_string[index + 1]

        final_string += sub_string.upper() * int(repetitions)
        sub_string = ""
        repetitions = ""


print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
