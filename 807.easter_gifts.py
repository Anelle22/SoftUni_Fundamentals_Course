gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    parts = command.split()

    if parts[0] == "OutOfStock":
        gift_name = parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_name:
                gifts[i] = "None"

    elif parts[0] == "Required":
        gift_name = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_name

    elif parts[0] == "JustInCase":
        gift_name = parts[1]
        gifts.pop()
        gifts.append(gift_name)

gifts = [gift for gift in gifts if gift != "None"]

print(" ".join(gifts))