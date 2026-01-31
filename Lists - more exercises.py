numbers_as_string = input().split()
string = str(input())
sum_of_digits = 0
message = []

for number in numbers_as_string:
    for i in range (len(number)):
        sum_of_digits += int(number[i])

    if sum_of_digits >= len(string):
        sum_of_digits = sum_of_digits - len(string)

    message.append(string[sum_of_digits])
    string = string[:sum_of_digits] + string[sum_of_digits + 1:]
    sum_of_digits = 0

print("".join(message))




