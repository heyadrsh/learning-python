from datetime import datetime, date
import time

# Creating datetime objects
dt1 = datetime(2023, 1, 17)  # Year, Month, Day
dt2 = datetime(2023, 1, 17, 14, 30, 0)  # Year, Month, Day, Hour, Minute, Second
dt3 = datetime.now()  # Current date and time
dt4 = datetime.strptime("2023/01/17", "%Y/%m/%d")  # Parse from string
dt5 = datetime.fromtimestamp(time.time())  # From timestamp

print("Different ways to create datetime objects:")
print(f"dt1: {dt1}")
print(f"dt2: {dt2}")
print(f"dt3: {dt3}")
print(f"dt4: {dt4}")
print(f"dt5: {dt5}")

# Accessing datetime components
print("\nDatetime components:")
print(f"Year: {dt3.year}")
print(f"Month: {dt3.month}")
print(f"Day: {dt3.day}")
print(f"Hour: {dt3.hour}")
print(f"Minute: {dt3.minute}")
print(f"Second: {dt3.second}")
print(f"Microsecond: {dt3.microsecond}")

# Converting to timestamp
timestamp = dt3.timestamp()
print(f"\nTimestamp: {timestamp}")

# Formatting datetime objects
print("\nFormatting datetime:")
print(f"Standard format: {dt3}")
print(f"Custom format: {dt3.strftime('%Y/%m/%d %H:%M:%S')}")
print(f"Date only: {dt3.date()}")
print(f"Time only: {dt3.time()}")

# Working with dates only
date1 = date(2023, 1, 17)
date2 = date.today()

print("\nWorking with dates:")
print(f"date1: {date1}")
print(f"date2: {date2}")
print(f"Year: {date1.year}")
print(f"Month: {date1.month}")
print(f"Day: {date1.day}")
print(f"Weekday: {date1.weekday()}")  # Monday is 0

# Date formatting
print(f"\nFormatted date: {date1.strftime('%Y/%m/%d')}")

# Comparing dates and times
print("\nComparisons:")
print(f"dt1 < dt2: {dt1 < dt2}")
print(f"dt1 == dt2: {dt1 == dt2}")
print(f"dt1 > dt2: {dt1 > dt2}")

# Getting current UTC time
utc_now = datetime.utcnow()
print(f"\nUTC time: {utc_now}") 