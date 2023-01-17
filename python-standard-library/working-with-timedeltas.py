from datetime import datetime, timedelta

# Create some sample dates
dt1 = datetime(2023, 1, 17)
dt2 = datetime.now()

# Calculate duration between dates
duration = dt2 - dt1
print("Time difference:")
print(f"Days: {duration.days}")
print(f"Seconds: {duration.seconds}")
print(f"Microseconds: {duration.microseconds}")
print(f"Total seconds: {duration.total_seconds()}")

# Creating timedelta objects
delta1 = timedelta(days=5)
delta2 = timedelta(hours=12)
delta3 = timedelta(minutes=30)
delta4 = timedelta(seconds=45)
delta5 = timedelta(weeks=2)

# Adding time to a date
future_date = dt1 + delta1
print(f"\nDate after adding 5 days: {future_date}")

# Subtracting time from a date
past_date = dt1 - delta1
print(f"Date before 5 days: {past_date}")

# Combining timedeltas
total_delta = delta1 + delta2 + delta3 + delta4
print(f"\nTotal duration: {total_delta}")

# Multiplying timedeltas
double_time = delta1 * 2
half_time = delta1 / 2
print(f"Double time: {double_time}")
print(f"Half time: {half_time}")

# Working with weeks
two_weeks = timedelta(weeks=2)
print(f"\nTwo weeks in days: {two_weeks.days}")

# Complex calculations
meeting_duration = timedelta(hours=1, minutes=30)
meeting_start = datetime.now()
meeting_end = meeting_start + meeting_duration

print("\nMeeting details:")
print(f"Start time: {meeting_start.strftime('%I:%M %p')}")
print(f"End time: {meeting_end.strftime('%I:%M %p')}")
print(f"Duration: {meeting_duration}")

# Finding a date in the past
one_month_ago = datetime.now() - timedelta(days=30)
print(f"\nOne month ago: {one_month_ago.strftime('%Y-%m-%d')}")

# Finding a date in the future
next_week = datetime.now() + timedelta(weeks=1)
print(f"Next week: {next_week.strftime('%Y-%m-%d')}")

# Checking if a date is within a time range
deadline = datetime.now() + timedelta(days=7)
submission = datetime.now() + timedelta(days=5)
time_left = deadline - submission
print(f"\nTime left for submission: {time_left}") 