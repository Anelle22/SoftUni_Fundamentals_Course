import re
encrypted_message = input()
valid_messages = []
pattern = r'([*^])([\sA-Za-z]{6,})([*^])([\W]+)([+])([0-9.,-]+)([+])'

matches = re.findall(pattern, encrypted_message)

if matches:
    for match in matches:
        print(f"Found {match[1]} at coordinates {match[5]}.")
else:
    print("No valid artifacts found.")