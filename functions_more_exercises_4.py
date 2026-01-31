def tribonacci_sequence (some_number):
    sequence = [int(1), int(1), int(2)]

    for i in range (3, some_number):
        sum_of_previous_elements = sum(sequence[-3:])
        sequence.append(sum_of_previous_elements)

    sequence_as_string = [str(char) for char in sequence]
    result = " ".join(sequence_as_string[:some_number])
    return result

number = int(input())
print(tribonacci_sequence(number))