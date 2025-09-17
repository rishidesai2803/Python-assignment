import datetime

dob = input("Enter your birth date (yyyy-mm-dd): ")
y, m, d = dob.split("-")

birth = datetime.date(int(y), int(m), int(d))
today = datetime.date.today()

years = today.year - birth.year
months = today.month - birth.month
days = today.day - birth.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

print("Your age is", years, "years", months, "months and", days, "days")
