text = input()

for index in range(len(text)):
    if text[index] == ":":
        if index + 1 < len(text):
            print(f":{text[index + 1]}")
