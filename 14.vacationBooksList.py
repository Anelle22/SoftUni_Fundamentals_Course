total_pages = int(input())
pages_hour = int(input())
days = int(input())

hours_day = int((total_pages // pages_hour) / days)

print(hours_day)