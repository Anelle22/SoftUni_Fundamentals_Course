key = int(input())
n = int(input())
word = ""

for i in range (n):
    symbol = input()
    symbol_number = ord(symbol)
    symbol_number += key
    word += chr(symbol_number)

print(word)



