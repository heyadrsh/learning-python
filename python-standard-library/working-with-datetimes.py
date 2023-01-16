from datetime import datetime, date
import time

dt1 = datetime(2023, 1, 16)
dt2 = datetime.now()
dt3 = datetime.strptime("2023/01/16", "%Y/%m/%d")
dt4 = datetime.fromtimestamp(time.time())

print(f"dt1: {dt1}")
print(f"dt2: {dt2}")
print(f"dt3: {dt3}")
print(f"dt4: {dt4}")

print(dt4.year)
print(dt4.month)
print(dt4.day)
print(dt4.hour)
print(dt4.minute)
print(dt4.timestamp())

print(f"Formatted: {dt4.strftime('%Y/%m/%d')}")

date1 = date(2023, 1, 16)
date2 = date.today()
print(f"date1: {date1}")
print(f"date2: {date2}")

print(date1.year)
print(date1.month)
print(date1.day) 