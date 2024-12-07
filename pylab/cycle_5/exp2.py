import time
from datetime import datetime
current_datetime=datetime.now()
print(f"current date and time:{current_datetime}")
print("current year:",current_datetime.year)
print("month of the year:",current_datetime.strftime("%B"))
print("week Number of the year:",current_datetime.strftime("%U"))
print("week day of the week:",current_datetime.strftime("%A"))
print("day of the year:",current_datetime.strftime("%j"))
print("day of the month:",current_datetime.day)
print("day of the week(0=monday,6=sunday):",current_datetime.weekday())







