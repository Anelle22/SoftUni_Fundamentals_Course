def contains (some_activation_key: list, substring):
    if substring in "".join(some_activation_key):
        return f'{"".join(some_activation_key)} contains {substring}'
    else:
        return "Substring not found!"

def flip (some_activation_key: list, type, start_index: int, end_index: int):
    for n in range (start_index, end_index):
        if type == "Upper":
            some_activation_key[n] = some_activation_key[n].upper()
        else:
            some_activation_key[n] = some_activation_key[n].lower()
    return some_activation_key

def slice_part (some_activation_key: list, start_index: int, end_index: int):
    new_activation_key = some_activation_key[0:start_index] + some_activation_key[end_index:]
    return new_activation_key

raw_activation_key = input()
key_as_a_list = list(raw_activation_key)
command = input()

while command != "Generate":
    instructions = command.split(">>>")
    if instructions[0] == "Contains":
        print(contains(key_as_a_list, instructions[1]))
    elif instructions[0] == "Flip":
        upper_or_lower = str(instructions[1])
        given_start_index = int(instructions[2])
        given_end_index = int(instructions[3])
        key_as_a_list = flip(key_as_a_list, upper_or_lower, given_start_index, given_end_index)
        print("".join(key_as_a_list))
    elif instructions[0] == "Slice":
        given_start_index = int(instructions[1])
        given_end_index = int(instructions[2])
        key_as_a_list = slice_part(key_as_a_list, given_start_index, given_end_index)
        print("".join(key_as_a_list))

    command = input()

print(f'Your activation key is: {"".join(key_as_a_list)}')