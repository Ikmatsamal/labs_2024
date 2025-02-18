#1
import datetime
day_now = datetime.datetime.today()
day_5ago = day_now - datetime.timedelta(days = 5)
print(day_5ago)
#2
import datetime
yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)
#3
import datetime
d1 = datetime.datetime.now()

print(d1.strftime("%c"))
#4
from datetime import datetime

date1 = datetime.strptime(input("Enter the first date: "), "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(input("Enter the second date: "), "%Y-%m-%d %H:%M:%S")

difference_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", difference_seconds)