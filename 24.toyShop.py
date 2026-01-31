holiday = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

toy_number = puzzles + dolls + bears + minions + trucks
revenue = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2

if toy_number >= 50:
    revenue = revenue * 0.75

revenue = revenue * 0.9
diff = abs(revenue - holiday)

if revenue >= holiday:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')