list_1 = input().split()
list_2 = input().split()
list_3 = input().split()
winner_found = False

for i in range(0, len(list_1)):
    if list_1[i] == list_2[i] == list_3[i] and list_1[i] != '0':
        if list_1[i] == '1':
            print("First player won")
            winner_found = True
            break
        else:
            print("Second player won")
            winner_found = True
            break

for row in [list_1, list_2, list_3]:
    if row[0] == row[1] == row[2] and row[0] != '0':
        if row[0] == '1':
            print("First player won")
        else:
            print("Second player won")
        winner_found = True
        break


if not winner_found:
    if (list_1[0] == list_2[1] == list_3[2] and list_2[1] != '0') or (list_1[2] == list_2[1] == list_3[0] and list_2[1] != '0'):
        if list_2[1] == '1':
            print("First player won")
            winner_found = True
        else:
            print("Second player won")
            winner_found = True


if not winner_found:
    print("Draw!")