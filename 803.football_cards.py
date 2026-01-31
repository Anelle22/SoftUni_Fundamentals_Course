team_a = []
team_b = []

for i in range(1, 12):
    team_a.append("A-" + str(i))
    team_b.append("B-" + str(i))

cards = input().split()

early_break = False

for card in cards:
    for number in team_a:
        if card == number:
            team_a.remove(card)
    for number in team_b:
        if card == number:
            team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        early_break = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if early_break:
    print("Game was terminated")





