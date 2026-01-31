number = int(input())
number_string = str(number)

largest_number = ''.join(sorted(number_string, reverse=True))

print(largest_number)
