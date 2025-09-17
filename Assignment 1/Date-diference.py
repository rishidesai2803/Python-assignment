import datetime

d1 = input("Enter first date (yyyy-mm-dd): ")
d2 = input("Enter second date (yyyy-mm-dd): ")

y1, m1, day1 = d1.split("-")
y2, m2, day2 = d2.split("-")

date1 = datetime.date(int(y1), int(m1), int(day1))
date2 = datetime.date(int(y2), int(m2), int(day2))

diff = date2 - date1
print("Difference is", diff.days, "days")
