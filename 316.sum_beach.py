string = input()
count = 0

for i in range(len(string)):
    if (string[i] == "s" or string[i] == "S") and (string[i+1] == "a" or string[i+1] == "A") and (string[i+2] == "n" or string[i+2] == "N") and (string[i+3] == "d" or string[i+3] == "D"):
        count += 1

    if (string[i] == "w" or string[i] == "W") and (string[i + 1] == "a" or string[i + 1] == "A") and (string[i+2] == "t" or string[i+2] == "T") and (string[i+3] == "e" or string[i+3] == "E") and (string[i+4] == "r" or string[i+4] == "R"):
        count += 1

    if (string[i] == "f" or string[i] == "F") and (string[i+1] == "i" or string[i+1] == "I") and (string[i+2] == "s" or string[i+2] == "S") and (string[i+3] == "h" or string[i+3] == "H"):
        count += 1

    if (string[i] == "s" or string[i] == "S") and (string[i+1] == "u" or string[i+1] == "U") and (string[i+2] == "n" or string[i+2] == "N"):
        count += 1


print(count)