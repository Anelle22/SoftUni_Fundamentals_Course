number_of_lines = int(input())
total_sum = 0
for i in range(number_of_lines):
    symbol = input()
    symbol_ascii = ord(symbol)
    total_sum += symbol_ascii

print(f"The sum equals: {total_sum}")
