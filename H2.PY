import calendar

# Input format: month day year
m, d, y = map(int, input().split())

# calendar.weekday() returns an integer (0 for Monday, 6 for Sunday)
day_index = calendar.weekday(y, m, d)

# calendar.day_name provides the name of the day at a given index
print(calendar.day_name[day_index].upper())
