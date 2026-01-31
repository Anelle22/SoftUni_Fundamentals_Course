from math import ceil

series_name = str(input())
series_length = int(input())
break_length = int(input())

lunch = break_length / 8
rest = 0.25 * break_length

time_left = break_length - lunch - rest

diff = abs(time_left - series_length)

if time_left >= series_length:
    print(f"You have enough time to watch {series_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(diff)} more minutes.")