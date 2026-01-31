deposit = float(input())
months = int(input())
interest = float(input())

sum = deposit + months * ((deposit * interest / 100) / 12)

print(sum)